#!/usr/bin/env python3
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

# fresh build
if os.path.exists(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST)

import generate_site  # noqa: E402
import build_pages  # noqa: E402  (executes page() calls, populating generate_site.PAGES)

BASE_URL = generate_site.BASE_URL
PAGES = generate_site.PAGES

# ---- static assets ----
os.makedirs(os.path.join(DIST, "css"), exist_ok=True)
os.makedirs(os.path.join(DIST, "js"), exist_ok=True)
os.makedirs(os.path.join(DIST, "images"), exist_ok=True)
shutil.copy(os.path.join(ROOT, "assets", "style.css"), os.path.join(DIST, "css", "style.css"))
shutil.copy(os.path.join(ROOT, "assets", "main.js"), os.path.join(DIST, "js", "main.js"))
for logo_asset in ("favicon.svg", "favicon-32.png", "favicon-48.png", "favicon-192.png",
                    "favicon-512.png", "apple-touch-icon.png", "logo.png", "logo@2x.png"):
    shutil.copy(os.path.join(ROOT, "assets", logo_asset), os.path.join(DIST, "images", logo_asset))
for fname in os.listdir(os.path.join(ROOT, "images")):
    shutil.copy(os.path.join(ROOT, "images", fname), os.path.join(DIST, "images", fname))

# ---- 404 page (special filename, not a directory) ----
NOINDEX_PATHS = {"/thank-you/"}
INDEXABLE_PAGES = [p for p in PAGES if p not in NOINDEX_PATHS]

with open(os.path.join(DIST, "404.html"), "w") as f:
    f.write(f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page Not Found | PB Softwash</title>
<meta name="description" content="This page could not be found. Browse our pressure washing, gutter cleaning and roof cleaning services, or head back to the homepage.">
<meta name="robots" content="noindex,follow">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
</head>
<body>
{generate_site.header_html("")}
<main id="main">
<h1>Page not found</h1>
<p class="lead">That page doesn't exist or has moved. Try one of these:</p>
<div class="area-links">
  <a href="/">Homepage</a>
  <a href="/pressure-washing/">Pressure washing</a>
  <a href="/gutter-and-fascia-cleaning/">Gutter &amp; fascia cleaning</a>
  <a href="/roof-cleaning/">Roof cleaning</a>
  <a href="/contact/">Contact</a>
</div>
</main>
{generate_site.footer_html()}
</body>
</html>""")

# ---- robots.txt (generated, not hand-typed, so it can't fall out of sync) ----
with open(os.path.join(DIST, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")

# ---- sitemap.xml — built from the exact same PAGES list that got rendered ----
url_entries = []
for p in INDEXABLE_PAGES:
    loc = f"{BASE_URL}/" if p == "/" else f"{BASE_URL}{p}"
    url_entries.append(f"  <url><loc>{loc}</loc></url>")
sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(url_entries)
    + "\n</urlset>\n"
)
with open(os.path.join(DIST, "sitemap.xml"), "w") as f:
    f.write(sitemap)

print(f"\nBuild complete: {len(PAGES)} pages rendered, {len(INDEXABLE_PAGES)} in sitemap.xml.")
print(f"Output: {DIST}")
