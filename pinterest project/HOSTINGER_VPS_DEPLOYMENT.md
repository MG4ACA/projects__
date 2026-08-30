# FutureNest Nuxt Deployment on Hostinger VPS

This guide deploys the separate FutureNest Nuxt repository to `future.lumicore-labs.com` on the existing Hostinger KVM1 VPS.

## Deployment Decisions

- **Repository:** separate Git repository inside this workspace, for example `future-nest/`.
- **Application:** Nuxt with static generation for the validation MVP.
- **Content:** Markdown and simple data files; no database or CMS initially.
- **Server:** Existing Ubuntu VPS with SSH, Node.js, Nginx, Git, and SSL capability.
- **Runtime:** Nginx serves the locally generated static files; PM2 is not needed for the static MVP.
- **VPS Node.js:** Node 20.20.0 remains unchanged because other applications depend on it.
- **Build location:** The supported local Node.js environment generates `.output/public`, which is committed to this repository for VPS deployment.
- **Analytics:** Google Analytics 4 can be added after the site is reachable.

## Architecture

```text
Pinterest
    |
    v
future.lumicore-labs.com
    |
    v
Nginx on Hostinger KVM1 VPS
    |
    v
/var/www/future-nest/.output/public
    |
    v
Nuxt-generated static pages
```

## Before Deployment

Confirm locally:

- [ ] The separate `future-nest` repository exists inside the workspace.
- [ ] The repository has its own Git history and remote.
- [ ] `npm run generate` completes successfully on the local development machine.
- [ ] `.output/public` is committed to the repository.
- [ ] No secrets are committed.
- [ ] Affiliate links and analytics IDs use the intended configuration.

## 1. Create the Subdomain DNS Record

In the DNS manager for `lumicore-labs.com`, create:

```text
Type: A
Name: future
Value: YOUR_VPS_PUBLIC_IP
TTL: 300 or automatic
```

Verify propagation:

```bash
nslookup future.lumicore-labs.com
```

The result should contain the VPS public IP.

## 2. Create the VPS Application Directory

SSH into the VPS using the existing account:

```bash
ssh YOUR_USER@YOUR_VPS_IP

sudo mkdir -p /var/www/future-nest
sudo chown -R "$USER":"$USER" /var/www/future-nest
cd /var/www/future-nest
```

## 3. Clone the Separate Repository

Use the repository URL created for FutureNest:

```bash
git clone https://github.com/MG4ACA/future-nest.git .
git branch --show-current
find .output/public -maxdepth 1 -type f | head
```

If the repository is private, use SSH deploy keys or your existing authenticated Git method. Do not place a GitHub token in shell history or a committed file.

## 4. Configure Nginx for HTTP

Create a site configuration:

```bash
sudo nano /etc/nginx/sites-available/future.lumicore-labs.com
```

Use:

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name future.lumicore-labs.com;

    root /var/www/future-nest/.output/public;
    index index.html;

    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location / {
        try_files $uri $uri/ $uri.html /index.html;
    }

    location ~* \.(js|css|png|jpg|jpeg|gif|webp|svg|ico|woff|woff2)$ {
        try_files $uri =404;
        expires 7d;
        add_header Cache-Control "public, max-age=604800";
    }
}
```

Enable and test it:

```bash
sudo ln -s /etc/nginx/sites-available/future.lumicore-labs.com /etc/nginx/sites-enabled/future.lumicore-labs.com
sudo nginx -t
sudo systemctl reload nginx
```

## 5. Enable HTTPS

After DNS resolves to the VPS:

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d future.lumicore-labs.com
sudo certbot renew --dry-run
```

Choose the redirect option when Certbot asks whether HTTP should redirect to HTTPS. Verify:

```bash
curl -I https://future.lumicore-labs.com
```

## 6. Deploy Updates

Here we use only the static files built locally and committed to Git because the VPS Node.js version is incompatible with the current Nuxt toolchain.
From the VPS application directory:

```bash
cd /var/www/future-nest
git pull origin development
sudo nginx -t
sudo systemctl reload nginx
```

If the repository uses another deployment branch, replace `development`. Do not use `git reset --hard` during normal deployment because it can discard server-side changes.

## 7. Optional Deployment Script

After manual deployment works, create `/var/www/future-nest/deploy.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

cd /var/www/future-nest
git pull --ff-only origin development
sudo nginx -t
sudo systemctl reload nginx
echo "FutureNest deployment complete"
```

Make it executable and run it:

```bash
chmod +x deploy.sh
./deploy.sh
```

## 8. Verify the Site

- [ ] `https://future.lumicore-labs.com` loads.
- [ ] Homepage assets load without 404 errors.
- [ ] Article URLs load directly.
- [ ] Mobile layout works.
- [ ] Affiliate disclosure is visible on commercial pages.
- [ ] Product tracking redirects work without exposing private values.
- [ ] Analytics receives a test page view.
- [ ] Nginx configuration passes `sudo nginx -t`.

Useful checks:

```bash
curl -I https://future.lumicore-labs.com
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
df -h
free -m
```

## Static Nuxt Notes

The validation site should not use a Nuxt server process on the VPS. Static generation is cheaper and simpler:

```bash
npm run generate
```

The deployable files are in:

```text
.output/public/
```

These files are generated locally and committed to Git because the VPS cannot run the current Nuxt toolchain under Node.js 20. The VPS only needs Git and Nginx to publish them.

Use Nuxt server routes only if a later experiment requires server-side redirects, event collection, or another backend capability. Reassess whether Nginx should proxy to a PM2-managed process at that point.

## Security Rules

- Never commit `.env`, API keys, affiliate credentials, or private tokens.
- Never copy passwords into deployment documentation.
- Use a non-root SSH account where possible.
- Keep SSH restricted to required IPs if practical.
- Keep ports 80 and 443 open and avoid exposing the Nuxt development server publicly.
- Review Nginx logs after the first deployment.
