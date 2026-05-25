# Claude Sonnet Content Generation Prompt

## Pinterest 7-Day Content Plan (42 Pins) — May 26–June 1, 2026

---

## Context & Data Sources

You have access to:

1. **Strategic Foundation Document:** `Content-Brief-for-Claude.md` — Complete Pinterest growth framework, visual formulas, audience analysis, posting strategy, batch history (v10 & v11), and content generation guidelines.

2. **Latest Analytics Data:**
   - Attached: Latest Audience Insights CSV (total audience snapshot)
   - Attached: Latest Pinterest Analytics Overview CSV (performance data)
   - Review all provided analytics files to extract current performance insights

3. **Previous Content Batches:**
   - All v10, v11 (and any earlier) PostIdeas CSVs are attached
   - Review all batches to understand what has been created, what performed well, and what themes are established

---

## Task: Generate v12 Content Plan

### Batch Specification

**Duration:** 7 days (May 26 – June 1, 2026)  
**Total Pins:** 42 (6 pins per day)  
**Posting Schedule (SL time):**

- Slot 1: 7:30am — Future Living & Off-Grid Tech
- Slot 2: 9:30am — Smart Pet Wellness
- Slot 3: 11:30am — Future Living & Off-Grid Tech
- Slot 4: 1:30pm — Smart Pet Wellness
- Slot 5: 3:30pm — Code. Build. Ship. — Freelance Tech Life (SE-Lifestyle)
- Slot 6: 8:30pm — Code. Build. Ship. — Freelance Tech Life (SE-Infographic)

**Boards (Do not create new boards):**

- Future Living & Off-Grid Tech
- Smart Pet Wellness
- Code. Build. Ship. — Freelance Tech Life

### Content Mix Rules

**Daily (per day):**

- 2 pins: Future Living architecture (Slot 1 & 3)
- 2 pins: Pet Wellness or Wilderkind animals (Slot 2 & 4)
- 1 pin: SE Bridge Lifestyle workspace (Slot 5)
- 1 pin: SE Bridge Infographic business framework (Slot 6)

**Your Primary Task: Comprehensive Research & Analysis**

Before generating any pins, conduct a complete research pass:

1. **Analyze All Analytics Files** to identify:
   - Current top-performing pins and boards
   - Top-performing themes and visual patterns
   - Audience affinity interests (highest, untapped opportunities)
   - Performance trends over time

2. **Review All PostIdeas CSVs** to identify:
   - What content has already been created and posted
   - Which themes performed well vs. underperformed
   - Visual formula patterns that drive engagement
   - Breed/animal types already featured
   - SE niches already covered
   - Ensure zero repetition for v12

3. **Ask Clarifying Questions** if needed:
   - Request context on batch posting dates or performance outcomes
   - Ask about specific pin performance if unclear
   - Clarify any ambiguities in the data
   - Request any additional context needed for accurate analysis

4. **Generate v12 Based on Your Findings:**
   - Do NOT follow prescriptive theme lists
   - Decide what v12 should prioritize based on data analysis
   - Recommend specific themes, niches, animal types, and SE verticals
   - Make strategic decisions informed by what the data shows

### Output Format

Generate the complete 42-pin content plan as a **valid CSV** with these exact headers:

```
"Post #","Board","Post Type","Theme","Title","Description","Alt Text","AI Prompt","In-App Text Hook","Status","Posting Day","Slot","SL Post Time"
```

**Field Requirements:**

- **Post #:** 1–42 (sequential)
- **Board:** One of the three boards listed above
- **Post Type:** Static Image (all pins)
- **Theme:** Descriptive theme (e.g., "Glass / Cantilevered Boat Dock Pod" or "Wilderkind / Snow Leopard Alpine Meadow")
- **Title:** SEO-optimized, emotion-driven, click-worthy. Include year (2026) and specific keywords
- **Description:** Narrative-driven, conversational. Begin with "Save this for your [interest] board." Explicitly call to save. Include brand terms like EcoFlow, Pinterest, off-grid. 150–250 words.
- **Alt Text:** Highly descriptive for visual search SEO. Every visual element named (architecture, animals, light, materials)
- **AI Prompt:** Detailed image generation prompt. Follow the formula from the Strategic Brief:
  - Hyper-realistic 9:16 vertical photo, [Style A or B]
  - Subject description + setting + light + interior visible elements + exterior elements
  - Material palette if relevant
  - Composition framing
  - No people / specific framing instruction
  - 8k, cinematic photography style
- **In-App Text Hook:** One bold statement (5–7 words) for text overlay or pin title shorthand
- **Status:** "Ready" (never change)
- **Posting Day:** "Day 1 — Mon May 26" through "Day 7 — Sun June 1"
- **Slot:** Static-1, Static-2, Static-3, Static-4, SE-Lifestyle, SE-Infographic
- **SL Post Time:** 7:30am, 9:30am, 11:30am, 1:30pm, 3:30pm, 8:30pm

### Strategic Constraints

1. **Visual Formula Consistency:** Every pin must use one of the proven formulas:
   - Glass + Drama (cantilevered, water mirror, geological, forest, extreme condition)
   - Pet Adventure (breed in dramatic landscape or interior moment)
   - Wilderkind (animal + raw landscape + twilight/cold light)
   - SE Bridge (dev workspace in glass cabin OR business strategy infographic)

2. **Strategic Differentiation (Identify from Your Research):**
   - Based on analytics, what themes are driving the highest engagement?
   - What visual variations haven't been explored yet?
   - What high-affinity audience interests are underexploited?
   - Propose specific new variations based on your analysis

3. **Audience & Niche Alignment (Data-Driven):**
   - Use audience affinity data to identify which niches to integrate
   - Select animal breeds/types based on past performance and untapped interests
   - Choose SE niches based on current trends and audience fit
   - Let the data guide your niche selection

4. **Quality Standards:**
   - No filler or generic descriptions
   - Every title must include a searchable keyword + emotional benefit + year
   - Every AI Prompt must be specific enough for DALL-E 3, Midjourney, or Claude to generate consistently
   - Every In-App Hook must be bold and actionable (avoid generic like "Beautiful" or "Amazing")

---

## Phase 1: Research Summary & Clarification

Before generating the 42-pin CSV, provide:

1. **Analytics Findings:**
   - Summary of current top performers (pins, themes, boards)
   - Key audience affinity insights
   - Recommended focus areas based on data

2. **PostIdeas Analysis:**
   - Themes already covered across v9-v11
   - Performance patterns you identified
   - Recommendations for what v12 should emphasize

3. **Clarifying Questions:**
   - If any data is unclear or incomplete, list questions here
   - Request any additional context needed

4. **v12 Strategic Recommendations:**
   - Based on research, what 3-5 core themes should v12 prioritize?
   - What high-affinity niches should be integrated?
   - What new animal types or SE verticals should be introduced?
   - Any other strategic insights?

---

## Phase 2: Output Delivery

Provide the complete 42-pin CSV in a single code block (markdown format). Do not break it into sections. Include all rows with no omissions.

**Format:**

```csv
[complete CSV content here]
```

---

## Reference: Strategic Brief Summary

**Visual Formula Examples:**

Glass + Drama:

> "Hyper-realistic 9:16 vertical photo, Style A Quiet Luxury. A full-glass cabin [setting with dramatic geological/natural element]. Interior: warm amber [furnishings]. An EcoFlow Delta Pro with green LEDs [location]. Light: [dramatic light description]. Composition emphasizes [depth/layering]. No people. 8k, cinematic photography."

Pet Adventure:

> "Hyper-realistic 9:16 vertical photo, Style A Quiet Luxury. [Specific breed] [action/pose] in [dramatic landscape]. Shot from [angle]. Fur lit by [light source], creating [effect]. [Landscape detail]. No people. 8k, [setting] photography."

Wilderkind:

> "Hyper-realistic 9:16 vertical photo, Style A Quiet Luxury. Wilderkind aesthetic. [Animal] in [landscape] at [time/light condition]. [Distinctive features] rimlit/detailed. [Landscape depth]. Shot from [angle]. No people. 8k, [setting] photography, [mood]."

SE Bridge Lifestyle:

> "Hyper-realistic 9:16 vertical photo, Style A Quiet Luxury. [Dev setup detail] inside a full-glass cabin at [light condition]. Screens showing [specific tech]. Behind: [mountain/forest visible through glass]. An EcoFlow [power details]. The glass reflects both [code/setup] and [landscape]. No person visible. 8k, cinematic developer workspace photography."

SE Bridge Infographic:

> "Clean editorial infographic, 9:16 vertical, Style B Dynamic Viral. Background: deep charcoal. Title: [CLEAR VALUE PROPOSITION]. Below: [5 items/steps with amber numbers]. [Visual progression]. Footer: [decision statement]. Colour: charcoal, amber-gold, white. No photography."

---

## Validation Checklist Before Submitting

- [ ] All 42 rows present (Post # 1–42)
- [ ] Correct daily distribution: 7 days × 6 pins/day
- [ ] Slot rotation consistent (Static-1, 2, 3, 4, SE-Lifestyle, SE-Infographic repeating)
- [ ] No duplicate themes from v10 or v11
- [ ] At least 2–3 new high-affinity elements integrated (Watercraft, Campers, Aircraft, Woodworking, Metal Art)
- [ ] At least 2–3 new Wilderkind animals introduced
- [ ] SE infographics shifted to scaling/growth topics (not onboarding)
- [ ] All titles include year (2026) + searchable keyword + emotional/benefit angle
- [ ] All descriptions begin with "Save this for your [board]"
- [ ] All AI Prompts follow formula structure (hyper-realistic, 9:16, style, subject, light, interior, exterior, composition, no people, 8k)
- [ ] All In-App Hooks are bold, specific, actionable (5–7 words)
- [ ] CSV format is valid (double-quoted fields, commas separated, no unescaped quotes)
- [ ] Status column = "Ready" for all pins
- [ ] No typos or formatting inconsistencies

---

## Questions to Ask Yourself (Internal Validation)

1. Does this pin remix a proven formula without repeating a specific v10/v11 pin?
2. Does this pin integrate a high-affinity audience element (audience affinity > 2.0×)?
3. Is the title scannable and clickable (emotion + benefit + keyword)?
4. Would this AI Prompt generate a consistent, high-quality image?
5. Does this pin fit naturally into the daily schedule and board mission?

---

## Notes for Claude

- You have all necessary context in the Strategic Brief
- Reference v10 and v11 specific pins to ensure no repetition
- Prioritize **differentiation** while maintaining formula consistency
- Quality over quantity: better to have 5 excellent pins than 6 mediocre ones (you have 42 slots, so go deep)
- Balance between proven winners and experimental high-affinity integrations (70% proven formula + 30% experimental)
- Ensure every SE pin drives founders toward your freelance engineering offer (the ecosystem should feel intentional)

---

**Ready for Claude Sonnet. Copy this entire prompt into Antigravity and include the strategic brief + analytics CSVs as context.**
