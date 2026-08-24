# FutureNest 30-Day Validation Daily Plan

**Start:** Tuesday, August 25, 2026  
**End:** Wednesday, September 23, 2026  
**Time budget:** Approximately 10 hours per week  
**Work pattern:** All 7 days, using flexible blocks of roughly 60-120 minutes  
**Website:** `future.lumicore-labs.com`  
**Repository:** Separate `future-nest` Git repository inside the current workspace  
**Analytics:** Google Analytics 4, free tier

**Seasonal campaign:** Halloween Home Decor & DIY
**Halloween destination:** `future.lumicore-labs.com/halloween`
**Halloween effort:** Approximately 20% of the weekly time budget; FutureNest validation remains 80%

## How to Use This Plan

- Complete **Must do** items first.
- Move **Should do** items to another day when a task takes longer than expected.
- Use **Optional** items only when the weekly 10-hour budget remains available.
- Check each box manually after verifying the result.
- Record decisions and metrics in the tracker files.
- Treat Halloween as a separate campaign and record its Pins separately from FutureNest Pins.

## Halloween Campaign

Use the board name **Halloween Home Decor & DIY**. Start with home decor, porch ideas, lighting, and DIY decorations because they fit the existing art, design, home, and DIY audience most naturally. Add a smaller number of party-planning and printable ideas; defer costumes as a primary topic.

The first batch is stored at `pinterest-post-generation/post-ideas/Pinterest_Halloween_PostIdeas_Aug25_Aug29_v25-halloween.csv`. It contains 30 Flow-ready Pins for August 25-29, six per day. Link each Pin to `https://future.lumicore-labs.com/halloween` after that page is live. Until then, do not publish links that lead to a missing page; use the Pin as a draft or point it to an available temporary page.

Track Halloween separately using the campaign name `halloween_2026` so its impressions, outbound clicks, sessions, and product intent can be compared with the FutureNest campaign.

## Day 1 - August 25: Create the Repository

**Outcome:** A separate Nuxt project exists locally with its own Git history.

### Must do

- [ ] Create a `future-nest` folder inside the current workspace.
- [ ] Initialize it as a separate Git repository.
- [ ] Create the Nuxt project using the current stable Nuxt setup.
- [ ] Confirm the project runs locally.
- [ ] Add a README with the project purpose and deployment target.
- [ ] Add `.env.example` and confirm secrets are ignored.

### Should do

- [ ] Create folders for pages, content, data, assets, and components.
- [ ] Add a simple homepage placeholder.
- [ ] Make the first local Git commit.

### Optional

- [ ] Create the remote repository and push the initial commit.
- [ ] Create the Wild Build board **Halloween Home Decor & DIY**.

## Day 2 - August 26: DNS and VPS Preparation

**Outcome:** The subdomain points to the VPS and the server directory is ready.

### Must do

- [ ] Add the `future` A record for `lumicore-labs.com` pointing to the VPS IP.
- [ ] Verify DNS with `nslookup`.
- [ ] Create `/var/www/future-nest` on the VPS.
- [ ] Clone the separate repository into that directory.
- [ ] Confirm the VPS Node.js version supports the Nuxt project.

### Should do

- [ ] Record DNS and VPS details in a private note.
- [ ] Confirm the repository branch used for deployment.

### Optional

- [ ] Perform the first VPS-side install and generation.

## Day 3 - August 27: First Deployment

**Outcome:** A basic Nuxt placeholder is reachable through the subdomain.

### Must do

- [ ] Generate the Nuxt static output.
- [ ] Configure Nginx for `future.lumicore-labs.com`.
- [ ] Confirm `sudo nginx -t` passes.
- [ ] Reload Nginx and open the site.
- [ ] Install or configure HTTPS with Certbot.
- [ ] Confirm the HTTPS page loads.

### Should do

- [ ] Test direct loading of the homepage URL.
- [ ] Check browser console and Nginx logs for errors.

### Optional

- [ ] Create and test the deployment script.

## Day 4 - August 28: MVP Scope and Site Skeleton

**Outcome:** The minimum page structure is agreed and visible.

### Must do

- [ ] Add the homepage structure.
- [ ] Add the `/off-grid` category page or equivalent.
- [ ] Add article route structure.
- [ ] Add a reusable product-card component placeholder.
- [ ] Add navigation and footer.

### Should do

- [ ] Add a responsive layout.
- [ ] Add basic metadata and site title.

### Optional

- [ ] Add a simple visual identity using existing project assets.
- [ ] Add the `/halloween` route placeholder so seasonal Pins have a planned destination.

## Day 5 - August 29: Affiliate Research and Applications

**Outcome:** Affiliate options are recorded with evidence instead of assumptions.

### Must do

- [ ] Check Impact publisher requirements and signup flow.
- [ ] Check Awin publisher requirements and signup flow.
- [ ] Check at least three relevant direct merchant programs.
- [ ] Record Sri Lanka eligibility, payout method, minimum payout, tax requirements, and traffic-source rules.
- [ ] Submit applications where requirements are clear and acceptable.

### Should do

- [ ] Record application dates and confirmation emails.
- [ ] Identify five solar, smart-home, or compact-home products.

### Optional

- [ ] Contact one relevant merchant directly.

## Day 6 - August 30: Tracking Design

**Outcome:** The measurement path is defined before content is published.

### Must do

- [ ] Create or select a free Google Analytics 4 property.
- [ ] Record the measurement ID privately.
- [ ] Add analytics configuration without committing secrets.
- [ ] Define `page_view`, `article_view`, `product_click`, and `affiliate_redirect` events.
- [ ] Define Pinterest UTM values from the event-tracking checklist.

### Should do

- [ ] Add a product-click redirect route if the static architecture supports it.
- [ ] Run a test visit locally.

### Optional

- [ ] Add a lightweight first-party event log only if it needs no database.

## Day 7 - August 31: Week 1 Review

**Outcome:** Week 1 is documented and Week 2 is unblocked.

### Must do

- [ ] Confirm subdomain, HTTPS, repository, and deployment path.
- [ ] Update the affiliate tracker.
- [ ] Complete the event-tracking checklist.
- [ ] Record blockers and next actions.
- [ ] Commit and push the working project state.

### Should do

- [ ] Write three decisions made this week.
- [ ] Confirm the three initial article topics.

### Optional

- [ ] Save a baseline screenshot.

## Day 8 - September 1: Homepage

**Outcome:** The homepage explains the site and leads visitors to useful content.

### Must do

- [ ] Replace the placeholder homepage.
- [ ] Add a clear Future Living value proposition.
- [ ] Add links to the first category and articles.
- [ ] Add affiliate disclosure access from the footer.

### Should do

- [ ] Add Open Graph metadata.
- [ ] Test mobile layout.

### Optional

- [ ] Add one featured-content section.
- [ ] Confirm the Halloween landing-page content outline.

## Day 9 - September 2: Article One

**Outcome:** The first useful commercial article is published locally.

### Must do

- [ ] Complete the article brief.
- [ ] Research and source each product claim.
- [ ] Write `10 Off-grid Gadgets You Can Actually Buy`.
- [ ] Add product cards with verified links or clearly marked pending links.
- [ ] Add disclosure and limitations.

### Should do

- [ ] Add internal links.
- [ ] Generate and inspect the output.

### Optional

- [ ] Prepare three Pin concepts.

## Day 10 - September 3: Article Two

**Outcome:** The second commercial article is published locally.

### Must do

- [ ] Complete the article brief.
- [ ] Write `7 Solar-powered Home Upgrades Worth Comparing`.
- [ ] Source energy and product claims.
- [ ] Add comparison criteria and limitations.
- [ ] Add product links only where the affiliate path is verified or clearly labeled.

### Should do

- [ ] Add SEO metadata and internal links.

### Optional

- [ ] Prepare three Pin concepts.

## Day 11 - September 4: Inspiration Article

**Outcome:** The site has informational content that is not only a buying page.

### Must do

- [ ] Write `12 Tiny-home Technologies That Make Small Spaces Work`.
- [ ] Focus on practical reader usefulness.
- [ ] Link naturally to relevant products without making every section a sales pitch.

### Should do

- [ ] Add a related-content section.
- [ ] Check reading flow on mobile.

### Optional

- [ ] Add one original diagram or comparison table.

## Day 12 - September 5: Legal and SEO Basics

**Outcome:** The public MVP has basic trust and discoverability pages.

### Must do

- [ ] Add privacy page.
- [ ] Add contact page using `dev.mg4@gmail.com` if needed.
- [ ] Add affiliate disclosure page or visible disclosure text.
- [ ] Add sitemap and robots file.
- [ ] Check canonical URLs and page titles.

### Should do

- [ ] Review image licenses and alt text.
- [ ] Remove unverified price or commission claims.

### Optional

- [ ] Set up Google Search Console.

## Day 13 - September 6: Local QA and Deploy

**Outcome:** The complete three-article MVP is live.

### Must do

- [ ] Test every navigation link and article URL.
- [ ] Test product links and tracking events.
- [ ] Generate the production build.
- [ ] Deploy through the separate Git repository.
- [ ] Verify HTTPS and mobile layout.

### Should do

- [ ] Check Nginx access and error logs.
- [ ] Record the deployment commit hash.

### Optional

- [ ] Ask one trusted person to test the site without explanation.

## Day 14 - September 7: Week 2 Review

**Outcome:** The site is ready for a controlled Pinterest traffic test.

### Must do

- [ ] Confirm all three articles are public.
- [ ] Confirm analytics test data is visible.
- [ ] Confirm product-click tracking works.
- [ ] Update the dashboard baseline.
- [ ] Record unresolved blockers.

### Should do

- [ ] Select the first 15-20 Pin topics.
- [ ] Create a Pin-to-article mapping.

### Optional

- [ ] Capture a baseline analytics screenshot.
- [ ] Review the Halloween batch status and select the first Pins to publish once `/halloween` is live.

## Day 15 - September 8: Pin Batch One

**Outcome:** The first batch of high-intent Pins is ready.

### Must do

- [ ] Create five Pins for Article One.
- [ ] Give each Pin a unique title, visual angle, and UTM value.
- [ ] Record each Pin in the campaign tracker.

### Should do

- [ ] Use concrete promises, comparisons, or checklists.
- [ ] Check every destination URL.

### Optional

- [ ] Prepare alternate descriptions.

## Day 16 - September 9: Pin Batch Two

**Outcome:** The second batch is ready and mapped to Article Two.

### Must do

- [ ] Create five Pins for Article Two.
- [ ] Record all metadata in the campaign tracker.
- [ ] Verify UTM links.

### Should do

- [ ] Include one budget angle and one use-case angle.

### Optional

- [ ] Create one comparison-style visual.

## Day 17 - September 10: Pin Batch Three

**Outcome:** The third batch is ready and mapped to Article Three.

### Must do

- [ ] Create five Pins for Article Three.
- [ ] Record all metadata in the campaign tracker.
- [ ] Verify that every Pin fulfills its article promise.

### Should do

- [ ] Include a tiny-home or small-space angle.

### Optional

- [ ] Prepare five additional variations.

## Day 18 - September 11: Publish and Schedule

**Outcome:** The controlled Pinterest test begins.

### Must do

- [ ] Publish or schedule the first 15 Pins.
- [ ] Start with the Future Living / Off-grid Tech board.
- [ ] Record actual publish times.
- [ ] Confirm Pinterest links resolve correctly.

### Should do

- [ ] Add up to five additional Pins if quality remains high.

### Optional

- [ ] Prepare a second relevant board only if the destination remains clear.
- [ ] Publish or schedule up to five Halloween Pins from `v25-halloween` if the landing page is live.

## Day 19 - September 12: First Measurement Check

**Outcome:** Early tracking problems are found.

### Must do

- [ ] Record Pinterest impressions, Pin clicks, outbound clicks, and saves.
- [ ] Record website sessions and article views.
- [ ] Check product-click and affiliate-redirect events.
- [ ] Fix broken links or missing UTM values.

### Should do

- [ ] Identify the strongest and weakest Pin promise.

### Optional

- [ ] Make one small landing-page improvement.

## Day 20 - September 13: Content and Funnel Review

**Outcome:** The test has a documented midpoint learning note.

### Must do

- [ ] Compare Pin performance by title angle.
- [ ] Compare traffic by article.
- [ ] Check whether visitors reach product cards.
- [ ] Record findings in the dashboard.

### Should do

- [ ] Improve one weak article section or product-card explanation.

### Optional

- [ ] Create two replacement Pins for the weakest angle.

## Day 21 - September 14: Week 3 Review

**Outcome:** The campaign is stable and the final week has a clear focus.

### Must do

- [ ] Confirm all published Pins are tracked.
- [ ] Confirm all website events are working.
- [ ] Update the campaign and affiliate trackers.
- [ ] Record cumulative sessions and product clicks.

### Should do

- [ ] Decide whether one controlled improvement is justified.

### Optional

- [ ] Publish replacement Pins if evidence supports them.
- [ ] Compare Halloween campaign performance separately from FutureNest.

## Day 22 - September 15: Affiliate Follow-up

**Outcome:** Affiliate uncertainty is reduced.

### Must do

- [ ] Check responses from Impact, Awin, and direct merchants.
- [ ] Follow up where applications allow it.
- [ ] Confirm payout and Sri Lanka restrictions.
- [ ] Update program status and dates.

### Should do

- [ ] Replace unusable programs with verified alternatives.

### Optional

- [ ] Contact one relevant merchant directly.

## Day 23 - September 16: Analytics Quality Review

**Outcome:** The final decision will use trustworthy data.

### Must do

- [ ] Compare Pinterest outbound clicks with attributed website sessions.
- [ ] Check UTM campaign and content values.
- [ ] Check for attribution problems.
- [ ] Confirm product-click events are not duplicated.
- [ ] Record known data limitations.

### Should do

- [ ] Add notes for Pinterest estimates or delayed reporting.

### Optional

- [ ] Create a simple chart from dashboard data.

## Day 24 - September 17: Conversion Improvement

**Outcome:** One evidence-based improvement is tested.

### Must do

- [ ] Choose one bottleneck: Pin click, article engagement, or product click.
- [ ] Make one focused change.
- [ ] Record the change and expected effect.

### Should do

- [ ] Improve one product-card CTA or comparison section.

### Optional

- [ ] Create one new Pin based on the strongest topic.

## Day 25 - September 18: Revenue and Economics Review

**Outcome:** The revenue model is assessed using actual evidence where available.

### Must do

- [ ] Record affiliate clicks, conversions, and revenue.
- [ ] Distinguish zero sales from missing tracking.
- [ ] Compare actual traffic with the conservative scenario.
- [ ] Record estimated weekly maintenance time.

### Should do

- [ ] Estimate revenue per 1,000 Pinterest-attributed sessions.

### Optional

- [ ] Identify one higher-value category worth testing later.

## Day 26 - September 19: Audience and Content Decision

**Outcome:** The next winning topic, if any, is identified.

### Must do

- [ ] Rank articles by Pinterest sessions.
- [ ] Rank articles by product-click rate.
- [ ] Rank Pin angles by outbound-click rate.
- [ ] Identify the strongest and weakest topics.

### Should do

- [ ] Write three lessons about audience intent.

### Optional

- [ ] Draft five follow-up article ideas.

## Day 27 - September 20: Final Data Capture

**Outcome:** The dashboard contains the final complete snapshot.

### Must do

- [ ] Export or record the final Pinterest date range.
- [ ] Record sessions, article views, product clicks, redirects, and revenue.
- [ ] Update every campaign-tracker row with available data.
- [ ] Update the validation dashboard.

### Should do

- [ ] Save screenshots or exports needed to explain the result.

### Optional

- [ ] Clean up duplicate or incomplete tracker rows.

## Day 28 - September 21: Draft the Decision

**Outcome:** A preliminary continue, reposition, or stop decision is written.

### Must do

- [ ] Compare results with the traffic, intent, and affiliate thresholds.
- [ ] Write evidence for and against continuing.
- [ ] Select one decision.

### Should do

- [ ] Estimate the next 30-day workload.
- [ ] Identify the biggest unresolved risk.

### Optional

- [ ] Ask for a second opinion.

## Day 29 - September 22: Final Review

**Outcome:** The decision is checked for data and scope mistakes.

### Must do

- [ ] Recheck dashboard arithmetic.
- [ ] Confirm affiliate status evidence.
- [ ] Confirm the decision uses attributable traffic, not impressions alone.
- [ ] Confirm the next scope fits 10 hours per week.

### Should do

- [ ] Write the top three lessons in plain language.

### Optional

- [ ] Archive unused drafts without deleting source data.

## Day 30 - September 23: Close the Experiment

**Outcome:** The validation cycle is complete and the next action is explicit.

### Must do

- [ ] Complete the validation dashboard.
- [ ] Finalize the one-page decision memo.
- [ ] Record the next 30-day scope only if evidence supports continuing.
- [ ] Commit and push project, tracker, and documentation changes.
- [ ] Note the date of the next review.

### Should do

- [ ] Update the weekly plan with approved changes.

### Optional

- [ ] Create the next daily plan only after the decision is approved.

## Completion Rules

- The experiment is not complete if the site is live but tracking is unverified.
- Affiliate applications are not successful until eligibility and payout details are confirmed.
- A failed traffic test should lead to a Pin or positioning change before a technology change.
- Do not add an AI tool, database, CMS, or second monetization site during this cycle.
