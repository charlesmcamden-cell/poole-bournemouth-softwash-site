#!/usr/bin/env python3
"""
Static site generator for Poole & Bournemouth Softwash.

Built this way on purpose, per SEO.md ("put the rule in the code, not in a
checklist"):
  - title/description are REQUIRED arguments to page() -> can't ship a page
    with a missing or inherited tag.
  - canonical is DERIVED from the url path + BASE_URL, never hand-typed on
    a page -> Rule 3 can't drift.
  - breadcrumb JSON-LD is generated from the same breadcrumb list used to
    render the visible breadcrumb trail -> the markup always matches what's
    on the page (Rule 5: never mark up something that isn't on the page).
  - sitemap.xml is generated from the exact same PAGES list that gets
    rendered -> it can never list a URL that wasn't actually built.

Run:  python3 generate_site.py
Output: ./dist/
"""
import os
import json
import shutil
from html import escape
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

# ---------------------------------------------------------------------------
# Site-wide constants. BASE_URL and PHONE are placeholders — see SETUP.md.
# ---------------------------------------------------------------------------
BASE_URL = "https://www.poolebournemouthsoftwash.co.uk"  # TODO: confirm real domain before cutover
BRAND = "Poole & Bournemouth Softwash"
PHONE_DISPLAY = "0330 122 8391"
PHONE_TEL = "tel:+443301228391"
EMAIL = "leads@eapionageseo.co.uk"
FORMSPREE_ENDPOINT = "https://formspree.io/f/mqpzgqjk"
TODAY = date.today().isoformat()

NAV = [
    ("/", "Home"),
    ("/pressure-washing/", "Pressure Washing"),
    ("/gutter-and-fascia-cleaning/", "Gutter & Fascia"),
    ("/roof-cleaning/", "Roof Cleaning"),
    ("/areas/", "Areas"),
    ("/guides/", "News & Info"),
    ("/contact/", "Contact"),
]
# About and FAQ are one click away via the footer on every page (Rule 9:
# reachable from another page in plain HTML), just not in the primary nav —
# keeps the header usable at normal desktop widths. News & Info earns a nav
# slot because it's the hub for every article and was otherwise footer-only,
# which made the articles effectively unfindable from the top of the site.

PAGES = []  # populated by page() as pages are defined; drives sitemap.xml


def img(src, alt, width, height, css_class="", loading="lazy", fetchpriority=None):
    assert alt is not None, f"missing alt text for {src}"
    attrs = f'src="/images/{src}" alt="{escape(alt)}" width="{width}" height="{height}" loading="{loading}"'
    if fetchpriority:
        attrs += f' fetchpriority="{fetchpriority}"'
    if css_class:
        attrs += f' class="{css_class}"'
    return f"<img {attrs}>"


def lead_form(source_page, compact=False):
    """The one lead-capture form, used everywhere, so FORMSPREE_ENDPOINT only
    ever needs changing in one place before relaunch."""
    heading = "Get a free, no-obligation quote" if not compact else "Request a quote"
    return f"""
    <div class="lead-form-card">
      <h2>{heading}</h2>
      <p>Tell us a bit about the job and we'll call you back with a price — usually the same day.</p>
      <form action="{FORMSPREE_ENDPOINT}" method="POST" class="lead-form">
        <input type="hidden" name="_subject" value="New website lead — {BRAND}">
        <input type="hidden" name="page" value="{escape(source_page)}">
        <input type="hidden" name="_next" value="{BASE_URL}/thank-you/">
        <label for="name-{source_page}">Full name <span aria-hidden="true">*</span></label>
        <input id="name-{source_page}" type="text" name="name" autocomplete="name" required>

        <label for="phone-{source_page}">Phone number <span aria-hidden="true">*</span></label>
        <input id="phone-{source_page}" type="tel" name="phone" autocomplete="tel" required
               placeholder="e.g. 07700 900123">

        <label for="email-{source_page}">Email address</label>
        <input id="email-{source_page}" type="email" name="email" autocomplete="email">

        <label for="postcode-{source_page}">Postcode</label>
        <input id="postcode-{source_page}" type="text" name="postcode" autocomplete="postal-code" placeholder="e.g. BH14">

        <label for="service-{source_page}">Service needed</label>
        <select id="service-{source_page}" name="service">
          <option value="Pressure washing">Pressure washing (driveway / patio)</option>
          <option value="Gutter and fascia cleaning">Gutter &amp; fascia cleaning</option>
          <option value="Roof cleaning">Roof cleaning (soft wash)</option>
          <option value="Not sure / more than one">Not sure / more than one</option>
        </select>

        <label for="message-{source_page}">Anything else we should know?</label>
        <textarea id="message-{source_page}" name="message" rows="3" placeholder="Size of driveway, how many storeys, access, etc. (optional)"></textarea>

        <button type="submit" class="btn btn-primary btn-block">Request my free quote</button>
        <p class="form-note">Required fields marked <span aria-hidden="true">*</span>. We'll only use your details to reply about this enquiry.
        See our <a href="/privacy-policy/">privacy policy</a>.</p>
      </form>
    </div>
    """


def quote_section(source_page, image, image_alt, heading, text_html):
    """The shared quote-form band, as a two-column layout: an image + short
    on-topic copy on the left, the lead form on the right. Replaces the old
    lone centered form (which left large empty margins on wide screens) —
    same <section id="quote"> anchor and lead_form() underneath, so nothing
    that links to #quote or relies on the form itself needs to change."""
    return f"""
    <section class="section quote-section" id="quote">
      <div class="wrap quote-grid">
        <div class="quote-media">
          {img(image, image_alt, 400, 270)}
          <h3>{escape(heading)}</h3>
          <p>{text_html}</p>
        </div>
        {lead_form(source_page)}
      </div>
    </section>
    """


def header_html(active_path):
    links = []
    for href, label in NAV:
        cls = ' class="active"' if href == active_path else ""
        links.append(f'<li><a href="{href}"{cls}>{escape(label)}</a></li>')
    return f"""
    <header class="site-header">
      <div class="header-inner">
        <a class="logo" href="/">
          <img class="logo-mark" src="/images/logo.png" width="256" height="240" alt="" loading="eager">
          <span class="logo-text">{escape(BRAND)}</span>
        </a>
        <button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav">
          <span class="sr-only">Menu</span>
          <span class="hamburger"></span>
        </button>
        <nav id="primary-nav" class="primary-nav">
          <ul>{''.join(links)}</ul>
        </nav>
        <a class="header-phone" href="{PHONE_TEL}">
          <span class="phone-icon" aria-hidden="true">&#9742;</span> {escape(PHONE_DISPLAY)}
        </a>
      </div>
    </header>
    """


def page_hero(bg_image, bg_alt, eyebrow, h1_text, subtitle, ctas_html="", tall=False, extra_html="", body_class=""):
    """Full-width, full-bleed hero banner used at the top of every inner page.
    bg_image is rendered via CSS background-image (not <img>) since it's
    decorative framing behind real text content, so no alt text is needed on
    it directly — bg_alt is kept only as a code comment for future editors."""
    tall_cls = " hero-tall" if tall else ""
    return f"""
    <section class="page-hero{tall_cls} {body_class}">
      <div class="hero-bg" style="background-image:url('/images/{bg_image}')" role="img" aria-label="{escape(bg_alt)}"></div>
      <div class="hero-overlay"></div>
      <div class="hero-content wrap">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h1>{escape(h1_text)}</h1>
        <p class="lead">{subtitle}</p>
        {ctas_html}
        {extra_html}
      </div>
    </section>
    """


def breadcrumb_html_and_schema(breadcrumbs, url_path):
    """breadcrumbs: list of (label, path) not including current page's own
    trailing entry beyond what's passed. Renders visible trail + matching
    BreadcrumbList JSON-LD (same list -> can't drift, per Rule 5)."""
    if not breadcrumbs:
        return "", ""
    items = []
    ld_items = []
    for i, (label, path) in enumerate(breadcrumbs, start=1):
        if path:
            items.append(f'<li><a href="{path}">{escape(label)}</a></li>')
        else:
            items.append(f'<li aria-current="page">{escape(label)}</li>')
        ld_items.append(
            f'{{"@type":"ListItem","position":{i},"name":"{escape(label)}"'
            + (f',"item":"{BASE_URL}{path}"' if path else "")
            + "}"
        )
    html = f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
    schema = (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        + ",".join(ld_items) + "]}"
        "</script>"
    )
    return html, schema


def footer_html():
    return f"""
    <footer class="site-footer">
      <div class="footer-inner">
        <div class="footer-col">
          <p class="footer-brand"><img src="/images/logo.png" width="256" height="240" alt="" loading="lazy"><span>{escape(BRAND)}</span></p>
          <p>Pressure washing, gutter &amp; fascia cleaning and roof cleaning across Poole, Bournemouth, Christchurch and the surrounding Dorset area.</p>
          <p><a href="{PHONE_TEL}">{escape(PHONE_DISPLAY)}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div class="footer-col">
          <p class="footer-heading">Services</p>
          <ul>
            <li><a href="/pressure-washing/">Pressure washing</a></li>
            <li><a href="/gutter-and-fascia-cleaning/">Gutter &amp; fascia cleaning</a></li>
            <li><a href="/roof-cleaning/">Roof cleaning</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <p class="footer-heading">Areas</p>
          <ul>
            <li><a href="/areas/poole/">Poole</a></li>
            <li><a href="/areas/bournemouth/">Bournemouth</a></li>
            <li><a href="/areas/christchurch/">Christchurch</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <p class="footer-heading">Company</p>
          <ul>
            <li><a href="/about/">About</a></li>
            <li><a href="/faq/">FAQ</a></li>
            <li><a href="/guides/">News &amp; Info</a></li>
            <li><a href="/contact/">Contact</a></li>
            <li><a href="/privacy-policy/">Privacy policy</a></li>
            <li><a href="/terms/">Terms</a></li>
          </ul>
        </div>
      </div>
      <p class="footer-legal">&copy; {date.today().year} {escape(BRAND)}. All rights reserved.</p>
    </footer>
    """


def page(url_path, title, description, h1, body_html, og_image="/images/hero-pressure-washing.jpg",
         breadcrumbs=None, extra_schema="", noindex=False):
    """Render one page. url_path must start and end with '/' (or be '/').
    title/description are required — no fallbacks, per Rule 2."""
    assert url_path == "/" or (url_path.startswith("/") and url_path.endswith("/"))
    assert 50 <= len(title) <= 60, f"title length {len(title)} out of range for {url_path}: {title}"
    assert 140 <= len(description) <= 160, f"description length {len(description)} out of range for {url_path}: {description}"
    canonical = f"{BASE_URL}/" if url_path == "/" else f"{BASE_URL}{url_path}"
    bc_html, bc_schema = breadcrumb_html_and_schema(breadcrumbs or [], url_path)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""

    html = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{escape(BRAND)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/images/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/images/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<noscript><style>.reveal,.reveal-stagger>*{{opacity:1!important;transform:none!important;}}</style></noscript>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header_html(url_path)}
{bc_html}
<main id="main">
{body_html}
</main>
{footer_html()}
{bc_schema}
{extra_schema}
<script src="/js/main.js" defer></script>
</body>
</html>"""

    if url_path == "/":
        out_dir = DIST
    else:
        out_dir = os.path.join(DIST, url_path.strip("/"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    PAGES.append(url_path)
    return html


def simple_hero(eyebrow, h1_text, subtitle, ctas_html="", bg_image=None):
    """Lighter, photo-free hero band for text-heavy pages (FAQ, guides, legal,
    contact) — full-width like every other hero, but a plain gradient rather
    than a background photo, so long-form reading pages load faster and read
    a bit calmer than the service/area pages."""
    # Purely decorative texture behind the gradient, so it's aria-hidden rather
    # than given a role/alt — the heading beside it already carries the meaning.
    # Photos need slightly different opacity to a line-art SVG to read the same.
    photo_cls = " is-photo" if bg_image and bg_image.lower().endswith((".jpg", ".jpeg", ".png")) else ""
    bg = (f'<div class="simple-hero-bg{photo_cls}" aria-hidden="true" '
          f"style=\"background-image:url('/images/{bg_image}')\"></div>") if bg_image else ""
    return f"""
    <section class="page-hero band-dark" style="position:relative;">
      {bg}
      <div class="hero-content wrap">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h1>{escape(h1_text)}</h1>
        <p class="lead">{subtitle}</p>
        {ctas_html}
      </div>
    </section>
    """


def h1(text):
    return f"<h1>{escape(text)}</h1>"


# ---------------------------------------------------------------------------
# Structured data (JSON-LD). Built with json.dumps rather than manual string
# concatenation so nothing here can produce broken JSON if a description or
# name ever contains a quote or ampersand.
# ---------------------------------------------------------------------------

def local_business_schema():
    """Sitewide Organization/LocalBusiness markup. No street address is given
    on purpose (this is a service-area business, not a shopfront) and no
    aggregateRating/review count is included — SEO.md rule 1 bars invented
    reviews, and we don't have real ones yet."""
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BRAND,
        "telephone": PHONE_TEL.replace("tel:", ""),
        "email": EMAIL,
        "url": f"{BASE_URL}/",
        "image": f"{BASE_URL}/images/logo.png",
        "areaServed": [
            {"@type": "City", "name": "Poole"},
            {"@type": "City", "name": "Bournemouth"},
            {"@type": "City", "name": "Christchurch"},
        ],
        "priceRange": "££",
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


def service_schema(service_name, description, areas=None):
    areas = areas or ["Poole", "Bournemouth", "Christchurch"]
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": service_name,
        "name": service_name,
        "description": description,
        "provider": {
            "@type": "LocalBusiness",
            "name": BRAND,
            "telephone": PHONE_TEL.replace("tel:", ""),
        },
        "areaServed": [{"@type": "City", "name": a} for a in areas],
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


def article_schema(headline, description, image, date_published="2026-08-18"):
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "image": f"{BASE_URL}{image}",
        "datePublished": date_published,
        "author": {"@type": "Organization", "name": BRAND},
        "publisher": {"@type": "Organization", "name": BRAND,
                       "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/images/logo.png"}},
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


def stat_row(stats):
    """A row of big-number callouts for a single headline statistic each —
    the dataviz house rule that not every number needs a chart; a stat tile
    is the right form when there's one figure to land, not a distribution.
    stats: list of (number_text, label_text)."""
    tiles = "".join(
        f'<div class="stat-tile"><span class="stat-num">{escape(num)}</span>'
        f'<span class="stat-label">{escape(label)}</span></div>'
        for num, label in stats
    )
    return f'<div class="stat-row">{tiles}</div>'


def bar_chart_svg(caption, unit, data, highlight_label=None, y_max=None):
    """Single-hue sequential bar chart as inline SVG (no JS dependency, so it
    renders identically with scripting off and is fully crawlable/indexable
    text+shapes rather than a raster image). data: list of (label, value).
    One bar may be highlighted in the accent colour to call out a specific
    point (e.g. the wettest month) — that's the only second colour used, and
    it's a callout, not a second data series.
    Follows the dataviz house rules: one hue for magnitude, thin bars with
    4px rounded top corners anchored to a shared baseline, direct value
    labels instead of a legend (single series), recessive axis line."""
    W, H = 720, 300
    pad_l, pad_r, pad_t, pad_b = 12, 12, 30, 46
    plot_w = W - pad_l - pad_r
    plot_h = H - pad_t - pad_b
    n = len(data)
    gap = 14
    bar_w = (plot_w - gap * (n - 1)) / n
    vmax = y_max or max(v for _, v in data) * 1.18
    bars, labels = [], []
    for i, (label, value) in enumerate(data):
        x = pad_l + i * (bar_w + gap)
        bar_h = (value / vmax) * plot_h
        y = pad_t + plot_h - bar_h
        is_hi = label == highlight_label
        fill = "var(--accent)" if is_hi else "var(--brand)"
        radius = min(6, bar_w / 2)
        bars.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{max(bar_h,2):.1f}" '
            f'rx="{radius:.1f}" ry="{radius:.1f}" fill="{fill}"></rect>'
            f'<text x="{x + bar_w/2:.1f}" y="{y-8:.1f}" text-anchor="middle" class="chart-value">{value:g}{unit}</text>'
            f'<text x="{x + bar_w/2:.1f}" y="{H-pad_b+22:.1f}" text-anchor="middle" class="chart-label">{escape(str(label))}</text>'
        )
    baseline_y = pad_t + plot_h
    svg = f"""
    <figure class="chart-figure">
      <svg viewBox="0 0 {W} {H}" role="img" aria-label="{escape(caption)}" class="bar-chart">
        <line x1="{pad_l}" y1="{baseline_y}" x2="{W-pad_r}" y2="{baseline_y}" class="chart-axis"></line>
        {''.join(bars)}
      </svg>
      <figcaption>{caption}</figcaption>
    </figure>
    """
    return svg
