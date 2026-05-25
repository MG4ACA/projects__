"""
Pinterest 12-Pin Content Plan | May 11-12, 2026
================================================
Based on: Pinterest Analytics overview 20260311-20260510
          audience-insights-total-audience-2026-05-08

KEY INSIGHTS FROM ANALYTICS:
- Total monthly audience: 35,000
- Top Board: Future Living Off Grid Tech → 38,137 impressions (3x pet board)
- #1 Pin (867646684481475922): 26,625 impressions — 69.8% of entire board = glass/architecture wins
- #2 Pin: 5,953 | #3: 1,849 | #4: 1,656
- Audience high-affinity: Architecture (2.156x), Animals (1.640x), Gardening (1.639x),
  Campers & RV (7.714x!), Vehicles (1.943x), Finance (2.884x)
- Gender: Male 48.8% / Female 44% — balanced
- Age: 25-34 (32.1%), 35-44 (22.5%)
- Top country: US 11.4% (largest single market)

POSTING TIME RATIONALE (Analytics file has daily data only — no hourly breakdown):
  Times optimized using audience demographics:
  - US is top single country (11.4%). Sri Lanka is UTC+5:30, EST is UTC-5.
  - 6:00pm SLST = 7:30am EST → hits US morning scroll (highest US engagement window)
  - 9:00pm SLST = 10:30am EST → hits US mid-morning peak
  - 7:00am SLST = 8:30pm EST (prev day) → hits US prime evening Pinterest scroll
  - 9:00am SLST = 10:30pm EST (prev day) → hits US late night
  - 11:00am SLST = 12:30am EST → reaches global "Other" 57% audience
  - 2:00pm SLST = 3:30am EST → global audience coverage
  Best slots for US reach: 7:00am, 6:00pm, 9:00pm SLST

CONTENT PLAN:
- Day 1 (May 11): 2 Future Living + 2 Pet Wellness + 2 Surfing Ceylon
- Day 2 (May 12): 2 Future Living + 2 Pet Wellness + 2 Surfing Ceylon
- "Others" board = Surfing Ceylon (user-specified new niche board)
- All Future Living pins iterate on #1 pin formula: glass walls + off-grid tech + dramatic landscape
"""

import csv, os

OUTPUT_FILE = r"c:\Mithuranga\printerest-project\pinterest project\Pinterest_Next12_PostIdeas_May11-May12.csv"

FIELDNAMES = [
    "Post #", "Board", "Post Type", "Theme", "Title", "Description",
    "Alt Text", "AI Prompt", "In-App Text Hook", "Status",
    "Posting Day", "Slot", "SL Post Time"
]

# ── Optimised time slots (see rationale above) ────────────────────────────────
TIMES = ["7:00am", "9:00am", "11:00am", "2:00pm", "6:00pm", "9:00pm"]
SLOTS = ["Static-1", "Static-2", "Static-3", "Static-4", "Static-5", "Static-6"]

PINS = [
    # ══════════════════════════════════════════════════════════════════════════
    # DAY 1 — May 11, 2026
    # ══════════════════════════════════════════════════════════════════════════

    # ── Future Living 1 ───────────────────────────────────────────────────────
    {
        "Board": "Future Living & Off-Grid Tech",
        "Post Type": "Static Image",
        "Theme": "Glass / Cliff Edge Ocean Pod Architecture",
        "Title": "Cliff Edge Glass Pod Ocean | Off-Grid Architecture 2026",
        "Description": (
            "Save this for your glass architecture and off-grid living board. "
            "A cantilevered glass pod on a sea cliff edge — EcoFlow Delta Pro on the rock face below "
            "solar panels flush on the pod roof the Pacific horizon at golden hour filling every wall. "
            "The formula that keeps winning. "
            "#GlassCabin #OffGridLiving #CliffHouseArchitecture #FutureLiving "
            "#SolarHome #OffGridTech #CliffEdgeCabin"
        ),
        "Alt Text": (
            "Glass pod cabin cantilevered over sea cliff at golden hour, warm amber interior visible "
            "through floor-to-ceiling glass walls, EcoFlow Delta Pro mounted on cliff face below, "
            "Pacific Ocean horizon line filling background"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a perfectly rectangular full-glass pod cabin "
            "cantilevered on a matte black steel frame projecting directly over a dramatic sea cliff "
            "edge at golden hour, shot from a 20-degree upward angle below the pod so the cliff face "
            "below and the ocean horizon beyond are both simultaneously visible, "
            "the entire cabin is glass on all four sides revealing the warm amber interior — "
            "a minimalist platform bed with white linen facing the ocean, a single Anglepoise lamp "
            "casting amber light in one corner, an EcoFlow Delta Pro x2 battery stack in the far "
            "corner its green LED charge bars glowing, "
            "on the natural rock cliff face directly below the steel cantilever supports an EcoFlow "
            "Delta Pro is wall-bolted to the rock in a matte black steel cradle — its green LED "
            "charge indicator visible against the rock texture, "
            "two flush-mounted matte black solar panels on the flat pod roof at optimal angle toward "
            "the sun, "
            "the cliff drops sheer 80 metres to white ocean surf breaking on dark rocks — "
            "the perspective shows both the vertiginous cliff face below and the Pacific Ocean horizon "
            "at the same level as the pod floor, "
            "the ocean at golden hour is hammered gold, "
            "maximum colour temperature contrast: warm amber interior through glass versus "
            "hammered gold ocean, the steel-and-glass pod is a perfect geometric rectangle on "
            "the cliff edge, no people, 8k, cinematic ocean cliff architectural photography"
        ),
        "In-App Text Hook": "Glass edge. Ocean horizon. Off-grid.",
        "Posting Day": "Day 1 — May 11",
        "Slot": SLOTS[0],
        "SL Post Time": TIMES[0],
    },

    # ── Future Living 2 ───────────────────────────────────────────────────────
    {
        "Board": "Future Living & Off-Grid Tech",
        "Post Type": "Static Image",
        "Theme": "Glass / Northern Lights A-Frame Arctic Cabin",
        "Title": "Northern Lights Glass Cabin | Off-Grid Arctic Architecture 2026",
        "Description": (
            "Save this for your northern lights cabin and off-grid dream board. "
            "A full-glass A-frame under the aurora — Jackery power stack on the cedar deck "
            "the northern lights painting the glass walls emerald the mountain wilderness behind. "
            "This is what off-grid living looks like. "
            "#NorthernLights #AuroraBorealis #GlassCabin #AFrame #OffGridLiving "
            "#FutureLiving #ArcticCabin"
        ),
        "Alt Text": (
            "A-frame glass cabin under aurora borealis at night, emerald and violet northern lights "
            "reflecting on full triangular glass front, warm amber interior visible inside, "
            "Jackery Explorer power station on cedar deck, undisturbed snow mountain landscape"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a classic A-frame cabin where the entire front "
            "triangular face is floor-to-ceiling glass panels, photographed at night under a dramatic "
            "aurora borealis display, "
            "the aurora fills the sky in sweeping curtains of emerald green and deep violet — "
            "the aurora light reflects and refracts through the glass walls creating a double-exposure "
            "effect where the warm amber interior (cream linen platform bed, Anglepoise lamp still on, "
            "oak bedside table) is simultaneously visible through the glass AND the aurora reflects "
            "off the exterior glass surface, "
            "on the exterior cedar deck a Jackery Explorer 2000 Pro power station is wall-mounted "
            "with its amber LED display showing full charge in the cold night air, "
            "completely undisturbed snow covers the ground and pine branches in all directions, "
            "the A-frame triangular silhouette is a perfect geometric form against the aurora sky, "
            "warm amber interior light through the glass creates an impossible colour contrast with "
            "the cold emerald aurora, "
            "no people, 8k, aurora architectural night photography, long-exposure feel, "
            "maximum aurora intensity and colour saturation"
        ),
        "In-App Text Hook": "Aurora. Glass walls. Off-grid silence.",
        "Posting Day": "Day 1 — May 11",
        "Slot": SLOTS[1],
        "SL Post Time": TIMES[1],
    },

    # ── Pet Wellness 1 ────────────────────────────────────────────────────────
    {
        "Board": "Smart Pet Wellness",
        "Post Type": "Static Image",
        "Theme": "Adventure / Corgi Sea Cliff Golden Hour",
        "Title": "Corgi Sea Cliff Golden Hour | Coastal Dog Photography 2026",
        "Description": (
            "Save this for your Corgi and coastal dog board. "
            "A Pembroke Welsh Corgi on a sea cliff at golden hour — ears fully up eyes on the horizon "
            "pure breed joy where land ends and ocean begins. "
            "#Corgi #PembrokeWelshCorgi #CoastalDog #BeachDog #CorgiLife "
            "#GoldenHour #DogPhotography"
        ),
        "Alt Text": (
            "Pembroke Welsh Corgi sitting on sea cliff edge at golden hour, both ears erect facing "
            "ocean horizon, fox-red and white fur backlit by sunset creating luminous halo, "
            "Pacific Ocean stretching to hammered-gold horizon behind"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a perfectly groomed Pembroke Welsh Corgi sits at "
            "the very edge of a sea cliff at golden hour, "
            "the dog's body is in three-quarter profile but its face turns directly toward camera — "
            "both pointed ears fully erect catching the warm backlight, "
            "its fox-red and white coat is completely backlit by the golden hour sun creating a "
            "luminous halo around its fur — particularly the white neck ruff and ear tips glow, "
            "the sea cliff drops sharply below to white surf breaking on dark rocks — the cliff edge "
            "is at the very bottom of the frame, "
            "the ocean stretches to the horizon in hammered gold reflecting the setting sun, "
            "the sky above deepens from gold to rose to violet at the zenith, "
            "the Corgi's expression: absolute alert contentment — this is its natural element, "
            "no people, no leash visible, 8k, golden hour coastal dog portrait photography, "
            "low-angle ground-level shot, backlit fur halo"
        ),
        "In-App Text Hook": "Where land ends. Corgi begins.",
        "Posting Day": "Day 1 — May 11",
        "Slot": SLOTS[2],
        "SL Post Time": TIMES[2],
    },

    # ── Pet Wellness 2 ────────────────────────────────────────────────────────
    {
        "Board": "Smart Pet Wellness",
        "Post Type": "Static Image",
        "Theme": "Indoor Luxury / Norwegian Forest Cat Geometric Steel Window",
        "Title": "Norwegian Forest Cat Geometric Window | Luxury Cat Photography 2026",
        "Description": (
            "Save this for your Norwegian Forest Cat and luxury interior board. "
            "A Norwegian Forest Cat in a geometric steel-frame window — the forest through "
            "geometric black steel the cat's lion's mane silhouetted against cold morning light. "
            "This image describes an entire lifestyle. "
            "#NorwegianForestCat #LuxuryCat #CatWindow #ForestCat #CatLife "
            "#IndoorCat #WildCatEnergy"
        ),
        "Alt Text": (
            "Large Norwegian Forest Cat with flowing silver-grey mane sitting in geometric "
            "black steel-frame window, pine forest visible through 9-pane window grid, "
            "morning light creating rim-light on cat fur, warm amber interior in background bokeh"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a large adult Norwegian Forest Cat with an "
            "extraordinary flowing lion's mane sits centred in a floor-height geometric "
            "steel-framed window — the window is divided into 9 equal rectangular panes by "
            "matte black steel bars (3x3 grid), "
            "the cat fills the centre 3 panes of the grid with its body, "
            "its dense flowing silvery-grey fur catches the cold morning light filtering through "
            "the pine forest outside creating a rim-light effect on its outer fur, "
            "through all 9 window panes a pine forest extends in soft focus — tall pine trunks "
            "in blue-grey morning mist, "
            "the cat's pale green eyes are directed directly at camera with the Norwegian Forest "
            "Cat's characteristic wild intelligence, "
            "the warm amber interior behind the cat is visible as soft bokeh contrasting with "
            "the cold grey forest beyond the glass, "
            "the geometric black steel frame creates a graphic design composition with the cat "
            "as the central visual anchor, "
            "no people, 8k, architectural cat portrait photography, morning light, geometric composition"
        ),
        "In-App Text Hook": "Geometric light. Wild soul.",
        "Posting Day": "Day 1 — May 11",
        "Slot": SLOTS[3],
        "SL Post Time": TIMES[3],
    },

    # ── Surfing Ceylon 1 ──────────────────────────────────────────────────────
    {
        "Board": "Surfing Ceylon",
        "Post Type": "Static Image",
        "Theme": "Surf / Arugam Bay Dawn Barrel",
        "Title": "Arugam Bay Dawn Barrel | Sri Lanka Surf Photography 2026",
        "Description": (
            "Save this for your Sri Lanka surf and Arugam Bay board. "
            "The perfect Arugam Bay right-hander at dawn — a lone surfer inside the barrel "
            "golden light refracting through the wave face the Indian Ocean as far as the eye can see. "
            "Sri Lanka's greatest surf break doing what it does. "
            "#ArugamBay #SriLankaSurf #SurfPhotography #BarrelWave #SurfSriLanka "
            "#IndianOcean #SurfingCeylon"
        ),
        "Alt Text": (
            "Surfer in classic crouch inside perfect right-hand barrel wave at Arugam Bay Sri Lanka "
            "at dawn, jade-green and turquoise wave lit from behind by golden dawn light, "
            "Arugam point with lone palm tree visible through barrel opening"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a lone surfer deep inside a perfect Arugam Bay "
            "right-hand barrel wave captured from water level inside the tube at dawn, "
            "the wave is a classic point-break barrel — a cylindrical tube of clear Indian Ocean "
            "water, the dawn light enters from behind the wave creating an extraordinary glow "
            "through the wave face — water lit from within in shades of jade green and turquoise "
            "with golden dawn light refracting through the thinner lip sections, "
            "the surfer is in classic barrel crouch — low wide stance arms out perfectly balanced "
            "in the deepest part of the tube, silhouetted against the glowing wave interior, "
            "the wave lip is pitching perfectly over creating the full circular barrel framing, "
            "through the barrel opening the Arugam Bay point is visible — the flat point with "
            "the iconic lone palm tree as a black silhouette, "
            "the Indian Ocean surface beyond is calm and golden in early morning light, "
            "photographed from inside the tube — water-level barrel perspective, "
            "no identifiable faces, 8k, barrel wave surf photography, dawn light, water perspective"
        ),
        "In-App Text Hook": "Arugam Bay. Perfect. Dawn.",
        "Posting Day": "Day 1 — May 11",
        "Slot": SLOTS[4],
        "SL Post Time": TIMES[4],
    },

    # ── Surfing Ceylon 2 ──────────────────────────────────────────────────────
    {
        "Board": "Surfing Ceylon",
        "Post Type": "Static Image",
        "Theme": "Surf / Hikkaduwa Sunset Cutback",
        "Title": "Hikkaduwa Sunset Surf Sri Lanka | Indian Ocean Photography 2026",
        "Description": (
            "Save this for your Sri Lanka travel and surf destination board. "
            "Hikkaduwa at sunset — a surfer cutting across a glowing orange wave face "
            "with the Sri Lankan palm horizon behind. The Indian Ocean's most beautiful surf session. "
            "#Hikkaduwa #SriLankaSurf #SunsetSurf #SurfingCeylon #IndianOcean "
            "#SriLankaTravel #TropicalSurf"
        ),
        "Alt Text": (
            "Surfer executing cutback carve on translucent orange wave at Hikkaduwa at sunset, "
            "backlit spray fan in burnt orange, palm tree silhouette horizon line, "
            "warm tropical sunset sky above Indian Ocean"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a skilled surfer executes a perfectly timed "
            "cutback carve on a 2-metre wave at Hikkaduwa at sunset, "
            "the wave face is completely lit from behind by the setting sun creating a translucent "
            "orange-gold wave — the water glows from within as the sunlight hits the thinnest "
            "part of the wave face at 90 degrees, "
            "the surfer is at the top third of the wave in full extended cutback position — "
            "the surfboard edge biting into the glowing orange water and sending a fan of "
            "backlit orange spray outward, "
            "the Hikkaduwa horizon behind is a flat line of coconut palms silhouetted in deep "
            "burnt orange against the sunset sky, "
            "the sky above transitions from molten orange at the horizon to deep magenta to "
            "violet at the zenith, "
            "the flat warm ocean between the breaking wave and the horizon catches the last "
            "golden light in long horizontal mirror reflections, "
            "no identifiable face, 8k, sunset surf photography, tropical warm tones, "
            "dramatic backlit spray capture"
        ),
        "In-App Text Hook": "Hikkaduwa. Sunset. Always.",
        "Posting Day": "Day 1 — May 11",
        "Slot": SLOTS[5],
        "SL Post Time": TIMES[5],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DAY 2 — May 12, 2026
    # ══════════════════════════════════════════════════════════════════════════

    # ── Future Living 3 ───────────────────────────────────────────────────────
    {
        "Board": "Future Living & Off-Grid Tech",
        "Post Type": "Static Image",
        "Theme": "Solar / Desert Canyon Glass Pod Off-Grid",
        "Title": "Desert Canyon Glass Pod | Off-Grid Solar Architecture 2026",
        "Description": (
            "Save this for your desert architecture and off-grid living board. "
            "A geometric glass pod on a red canyon rim — dual-axis solar tracker on the rock plateau "
            "EcoFlow stack inside the glass the canyon 100 metres below at golden hour. "
            "Off-grid in the most dramatic landscape on earth. "
            "#DesertArchitecture #OffGridLiving #SolarHome #GlassPod #FutureLiving "
            "#CanyonCabin #OffGridTech"
        ),
        "Alt Text": (
            "Geometric full-glass pod cabin on red sandstone canyon rim at golden hour, "
            "dual-axis solar panel tracker on adjacent rock plateau, warm amber interior with "
            "EcoFlow Delta Pro visible through glass walls, 100m sheer canyon drop below"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a compact perfectly square full-glass pod cabin "
            "sits on the very rim of a red sandstone canyon at golden hour, "
            "all four sides are floor-to-ceiling glass revealing the warm interior: "
            "a single minimalist desk with a laptop, a hanging hammock chair, "
            "an EcoFlow Delta Pro stack in the corner with amber display glowing, "
            "on the red rock plateau immediately adjacent to the glass pod a large dual-axis solar "
            "panel tracker on a steel pole mount points at the setting sun at optimal angle, "
            "the canyon below is a sheer 100-metre drop of layered red and ochre sandstone walls "
            "descending to a dry river bed of white sand in deep blue-grey shadow, "
            "the sky above the canyon rim is a perfect desert sunset gradient — deep orange at "
            "the horizon transitioning to violet-blue at the zenith, "
            "the red sandstone of the canyon rim glows in the last warm light contrasting "
            "dramatically with the cold canyon shadow below, "
            "no people, 8k, desert canyon architectural photography, golden hour, maximum drama"
        ),
        "In-App Text Hook": "Canyon edge. Solar. Off-grid.",
        "Posting Day": "Day 2 — May 12",
        "Slot": SLOTS[0],
        "SL Post Time": TIMES[0],
    },

    # ── Future Living 4 ───────────────────────────────────────────────────────
    {
        "Board": "Future Living & Off-Grid Tech",
        "Post Type": "Static Image",
        "Theme": "Glass / Mountain Lake Floating Cabin Blue Hour",
        "Title": "Floating Glass Lake Cabin | Off-Grid Architecture 2026",
        "Description": (
            "Save this for your lake cabin and off-grid living board. "
            "A full-glass floating cabin on a mountain lake at blue hour — EcoFlow powering the interior "
            "the glass walls doubling in the mirror-still lake surface the mountain ridgeline above. "
            "The most peaceful off-grid structure ever built. "
            "#LakeCabin #FloatingCabin #GlassCabin #OffGridLiving #FutureLiving "
            "#MountainLake #OffGridTech"
        ),
        "Alt Text": (
            "Full-glass rectangular cabin floating on perfectly still mountain lake at blue hour, "
            "warm amber interior light reflecting in mirror lake surface below, "
            "mountain black silhouette above, EcoFlow power station visible through glass walls, "
            "perfect mirror double reflection"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a perfectly rectangular full-glass cabin floats "
            "on a completely still mountain lake at blue hour — "
            "the cabin sits on a low matte black steel pontoon platform flush with the water surface "
            "so the cabin appears to float directly on the lake, "
            "all four sides are floor-to-ceiling glass revealing the interior completely: "
            "a cream platform bed facing the glass wall, an EcoFlow Delta Pro stack against the "
            "far interior glass wall its green LED charge bars glowing through two layers of glass, "
            "the completely still lake surface creates a perfect mirror reflection of the entire "
            "cabin — doubling the warm amber interior light and the mountain silhouette, "
            "the mountain ridgeline above is a clean black silhouette against the blue hour sky — "
            "that deep cobalt blue that exists only for 12 minutes after sunset, "
            "the glass cabin walls also reflect the mountain and cobalt sky creating an additional "
            "layer of visual depth — three simultaneous versions of the same image, "
            "no people, 8k, blue hour lake architectural photography, perfect mirror reflections, "
            "absolute stillness"
        ),
        "In-App Text Hook": "Floating. Still. Off-grid.",
        "Posting Day": "Day 2 — May 12",
        "Slot": SLOTS[1],
        "SL Post Time": TIMES[1],
    },

    # ── Pet Wellness 3 ────────────────────────────────────────────────────────
    {
        "Board": "Smart Pet Wellness",
        "Post Type": "Static Image",
        "Theme": "Adventure / Siberian Husky Arctic Ice Ridge Aurora",
        "Title": "Siberian Husky Arctic Ice Ridge | Aurora Dog Photography 2026",
        "Description": (
            "Save this for your Siberian Husky and arctic dog board. "
            "A Siberian Husky on an arctic ice ridge under the aurora — "
            "blue eyes reflecting emerald northern lights the infinite tundra below. "
            "This is what this breed was engineered for. "
            "#SiberianHusky #ArcticDog #HuskyLife #AuroraDog #NorthernLights "
            "#WinterDog #DogPhotography"
        ),
        "Alt Text": (
            "Pure white Siberian Husky standing at apex of arctic ice ridge under aurora borealis "
            "at night, wolf-like commanding posture, icy blue eyes reflecting emerald aurora green, "
            "frozen tundra stretching below, emerald and violet northern lights filling sky"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a large adult pure white Siberian Husky stands "
            "at the apex of an arctic ice ridge at night under a dramatic aurora borealis, "
            "the dog's posture is wolf-like and commanding — head slightly raised, both ears fully "
            "erect, tail carried high, "
            "its icy blue eyes reflect the emerald aurora light above, "
            "the ice ridge is a knife-edge of translucent blue-white glacial ice that the dog "
            "balances on with absolute certainty, "
            "the aurora fills the entire sky in sweeping curtains of emerald green with electric "
            "violet at the outer edges — the aurora light reflects on the ice ridge and snow "
            "fields below creating an otherworldly emerald-white landscape, "
            "the dog's white fur catches the aurora green in its outer guard coat while the "
            "undercoat remains pure white creating a dual-tone effect, "
            "the frozen tundra stretches in all directions below the ice ridge in complete silence, "
            "photographed from slightly below the dog making it appear monumental against the "
            "aurora sky, no people, 8k, arctic aurora dog portrait photography, "
            "otherworldly atmosphere, ice and light"
        ),
        "In-App Text Hook": "Arctic. Aurora. Pure husky.",
        "Posting Day": "Day 2 — May 12",
        "Slot": SLOTS[2],
        "SL Post Time": TIMES[2],
    },

    # ── Pet Wellness 4 ────────────────────────────────────────────────────────
    {
        "Board": "Smart Pet Wellness",
        "Post Type": "Static Image",
        "Theme": "Indoor Luxury / Silver Persian Cat Marble Fireplace",
        "Title": "Silver Persian Cat Marble Fireplace | Quiet Luxury Photography 2026",
        "Description": (
            "Save this for your Persian cat and quiet luxury home board. "
            "A silver Persian cat on a white marble hearth — firelight on silver fur "
            "the minimalist luxury interior framing pure feline elegance. "
            "The definition of quiet luxury. "
            "#PersianCat #QuietLuxury #CatLife #LuxuryInterior #MarbleFireplace "
            "#IndoorCat #CatPhotography"
        ),
        "Alt Text": (
            "Perfectly groomed silver Persian cat sitting on white Carrara marble fireplace hearth, "
            "real wood fire burning behind creating orange-amber halo on silver fur, "
            "flat Persian face and copper eyes facing side, minimalist white luxury interior bokeh"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a perfectly groomed silver Persian cat sits "
            "centred on a wide white Carrara marble fireplace hearth, "
            "the fireplace has a real wood fire burning — the warm orange-amber firelight "
            "illuminates the Persian's extraordinarily dense fluffy silver coat from below "
            "and behind creating a fire-lit halo effect on its fur, "
            "the Persian's flat face and large copper eyes are directed slightly to one side "
            "in the characteristic Persian regal disinterest, "
            "the fireplace surround is a floor-to-ceiling slab of white Carrara marble with "
            "natural grey veining — the marble surface reflects the firelight in warm flickering, "
            "the room behind is quiet luxury: white walls, warm linen furniture visible only "
            "in the deep soft bokeh background, "
            "the central visual contrast: intense amber firelight on silver fur against the "
            "cold white marble of the hearth, "
            "no people, 8k, quiet luxury interior cat portrait photography, "
            "firelight cinematography, warm-cold contrast"
        ),
        "In-App Text Hook": "Silver. Fire. Quiet luxury.",
        "Posting Day": "Day 2 — May 12",
        "Slot": SLOTS[3],
        "SL Post Time": TIMES[3],
    },

    # ── Surfing Ceylon 3 ──────────────────────────────────────────────────────
    {
        "Board": "Surfing Ceylon",
        "Post Type": "Static Image",
        "Theme": "Surf / Mirissa Dawn Glass-Off Paddle-Out",
        "Title": "Mirissa Morning Glass Sri Lanka | Surf Photography 2026",
        "Description": (
            "Save this for your Sri Lanka surf and Mirissa board. "
            "Mirissa at sunrise — a lone surfer paddling through perfect mirror-glass conditions "
            "into the morning light. The Indian Ocean at its absolute best. "
            "Sri Lanka surf culture in one frame. "
            "#Mirissa #SriLankaSurf #GlassWave #SunriseSurf #SurfingCeylon "
            "#IndianOcean #SriLankaTravel"
        ),
        "Alt Text": (
            "Lone surfer paddling on shortboard through mirror-flat glass-off ocean at Mirissa "
            "Sri Lanka at sunrise, white-gold sun on horizon with perfect vertical reflection, "
            "surfboard cutting precise V-wake through still water, palm-lined horizon in distance"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a lone surfer paddles on a shortboard through "
            "perfectly glass-off morning ocean conditions at Mirissa Sri Lanka at sunrise, "
            "photographed from water level directly behind the surfer — we see the back of their "
            "head and surfboard cutting a perfect white line through the mirror-flat water ahead, "
            "the sunrise is directly ahead — a white-gold circle of sun just clearing the flat "
            "horizon, its reflection a long vertical stripe of gold on the mirror-flat water "
            "surface running directly toward the surfer, "
            "the glass-off conditions make the water surface a perfect mirror — the pink-gold "
            "sunrise sky doubled below the waterline, "
            "the surfboard fins and tail cut a precise V-shaped wake in the mirror surface, "
            "in the far distance the Mirissa palm-lined coast is a thin dark strip between "
            "the glowing water and the sunrise sky, "
            "the surfer's silhouette against the sunrise is the central composition element, "
            "no identifiable face, 8k, sunrise surf photography, Mirissa morning glass, "
            "water-level perspective, mirror reflection"
        ),
        "In-App Text Hook": "Mirissa morning. Pure glass.",
        "Posting Day": "Day 2 — May 12",
        "Slot": SLOTS[4],
        "SL Post Time": TIMES[4],
    },

    # ── Surfing Ceylon 4 ──────────────────────────────────────────────────────
    {
        "Board": "Surfing Ceylon",
        "Post Type": "Static Image",
        "Theme": "Surf / Weligama Bay Tropical Wave Culture",
        "Title": "Weligama Bay Perfect Wave | Sri Lanka Surf Destination 2026",
        "Description": (
            "Save this for your Weligama and Sri Lanka surf travel board. "
            "Weligama Bay in its purest form — a rolling left-hander in warm turquoise water "
            "the traditional oruwa fishing boats in the bay behind. "
            "The most welcoming surf destination in Asia. "
            "#Weligama #SriLankaSurf #SurfTravel #SurfingCeylon #IndianOcean "
            "#SriLankaTravel #TropicalSurf"
        ),
        "Alt Text": (
            "Surfer riding clean left-hand wave at Weligama Bay Sri Lanka in turquoise water, "
            "traditional blue oruwa outrigger fishing boats on white sand beach in background bay, "
            "coconut palms lining the beach, tropical midday light, welcoming warm scene"
        ),
        "AI Prompt": (
            "Hyper-realistic 9:16 vertical photo, a surfer rides a classic Weligama Bay left-hand "
            "point break wave in warm turquoise water at midday, "
            "the wave is a clean shoulder-high rolling left-hander — the kind Weligama is famous for, "
            "the surfer is in the middle of a graceful forehand bottom turn, board angled up the "
            "wave face in turquoise water with small white spray at the fins, "
            "in the background the iconic Weligama Bay curves gently — traditional blue-painted "
            "oruwa outrigger fishing boats pulled up on a white sand beach, "
            "tall coconut palms lean over the beach behind the boats, "
            "the bay water inside the surf break is flat calm turquoise contrasting with the "
            "breaking wave in the foreground, "
            "the sky is tropical midday blue with small white cumulus clouds, "
            "warm tropical light gives the entire image a warm colour temperature, "
            "the image captures the laid-back approachable character of Weligama — "
            "beautiful and friendly rather than extreme, "
            "no identifiable face, 8k, tropical surf travel photography, warm turquoise tones"
        ),
        "In-App Text Hook": "Weligama. Warm. Perfect.",
        "Posting Day": "Day 2 — May 12",
        "Slot": SLOTS[5],
        "SL Post Time": TIMES[5],
    },
]

# ── Write CSV ─────────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
    writer.writeheader()
    for i, pin in enumerate(PINS, start=1):
        pin["Post #"] = str(i)
        pin["Status"] = "Ready"
        writer.writerow({k: pin.get(k, "") for k in FIELDNAMES})

print(f"SUCCESS: Written {len(PINS)} rows to {OUTPUT_FILE}")
print("\nPosting Time Logic (SLST):")
print("  7:00am SLST → 9:30pm EST (previous day) — US prime evening scroll")
print("  9:00am SLST → 11:30pm EST — US late night")
print("  11:00am SLST → 1:30am EST — global 'Other' audience coverage")
print("  2:00pm SLST → 4:30am EST — global coverage")
print("  6:00pm SLST → 7:30am EST — US MORNING PEAK ★")
print("  9:00pm SLST → 10:30am EST — US MID-MORNING PEAK ★")
