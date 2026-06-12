# Pinterest Content Generation Brief — Master SOP
**Account:** `pinterest.com/wildbuild`
**Reader:** Claude Sonnet (AI agent) — this document is your primary instruction set for every batch session.
**Last Updated:** June 12, 2026 (v1.1)

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
| **Total Monthly Audience** | **115,000** (jumped from 99k → 115k between June 4–9, 2026) |
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
| `Future Living & Off-Grid Tech` | `pinterest.com/wildbuild/future-living-off-grid-tech/` | Slot-1 (7:30am) + Slot-4 (12:30pm) | Static Image |
| `Smart Pet Wellness` | `pinterest.com/wildbuild/smart-pet-wellness-eco-tech-quiet-luxury/` | Slot-2 (9:30am) + Slot-6 (3:30pm) | Static Image |
| `Nail Aesthetic & Art Inspo` | `pinterest.com/wildbuild/nail-aesthetic-art-inspo/` | Slot-3 (11:00am) + Slot-5 (2:00pm) | Static Image |
| `Build. Scale. Ship. — Software Studio` | `pinterest.com/wildbuild/build-scale-ship-software-studio/` | Slot-7 (6:30pm) + Slot-8 (9:00pm) | Static Image |

> ⚠️ **Board renamed from v13:** `Code. Build. Ship. — Freelance Tech Life` → `Build. Scale. Ship. — Software Studio` (effective v14, June 16 2026)

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
**Mission:** Eye-catching, scroll-stopping nail art that earns saves from a beauty audience — with a visual upgrade to ultra-sharp photorealism and bold dramatic styling that outperforms generic nail content.

**Board Aesthetic Direction:**
- **Primary aesthetic:** Ultra-photorealistic, drama-first, luxury editorial — think Vogue beauty shoot meets nail close-up
- **Visual quality bar:** Every pin must feel like it was shot in a premium photography studio. The nail finish texture (chrome shift, gel gloss, glitter refraction) must be the hero.
- **Avoid:** Flat lighting, generic simple sets, basic pink without drama, anything that looks like a phone selfie

**10 Nail Designs per batch — v14+ Format Mix (Trending 2026):**
| Format | Per Batch | 2026 Trend Notes |
|---|---|---|
| 3D Gel Gem / Crystal | 2 | Swarovski-style crystals, jelly gem nails, faceted stone embeds — shoot with macro lens to show refraction |
| Chrome Powder / Cat-Eye Gel | 2 | Duochrome shift nails, cat-eye magnetic gel (colour-shifting under light), mirror-finish chrome powder |
| Holographic / Aurora | 2 | Rainbow holographic foil, aurora shifting nails, multichromatic iridescent gel |
| Dark Luxury Matte | 1 | Black jelly nails, ink-dark gel, deep gothic plum — matte velvety surface |
| Glazed / Glass Effect | 1 | Sheer glazed nude, glass nails with inner shimmer, ice-effect gel |
| Trend Statement | 2 | Rotate: coquette 3D bow, stiletto chrome, summer jewel tone, nail art as wearable art |

**UPGRADED Nail AI Prompt Specification (v14+):**

Use this enhanced template for ALL nail pins:
```
Ultra-photorealistic 9:16 vertical macro nail photograph, shot on a Phase One medium format camera.
[Nail description: shape, length, finish type in extreme detail — describe the optical properties
of the finish, e.g. 'the chrome powder creates a mirror that reflects the studio lights as two
pinpoint hotspots on each nail surface'].  
[Backdrop: premium studio surface — black obsidian stone / wet smoked glass / brushed gold metal
/ crumpled black silk / deep navy crushed velvet / frosted acrylic].  
[Styling props: 1–2 objects — Swarovski crystal, fresh flower petal, liquid mercury droplet,
gold leaf flake, cut gemstone, rose gold chain].  
[Lighting: specify exactly — 'single hard light source from the left creating a sharp chrome
reflection' / 'two softbox lights creating a clean double-hotspot on the chrome finish' /
'ring light creating a perfect circular reflection in each nail'].  
[Composition: overhead flat-lay / 45-degree angle / extreme close-up of 3 nails / side profile
showing nail depth / fan-spread fingers].  
8k, tack-sharp nail macro photography, nail finish is the hero of the shot.
```

**Key visual upgrades vs previous batches:**
- Describe the **optical physics** of the finish in the prompt (how light behaves on the surface)
- Use **premium backdrops** that create contrast and drama (obsidian, smoked glass, crushed velvet)
- Include **props with texture** that echo the nail finish (crystals for gem nails, liquid for glazed)
- Specify **exact lighting** — not just 'side light' but 'a single 1x1 softbox at 45 degrees creating a gradient reflection'
- Push **extreme close-up framing** on hero nails — 2–3 nails filling the frame, not a full 5-finger spread

**2026 High-Search Nail Keywords to rotate through:**
`3D nail art`, `crystal nails`, `gem nails`, `chrome nails 2026`, `cat eye nails`, `holographic nails`,
`aurora nails`, `glazed nails`, `jelly nails`, `coquette nails`, `dark nails`, `glass nails`,
`duochrome nails`, `nail inspo 2026`, `quiet luxury nails`

### 7D. Build. Scale. Ship. — Software Studio
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

## 13. PERFORMANCE INTELLIGENCE (Updated June 12, 2026)

### 🚀 Audience Growth
| Date | Monthly Audience | Growth |
|---|---|---|
| June 4, 2026 | 99,000 | baseline |
| June 9, 2026 | **115,000** | **+16% in 5 days** |

### Board Velocity (May 13 – June 12, 2026)
| Board | Impressions | Saves | Save Rate | Trend |
|---|---|---|---|---|
| Smart Pet Wellness | **84,127** | **450** | 0.53% | ⬆️ New high — best board |
| Future Living & Off-Grid Tech | **80,274** | **259** | 0.32% | ⬆️ Steady |
| Build. Scale. Ship. | **9,248** | **28** | 0.30% | ⬆️ +87% saves vs prior period |
| Nail Aesthetic & Art Inspo | **22** | **0** | — | 🆕 Brand new — needs visual upgrade |

### Affinity Score Changes (June 4 → June 9, 2026)
| Interest | June 4 | June 9 | Change |
|---|---|---|---|
| **Watercraft** | 5.858x | **5.925x** | ⬆️ +0.067 — still #1, growing |
| **Metal Art** | 5.213x | 5.130x | ↘️ -0.083 — minor dip, stable |
| **Campers & RV** | 4.910x | 4.766x | ↘️ -0.144 — softening, reduce priority |
| **Aircraft** | 4.286x | 4.281x | → Stable |
| **Illustration** | 1.382x | 1.405x | ⬆️ +0.023 — supports editorial nail content |
| **Body Art** | 1.164x | 1.182x | ⬆️ +0.018 — nail board signal growing |

### All-Time Top Pin Themes (by Impressions — updated June 12)
| Rank | Visual Formula | Impressions | Board |
|---|---|---|---|
| 1 | Glass + watercraft + water mirror symmetry | **20,115** | Future Living |
| 2 | Mirrored glass on still water | 8,725 | Future Living |
| 3 | Modular floating glass dock platform | 8,334 | Future Living |
| 4 | Wilderkind predator + twilight rim-light | 8,259 | Smart Pet |
| 5 | PNW glass + amber interior | 6,114 | Future Living |

**Key takeaway:** The #1 pin grew from 16,081 → **20,115 impressions** — it's still gaining. Water reflection formula is compounding. Double down every batch.

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
| v1.1 | June 12, 2026 | Code board repositioned: freelance → software studio (agency+products). Nail prompts upgraded to ultra-photorealistic macro with 3D/holographic/cat-eye trending formats. Board renamed to 'Build. Scale. Ship. — Software Studio'. Performance intel updated to 115k audience milestone. |

---

*This document is the single source of truth for all Pinterest content generation sessions. Update this file whenever a new board is added, a significant affinity score change is detected, or a new winning visual formula is identified.*
