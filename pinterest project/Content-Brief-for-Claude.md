# Pinterest Content Generation Brief — Master SOP
**Account:** `pinterest.com/wildbuild`
**Reader:** Claude Sonnet (AI agent) — this document is your primary instruction set for every batch session.
**Last Updated:** June 8, 2026

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

[ ] 4. Note the batch dates: next batch always runs Mon–Fri (5 days).
        Calculate Day 1 as the next Monday after the current date.

[ ] 5. Confirm the output filename follows the naming convention
        (see Section 9) before writing the CSV.
```

---

## 🚀 COPY-PASTE SESSION STARTER PROMPT

Use this prompt at the start of every new batch session:

```
Role: You are a Pinterest Growth Scientist and AI Content Strategist
for the @wildbuild Pinterest account. Your task is to generate a new
5-day content plan (40 pins, 8 pins/day, Mon–Fri).

Follow the instructions in Content-Brief-for-Claude.md exactly.

Step 1: Read the two most recent analytics files in the project folder
(Analytics overview CSV + audience-insights total audience CSV).
Extract top pin performance, board velocity, and affinity score changes.

Step 2: Cross-reference top pin IDs with previous PostIdeas CSVs to
identify the winning visual formulas to replicate.

Step 3: Generate the 40-pin CSV for [INSERT NEXT MONDAY DATE] to
[INSERT NEXT FRIDAY DATE] following the CSV schema in the brief exactly.

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
| **Total Monthly Audience** | ~99,000 (growing ~18% over 5 weeks as of June 2026) |
| **Primary Device** | Web (46.8%), Android Mobile (40.6%), iPhone (33.1%) |

### Software Engineering Identity (for Code board)
The account owner is a **software engineer** building a freelance consulting practice targeting **startup founders** as clients. The Code board is a **lead generation channel** — not just tech content. Every Code pin must either:
- Attract a startup founder who needs a developer, or
- Position the account owner as a high-value senior/principal engineer worth $15K–$25K/month in consulting fees.

**Target client:** Early-stage startup founders (pre-seed to Series B), building SaaS products, usually non-technical or with small engineering teams.

---

## 2. ACTIVE BOARDS — EXACT NAMES & PINTEREST URLS

> ⚠️ Always use these exact board names. Copy-paste — do not paraphrase.

| Board Name | Pinterest URL | Daily Slots | Post Type |
|---|---|---|---|
| `Future Living & Off-Grid Tech` | `pinterest.com/wildbuild/future-living-off-grid-tech/` | Slot-1 (7:30am) + Slot-4 (12:30pm) | Static Image |
| `Smart Pet Wellness` | `pinterest.com/wildbuild/smart-pet-wellness-eco-tech-quiet-luxury/` | Slot-2 (9:30am) + Slot-6 (3:30pm) | Static Image |
| `Nail Aesthetic & Art Inspo` | `pinterest.com/wildbuild/nail-aesthetic-art-inspo/` | Slot-3 (11:00am) + Slot-5 (2:00pm) | Static Image |
| `Code. Build. Ship. — Freelance Tech Life` | `pinterest.com/wildbuild/code-build-ship-freelance-tech-life/` | Slot-7 (6:30pm) + Slot-8 (9:00pm) | Static Image |

---

## 3. DAILY POSTING SCHEDULE

**8 pins per day · 5 days (Monday–Friday) · 40 pins per batch**
All times are **US Eastern Standard Time (EST)**.

| Slot | Time (EST) | Board | Pin Sub-Type |
|---|---|---|---|
| Slot-1 | 7:30am | Future Living & Off-Grid Tech | Architecture / Landscape |
| Slot-2 | 9:30am | Smart Pet Wellness | Wilderkind or Adventure Dog |
| Slot-3 | 11:00am | Nail Aesthetic & Art Inspo | Nail Art / Trend |
| Slot-4 | 12:30pm | Future Living & Off-Grid Tech | Material / Tech / Detail |
| Slot-5 | 2:00pm | Nail Aesthetic & Art Inspo | Nail Art / Trend |
| Slot-6 | 3:30pm | Smart Pet Wellness | Adventure Dog or Indoor Luxury |
| Slot-7 | 6:30pm | Code. Build. Ship. | SE-Lifestyle (workspace image) |
| Slot-8 | 9:00pm | Code. Build. Ship. | SE-Infographic (dark editorial) |

---

## 4. AUDIENCE AFFINITY SCORES (June 2026 Baseline)

These are the **multiplier scores** showing how much more likely our audience is to engage with a topic vs. the average Pinterest user. Use these to prioritise visual concepts.

> ⚠️ Always read the latest audience CSV at the start of each session and note any scores that have changed significantly (>0.3 change). Flag changes in your pre-generation analysis.

### 🔴 Tier 1 — Hyper-Affinity (5x+): Must appear in ≥40% of Future Living pins
| Interest | Affinity Score | Application |
|---|---|---|
| **Watercraft** | **5.858x** | Glass boathouses, floating platforms, custom lake docks, seaplane docks, pontoon architecture |
| **Metal Art / Industrial** | **5.213x** | Corten steel cladding, raw I-beam frames, welded steel facades, steel joinery |

### 🟠 Tier 2 — High Affinity (4–5x): Target ≥20% of Future Living pins
| Interest | Affinity Score | Application |
|---|---|---|
| **Aircraft** | **4.286x** *(rising)* | Float planes moored at glass cabins, seaplane ramps, hangar-aesthetic buildings, Cessna 185 aesthetics |
| **Campers & RV** | **4.91x** | Ultra-luxury van builds, glass pod trailers, Land Cruiser expedition rigs |

### 🟡 Tier 3 — Strong Affinity (3–4x): Weave through both Future Living and nail content
| Interest | Affinity Score | Application |
|---|---|---|
| **Woodworking** | **3.728x** | Japanese joinery, live-edge slabs, timber frames, shou sugi ban decking |
| **Cycling** | **3.984x** | (lower priority — keep in mind for outdoor lifestyle content) |
| **Exterior / Door Design** | **3.349x / 3.449x** | Architectural entrance sequences, threshold moments, exterior material details |
| **Educational Architecture** | **4.330x** | Glass structure engineering logic, parametric design, structural honesty |

### 🟢 Tier 4 — Moderate Affinity: Supporting context
| Interest | Score | Notes |
|---|---|---|
| Landscape & Urbanism Architecture | 2.545x | Background context for architecture pins |
| Garden Design | 2.513x | Outdoor spaces around cabins |
| Mosaic / Poster Design | 2.132x / 2.334x | Design-adjacent content |
| Body Art / Nails | 1.164x / 0.528x | Supports nail board — growing signal |
| Illustration | 1.382x | Supports design-forward nail art content |

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

### 7C. Nail Aesthetic & Art Inspo
**Mission:** Aspirational nail art content aligned with quiet luxury aesthetics — attracts the beauty-interest segment of the audience while maintaining aesthetic coherence with the off-grid/architecture visual language.

**Board Aesthetic Direction:**
- **Primary aesthetic:** Quiet luxury, editorial, dark and moody, material-focused
- **Avoid:** Bright neon, generic pink, overtly maximalist sets, heavily decorated "TikTok" nail art
- **Align with:** The same audience that saves Corten steel cabins and dark chrome architecture

**10 Nail Designs per batch — Rotating Format Mix:**
| Format | Per Batch | Description |
|---|---|---|
| Dark Chrome / Metallic | 2 | Chrome silver, chrome burgundy, mercury, dark gold |
| Glass / Aurora / Glazed | 2 | Translucent, ice-effect, glazed donut chrome |
| Dark Matte | 1 | Forest green, charcoal, deep plum, wine matte |
| Neutral Luxury | 1 | Mocha latte, nude pearl, caramel soft gel |
| Editorial Nail Art | 2 | Marble, abstract line, minimalist negative space |
| Trend-Led | 2 | Coquette/bow, coastal, seasonal, high-search trend |

**Nail Photography Style (for AI Prompt):**
- Always: "Hyper-realistic 9:16 vertical editorial nail photograph"
- Always specify: nail shape (almond / oval / coffin / square / stiletto), length, finish (matte / chrome / gel / glazed)
- Always include: a specific backdrop (marble, slate, silk, driftwood, velvet, linen) and 1 styling prop (dried flower, pearl, ring, sea glass, orchid)
- Always specify: light direction (directional side light / overhead / soft warm / hard single source)
- Never: show the full arm — close-up hand only, palm-down or fingers slightly fanned

**2026 High-Search Nail Keywords to rotate through:**
`chrome nails`, `glazed donut nails`, `quiet luxury nails`, `glass nails`, `aurora nails`, `coquette nails`, `matte nails`, `marble nail art`, `mocha latte nails`, `abstract nail art`, `dark nails`, `coastal nails`

### 7D. Code. Build. Ship. — Freelance Tech Life
**Mission:** Lead generation for software engineering consulting. Target: startup founders who need a senior/principal-level freelance developer. Position the account owner as a fractional CTO / senior dev worth $15K–$25K/month.

**Pin Architecture per day:**
- **Slot-7 (6:30pm) — SE-Lifestyle:** A workspace photograph inside an aspirational off-grid or urban-premium setting, with monitor screens showing client-facing work (proposals, pipelines, architecture diagrams, revenue dashboards). The visual says: "This person is successful, commands high fees, and works from extraordinary places."
- **Slot-8 (9:00pm) — SE-Infographic:** A dark editorial infographic providing genuine strategic value to a startup founder — positioning, pricing, client acquisition, tech stack, team scaling. The information says: "This account understands how to build a startup. Follow for more."

**SE-Infographic Design Specification:**
```
Background: Deep charcoal (#0d0d1a or #1a1a2e)
Title: Bold white, Outfit or Inter font
Subtitle: Amber (#f59e0b or similar)
Accent colours: Amber (primary), Teal (#14b8a6, secondary), Green (#22c55e for positive outcomes), Red (#ef4444 for warnings)
No photography inside the infographic
Footer: Always includes an amber-coloured summary statement or stat
Layout: Clean, structured, scannable — no decorative flourishes
```

**SE-Lifestyle Workspace Specification:**
```
Always: No person visible at the desk
Always: Monitors showing specific, legible content (real UI: Stripe, Notion, GitHub, Figma, Linear, Loom, CRM pipeline)
Always: Named revenue figures on screen (e.g. "$18,400 MRR", "$28K retainer")
Always: EcoFlow system on the floor with green LED
Always: Aspirational view through glass (lake, float plane dock, city skyline, red rocks, forest)
Desk materials: live-edge walnut, concrete top, Corten steel frame — rotate between batches
Settings: Rotate between PNW glass cabin lake, Sedona glass office, Sierra Nevada cabin, NYC glass loft, SF Bay office, Austin glass loft, Pacific Coast van
```

**SE Content Themes to rotate (never repeat same theme in consecutive batches):**
- Client acquisition: cold outreach, proposal writing, pipeline management
- Pricing strategy: hourly → retainer → outcome-based → fractional CTO
- Positioning: niche definition, language shift, founder psychology
- Tech content: SaaS MVP stack, system architecture, scaling decisions
- Income milestone: MRR growth reality, revenue model, agency transition
- Team/business: delegation, hiring, remote culture, agency model

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
"Post #","Board","Title","Description","Alt Text","AI Prompt","In-App Text Hook","Status","Posting Day","Slot","SL Post Time"
```

| Field | Rule |
|---|---|
| `Post #` | Sequential 1–40 (for standard 5-day batch) |
| `Board` | Exact board name from Section 2 — copy-paste, no paraphrase |
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
- `Pinterest_Next40_PostIdeas_June9_June13_v13.csv` ✅
- `Pinterest_Next40_PostIdeas_June16_June20_v14.csv` ✅

**Rules:**
- `[PIN COUNT]` = total pins in the batch (always 40 for standard 5-day batch)
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

**Nail Aesthetic & Art Inspo (rotate, 4–5 per pin):**
`#NailInspo` `#NailAesthetic` `#GelNails` `#NailArt` `#QuietLuxuryNails` + [colour/trend hashtag e.g. `#ChromeNails` `#GlassNails` `#MattNails`] + [seasonal e.g. `#SummerNails` `#AutumnNails`]

**Code. Build. Ship. (rotate, 4–5 per pin):**
`#FreelanceDev` `#BuildInPublic` `#SoloFounder` `#TechConsulting` `#RemoteWork` + [topic hashtag e.g. `#ClientAcquisition` `#FractionalCTO` `#SaaSFounder` `#StartupLife`]

---

## 13. PERFORMANCE INTELLIGENCE (Updated June 2026)

### Board Velocity (May 8 – June 7, 2026)
| Board | Impressions | Saves | Save Rate | Trend |
|---|---|---|---|---|
| Smart Pet Wellness | 75,750 | **389** | 0.51% | ⬆️ +26% saves vs previous period |
| Future Living & Off-Grid Tech | 76,114 | **246** | 0.32% | ⬆️ Stable growth |
| Code. Build. Ship. | 6,626 | **15** | 0.23% | ⬆️ +50% (low base, accelerating) |

### All-Time Top Pin Themes (by Impressions)
| Rank | Visual Formula | Impressions | Board |
|---|---|---|---|
| 1 | Glass + watercraft + water mirror symmetry | 16,081 | Future Living |
| 2 | Mirrored glass on still water | 9,496 | Future Living |
| 3 | Wilderkind predator + twilight rim-light | 8,191 | Smart Pet |
| 4 | Modular floating glass dock platform | 7,970 | Future Living |
| 5+ | PNW glass + amber interior / Wilderkind big cat | 5,000–5,500 | Both |

**Key takeaway:** Water reflection + glass transparency is the single most powerful visual formula in the account. Prioritise in every batch.

---

## 14. QUALITY CHECKLIST (Run Before Saving CSV)

```
[ ] Exactly 40 rows (pins 1–40) present — no truncation, no skipped lines
[ ] Timeline is correct: Day 1 = Monday, Day 5 = Friday
[ ] Every Title contains the current year + visual descriptor + category keyword
[ ] Every Description starts with "Save this for your [specific] board."
[ ] Every Description ends with 5–7 hashtags
[ ] Every AI Prompt contains "No people visible" (exception: nail pins — check hand-only framing)
[ ] No species/breed repeated in Wilderkind pins within the same batch
[ ] No US location repeated more than 2x per board per batch
[ ] Tier 1 affinity elements (Watercraft, Metal Art) appear in ≥40% of Future Living pins
[ ] Every SE-Lifestyle workspace pin has named revenue figures on monitor screens
[ ] Every SE-Infographic uses the dark charcoal (#0d0d1a) colour specification
[ ] File named correctly and saved to project folder — NOT output in full to chat window
[ ] Status column = "Ready" for all 40 rows
```

---

## 15. REVISION HISTORY

| Version | Date | Change |
|---|---|---|
| v1.0 | June 8, 2026 | Initial document created from v9–v13 batch learnings |

---

*This document is the single source of truth for all Pinterest content generation sessions. Update this file whenever a new board is added, a significant affinity score change is detected, or a new winning visual formula is identified.*
