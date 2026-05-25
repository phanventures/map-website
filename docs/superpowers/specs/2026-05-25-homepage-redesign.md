# mranhphan.com — Homepage Redesign Spec

**Date:** 2026-05-25
**Status:** Approved for implementation

---

## Summary

Rebuild the homepage around a new positioning: helping entrepreneurs and solopreneurs get more done through a three-step framework — Habits → Systems → Technology. The queer identity remains present as a design signal (pride stripe) but is not the defining filter for the audience.

The homepage has one job: **get people onto the free 3-part email series.** Everything else is secondary.

---

## Positioning

- **Was:** "Practical productivity systems and a community built for queer entrepreneurs and their allies"
- **Now:** Helping people stop being busy and start getting things done — through Habits, Systems, and Technology in that order
- **Audience:** Entrepreneurs and solopreneurs who want motivation, guidance, and practical tools. Queer identity is one layer of who Anh is, not the audience filter.
- **Anh's role:** Guide, not subject. The framework sells itself. His story is context, not the hook.

---

## Site Structure

**Nav:** Anh Phan (orange) · Community · Programs · Consulting · [Join the Community CTA]

- **Community** — The Phan Club (live, founding members open)
- **Programs** — Cohort + courses (coming soon / waitlist) — *inner page designed later*
- **Consulting** — 1:1 work (accepting interest for end of year) — *inner page designed later*

---

## Homepage Section Order

```
Progress Pride Stripe
Nav
Progress Pride Stripe
────────────────────
Hero
Process (3-column)
Email Capture
YouTube
────────────────────
Progress Pride Stripe
Footer
Progress Pride Stripe
```

---

## Section Specs

### Progress Pride Stripe
- Height: 6px
- Color order (left to right, equal segments): Red · Orange · Yellow · Green · Blue · Violet · Pink · Light Blue · Brown · Black
- Hex values: `#E40303` · `#FF8C00` · `#FFED00` · `#008026` · `#004DFF` · `#750787` · `#F7A8B8` · `#55CDFC` · `#613915` · `#000000`
- Appears 4 times total: above nav, below nav, above footer, below footer

### Nav
- Background: white (`#fff`), no bottom border
- Left: wordmark "Anh **Phan**" — "Anh" in `#111`, "Phan" in `#E04E1F`
- Center: Community · Programs · Consulting (muted, `#888`)
- Right: "Join the Community" button — orange bg (`#E04E1F`), white text
- Sandwiched between the two top stripes

### Hero
- Background: white
- Bottom border: `1px solid #e5e2db`
- Layout: centered, max-width ~560px
- Eyebrow: "Habits · Systems · Technology" — small caps, `#999`
- Headline: "Stop being busy." + italic line "Start getting things done." in `#E04E1F`
- Subtext: "Getting things done starts with the right habits, builds into repeatable systems, and gets amplified by the right tools. I'll walk you through all three."
- CTA button: "Get the free 3-part series →" — orange bg, white text
- No photo in the hero (framework-first, not personal brand flex)

### The Process
- Background: warm orange tint `#FFF3EE`, border `#f5d9ce`
- Label: "THE PROCESS" in orange, small caps
- Layout: 3 equal columns side by side
- Each card: white bg (`#fff`), border `#f5d9ce`, border-radius 10px
- Card content: large orange number (01/02/03), bold title, body copy
  - **01 — Habits:** "Before systems or tools, you need consistent, repeatable behaviors. We start here — with what habits actually are, why they work, and how to build ones that stick."
  - **02 — Systems:** "Once the habits are in place, you build systems — repeatable workflows you can run over and over to accomplish what matters, without starting from scratch every time."
  - **03 — Technology:** "The right software and automations at the right time — after the habits and systems are solid. Technology multiplies what's already working."

### Email Capture
- Background: white
- Label: "FREE · NO SPAM · UNSUBSCRIBE ANY TIME" in orange small caps
- Headline: "Start at the beginning. It's free."
- Subtext: "A 3-part email series — one pillar per week. Week 1: Habits · Week 2: Systems · Week 3: Technology"
- Form: email input (warm bg `#F8F7F3`) + "Start the series →" button (orange)
- Secondary nudge (below a divider): "Want community alongside it? Founding members of The Phan Club are open now." + orange outline button "Join The Phan Club →"

### YouTube
- Background: warm orange tint `#FFF3EE`
- Label: "ON YOUTUBE" in orange small caps
- Headline: "Habits, systems, and tools — in plain language."
- Subtext: "Practical videos for people who want to build better, not just busier."
- Layout: 3 equal video columns — dark thumbnail placeholder, title, "Coming soon" tag
- Placeholder titles:
  - "What are habits and why do they matter?"
  - "How to build a system that actually works"
  - "The best tools for solopreneurs in 2026"
- Subscribe CTA: red YouTube button "Subscribe on YouTube →"
- Note: swap placeholders for real thumbnails + titles once channel is live

### Footer
- Background: white, no top border (stripe acts as divider)
- Left: "Anh Phan" wordmark (orange "Phan")
- Center: Instagram · TikTok · YouTube (muted links)
- Right: © 2026 Phan Ventures LLC

---

## Color Palette

| Token | Value | Usage |
|---|---|---|
| Background | `#fff` | Hero, email capture, footer |
| Warm tint | `#FFF3EE` | Process, YouTube sections |
| Warm border | `#f5d9ce` | Borders in warm sections |
| Standard border | `#e5e2db` | Borders in white sections |
| Primary text | `#111` | Headlines |
| Muted text | `#666` / `#888` | Body, nav links |
| Orange accent | `#E04E1F` | Buttons, numbers, labels, wordmark |
| YouTube red | `#FF0000` | YouTube subscribe button only |

---

## What's Live vs. Coming Soon

| Offering | Status | CTA |
|---|---|---|
| 3-part email series | Build before launch | Primary homepage CTA |
| The Phan Club | Live, no members | "Join now" — founding member framing |
| Programs (cohort + courses) | Not built | "Join waitlist" |
| Consulting | Not active | "Express interest" |
| YouTube | Not started | "Coming soon" placeholders |

---

## Pages Not Yet Designed

- `community.html` — The Phan Club full pitch page
- `programs.html` — Cohort + courses, waitlist focus
- `consulting.html` — 1:1 work, accepting interest

These follow the same visual system (pride stripes, warm tint / white alternating sections, orange accents) and will be designed in a separate session.

---

## Files to Change

| File | Action |
|---|---|
| `index.html` | Full rebuild per this spec |
| `styles.css` | Update shared styles — new color tokens, new section classes |
| `phan-club.html` | Rename/replace with `community.html` — redesign later |
| `roundtable.html` | Replace with `programs.html` — redesign later |
| `start-here.html` | Remove — no longer in nav |
| `CLAUDE.md` | Update to reflect new positioning and file structure |
