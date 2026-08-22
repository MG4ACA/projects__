# Pinterest Content Generation Brief — Master SOP
**Account:** `pinterest.com/wildbuild`
**Reader:** Claude Sonnet (AI agent) — this document is your primary instruction set for every batch session.
**Last Updated:** August 22, 2026 (v1.6)

---

## ⚡ QUICK-START CHECKLIST (Run This First, Every Session)

Before generating any content, Claude must complete these steps in order:

```
[ ] 1. Read the latest analytics CSV: find the most recent
        "Pinterest Analytics overview YYYYMMDD-YYYYMMDD.csv" file
        in the project folder and extract top pins + board performance.

[ ] 2. Read the latest audience insights CSV: find the most recent
        "audience-insights-total-audience-YYYY-MM-DD.csv" file
        and extract affinity scores and demographic shifts.

[ ] 3. Cross-reference top pin IDs with previous PostIdeas CSVs
        to identify the exact Themes, AI Prompts, and visual formulas
        behind the highest-performing pins.

[ ] 4. Note the batch dates: 5-day batch (no fixed weekday).
        Day 1 = first available posting day after current date.

[ ] 5. Confirm the output filename follows the naming convention
        (see Section 9) before writing the CSV.
```

---

## 🚀 COPY-PASTE SESSION STARTER PROMPT

Use this prompt at the start of every new batch session:

```
Role: You are a Pinterest Growth Scientist and AI Content Strategist
for the @wildbuild Pinterest account. Your task is to generate a new
5-day content plan (30 pins, 6 pins/day, 5-day batch).

Follow the instructions in Content-Brief-for-Claude.md exactly.

Step 1: Read the two most recent analytics files in the project folder
(Analytics overview CSV + audience-insights total audience CSV).
Extract top pin performance, board velocity, and affinity score changes.

Step 2: Cross-reference top pin IDs with previous PostIdeas CSVs to
identify the winning visual formulas to replicate.

Step 3: Generate the 30-pin CSV for [INSERT DAY 1 DATE] to
[INSERT DAY 5 DATE] following the CSV schema in the brief exactly.

Output the file to the project folder using the naming convention in
the brief. Do not output the full CSV in the chat window.
```

---

## 1. ACCOUNT & IDENTITY

| Field | Value |
|---|---|
| **Pinterest Handle** | `@wildbuild` |
| **Profile URL** | `pinterest.com/wildbuild` |
| **Primary Market** | United States (11.7% of audience) |
| **Top US Metros** | Los Angeles (6%), New York (5%), Seattle-Tacoma (2.8%), Washington DC (2.5%), San Francisco (2.5%), Chicago (2.3%) |
| **Gender Split** | Male 48.9% / Female 44% / Other 7.1% |
| **Primary Age Bracket** | 25–34 (34.8%), then 35–44 (20.6%) |
| **Total Monthly Audience** | **365,000** (up from 338k Aug 15 → 365k Aug 19 — +8% in 4 days; **3.7x growth since June**) |
| **Primary Device** | Web (46.8%), Android Mobile (40.6%), iPhone (33.1%) |

### Software Company Identity (for Code board)
The account owner runs a **small software studio / freelance team** that:
- Builds custom web apps, mobile apps, and websites for clients
- Has **productised software** (a salon booking system, a tuition institute management system, and similar vertical SaaS products)
- Targets **both startups and SMEs** — any business owner who needs a software solution

The Code board is a **direct lead generation channel**. Every pin must speak to a **business owner's pain point** and position the studio as the obvious solution.

**Target clients:**
- Small business owners (salons, tuition centres, retail, hospitality) who need management software
- Startups and SMEs needing custom web apps or mobile apps
- Founders who need a reliable dev team without hiring in-house

**Positioning:** A professional, premium software studio that delivers real business outcomes — not a random freelancer, but a trusted technology partner.

---

## 2. ACTIVE BOARDS — EXACT NAMES & PINTEREST URLS

> ⚠️ Always use these exact board names. Copy-paste — do not paraphrase.

| Board Name | Pinterest URL | Daily Slots | Post Type |
|---|---|---|---|
| `Future Living & Off-Grid Tech` | `pinterest.com/wildbuild/future-living-off-grid-tech/` | Slot-1 (7:30am) + Slot-3 (11:00am) + Slot-5 (2:00pm) | Static Image |
| `Smart Pet Wellness` | `pinterest.com/wildbuild/smart-pet-wellness-eco-tech-quiet-luxury/` | Slot-2 (9:30am) + Slot-4 (12:30pm) + Slot-6 (3:30pm) | Static Image |

> ⚠️ **Build. Scale. Ship. board HALTED** (effective August 2026). Sri Lankan tourism board (Arachi Tours) planned as replacement — details TBD.
> ⚠️ **Nail Aesthetic board DISCONTINUED** (effective July 2026).

---

## 3. DAILY POSTING SCHEDULE

**6 pins per day · 5-day batch · 30 pins per batch**
All times are **US Eastern Standard Time (EST)**.

| Slot | Time (EST) | Board | Pin Sub-Type |
|---|---|---|---|
| Slot-1 | 7:30am | Future Living & Off-Grid Tech | Architecture / Landscape / Watercraft |
| Slot-2 | 9:30am | Smart Pet Wellness | Wilderkind Wild Predator |
| Slot-3 | 11:00am | Future Living & Off-Grid Tech | Material Detail / Campers & RV / Aircraft |
| Slot-4 | 12:30pm | Smart Pet Wellness | Adventure Dog |
| Slot-5 | 2:00pm | Future Living & Off-Grid Tech | Floating / Cantilevered / New Structural Format |
| Slot-6 | 3:30pm | Smart Pet Wellness | Adventure Dog or Indoor Luxury Cat |

---

## 4. AUDIENCE AFFINITY SCORES (June 2026 Baseline)

These are the **multiplier scores** showing how much more likely our audience is to engage with a topic vs. the average Pinterest user. Use these to prioritise visual concepts.

> ⚠️ Always read the latest audience CSV at the start of each session and note any scores that have changed significantly (>0.3 change). Flag changes in your pre-generation analysis.

> ⚠️ Updated August 22, 2026 — Campers & RV at new all-time record 8.718x. All Tier 1/2 affinities stable-to-rising. Account consolidating strongly.

### 🔴 Tier 1 — Hyper-Affinity (6x+): Must appear in ≥60% of Future Living pins
| Interest | Affinity Score | Change | Application |
|---|---|---|---|
| **Campers & RV** | **8.718x** | ⬆️ +0.150 from Aug 15 — **NEW ALL-TIME RECORD, 6th consecutive rise** | Ultra-luxury van builds, glass pod trailers, Airstream integrations, expedition pods, Land Cruiser/Hilux/G-Wagon/Defender/Tacoma builds — **ABSOLUTE PRIORITY #1** |
| **Watercraft** | **7.379x** | ↔️ -0.033 from Aug 15 — stable above 7x | Glass boathouses, floating platforms, custom lake docks, seaplane docks, pontoon architecture, houseboats — **DOUBLE DOWN** |
| **Metal Art / Industrial** | **6.596x** | ↔️ +0.013 from Aug 15 — stable above 6.5x | Corten steel cladding, raw I-beam frames, welded steel facades, steel joinery — **≥40% of FL pins** |

### 🟡 Tier 2 — Strong Affinity (4–6x): Weave through Future Living pins
| Interest | Affinity Score | Change | Application |
|---|---|---|---|
| **Cycling** | **5.457x** | ↔️ stable above 5.4x | Bikepacking-related van builds, gravel bike on expedition roof racks — weave as accent elements |
| **Aircraft** | **4.880x** | ↔️ stable near 4.9x | Float planes moored at glass cabins, seaplane ramps, hangar-aesthetic buildings, Cessna 185/de Havilland Beaver aesthetics |
| **Woodworking** | **4.386x** | ↔️ +0.017 — steady climb | Japanese joinery, live-edge slabs, timber frames, shou sugi ban decking |
| **Exterior / Door Design** | **3.742x / 3.461x** | ⬆️ Continued rise | Architectural entrance sequences, threshold moments, exterior material details |
| **Educational Architecture** | **3.695x** | ↔️ Stable | Parametric design, structural honesty, engineering-forward architecture |

### 🟢 Tier 4 — Moderate Affinity: Supporting context
| Interest | Score | Notes |
|---|---|---|
| Landscape & Urbanism Architecture | 2.521x | Background context for architecture pins |
| Garden Design | 2.484x | Outdoor spaces around cabins |
| Mosaic / Poster Design | 1.924x / 2.232x | Design-adjacent content |

---

## 5. WINNING VISUAL FORMULAS (From Top Pin Data)

These formulas are extracted from actual high-performing pins. **Replicate the formula, not the exact pin.**

### Formula #1 — "Glass + Water + Mirror Symmetry" ⭐ TOP PERFORMER
- **Proven result:** 16,081 impressions (highest single pin May–June 2026)
- **Recipe:** Full-glass structure (cabin / boathouse / pod) + mirror-still water body + perfect reflection of structure AND landscape in water + warm amber interior visible + no people
- **Light condition:** Dawn or golden hour — mist at water level
- **Must-include:** EcoFlow unit with green LED barely visible inside
- **Setting:** PNW lake / Lake Tahoe / Columbia River Gorge

### Formula #2 — "Wilderkind Predator + Twilight Rim-Light" ⭐ TOP PET SAVER
- **Proven result:** Drives highest save rate on Smart Pet Wellness board (389 saves / 75k impressions)
- **Recipe:** Wild predator cat (not domestic) + bare alpine/desert/river setting + cool twilight or golden-hour rim-light on fur/coat + direct eye contact with camera + low angle shot (below eye level)
- **Proven species:** Snow Leopard, Puma, Jaguar, Caracal, Lynx, Clouded Leopard, Serval
- **Style label in prompt:** "Wilderkind aesthetic"
- **Key detail:** Always describe eyes specifically (colour, intensity, directness)

### Formula #3 — "Floating / Cantilevered Architecture Drama"
- **Recipe:** Structure cantilevered or floating over void (cliff, water, forest floor) + structural elements visible + glass transparency showing depth below + EcoFlow system inside
- **High performers:** Cliff cantilever, floating pontoon cabin, treehouse pod, cliff overhang

### Formula #4 — "Adventure Dog + Dramatic US Landscape"
- **Recipe:** Specific breed (not generic dog) + named US location (Sierra Nevada, PNW, Sedona, Moab) + peak action (mid-gallop, mid-leap) + breed-specific feature highlighted (ridge on Ridgeback, tufts on Lynx, merle coat on Aussie) + golden hour or dawn light
- **No people. No leash.**

### Formula #5 — "SE-Lifestyle Bridge Workspace"
- **Recipe:** Minimal desk with visible monitors showing client-facing content (CRM pipeline, Stripe revenue, consulting proposal, architecture diagram) + glass cabin or high-end loft setting + aspirational view (lake, float plane dock, city skyline, red rocks) + EcoFlow on floor + no person visible
- **Key:** The monitor content must be legible and specific — actual numbers, actual software UI

### Formula #6 — "SE-Infographic — Dark Editorial Authority"
- **Recipe:** Deep charcoal background (#0d0d1a or #1a1a2e) + bold white title + amber subtitle and accent numbers + framework content positioned as founder-facing intelligence + footer stat that creates urgency + no photography
- **Font feel:** Outfit or Inter — bold, professional, clean
- **Emotional register:** Authoritative, specific, saves-the-founder-from-a-mistake

---

## 6. GEOGRAPHIC TARGETING (US Market)

Anchor visual prompts in recognisable aspirational US settings. Mix across the batch — no single location should dominate more than 30% of any batch.

| Location | Visual Markers | Priority |
|---|---|---|
| **Pacific Northwest (PNW)** | Old-growth Douglas fir/cedar, sword ferns, grey-green moss, coastal fog, Sitka spruce, Olympic Peninsula, Columbia River Gorge basalt | High |
| **Sierra Nevada / Lake Tahoe** | Pale cream granite boulders, crystal-clear alpine lakes, lodgepole pines, snowcapped peaks, sapphire-blue lake colour | High |
| **High Desert — Sedona / Joshua Tree** | Red Navajo sandstone, orange-rust rock formations, Joshua trees, creosote brush, sagebrush chaparral, stark desert blue sky | High |
| **US Tech Hubs — Austin / NYC / SF Bay** | Glass loft interiors, skyline views at sunset/dusk, Bay Bridge, Hudson River, Colorado River Austin | Medium |
| **Colorado Rockies** | Aspen groves (golden autumn), fourteener granite summits, cloud seas below peaks, lodgepole pine ridges | Medium |
| **Oregon / California Pacific Coast** | Coastal bluffs, windswept headlands, sea stacks, coastal scrub, Pacific sunset over water | Medium |
| **Moab / Utah Canyon Country** | Navajo sandstone, Arches National Park, canyon depth, ochre rock | Low |

---

## 7. BOARD-SPECIFIC CONTENT GUIDELINES

### 7A. Future Living & Off-Grid Tech
**Mission:** Aspirational off-grid architecture, sustainable technology, extraordinary residential design.

**Content Mix per batch (10 pins):**
- 3–4 pins: Watercraft / floating architecture (Tier 1 affinity — always lead here)
- 2–3 pins: Steel / metal art / industrial architecture (Corten, welded steel, brutalist)
- 1–2 pins: Timber / woodworking architectural detail (joinery, live-edge, shou sugi ban)
- 1–2 pins: Camper / mobile architecture (van builds, expedition pods, glass trailers)
- 0–1 pin: New / emerging visual (aircraft, earth shelter, bioclimatic, parametric)

**Always include:**
- EcoFlow brand (Delta Pro, Pro series) — always mention and show with green LED
- "No people visible" in every AI prompt
- Material specificity: name the material, the weathering stage, the joinery type
- Interior warmth: always a "warm amber glow" visible inside any glass structure

**Never include:**
- Generic "modern house" without a specific off-grid or unconventional element
- People (humans) in any pin
- Urban residential architecture without a dramatic natural setting

### 7B. Smart Pet Wellness
**Mission:** Premium aspirational pet content — Wilderkind wildlife portraits and adventure dog lifestyle.

**Content Split per batch (10 pins):**
- 4 pins: **Wilderkind** — wild predator cats in dramatic natural settings
- 4 pins: **Adventure Dogs** — specific breeds in named US locations at peak action
- 2 pins: **Indoor Luxury** — domestic cats (specific rare breeds) in architectural interiors (often boathouse, glass cabin, skylight)

**Wilderkind Rules:**
- Always use "Wilderkind aesthetic" in the AI prompt
- Never repeat a species within the same batch (rotate across: Snow Leopard, Jaguar, Puma, Caracal, Lynx, Clouded Leopard, Serval, Wolverine, Arctic Fox, Red Fox, etc.)
- Always: direct eye contact, low angle, dramatic light (twilight/golden hour/moonlight), rim-light on fur
- Never: cute/domesticated framing, bright midday flat light, cluttered backgrounds

**Adventure Dog Rules:**
- Always name the specific breed — never "a dog"
- Always name the US location — never generic "mountains"
- Always include peak action (mid-gallop or mid-leap for dogs, alert standing for cats)
- Always specify the breed's distinctive physical feature in the prompt
- No people. No leash visible.

**Indoor Luxury Rules:**
- Setting must be architecturally interesting (glass boathouse, skylight window seat, floating glass shelf)
- Light source must be specific (lake-reflected aquamarine, amber interior, moonlight from circular skylight)
- Rare/distinguished breeds only (Maine Coon, Norwegian Forest Cat, Birman, Russian Blue, Turkish Angora, Bengal, etc.)

### 7C. Build. Scale. Ship. — Software Studio
**Mission:** Direct lead generation for the software studio. Target: business owners (SMEs and startups) who have a software problem and need a professional team to solve it. Every pin must address a **specific business pain point** and make the studio the obvious answer.

**What the studio offers (use these in content):**
- Custom web applications and mobile apps
- Salon booking management system (productised)
- Tuition institute management system (productised)
- Business websites and e-commerce
- Digital transformation for small businesses

**Pin Architecture per day:**
- **Slot-7 (6:30pm) — Studio Lifestyle:** A premium workspace visual inside an aspirational setting. Monitors show studio work (client project dashboard, app UI design, booking system interface, Figma prototype). The visual says: "This is a professional team that delivers premium results."
- **Slot-8 (9:00pm) — Business Pain Infographic:** A dark editorial infographic that speaks directly to a business owner's software-related pain point. Opens with the problem they have today. Closes with a clear positioning of the studio as the solution. **No jargon. Business language only.**

**Infographic Design Specification:**
```
Background: Deep charcoal (#0d0d1a or #1a1a2e)
Title: Bold white — always opens with a BUSINESS PAIN POINT, not a tech concept
  Examples: '5 Signs Your Salon Is Losing Bookings to Bad Software'
           'Why Your Business Needs a Custom App (Not Another Spreadsheet)'
           'The Hidden Cost of Manual Booking Systems'
Subtitle: Amber (#f59e0b)
Accent: Teal for solution elements, Red for problem elements, Green for outcome/result
Footer: Always ends with a clear CTA-adjacent statement (not a direct CTA, but implies one)
  Example: 'The right software pays for itself in 90 days.'
Language: Business owner language — no technical jargon
```

**Business Pain Topics to rotate across batches:**
- Salon / beauty business: losing bookings, no-shows, manual scheduling chaos, WhatsApp booking mess
- Tuition centres / education: manual fee tracking, student management, parent communication
- Retail / hospitality: inventory management, customer data, loyalty systems
- General SME: why custom software beats off-the-shelf, ROI of a proper web app, cost of bad tech
- Startups: MVP development, when to build vs buy, how to brief a dev team correctly

**Studio Workspace Specification:**
```
Always: No person visible at the desk
Always: Monitors showing real studio work:
  - Figma app UI design (booking system, dashboard, mobile app screens)
  - Client project management board (Linear or Notion)
  - App prototype or live product in browser
  - Analytics dashboard showing a client's business metrics improving
Desk materials: live-edge walnut, glass top, clean modern studio aesthetic
Settings: Modern studio office, glass cabin, premium co-working space, rooftop studio
```

---

## 8. COPY GUIDELINES

### Titles
- Must be SEO-optimised and emotion-driven
- Format: `[Specific Visual Hook] | [Benefit/Category Keyword] YYYY`
- Example: `"Float Plane Dock Glass Boathouse | Off-Grid Waterfront Architecture 2026"`
- Must include: the year (2026 or current year), a specific visual descriptor, a category keyword
- Length: 60–100 characters ideal
- No emojis in titles

### Descriptions
- **Always begin with:** `"Save this for your [specific interest] board."`
  - Be specific: not "off-grid board" but "off-grid waterfront and float plane architecture board"
- Length: 150–250 words
- Tone: conversational, narrative-driven, aspirational but grounded
- Must include: an explicit call to save ("Save this before it disappears from your feed.")
- Must include: 5–7 hashtags at the end, inline with the description text
- Include brand/lifestyle terms where relevant: EcoFlow, Starlink, Wilderkind, Jackery, off-grid
- No destination URLs

### Alt Text
- Purpose: Visual search SEO + accessibility
- Must specify: materials, animal breeds (exact), light conditions, landscape type, structural elements
- Length: 2–4 sentences, highly descriptive, no fluff
- Format: reads like a precise visual description for someone who cannot see the image

### In-App Text Hook
- 4–7 words maximum
- Bold, punchy, high contrast — this appears as a text overlay on the pin
- Avoid generic: "save this", "click here", "amazing"
- Should intrigue, provoke, or create desire — never describe what's already visible
- Examples: `"Float. Fly. Off-grid."` / `"Two worlds. One predator."` / `"Stop selling hours. Now."`

---

## 9. AI IMAGE PROMPT SPECIFICATION (for Nano Banana)

**Standard prompt structure — use this format for every pin:**

```
Hyper-realistic 9:16 vertical photo, [Style Tag]. [Subject description in detail] + 
[US geographic setting with specific markers] + [specific lighting condition] + 
[interior/exterior elements visible] + [affinity elements: Watercraft/Corten/Aircraft/Timber] + 
[composition details: angle, framing] + [No people visible.] + 
[8k, cinematic photography style descriptor.]
```

**Style Tags (use one per pin):**
- `Style A Quiet Luxury` — for architecture, pet, and lifestyle pins. Cinematic, film-quality, soft-premium aesthetic.
- `Style B Dynamic Viral` — for SE-Infographic pins ONLY. Clean editorial, high contrast, dark background.
- For nail pins: use `"Hyper-realistic 9:16 vertical editorial nail photograph"` as the opener instead.

**Lighting vocabulary to rotate:**
- `dawn mist at water level` / `golden hour side-light from the left` / `cool twilight rim-light` / `diffused coastal fog light` / `harsh noon raking desert light` / `silver lunar moonlight` / `pale alpine blue dawn` / `warm amber interior glow` / `direct overhead noon summer light`

**Mandatory inclusions in architecture AI prompts:**
- EcoFlow system reference (on floor, barely visible, green LED indicator)
- "No people visible" — must appear in every non-infographic prompt
- Interior warmth: "warm amber interior visible" for all glass structures

**Mandatory inclusions in Wilderkind AI prompts:**
- "Wilderkind aesthetic" at the start of the subject description
- Shot angle: "slightly lower than eye level" or "from ground level looking up"
- "No people." at the end

---

## 10. CSV SCHEMA — EXACT HEADERS AND FIELD RULES

> ⚠️ Use these headers exactly, in this order, every batch. Do not add or remove columns.

```csv
"Post #","Pinterest board","Title","Description","Alt Text","AI Prompt","In-App Text Hook","Status","Posting Day","Slot","SL Post Time"
```

| Field | Rule |
|---|---|
| `Post #` | Sequential 1–45 (for standard 5-day batch) |
| `Pinterest board` | Exact board name from Section 2 — copy-paste, no paraphrase |
| `Title` | See Section 8 — must include year (2026), specific visual, category keyword |
| `Description` | Must start "Save this for your [specific] board." — 150–250 words + 5–7 hashtags |
| `Alt Text` | 2–4 sentences, material/breed/light/landscape specific |
| `AI Prompt` | Full detailed prompt following Section 9 structure |
| `In-App Text Hook` | 4–7 words, punchy, not generic |
| `Status` | Always `"Ready"` |
| `Posting Day` | Format: `"Day 1 — Mon June 9"` (full weekday + date) |
| `Slot` | One of: `Slot-1` / `Slot-2` / `Slot-3` / `Slot-4` / `Slot-5` / `Slot-6` / `Slot-7` / `Slot-8` |
| `SL Post Time` | EST time: `7:30am` / `9:30am` / `11:00am` / `12:30pm` / `2:00pm` / `3:30pm` / `6:30pm` / `9:00pm` |

---

## 11. OUTPUT FILE NAMING CONVENTION

```
Pinterest_Next[PIN COUNT]_PostIdeas_[StartMonthDay]_[EndMonthDay]_v[VERSION].csv
```

**Examples:**
- `Pinterest_Next45_PostIdeas_July26_July30_v21.csv` ✅
- `Pinterest_Next45_PostIdeas_Aug3_Aug7_v22.csv` ✅

**Rules:**
- `[PIN COUNT]` = total pins in the batch (always 45 for standard 5-day batch)
- Version number increments by +1 from the previous batch's version
- Save directly to: `c:\Mithuranga\printerest-project\pinterest project\`
- Do NOT output the full CSV content in the chat window — write directly to file and confirm

---

## 12. HASHTAG STRATEGY

**Rule:** 5–7 hashtags per pin, inline at the end of the Description field. Mix board-specific + content-specific tags.

### Board Hashtag Banks

**Future Living & Off-Grid Tech (rotate, 3–4 per pin):**
`#OffGridLiving` `#FutureLiving` `#GlassArchitecture` `#OffGridHome` `#SustainableArchitecture` `#ModernCabin` `#WatercraftArchitecture` `#EcoFlow` `#OffGridTech` `#GlassBoathouse` `#FloatPlane` `#CortenSteel` `#MetalArt` `#TimberArchitecture` `#JapaneseJoinery` `#VanLife` `#CampersRV` `#SierraNevada` `#PNWArchitecture` `#JoshuaTree` `#ColoradoRockies`

**Smart Pet Wellness (rotate, 3–4 per pin):**
`#Wilderkind` `#AdventureDog` `#DogPhotography` `#CatPhotography` `#PetWellness` `#AnimalPhotography` `#WildlifePhotography` `#PredatorPortrait` + [breed-specific hashtag] + [location hashtag]

**Build. Scale. Ship. — Software Studio (rotate, 4–5 per pin):**
`#FreelanceDev` `#BuildInPublic` `#SoloFounder` `#TechConsulting` `#RemoteWork` + [topic hashtag e.g. `#ClientAcquisition` `#FractionalCTO` `#SaaSFounder` `#StartupLife`]

---

## 13. PERFORMANCE INTELLIGENCE (Updated August 22, 2026)

### 🚀 Audience Growth
| Date | Monthly Audience | Growth |
|---|---|---|
| July 22, 2026 | **220,000** | baseline tracking |
| July 28, 2026 | **253,000** | **+15% in 6 days** |
| August 4, 2026 | **285,000** | **+12.6% in 7 days** |
| August 15, 2026 | **338,000** | **+18.6% in 11 days** |
| August 19, 2026 | **365,000** | **+8.0% in 4 days — 3.7x growth since June** |

### Board Velocity (July 23 – August 22, 2026)
| Board | Impressions | Saves | Trend |
|---|---|---|---|
| Future Living & Off-Grid Tech | **418,152** | **2,749** | ⬆️ #1 by far — DOMINATING |
| Smart Pet Wellness | **164,188** | **963** | ⬆️ #2, strong save rate |

### Affinity Score Changes (Aug 4 → Aug 15 → Aug 19, 2026)
| Interest | Aug 4 | Aug 15 | Aug 19 | Trend |
|---|---|---|---|---|
| **Campers & RV** | 7.769x | 8.568x | **8.718x** | ⬆️ NEW ALL-TIME RECORD — 6th consecutive rise |
| **Watercraft** | 7.070x | 7.412x | **7.379x** | ↔️ stable above 7.3x |
| **Metal Art** | 6.156x | 6.583x | **6.596x** | ↔️ stable above 6.5x |
| **Cycling** | 5.064x | 5.435x | **5.457x** | ↔️ stable above 5.4x |
| **Aircraft** | 4.643x | 4.883x | **4.880x** | ↔️ stable near 4.9x |
| **Woodworking** | 4.130x | 4.369x | **4.386x** | ↔️ slow steady climb |

### All-Time Top Pin Themes (by Impressions — updated August 22)
| Rank | Visual Formula | Impressions | Board |
|---|---|---|---|
| 1 | Glass + watercraft + water mirror symmetry | **41,537** | Future Living |
| 2 | Architecture/landscape/vehicle pin | **38,897** | Future Living |
| 3 | Architecture/landscape pin | **35,554** | Future Living |
| 4 | Architecture/vehicle pin | **32,714** | Future Living |
| 5 | Other FL / Smart Pet pin | **19,063** | Future Living / Smart Pet |

**Key takeaway:** All four top pins now above 32k impressions — the top is at 41,537. Campers & RV affinity at 8.718x is the highest ever recorded. Daily impressions now running 25–28k/day as the new normal. Campers & RV must appear in ≥60% of all FL pins.

---

## 14. QUALITY CHECKLIST (Run Before Saving CSV)

```
[ ] Exactly 30 rows (pins 1–30) present — no truncation, no skipped lines
[ ] Timeline is correct: 5 days, 6 pins per day
[ ] Every Title contains the current year + visual descriptor + category keyword
[ ] Every Description starts with "Save this for your [specific] board."
[ ] Every Description ends with 5–7 hashtags
[ ] Every AI Prompt contains "No people visible"
[ ] No species/breed repeated in Wilderkind pins within the same batch
[ ] No US location repeated more than 2x per board per batch
[ ] Tier 1 affinity elements (Campers & RV 8.72x + Watercraft 7.38x + Metal Art 6.60x) appear in ≥60% of Future Living pins
[ ] VARIETY CHECK: No more than 2 glass boathouse / mirror water pins per batch
[ ] VARIETY CHECK: No more than 2 Corten steel cantilever pins per batch
[ ] File named correctly and saved to project folder — NOT output in full to chat window
[ ] Status column = "Ready" for all 30 rows
```

---

## 15. REVISION HISTORY

| Version | Date | Change |
|---|---|---|
| v1.0 | June 8, 2026 | Initial document created from v9–v13 batch learnings |
| v1.1 | June 12, 2026 | Code board repositioned: freelance → software studio (agency+products). Nail prompts upgraded. Board renamed to 'Build. Scale. Ship. — Software Studio'. Performance intel updated to 115k audience. |
| v1.2 | July 25, 2026 | **Major update:** Nail board discontinued. Schedule updated to 9 slots/day across 3 boards (Future Living + Smart Pet + Build.Scale.Ship), 45 pins/5-day batch. Mon–Fri restriction removed — now flexible 5-day batch. Audience updated to 220k. Campers & RV elevated to Tier 1 (6.328x — major surge). Watercraft updated to 6.491x. Variety rules added to Quality Checklist to prevent repetitive visual formulas. |
| v1.3 | July 31, 2026 | **Affinity update:** Campers & RV overtook Watercraft as #1 affinity at 7.140x (all-time high). Watercraft updated to 6.759x. Metal Art jumped to 5.760x. Aircraft up to 4.463x. Woodworking up to 3.943x. Audience updated to 253,000. Board velocity updated with July full-month data. Top pin impressions updated to 25,948. |
| v1.4 | August 10, 2026 | **Major structure change:** Build.Scale.Ship board HALTED. Schedule reduced to 6 posts/day (3 Future Living + 3 Smart Pet = 30 pins/batch). Sri Lankan tourism board (Arachi Tours) planned as replacement — details TBD. Affinity updated: Campers & RV 7.769x (#1), Watercraft 7.070x, Metal Art 6.156x (crossed 6x, now Tier 1), Woodworking 4.130x (crossed 4x), Cycling 5.064x (new entrant). Audience at 285,000. Top pin at 31,902 impressions. |
| v1.5 | August 18, 2026 | **Audience & Affinity surge:** Audience exploded to 338,000. Campers & RV spiked to 8.568x, Watercraft 7.412x, Metal Art 6.583x. Top pin approached 39k impressions. Future Living board at 394k monthly impressions. |
| v1.6 | August 22, 2026 | **Continued acceleration:** Audience at 365,000 (3.7x since June). Campers & RV hit new all-time record 8.718x. All other Tier 1/2 affinities stable-to-rising. Top pin at 41,537 impressions. Daily impressions new baseline 25–28k/day. Future Living board at 418k monthly impressions. |

---

*This document is the single source of truth for all Pinterest content generation sessions. Update this file whenever a new board is added, a significant affinity score change is detected, or a new winning visual formula is identified.*
