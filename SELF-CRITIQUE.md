# Self-critique — the redesign

Honest assessment, not a highlight reel. Structured as: what's genuinely
better, what's still a compromise, and what I'd flag if I were reviewing
someone else's work before it went live.

## What's genuinely better

- **The homepage now makes its one ask obvious in one screen.** The old
  layout put a small side-by-side hero above a separate services section
  above a form buried further down. The lead form is now inside the hero
  itself, above the fold, next to the reason to fill it in. That's the
  single highest-impact change for a lead-gen site — everything else here
  is polish by comparison.
- **The image reassignment is a real fix, not just a coat of paint.** The
  old homepage/pressure-washing hero was a photo of someone pressure
  washing an *indoor garage floor* — on a site selling *exterior* cleaning.
  It's now used lower down as a supporting "professional equipment" shot,
  and the pressure-washing hero uses the outdoor stone-steps photo instead,
  which is what the page is actually about.
- **Scroll animations are restrained and turn off cleanly.** Reveal
  animations use `IntersectionObserver`, degrade to fully-visible content
  if JS is disabled or unsupported (both a `<noscript>` CSS override and a
  feature-detect fallback), and respect `prefers-reduced-motion`. This
  matters more than it sounds — a lot of "wow" redesigns break
  accessibility or SEO crawlability by hiding content behind animation
  that never fires for a crawler or a screen-reader user. Google's crawler
  does execute JS, but I didn't want to bet the whole page on that working
  perfectly, hence the fallbacks.
- **Content expansion is genuinely differentiated, not padding.** Rather
  than repeating the same generic paragraph with a different town name
  swapped in (a doorway-page pattern SEO.md explicitly rules out), the new
  sections — "signs you need X", per-surface detail on the pressure
  washing page, "what we don't do" on About, a third guide article — say
  something a competitor's templated page wouldn't. The area pages already
  did this reasonably well before my changes; I kept that structure and
  extended the same standard to the service pages, which needed it more.
- **One real bug caught and fixed during this pass, unrelated to the
  redesign brief:** the About and Contact pages had the phone number and
  `tel:` link hand-typed as literal text instead of referencing the
  `PHONE_DISPLAY`/`PHONE_TEL` constants. If you'd filled in the real number
  in `generate_site.py` per `SETUP.md`, the header and footer would have
  updated but About and Contact would have silently kept showing
  `[PHONE NUMBER TODO]`. That's now fixed — every page pulls from the same
  constant, which was the whole point of centralising it in the first
  place.

## Real compromises, made on purpose

- **The lead form is only "huge in the hero" on the homepage.** You asked
  for the form in a huge hero header; I read that as primarily about the
  homepage, since repeating the full form as the first thing on every
  single page would be repetitive and would bury the actual page content
  (what pressure washing involves, what areas are covered) below a form
  someone hasn't decided to fill in yet. Service and area pages instead
  get a full-width photo hero with a clear "Get a free quote" button that
  jumps to the form further down. If you want the full form in every
  page's hero too, that's a straightforward change to `page_hero()` — I
  didn't do it by default because I think it would hurt conversion more
  than help it, but it's your call, not mine to make silently.
- **I didn't source new photography for this pass.** "Clean up the
  images" was handled by re-casting the 11 existing Pexels photos into
  better-fitting roles (see above) and normalising how they're cropped in
  cards/heroes, not by pulling in new stock. The existing library was
  serviceable everywhere once correctly assigned; I judged that spending
  the time on layout, content and animation would move the needle more
  than swapping in marginally-better stock photos of driveways. If you
  want a specific hero photo replaced, that's a five-minute fetch through
  the same Pexels workflow used originally.
- **The logo has a visible flaw if you look closely: the shield outline
  and the swash/ribbon shape overlap in a way that reads a little busy at
  small sizes (32px favicon).** I generated it once in Gemini, fixed the
  transparency (it came back as a flattened checkerboard baked into JPEG
  pixels, not real alpha — I rebuilt the alpha channel with a
  saturation-threshold pass rather than re-prompting), and used it as-is
  rather than iterating on the design itself. A second design pass
  specifically for favicon legibility at 16–32px would be worth doing
  before this goes live at full scale.
- **"What we don't do" and similar values-based copy is new content I
  wrote to fill out the About page.** It's honest and consistent with
  everything else on the site (no invented claims), but it's still
  marketing copy I generated, not something you told me about the
  business. Read it before launch and confirm it's actually how you want
  to represent the business — I'd rather you catch anything that doesn't
  sound right than have it ship unreviewed.

## What I'd flag if this were someone else's PR

- **The three `[PHONE NUMBER TODO]` / `tel:+44TODO` placeholders are still
  there, unavoidably** — no real number was ever provided, and inventing
  one would be worse than a visible placeholder. But a visible
  `[PHONE NUMBER TODO]` pill sitting in the header of a "beautiful,
  wow-factor" redesign is a jarring visual note, and it's the first thing
  anyone previewing this site will see. This is the single most important
  thing to fix before showing this to anyone outside your own review.
- **The Formspree endpoint is still the placeholder** (`YOUR_FORM_ID`), so
  the form doesn't currently deliver anywhere — `SETUP.md` step 2 covers
  the five-minute signup to fix that. Test it end-to-end once it's live;
  I've verified the HTML/markup is correct, but I can't confirm delivery
  without your real endpoint.
- **I didn't add real go-live infrastructure this pass** — no analytics,
  no Search Console verification, no CDN/host chosen. That was out of
  scope for "make it wow" but is still between here and actually being
  found in search.
- **Every measurement I've reported (title/description lengths, zero
  horizontal overflow at 375/1030/1440px, zero broken internal links, no
  missing images) was checked programmatically against the built `dist/`
  output** — via small Python scripts and a headless Playwright sweep —
  not eyeballed. That's a habit worth keeping, but it's also worth you
  independently spot-checking on a real phone once it's deployed;
  automated checks catch what I thought to check for, not everything.
