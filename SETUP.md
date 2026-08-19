# Setup — before this goes live

This site was built as static HTML/CSS/JS (no server or framework required)
following the house SEO.md standard you uploaded: every page has its own
real URL, its own title/description/canonical, one h1, alt text on every
image, a generated robots.txt/sitemap.xml, and no invented reviews, ratings,
stats or years-in-business anywhere. A couple of things were placeholders
on purpose — status below.

## 1. Phone number — done

`PHONE_DISPLAY` is set to `0330 122 8391` and `PHONE_TEL` to
`tel:+443301228391` in `generate_site.py`, live site-wide (header, footer,
About, Contact). To change it later: edit those two constants and re-run
`python3 build.py` — every page updates from this one place.

## 2. Lead form → Formspree — almost done

Formspree account created ("jet washing form"), and `FORMSPREE_ENDPOINT`
is set to `https://formspree.io/f/mqpzgqjk` in `generate_site.py` — every
page's form now POSTs there.

One step left, and it's not one I can do for you: the Email action in the
form's Workflow tab was still pointing at your personal Gmail by default,
so I added **leads@eapionageseo.co.uk** as a second linked email on the
Formspree account (Account → Linked Emails). Formspree just sent a
verification link to that inbox — click it, then go to
**Workflow → Email → Settings** on the form and switch the recipient
dropdown from your Gmail to `leads@eapionageseo.co.uk`. Until that's done,
submissions succeed but land in the Gmail address, not the leads inbox.

## 3. Domain

Every canonical URL, the sitemap, and the Organization schema currently
point at a placeholder: `https://www.poolebournemouthsoftwash.co.uk`.
Once you've registered/confirmed the real domain:

1. Update `BASE_URL` in `generate_site.py`.
2. Re-run `python3 build.py`.
3. Work through Rule 10 in SEO.md before pointing DNS at it — sitemap
   submitted in Search Console, analytics installed, no 404s.

## 4. Daily blog post automation — live

A scheduled cloud agent ("PB Softwash — daily blog post") runs every day at
7am Europe/London. Each run: picks one new guide topic not already covered
in `build_pages.py`'s `NEWS_CATEGORIES`, writes a 600+ word article
following this site's content rules (no invented reviews/stats/testimonials,
title 50–60 chars, description 140–160 chars), adds it to the News & Info
hub, rebuilds the site, commits, and pushes to `origin main`. Vercel is
connected via GitHub integration and auto-deploys on push — no manual
deploy step needed.

Manage/pause/delete it at:
https://claude.ai/code/routines/trig_01878K6pXQaxQQYMYBwm7roa

Note: the daily agent does **not** use `build.py` (see below — it's stale).
It rebuilds by pointing `generate_site.DIST` at the repo root directly, so
pages land in their existing `folder/index.html` locations. Any manual
rebuild should do the same rather than running `python3 build.py` as-is.

## Other things intentionally left out, not forgotten

- **No testimonials, star ratings, review counts, or "X years in
  business."** SEO.md's rule 1 is explicit: an invented one is worse than
  none. Add these once you have real ones — there's a marked spot on the
  About page (`build_pages.py`, look for the `<!-- TODO -->` comment) ready
  for genuine job photos.
- **Privacy policy has two open TODOs** — whether leads are ever shared
  with or sold to a third party (a straight rank-and-rent arrangement would
  need to say so explicitly under UK GDPR), and your actual data retention
  period. Both are marked in `build_pages.py` under `/privacy-policy/`.
- **Terms page** has a TODO for real trading terms (cancellation, payment,
  insurance) — nothing was invented there either.

## How to rebuild after any edit

```
cd site
python3 build.py
```

This regenerates the entire `dist/` folder from `generate_site.py` +
`build_pages.py`. Titles/descriptions are asserted to be within the
50–60 / 140–160 character ranges from SEO.md — the build will fail loudly
with the exact page and length if one's out of range, rather than shipping
a bad tag silently.

## Deploying

`dist/` is a complete static site — drag-and-drop onto Netlify/Vercel/
Cloudflare Pages, or upload via FTP to any standard host. Clean URLs
(`/pressure-washing/` etc.) work out of the box because every page is
built as `folder/index.html`, which every static host resolves automatically.

## Images

All stock photography is Pexels-licensed (free commercial use, no
attribution required) — full source log in `IMAGE-CREDITS.md`. They're
there to make the site launch-ready today; real job photos will convert
better than stock the moment you have some to swap in.

## Logo

The header/footer/favicon logo (`assets/logo.png`, `assets/favicon-*.png`)
was generated in Gemini and is already wired in everywhere. If you want a
different mark later, drop the new image in as `assets/logo.png` (and
regenerate the favicon sizes — any image resizer will do 32/48/192/512px
PNGs plus a 180px `apple-touch-icon.png`) and re-run `python3 build.py`.
