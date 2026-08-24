# Validation Event-Tracking Checklist

## Experiment Details

- Start date: 2026-08-25
- Working URL: `future.lumicore-labs.com`
- Pinterest account/board: Wild Build / Future Living - Off-grid Tech
- Analytics property ID:
- VPS deployment version:
- Date tracking verified:

## Required Events

| Event                  | Trigger                                | Required fields                                 | Verified |
| ---------------------- | -------------------------------------- | ----------------------------------------------- | -------- |
| `page_view`            | Any public page loads                  | page path, referrer, UTM values                 | [ ]      |
| `article_view`         | Article page loads                     | article slug, category                          | [ ]      |
| `product_click`        | Visitor clicks a product CTA           | product ID, article slug, merchant, position    | [ ]      |
| `affiliate_redirect`   | Tracking endpoint receives request     | product ID, article slug, campaign, destination | [ ]      |
| `external_destination` | Redirect is completed where measurable | merchant, campaign                              | [ ]      |

## UTM Convention

Use this format for Pinterest links:

`?utm_source=pinterest&utm_medium=organic&utm_campaign=validation_2026_08&utm_content=<pin-id-or-short-name>`

Rules:

- Use lowercase values.
- Keep the campaign constant for the 30-day test.
- Give every Pin a unique `utm_content` value.
- Do not put affiliate identifiers in public Pin URLs.

## Pre-launch Checks

- [ ] HTTPS works on the subdomain.
- [ ] Mobile page loads correctly.
- [ ] Analytics receives a test page view.
- [ ] Article view records the correct slug.
- [ ] Product click records the correct article and product.
- [ ] Redirect does not expose private configuration.
- [ ] Affiliate disclosure is visible on commercial pages.
- [ ] Privacy and cookie notices match the tools actually used.
- [ ] UTM parameters survive the landing-page visit.
- [ ] A test visit appears in the correct acquisition report.

## Weekly Data Capture

Record data from the same date range and note whether Pinterest marks it as estimated.

| Date checked        | Date range    | Impressions | Pin clicks | Outbound clicks | Sessions | Article views | Product clicks | Affiliate redirects | Revenue | Notes |
| ------------------- | ------------- | ----------: | ---------: | --------------: | -------: | ------------: | -------------: | ------------------: | ------: | ----- |
| 2026-08-25 baseline | Before launch |             |            |                 |          |               |                |                     |         |       |
|                     | Week 1        |             |            |                 |          |               |                |                     |         |       |
|                     | Week 2        |             |            |                 |          |               |                |                     |         |       |
|                     | Week 3        |             |            |                 |          |               |                |                     |         |       |
|                     | Week 4        |             |            |                 |          |               |                |                     |         |       |

## Calculated Metrics

- Pinterest Pin-click rate = Pin clicks / impressions.
- Pinterest outbound-click rate = outbound clicks / impressions.
- Session-to-product-click rate = product clicks / Pinterest-attributed sessions.
- Affiliate redirect rate = affiliate redirects / product clicks.
- Revenue per Pinterest session = revenue / Pinterest-attributed sessions.

Do not treat missing affiliate data as zero revenue unless the tracking and program connection are confirmed to be working.
