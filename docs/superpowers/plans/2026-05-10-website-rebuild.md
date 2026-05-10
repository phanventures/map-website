# mranhphan.com Website Rebuild — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild mranhphan.com from a single overloaded homepage into a focused 3-page site where email list capture is the primary homepage conversion goal.

**Architecture:** Extract shared CSS to `styles.css` so all pages share a single source of truth. Rebuild `index.html` as a tight homepage (hero → stats → story → email capture → offerings preview → footer). Create `phan-club.html` and `cohort.html` as dedicated offer pages holding the full content currently buried on the homepage. Remove the rainbow gradient from the homepage — it moves exclusively to `cohort.html` where it can land as one intentional visual moment. Pride stripe bars stay as the queer identity signal across all pages.

**Tech Stack:** Static HTML, CSS (no framework, no build step), Google Fonts (Inter via CDN)

---

## File Structure

| File | Status | Responsibility |
|---|---|---|
| `styles.css` | **Create** | All shared styles — reset, variables, nav, footer, utility classes |
| `index.html` | **Modify** | Rebuilt homepage — hero, stats, story, email lead magnet, offerings preview |
| `phan-club.html` | **Create** | Full Phan Club pitch page |
| `cohort.html` | **Create** | Full Cohort Program page |

---

## Task 1: Extract Shared CSS

**Goal:** Pull all inline `<style>` CSS out of `index.html` into `styles.css` and verify the page looks identical.

**Files:**
- Create: `styles.css`
- Modify: `index.html` (replace `<style>` block with `<link>` tag)

- [ ] **Step 1: Create styles.css**

Copy the entire contents of the `<style>...</style>` block in `index.html` (lines 11–921) into a new file `styles.css`. The file should start with `*, *::before, *::after { ... }` and contain all current CSS.

- [ ] **Step 2: Replace inline styles in index.html**

In `index.html`, replace the entire `<style>...</style>` block (lines 11–921) with:

```html
  <link rel="stylesheet" href="styles.css">
```

Place it directly after the Google Fonts `<link>` tag (before `</head>`).

- [ ] **Step 3: Verify**

Open `index.html` in a browser. Confirm the page looks identical to before — layout, colors, fonts, spacing unchanged. Check at mobile width (375px) too.

- [ ] **Step 4: Commit**

```bash
git add styles.css index.html
git commit -m "refactor: extract inline styles to shared styles.css"
```

---

## Task 2: Rebuild the Nav

**Goal:** Replace the current social-link nav with a hybrid nav: logo left · page links center · CTA right. Move social icons to the footer.

**Files:**
- Modify: `styles.css` (update `.nav-socials`, add `.nav-links`, update responsive breakpoints)
- Modify: `index.html` (update `<nav>` HTML)

- [ ] **Step 1: Update nav CSS in styles.css**

Replace the existing nav-related rules (`.nav-socials`, `.nav-social-link`, `.nav-divider`) with:

```css
.nav-links {
  display: flex;
  align-items: center;
  gap: 32px;
}

.nav-link {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-muted);
  transition: color 0.2s;
  letter-spacing: -0.01em;
}
.nav-link:hover { color: var(--text); }

.nav-divider { width: 1px; height: 20px; background: var(--border); }

.nav-login {
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  background: #1D4ED8;
  padding: 7px 16px;
  border-radius: 6px;
  transition: opacity 0.2s;
}
.nav-login:hover { opacity: 0.88; }
```

Also update the responsive breakpoint at `@media (max-width: 960px)` — replace the nav padding rule with:

```css
nav { padding: 0 24px; }
.nav-links { gap: 20px; }
```

And at `@media (max-width: 640px)`:

```css
nav { padding: 0 20px; }
.nav-links { gap: 14px; }
.nav-link { font-size: 13px; }
```

- [ ] **Step 2: Update nav HTML in index.html**

Replace the entire `<nav>...</nav>` block with:

```html
<nav>
  <div class="nav-logo">Anh <span class="nav-logo-accent">Phan</span></div>
  <div class="nav-links">
    <a href="cohort.html" class="nav-link">Cohort</a>
    <a href="phan-club.html" class="nav-link">The Phan Club</a>
  </div>
  <div style="display:flex;align-items:center;gap:12px;">
    <div class="nav-divider"></div>
    <a href="phan-club.html" class="nav-login">Join The Phan Club</a>
  </div>
</nav>
```

- [ ] **Step 3: Update footer HTML to add social icons**

Add social links to the footer `<div class="footer-links">` block. Replace the current footer-links content with:

```html
<div class="footer-links">
  <a href="https://www.instagram.com/mr_anhphan" target="_blank" class="footer-social">
    <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
    Instagram
  </a>
  <a href="https://www.tiktok.com/@mr_anhphan" target="_blank" class="footer-social">
    <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.95a8.16 8.16 0 0 0 4.77 1.52V7.02a4.85 4.85 0 0 1-1-.33z"/></svg>
    TikTok
  </a>
  <a href="https://www.youtube.com/@mr_anhphan" target="_blank" class="footer-social">
    <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    YouTube
  </a>
</div>
```

Add this CSS to `styles.css`:

```css
.footer-social {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: var(--text-muted);
  font-weight: 500;
  transition: color 0.2s;
}
.footer-social:hover { color: var(--text); }
```

- [ ] **Step 4: Verify**

Open `index.html`. Nav shows: "Anh Phan" · Cohort · The Phan Club · Join button. Footer shows social icons. No broken layout at mobile width.

- [ ] **Step 5: Commit**

```bash
git add styles.css index.html
git commit -m "feat: rebuild nav with hybrid layout, move socials to footer"
```

---

## Task 3: Rebuild Homepage Body

**Goal:** Replace the current homepage body sections with the new conversion-focused structure: hero → stats → 2-sentence story → email lead magnet (primary CTA) → offerings preview (Cohort + Phan Club only) → footer.

**Files:**
- Modify: `index.html` (replace hero through footer body content)
- Modify: `styles.css` (new section styles, remove unused styles from old sections)

- [ ] **Step 1: Update hero CSS in styles.css**

Replace the existing `.hero`, `.hero-text`, `.hero-eyebrow`, `.hero-belief`, `.hero-sub`, `.hero-cta` rules with:

```css
.hero {
  padding: 96px 48px 80px;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  text-align: center;
}

.hero-eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--text-light);
  margin-bottom: 24px;
}

.hero-belief {
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 1.05;
  margin-bottom: 24px;
  color: var(--text);
  max-width: 760px;
  margin-left: auto;
  margin-right: auto;
}

.hero-belief em {
  font-style: italic;
  color: var(--text-muted);
}

.hero-sub {
  font-size: 17px;
  color: var(--text-muted);
  line-height: 1.75;
  margin-bottom: 40px;
  max-width: 560px;
  margin-left: auto;
  margin-right: auto;
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  background: var(--accent);
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  font-weight: 800;
  padding: 14px 28px;
  border-radius: 8px;
  transition: opacity 0.2s;
}
.hero-cta:hover { opacity: 0.88; }
```

- [ ] **Step 2: Add story + lead magnet + offerings CSS to styles.css**

Add these new rules to `styles.css`:

```css
/* ── STORY MICRO ── */
.story-micro {
  padding: 48px 48px;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
}

.story-micro-inner {
  max-width: 680px;
  margin: 0 auto;
  text-align: center;
}

.story-micro-inner p {
  font-size: 17px;
  color: var(--text-muted);
  line-height: 1.8;
}

.story-micro-inner em { font-style: italic; color: var(--text); }

/* ── LEAD MAGNET ── */
.lead-section {
  padding: 80px 48px;
  background: #fff;
  border-bottom: 1px solid var(--border);
}

.lead-inner {
  max-width: 640px;
  margin: 0 auto;
  text-align: center;
}

.lead-inner .section-label { margin-bottom: 20px; }

.lead-inner h2 {
  font-size: clamp(26px, 3vw, 38px);
  font-weight: 900;
  letter-spacing: -0.035em;
  line-height: 1.1;
  margin-bottom: 16px;
}

.lead-inner .lead-sub {
  font-size: 16px;
  color: var(--text-muted);
  line-height: 1.75;
  margin-bottom: 32px;
}

.lead-form {
  display: flex;
  gap: 8px;
  max-width: 480px;
  margin: 0 auto;
}

.lead-form input[type="email"] {
  flex: 1;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  font-weight: 500;
  color: var(--text);
  background: var(--bg);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  outline: none;
  transition: border-color 0.2s;
}
.lead-form input[type="email"]::placeholder { color: var(--text-light); }
.lead-form input[type="email"]:focus { border-color: var(--accent); }

.lead-form button {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  background: var(--accent);
  border: none;
  border-radius: 8px;
  padding: 12px 20px;
  cursor: pointer;
  white-space: nowrap;
  transition: opacity 0.2s;
}
.lead-form button:hover { opacity: 0.88; }

.lead-note {
  font-size: 12px;
  color: var(--text-light);
  margin-top: 12px;
}

/* ── OFFERINGS PREVIEW ── */
.preview-section {
  padding: 80px 48px;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
}

.preview-inner { max-width: 1000px; margin: 0 auto; }

.preview-header { margin-bottom: 40px; }

.preview-header h2 {
  font-size: clamp(24px, 2.8vw, 34px);
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.1;
}

.preview-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.preview-card {
  padding: 40px 36px;
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #fff;
}

.preview-card:last-child { border-right: none; }

.preview-num {
  font-size: 11px;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.preview-card h3 {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.preview-card p {
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.75;
  flex: 1;
}

.preview-link {
  display: inline-block;
  font-size: 13px;
  font-weight: 700;
  color: var(--accent);
  border-bottom: 1px solid rgba(224, 78, 31, 0.3);
  padding-bottom: 2px;
  width: fit-content;
  transition: opacity 0.2s;
}
.preview-link:hover { opacity: 0.75; }
```

Also add these responsive rules at the end of the existing `@media (max-width: 960px)` block:

```css
.hero { padding: 72px 32px 60px; }
.story-micro { padding: 40px 32px; }
.lead-section { padding: 60px 24px; }
.preview-section { padding: 60px 24px; }
.preview-grid { grid-template-columns: 1fr; }
.preview-card { border-right: none; border-bottom: 1px solid var(--border); }
.preview-card:last-child { border-bottom: none; }
```

And in `@media (max-width: 640px)`:

```css
.hero { padding: 60px 20px 48px; }
.hero-belief { font-size: 28px; }
.story-micro { padding: 32px 20px; }
.lead-section { padding: 52px 20px; }
.lead-form { flex-direction: column; }
.lead-form button { width: 100%; }
.preview-section { padding: 52px 20px; }
.preview-card { padding: 32px 24px; }
```

- [ ] **Step 3: Replace body sections in index.html**

Replace everything between `<!-- HERO -->` and `<!-- FOOTER -->` (inclusive of hero through the youtube section, but not the footer itself) with:

```html
  <!-- HERO -->
  <div class="hero" id="top">
    <div class="hero-eyebrow">Queer Entrepreneur &nbsp;·&nbsp; Productivity Systems &nbsp;·&nbsp; Community Builder</div>
    <h1 class="hero-belief">Build systems that work.<br><em>Get things done. Find your people.</em></h1>
    <p class="hero-sub">I run 3 businesses alongside a full-time job — not by working more hours, but by building systems that actually work. Get the free guide.</p>
    <a href="#system" class="hero-cta">Get the free system guide →</a>
  </div>

  <!-- STATS STRIP -->
  <div class="story-stats">
    <div class="story-stat">
      <div class="fact-num">400+</div>
      <div class="fact-label">People who've played in Minnesota Dodgeball</div>
    </div>
    <div class="story-stat">
      <div class="fact-num">100</div>
      <div class="fact-label">People showing up every single week</div>
    </div>
    <div class="story-stat">
      <div class="fact-num">3</div>
      <div class="fact-label">Businesses, solo-operated alongside a full-time job</div>
    </div>
    <div class="story-stat">
      <div class="fact-num">100%</div>
      <div class="fact-label">Queer-owned &amp; operated</div>
    </div>
  </div>

  <!-- STORY MICRO -->
  <div class="story-micro">
    <div class="story-micro-inner">
      <p>My parents came to America from Vietnam with no English and no safety net — just the drive to make it work. <em>What I learned running three businesses is that drive alone isn't enough.</em> You need the right systems, and the right people around you. That's what I'm building here.</p>
    </div>
  </div>

  <!-- LEAD MAGNET -->
  <div class="lead-section" id="system">
    <div class="lead-inner">
      <span class="section-label">Free Guide</span>
      <h2>The exact system I use to run 3 businesses.</h2>
      <p class="lead-sub">The tools, workflows, and weekly rhythms — broken down step by step. No fluff. Just what actually works when you're running a business alongside everything else.</p>
      <form class="lead-form" action="#" method="post">
        <input type="email" name="email" placeholder="your@email.com" required>
        <button type="submit">Send me the guide →</button>
      </form>
      <p class="lead-note">Free. No spam. Unsubscribe any time.</p>
    </div>
  </div>

  <!-- OFFERINGS PREVIEW -->
  <div class="preview-section">
    <div class="preview-inner">
      <div class="preview-header">
        <span class="section-label">Go Deeper</span>
        <h2>Ready for more than a guide?</h2>
      </div>
      <div class="preview-grid">

        <div class="preview-card">
          <span class="preview-num">01</span>
          <h3>The Cohort Program</h3>
          <p>Six weeks, small group, real accountability. A structured program for queer entrepreneurs and their allies ready to stop spinning and start building — with live sessions and a cohort of people doing the same thing alongside you.</p>
          <a href="cohort.html" class="preview-link">Learn about the cohort →</a>
        </div>

        <div class="preview-card">
          <span class="preview-num">02</span>
          <h3>The Phan Club</h3>
          <p>The ongoing community for queer entrepreneurs and their allies who want to keep building. Accountability, connection, shared wins, real talk — and a space where you actually belong.</p>
          <a href="phan-club.html" class="preview-link">Join the community →</a>
        </div>

      </div>
    </div>
  </div>
```

- [ ] **Step 4: Remove now-unused CSS from styles.css**

Delete these rule blocks from `styles.css` (they belonged to old homepage sections now moved to dedicated pages):
- `.story-section`, `.story-text`, `.story-photo` (the full 2-col story layout)
- `.offerings-section`, `.offerings-inner`, `.offerings-header`, `.offerings-grid`, `.offering-card`, `.offering-num`, `.offering-link`
- `.system-section`, `.system-inner`, `.system-header`, `.system-sub`, `.system-lead-box`, `.system-lead-form`, `.system-steps`, `.system-step`, `.step-num`, `.step-body`
- `.cohort-section`, `.cohort-inner`, `.cohort-heading`, `.cohort-sub`, `.cohort-stats`, `.cohort-stat`, `.cohort-stat-num`, `.cohort-stat-label`, `.cohort-apply`, `.cohort-modules`, `.cohort-module`, `.module-num`, `.module-body`
- `.phan-club-section`, `.phan-club-inner`, `.phan-club-left`, `.phan-club-heading`, `.phan-club-body`, `.phan-club-cta`, `.phan-club-card`, `.phan-club-card-heading`, `.phan-club-features`, `.btn-white`, `.founding-note`
- `.content-section`, `.content-inner`, `.content-header`, `.subscribe-link`, `.video-grid`, `.video-card`, `.video-thumb`, `.thumb-placeholder`, `.play-btn`, `.play-circle`, `.video-info`

Keep: reset, `:root` variables, body, nav rules, `.pride-stripe`, `.site-header`, `.story-stats`, `.story-stat`, `.fact-num`, `.fact-label`, `.section-label`, footer rules, responsive rules (updated in Step 2 above).

- [ ] **Step 5: Verify**

Open `index.html`. Confirm:
- Hero is warm off-white background (no rainbow gradient)
- Stats strip appears below hero
- Short story paragraph appears below stats
- Email capture section appears with form
- Two offering cards appear (Cohort, Phan Club)
- Footer shows social icons
- No broken styles or console errors
- Check at 375px mobile width — everything stacks correctly, form inputs are full-width

- [ ] **Step 6: Commit**

```bash
git add styles.css index.html
git commit -m "feat: rebuild homepage — email-first layout, remove old bloated sections"
```

---

## Task 4: Create phan-club.html

**Goal:** Build the dedicated Phan Club page with the full pitch, features, and founding member CTA. Uses the dark `#0f0e0d` visual treatment (moved off the homepage).

**Files:**
- Create: `phan-club.html`

Note: `styles.css` already contains the shared nav, footer, and base styles. This task adds page-specific styles inside a `<style>` block in `phan-club.html` (page-specific styles don't warrant a separate file for this project size).

- [ ] **Step 1: Create phan-club.html**

Create `/MAP - New Mr Anh Phan Website/phan-club.html` with this complete content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Phan Club — Anh Phan</title>
  <meta name="description" content="The ongoing community for queer entrepreneurs and their allies who want to keep building. Accountability, connection, and a space where you actually belong.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;0,14..32,800;0,14..32,900;1,14..32,400;1,14..32,700;1,14..32,800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <style>
    /* ── PAGE HERO ── */
    .page-hero {
      background: #0f0e0d;
      padding: 100px 48px 80px;
      border-bottom: 5px solid transparent;
      border-image: var(--pride-gradient) 1;
      text-align: center;
    }

    .page-hero .section-label { color: rgba(255,255,255,0.4); margin-bottom: 20px; }

    .page-hero h1 {
      font-size: clamp(32px, 4.5vw, 56px);
      font-weight: 900;
      letter-spacing: -0.04em;
      line-height: 1.05;
      color: #fff;
      max-width: 760px;
      margin: 0 auto 24px;
    }

    .page-hero h1 em { font-style: italic; color: rgba(255,255,255,0.5); }

    .page-hero .hero-sub {
      font-size: 17px;
      color: rgba(255,255,255,0.65);
      line-height: 1.75;
      max-width: 560px;
      margin: 0 auto 40px;
    }

    .btn-white {
      display: inline-flex;
      align-items: center;
      background: #fff;
      color: #111110;
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      font-weight: 800;
      padding: 14px 28px;
      border-radius: 8px;
      transition: opacity 0.2s;
    }
    .btn-white:hover { opacity: 0.92; }

    /* ── FEATURES SECTION ── */
    .features-section {
      padding: 80px 48px;
      background: var(--bg);
      border-bottom: 1px solid var(--border);
    }

    .features-inner {
      max-width: 1000px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 80px;
      align-items: start;
    }

    .features-left h2 {
      font-size: clamp(26px, 3vw, 36px);
      font-weight: 900;
      letter-spacing: -0.03em;
      line-height: 1.1;
      margin-bottom: 24px;
    }

    .features-left p {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.8;
      margin-bottom: 16px;
    }

    .features-left p strong { color: var(--text); font-weight: 600; }

    .features-left p:last-of-type { margin-bottom: 0; }

    .features-card {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 40px 36px;
    }

    .features-card-heading {
      font-size: 17px;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 24px;
      letter-spacing: -0.02em;
    }

    .features-list {
      list-style: none;
      border-top: 1px solid var(--border);
    }

    .features-list li {
      padding: 18px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .features-list strong {
      font-size: 14px;
      font-weight: 700;
      color: var(--text);
      letter-spacing: -0.01em;
    }

    .features-list span {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* ── JOIN CTA SECTION ── */
    .join-section {
      padding: 80px 48px;
      background: #fff;
      text-align: center;
    }

    .join-inner { max-width: 560px; margin: 0 auto; }

    .join-inner h2 {
      font-size: clamp(26px, 3vw, 36px);
      font-weight: 900;
      letter-spacing: -0.03em;
      margin-bottom: 16px;
    }

    .join-inner p {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.75;
      margin-bottom: 32px;
    }

    .founding-note { font-size: 13px; color: var(--text-light); margin-top: 12px; font-weight: 500; }

    /* ── RESPONSIVE ── */
    @media (max-width: 960px) {
      .page-hero { padding: 72px 32px 60px; }
      .features-section { padding: 60px 24px; }
      .features-inner { grid-template-columns: 1fr; gap: 40px; }
      .join-section { padding: 60px 24px; }
    }

    @media (max-width: 640px) {
      .page-hero { padding: 60px 20px 48px; }
      .features-section { padding: 52px 20px; }
      .features-card { padding: 32px 24px; }
      .join-section { padding: 52px 20px; }
    }
  </style>
</head>
<body>

  <div class="site-header">
    <div class="pride-stripe"></div>
    <nav>
      <a href="index.html" class="nav-logo">Anh <span class="nav-logo-accent">Phan</span></a>
      <div class="nav-links">
        <a href="cohort.html" class="nav-link">Cohort</a>
        <a href="phan-club.html" class="nav-link" style="color:var(--text);font-weight:700;">The Phan Club</a>
      </div>
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="nav-divider"></div>
        <a href="https://community.mranhphan.com/invitation?code=55FC2F" target="_blank" class="nav-login">Join The Phan Club</a>
      </div>
    </nav>
    <div class="pride-stripe"></div>
  </div>

  <!-- PAGE HERO -->
  <div class="page-hero">
    <span class="section-label">The Phan Club</span>
    <h1>The ongoing home for queer entrepreneurs — <em>who want to keep building.</em></h1>
    <p class="hero-sub">Community, accountability, and people who actually show up for each other. Queer-led and values-forward — genuine allies belong here too.</p>
    <a href="https://community.mranhphan.com/invitation?code=55FC2F" target="_blank" class="btn-white">Join The Phan Club →</a>
  </div>

  <!-- FEATURES -->
  <div class="features-section">
    <div class="features-inner">

      <div class="features-left">
        <span class="section-label">What It Is</span>
        <h2>You don't have to build alone.</h2>
        <p>The Phan Club is where you stay after the cohort — or where you start if you're not ready for the intensive yet. It's a community for queer entrepreneurs and allies who want real connection, real accountability, and people who actually show up for each other.</p>
        <p><strong>This isn't a passive membership.</strong> It's a space where people share wins, navigate hard decisions together, and build real friendships across industries and stages.</p>
        <p>We're working toward in-person retreats and experiences too — because the best conversations happen in the same room.</p>
        <p>Queer-led and values-forward. The majority of us are queer, but genuine allies who show up for this community belong here too.</p>
        <p>We're in <strong>founding member mode</strong> — building the first core group who will shape what this becomes. Founding members lock in a special rate for the long haul.</p>
      </div>

      <div class="features-card">
        <p class="features-card-heading">What's included</p>
        <ul class="features-list">
          <li>
            <strong>Queer entrepreneurs &amp; their allies</strong>
            <span>All stages, all industries — real people building real things</span>
          </li>
          <li>
            <strong>Accountability &amp; community</strong>
            <span>Show up, share progress, get honest feedback</span>
          </li>
          <li>
            <strong>Systems &amp; productivity resources</strong>
            <span>Tools, frameworks, and walkthroughs that actually translate to results</span>
          </li>
          <li>
            <strong>Cohort program access</strong>
            <span>Members get priority access and founding-member pricing</span>
          </li>
          <li>
            <strong>In-person experiences &amp; trips</strong>
            <span>Because community happens IRL too</span>
          </li>
        </ul>
      </div>

    </div>
  </div>

  <!-- JOIN CTA -->
  <div class="join-section">
    <div class="join-inner">
      <span class="section-label">Ready?</span>
      <h2>Founding member spots are open.</h2>
      <p>Come as you are. Lock in founding-member pricing before we open the doors wider.</p>
      <a href="https://community.mranhphan.com/invitation?code=55FC2F" target="_blank" class="btn-white" style="background:var(--accent);color:#fff;">Join The Phan Club →</a>
      <p class="founding-note">Founding members lock in the special rate for as long as they stay.</p>
    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    <div class="footer-inner">
      <a href="index.html" class="footer-logo">Anh <span class="nav-logo-accent">Phan</span></a>
      <div class="footer-links">
        <a href="https://www.instagram.com/mr_anhphan" target="_blank" class="footer-social">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          Instagram
        </a>
        <a href="https://www.tiktok.com/@mr_anhphan" target="_blank" class="footer-social">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.95a8.16 8.16 0 0 0 4.77 1.52V7.02a4.85 4.85 0 0 1-1-.33z"/></svg>
          TikTok
        </a>
        <a href="https://www.youtube.com/@mr_anhphan" target="_blank" class="footer-social">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          YouTube
        </a>
      </div>
      <div class="footer-copy">&copy; 2026 Phan Ventures LLC</div>
    </div>
  </footer>

</body>
</html>
```

- [ ] **Step 2: Verify**

Open `phan-club.html` in a browser. Confirm:
- Dark hero with pride stripe border at bottom
- Features section shows 2-col layout (text + card)
- Join CTA section at bottom
- Nav links work: clicking "Cohort" navigates to `cohort.html` (even if the page doesn't exist yet — that's fine)
- Nav logo links back to `index.html`
- Check at 375px mobile — single column, no overflow

- [ ] **Step 3: Commit**

```bash
git add phan-club.html
git commit -m "feat: add dedicated Phan Club page"
```

---

## Task 5: Create cohort.html

**Goal:** Build the dedicated Cohort Program page. This is the one place where the rainbow gradient gets used as a full-bleed background — an intentional, high-impact visual moment for the highest-commitment offer.

**Files:**
- Create: `cohort.html`

- [ ] **Step 1: Create cohort.html**

Create `/MAP - New Mr Anh Phan Website/cohort.html` with this complete content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Cohort Program — Anh Phan</title>
  <meta name="description" content="Six weeks. Small group. Real accountability. A structured program for queer entrepreneurs and their allies ready to stop spinning and start building.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;0,14..32,800;0,14..32,900;1,14..32,400;1,14..32,700;1,14..32,800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <style>
    /* ── PAGE HERO ── */
    .cohort-hero {
      position: relative;
      padding: 100px 48px 80px;
      background: linear-gradient(
        150deg,
        #6D28D9  0%,
        #1D4ED8  22%,
        #0891B2  44%,
        #059669  66%,
        #D97706  88%,
        #DC2626  100%
      );
      text-align: center;
    }

    .cohort-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.30);
      pointer-events: none;
    }

    .cohort-hero-inner {
      position: relative;
      z-index: 1;
    }

    .cohort-hero .section-label { color: rgba(255,255,255,0.5); margin-bottom: 20px; }

    .cohort-hero h1 {
      font-size: clamp(32px, 4.5vw, 56px);
      font-weight: 900;
      letter-spacing: -0.04em;
      line-height: 1.05;
      color: #FCD34D;
      max-width: 760px;
      margin: 0 auto 24px;
    }

    .cohort-hero h1 em { font-style: italic; color: rgba(255,255,255,0.65); }

    .cohort-hero .hero-sub {
      font-size: 17px;
      color: rgba(255,255,255,0.72);
      line-height: 1.75;
      max-width: 560px;
      margin: 0 auto 40px;
    }

    .cohort-stats-strip {
      display: flex;
      justify-content: center;
      gap: 48px;
      margin-bottom: 40px;
    }

    .cohort-stat { display: flex; flex-direction: column; gap: 4px; text-align: center; }

    .cohort-stat-num {
      font-size: 40px;
      font-weight: 900;
      letter-spacing: -0.04em;
      line-height: 1;
      color: #fff;
    }

    .cohort-stat-label {
      font-size: 11px;
      font-weight: 700;
      color: rgba(255,255,255,0.5);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    .cohort-apply {
      display: inline-flex;
      align-items: center;
      background: #fff;
      color: #111110;
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      font-weight: 800;
      padding: 14px 28px;
      border-radius: 8px;
      transition: opacity 0.2s;
    }
    .cohort-apply:hover { opacity: 0.9; }

    /* ── MODULES SECTION ── */
    .modules-section {
      padding: 80px 48px;
      background: var(--bg);
      border-bottom: 1px solid var(--border);
    }

    .modules-inner {
      max-width: 1000px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 80px;
      align-items: start;
    }

    .modules-left h2 {
      font-size: clamp(26px, 3vw, 36px);
      font-weight: 900;
      letter-spacing: -0.03em;
      line-height: 1.1;
      margin-bottom: 24px;
    }

    .modules-left p {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.8;
      margin-bottom: 16px;
    }

    .modules-left p strong { color: var(--text); font-weight: 600; }

    .modules-list {
      border-top: 1px solid var(--border);
    }

    .module-item {
      display: flex;
      gap: 24px;
      padding: 28px 0;
      border-bottom: 1px solid var(--border);
      align-items: flex-start;
    }

    .module-num {
      font-size: 11px;
      font-weight: 800;
      color: var(--accent);
      letter-spacing: 0.08em;
      min-width: 24px;
      padding-top: 3px;
    }

    .module-body strong {
      display: block;
      font-size: 16px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
      letter-spacing: -0.01em;
    }

    .module-body span {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.65;
    }

    .cohort-details-card {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 40px 36px;
    }

    .cohort-details-card h3 {
      font-size: 17px;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }

    .cohort-details-card .card-sub {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 28px;
    }

    .details-list {
      list-style: none;
      border-top: 1px solid var(--border);
    }

    .details-list li {
      padding: 16px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .details-list strong {
      font-size: 14px;
      font-weight: 700;
      color: var(--text);
    }

    .details-list span {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    .card-cta {
      margin-top: 28px;
    }

    .btn-accent {
      display: inline-flex;
      align-items: center;
      background: var(--accent);
      color: #fff;
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      font-weight: 800;
      padding: 14px 28px;
      border-radius: 8px;
      transition: opacity 0.2s;
      width: 100%;
      justify-content: center;
    }
    .btn-accent:hover { opacity: 0.88; }

    /* ── RESPONSIVE ── */
    @media (max-width: 960px) {
      .cohort-hero { padding: 72px 32px 60px; }
      .cohort-stats-strip { gap: 28px; }
      .modules-section { padding: 60px 24px; }
      .modules-inner { grid-template-columns: 1fr; gap: 40px; }
    }

    @media (max-width: 640px) {
      .cohort-hero { padding: 60px 20px 48px; }
      .cohort-stats-strip { gap: 20px; }
      .cohort-stat-num { font-size: 30px; }
      .modules-section { padding: 52px 20px; }
      .cohort-details-card { padding: 32px 24px; }
    }
  </style>
</head>
<body>

  <div class="site-header">
    <div class="pride-stripe"></div>
    <nav>
      <a href="index.html" class="nav-logo">Anh <span class="nav-logo-accent">Phan</span></a>
      <div class="nav-links">
        <a href="cohort.html" class="nav-link" style="color:var(--text);font-weight:700;">Cohort</a>
        <a href="phan-club.html" class="nav-link">The Phan Club</a>
      </div>
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="nav-divider"></div>
        <a href="https://community.mranhphan.com/invitation?code=55FC2F" target="_blank" class="nav-login">Apply Now</a>
      </div>
    </nav>
    <div class="pride-stripe"></div>
  </div>

  <!-- PAGE HERO -->
  <div class="cohort-hero">
    <div class="cohort-hero-inner">
      <span class="section-label">The Cohort Program</span>
      <h1>6 weeks. Small group.<br><em>Real systems.</em></h1>
      <p class="hero-sub">For queer entrepreneurs and their allies who are ready to stop spinning and start building with intention. Direct access, live sessions, and a cohort of people who get it — because they're living it too.</p>
      <div class="cohort-stats-strip">
        <div class="cohort-stat">
          <span class="cohort-stat-num">6</span>
          <span class="cohort-stat-label">Weeks</span>
        </div>
        <div class="cohort-stat">
          <span class="cohort-stat-num">10–15</span>
          <span class="cohort-stat-label">Entrepreneurs</span>
        </div>
        <div class="cohort-stat">
          <span class="cohort-stat-num">Live</span>
          <span class="cohort-stat-label">Sessions</span>
        </div>
      </div>
      <a href="https://community.mranhphan.com/invitation?code=55FC2F" target="_blank" class="cohort-apply">Apply to a Cohort →</a>
    </div>
  </div>

  <!-- MODULES -->
  <div class="modules-section">
    <div class="modules-inner">

      <div class="modules-left">
        <span class="section-label">What You'll Build</span>
        <h2>A system that fits your actual life.</h2>
        <p>In six weeks, you'll establish the workflows, tools, and rhythms that let you run a business without burning out. Not a template you force yourself into — a system built around how you actually operate.</p>
        <p><strong>You'll work alongside 10–15 other people who get it,</strong> because they're living it too. Direct access to me, live group sessions, and real feedback on your actual situation.</p>

        <div class="modules-list">
          <div class="module-item">
            <span class="module-num">01</span>
            <div class="module-body">
              <strong>Audit Your Current Reality</strong>
              <span>Where is your time and energy actually going? Before you build new systems, you have to see clearly what's running (and draining) you right now.</span>
            </div>
          </div>
          <div class="module-item">
            <span class="module-num">02</span>
            <div class="module-body">
              <strong>Design Your System</strong>
              <span>Tools, workflows, and rhythms — built for how you actually operate. Not a template you force yourself into. A system that fits your life and your goals.</span>
            </div>
          </div>
          <div class="module-item">
            <span class="module-num">03</span>
            <div class="module-body">
              <strong>Operations for Solo Operators</strong>
              <span>Running a business without a team. The infrastructure that keeps you moving — without burning out or dropping everything the moment life gets full.</span>
            </div>
          </div>
          <div class="module-item">
            <span class="module-num">04</span>
            <div class="module-body">
              <strong>Accountability &amp; Peer Learning</strong>
              <span>Weekly group sessions, real feedback, and a cohort of queer entrepreneurs and allies who are building at the same time as you. You're not doing this alone.</span>
            </div>
          </div>
        </div>
      </div>

      <div class="cohort-details-card">
        <h3>Cohort details</h3>
        <p class="card-sub">What to expect when you apply.</p>
        <ul class="details-list">
          <li>
            <strong>6-week structured program</strong>
            <span>Weekly live sessions, frameworks, and between-session accountability</span>
          </li>
          <li>
            <strong>Small group (10–15 people)</strong>
            <span>Intentionally small so everyone gets real attention — not a webinar</span>
          </li>
          <li>
            <strong>Direct access to Anh</strong>
            <span>Live sessions, Q&amp;A, feedback on your actual situation</span>
          </li>
          <li>
            <strong>Queer entrepreneurs &amp; allies</strong>
            <span>A community where you actually belong — built into the program</span>
          </li>
          <li>
            <strong>Phan Club membership included</strong>
            <span>Continue the community after the cohort ends</span>
          </li>
        </ul>
        <div class="card-cta">
          <a href="https://community.mranhphan.com/invitation?code=55FC2F" target="_blank" class="btn-accent">Apply to a Cohort →</a>
        </div>
      </div>

    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    <div class="footer-inner">
      <a href="index.html" class="footer-logo">Anh <span class="nav-logo-accent">Phan</span></a>
      <div class="footer-links">
        <a href="https://www.instagram.com/mr_anhphan" target="_blank" class="footer-social">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          Instagram
        </a>
        <a href="https://www.tiktok.com/@mr_anhphan" target="_blank" class="footer-social">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.95a8.16 8.16 0 0 0 4.77 1.52V7.02a4.85 4.85 0 0 1-1-.33z"/></svg>
          TikTok
        </a>
        <a href="https://www.youtube.com/@mr_anhphan" target="_blank" class="footer-social">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          YouTube
        </a>
      </div>
      <div class="footer-copy">&copy; 2026 Phan Ventures LLC</div>
    </div>
  </footer>

</body>
</html>
```

- [ ] **Step 2: Verify**

Open `cohort.html` in a browser. Confirm:
- Rainbow gradient hero (this is the ONLY page where it appears — intentional)
- Yellow headline, stats strip, white CTA button in hero
- Modules section shows 2-col layout (module list + details card)
- "Apply to a Cohort" buttons work (link to community)
- Nav logo links back to `index.html`
- Check at 375px — stacks correctly

- [ ] **Step 3: Final cross-page verification**

Open all three pages and verify:
- `index.html` → homepage: warm off-white hero, no rainbow, email form prominent, two offering cards link correctly
- `phan-club.html` → dark hero, 2-col features section, join CTA
- `cohort.html` → rainbow hero (one place, intentional), modules, apply CTA
- Nav links are consistent across all pages
- Footer social icons appear on all pages
- All internal links work (Cohort → cohort.html, Phan Club → phan-club.html, nav logos → index.html)

- [ ] **Step 4: Commit**

```bash
git add cohort.html
git commit -m "feat: add dedicated Cohort Program page"
```

---

## Self-Review

**Spec coverage check:**
- ✅ Multi-page structure (homepage + phan-club.html + cohort.html)
- ✅ Email list as primary homepage conversion goal (lead magnet section, hero CTA anchors to it)
- ✅ Hybrid nav (logo + 2 page links + CTA button)
- ✅ Story shortened to 2-3 sentences (story-micro section)
- ✅ Rainbow gradient removed from homepage, kept exclusively on cohort.html
- ✅ Pride stripe bars on all pages
- ✅ Warm off-white + white visual system on homepage
- ✅ Dark treatment moved to phan-club.html hero
- ✅ YouTube downgraded to footer link only
- ✅ Socials moved from nav to footer
- ✅ Stats strip kept on homepage

**Type/class consistency check:**
- `.section-label` used across all tasks — defined in styles.css (Task 1)
- `.nav-logo`, `.nav-logo-accent`, `.nav-links`, `.nav-link`, `.nav-login`, `.nav-divider` — defined in styles.css (Task 2)
- `.footer-social` — defined in styles.css (Task 2)
- `.story-stats`, `.story-stat`, `.fact-num`, `.fact-label` — from original styles.css (Task 1 extraction, unchanged)
- `--pride-gradient`, `--bg`, `--text`, `--accent`, `--border` CSS variables — from original styles.css `:root`
- Page-specific classes (`.cohort-hero`, `.features-section`, etc.) — scoped to `<style>` blocks in each page file
