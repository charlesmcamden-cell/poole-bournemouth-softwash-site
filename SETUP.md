# Setup — before this goes live

This site was built as static HTML/CSS/JS (no server or framework required)
following the house SEO.md standard you uploaded: every page has its own
real URL, its own title/description/canonical, one h1, alt text on every
image, a generated robots.txt/sitemap.xml, and no invented reviews, ratings,
stats or years-in-business anywhere. Three things are placeholders on
purpose — fill these in before it goes live.

## 1. Phone number (currently `[PHONE NUMBER TODO]`)

Per the "never fabricate" rule, a phone number wasn't invented — publishing
a fake one on a live lead site would mislead callers. To set the real one:

1. Open `generate_site.py`
2. Set `PHONE_DISPLAY = "01202 XXX XXX"` (however you want it shown)
3. Set `PHONE_TEL = "tel:+441202XXXXXX"` (the `tel:` link format — no
   spaces, UK country code)
4. Re-run `python3 build.py` — every page updates from this one place.

## 2. Lead form → Formspree

The quote form on every page POSTs to a placeholder Formspree endpoint.
To make it actually deliver leads to **leads@eapionageseo.co.uk**:

1. Go to https://formspree.io and sign up (free tier covers this).
2. Create a new form, and verify **leads@eapionageseo.co.uk** as the
   recipient address (Formspree emails a confirmation link).
3. Copy the form endpoint it gives you — looks like
   `https://formspree.io/f/abcdwxyz`.
4. Open `generate_site.py`, set `FORMSPREE_ENDPOINT` to that URL.
5. Re-run `python3 build.py`. Because every page shares the one
   `lead_form()` function, this one change updates the form on all 17 pages.
6. Submit a test enquiry on the live site once deployed and confirm it
   lands in the inbox.

No account was created on your behalf — this step needs your login.

## 3. Domain

Every canonical URL, the sitemap, and the Organization schema currently
point at a placeholder: `https://www.poolebournemouthsoftwash.co.uk`.
Once you've registered/confirmed the real domain:

1. Update `BASE_URL` in `generate_site.py`.
2. Re-run `python3 build.py`.
3. Work through Rule 10 in SEO.md before pointing DNS at it — sitemap
   submitted in Search Console, analytics installed, no 404s.

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
