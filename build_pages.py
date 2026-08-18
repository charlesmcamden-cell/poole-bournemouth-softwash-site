#!/usr/bin/env python3
from html import escape
from generate_site import (
    page, img, lead_form, h1, page_hero, simple_hero,
    PAGES, BASE_URL, BRAND, PHONE_DISPLAY, PHONE_TEL,
)

# ===========================================================================
# HOMEPAGE
# ===========================================================================
page(
    "/",
    title="Pressure Washing, Gutter & Roof Cleaning | PB Softwash",
    description="Pressure washing, gutter & fascia cleaning and roof cleaning across Poole, Bournemouth and Christchurch. Free quotes, fast callback. Get a price today.",
    h1="Pressure Washing, Gutter & Roof Cleaning in Poole & Bournemouth",
    breadcrumbs=None,
    og_image="/images/clean-house-driveway.jpg",
    body_html=f"""
<section class="page-hero hero-tall" id="quote">
  <div class="hero-bg" style="background-image:url('/images/clean-house-driveway.jpg')" role="img" aria-label="A modern house with a clean paved driveway"></div>
  <div class="hero-overlay"></div>
  <div class="hero-content wrap">
    <div class="home-hero-grid">
      <div class="hero-text">
        <p class="eyebrow">Poole &middot; Bournemouth &middot; Christchurch</p>
        {h1("Pressure Washing, Gutter & Roof Cleaning in Poole & Bournemouth")}
        <p class="lead">Local exterior cleaning covering driveways, patios, gutters, fascias and roofs across Poole, Bournemouth, Christchurch and the surrounding Dorset area.</p>
        <div class="hero-trust">
          <span>Free, no-obligation quotes</span>
          <span>Pressure matched to the surface</span>
          <span>You're told what we find</span>
        </div>
      </div>
      <div class="hero-form-card lead-form-card">
        {lead_form("home")}
      </div>
    </div>
  </div>
</section>

<section class="band band-soft">
  <div class="band-inner">
    <p class="eyebrow">What we do</p>
    <h2>Three services, one call</h2>
    <div class="card-grid reveal-stagger">
      <a class="service-card" href="/pressure-washing/">
        <div class="img-wrap">{img("pressure-washing-steps.jpg", "Pressure washer being used to clean grime from outdoor steps", 400, 370)}</div>
        <h3>Pressure Washing</h3>
        <p>Driveways, patios, block paving and pathways — grime, moss and algae removed without damaging the surface.</p>
        <span class="card-link">Learn more &rarr;</span>
      </a>
      <a class="service-card" href="/gutter-and-fascia-cleaning/">
        <div class="img-wrap">{img("gutter-cleaning-service.jpg", "Gutter being cleared of moss and debris with a pressure washer attachment", 400, 370)}</div>
        <h3>Gutter &amp; Fascia Cleaning</h3>
        <p>Blocked gutters cause overflow and damp. We clear gutters and wash down fascias and soffits from ground level.</p>
        <span class="card-link">Learn more &rarr;</span>
      </a>
      <a class="service-card" href="/roof-cleaning/">
        <div class="img-wrap">{img("moss-covered-roof.jpg", "Close-up of a moss-covered roof in need of cleaning", 400, 370)}</div>
        <h3>Roof Cleaning</h3>
        <p>Soft washing to remove moss, algae and lichen from tiled and slate roofs — low pressure, roof-safe.</p>
        <span class="card-link">Learn more &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="band band-dark">
  <div class="band-inner">
    <p class="eyebrow">Why choose us</p>
    <h2>What you actually get</h2>
    <div class="feature-grid reveal-stagger">
      <div class="feature-card">
        <div class="feature-icon">1</div>
        <h3>Local to Dorset</h3>
        <p>Based in the Poole/Bournemouth area and familiar with the coastal conditions that make render, roofs and paving here dirty faster than most of the UK.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">2</div>
        <h3>Method matched to the surface</h3>
        <p>Block paving, natural stone, tile and slate all need different pressure and technique. We adjust rather than run one setting on everything.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">3</div>
        <h3>Told what we find</h3>
        <p>A cracked gutter joint, a soft fascia board — you'll hear about it, even though we don't carry out repairs ourselves.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">4</div>
        <h3>No pressure to book</h3>
        <p>Quotes are free and no-obligation. Confirm a price before anything starts, or don't — no hard sell either way.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="band-inner">
    <p class="eyebrow">How it works</p>
    <h2>From enquiry to a cleaner exterior</h2>
    <div class="process-grid reveal-stagger">
      <div class="process-step">
        <div class="step-num">1</div>
        <h3>Tell us the job</h3>
        <p>Use the form above with the surface or area, roughly how big it is, and a photo if that's easier than describing it.</p>
      </div>
      <div class="process-step">
        <div class="step-num">2</div>
        <h3>Get a free quote</h3>
        <p>We call or message back, usually the same day, with a price based on what you've told us.</p>
      </div>
      <div class="process-step">
        <div class="step-num">3</div>
        <h3>Job carried out</h3>
        <p>Pressure, nozzle and method matched to the surface or roof type — nothing generic run over everything.</p>
      </div>
      <div class="process-step">
        <div class="step-num">4</div>
        <h3>Checked before we leave</h3>
        <p>A quick walkthrough so you can see the result and flag anything before we pack up.</p>
      </div>
    </div>
  </div>
</section>

<section class="band band-tint">
  <div class="band-inner split reveal">
    <div class="split-media">
      {img("garden-path.jpg", "A clean, curved brick driveway bordered by planting", 752, 1092)}
    </div>
    <div class="split-text">
      <p class="eyebrow">Why this matters here</p>
      <h2>Coastal air and mature tree cover work against you</h2>
      <p>Coastal salt air, mature tree cover and a damp maritime climate mean render, roofs, gutters and paving in the Poole/Bournemouth/Christchurch area pick up algae, moss and black spot staining faster than most of the UK. Left alone, blocked gutters overflow into fascias and walls, and moss on a roof holds moisture against the tiles.</p>
      <p>Regular exterior cleaning is maintenance, not vanity — and it's cheaper than the fascia, render or roofing repairs that come from ignoring it.</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="band-inner reveal">
    <p class="eyebrow">Where we work</p>
    <h2>Covering Poole, Bournemouth, Christchurch &amp; beyond</h2>
    <p class="lead">We work across the BH postcode area — from Sandbanks and Canford Cliffs through central Bournemouth to Christchurch and Mudeford. Not sure if we cover your road? Ask when you request a quote.</p>
    <div class="area-links">
      <a href="/areas/poole/">Poole</a>
      <a href="/areas/bournemouth/">Bournemouth</a>
      <a href="/areas/christchurch/">Christchurch</a>
      <a href="/areas/">All areas &rarr;</a>
    </div>
  </div>
</section>

<section class="band band-dark cta-band">
  <div class="band-inner reveal">
    <h2>Ready for a free quote?</h2>
    <p>Tell us about the job above, or skip straight to the phone.</p>
    <a class="cta-phone-big" href="{PHONE_TEL}">&#9742; {escape(PHONE_DISPLAY)}</a>
    <p style="margin-top:1.4em;"><a class="btn btn-secondary" href="#quote">Back to the quote form</a></p>
  </div>
</section>
""",
)

# ===========================================================================
# SERVICE PAGES
# ===========================================================================
page(
    "/pressure-washing/",
    title="Driveway & Patio Pressure Washing in Poole | PB Softwash",
    description="Professional pressure washing for driveways, patios and block paving in Poole, Bournemouth & Christchurch. Removes moss, algae and grime. Free quotes.",
    h1="Driveway & Patio Pressure Washing",
    breadcrumbs=[("Home", "/"), ("Pressure Washing", None)],
    og_image="/images/pressure-washing-steps.jpg",
    body_html=f"""
{page_hero("pressure-washing-steps.jpg", "Pressure washer being used to clean grime from outdoor stone steps",
            "Pressure Washing", "Driveway & Patio Pressure Washing",
            "Block paving, concrete, tarmac, patios and pathways cleaned back to their original colour — without damaging the jointing sand or the surface underneath.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {escape(PHONE_DISPLAY)}</a></div>')}

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What we clean</h2>
    <ul class="checklist">
      <li>Block paved and brick driveways</li>
      <li>Concrete and tarmac driveways</li>
      <li>Patios, decking and pathways</li>
      <li>Garden walls and steps</li>
      <li>Communal/commercial forecourts and car parks</li>
    </ul>
  </div>
</section>

<section class="wrap section split reveal">
  <div class="split-media">
    {img("garden-path.jpg", "A clean, curved brick driveway after pressure washing", 752, 1092)}
  </div>
  <div class="split-text">
    <h2>Signs it's time to book a clean</h2>
    <ul class="checklist">
      <li>Green or black staining spreading across the surface, especially in shaded corners</li>
      <li>The surface feels slippery underfoot when damp — usually algae, not just dirt</li>
      <li>Weeds and moss establishing in the joints between block paving</li>
      <li>The driveway or patio has visibly darkened compared to when it was laid</li>
      <li>Getting the house ready to sell — kerb appeal matters at viewings</li>
    </ul>
  </div>
</section>

<section class="band band-dark">
  <div class="band-inner reveal">
    <p class="eyebrow">How it works</p>
    <h2>Our process</h2>
    <div class="process-grid reveal-stagger">
      <div class="process-step">
        <div class="step-num">1</div>
        <h3>Free assessment</h3>
        <p>Tell us the surface type and approximate size using the form below, or send a photo.</p>
      </div>
      <div class="process-step">
        <div class="step-num">2</div>
        <h3>Pressure matched to the surface</h3>
        <p>Block paving, natural stone and older tarmac all need different pressures and nozzles — too much strips jointing sand or etches soft stone.</p>
      </div>
      <div class="process-step">
        <div class="step-num">3</div>
        <h3>Run-off contained</h3>
        <p>Debris and run-off contained where the job requires it, particularly near drains.</p>
      </div>
      <div class="process-step">
        <div class="step-num">4</div>
        <h3>Optional re-sanding</h3>
        <p>For block paving once it's dry, to stop the joints washing out and weeds coming back through.</p>
      </div>
    </div>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Surfaces, in a bit more detail</h2>
  <div class="feature-grid">
    <div class="feature-card">
      <h3>Block paving</h3>
      <p>The most common driveway type we quote for in this area. Pressure is kept low enough to protect the jointing sand — stripping it out is what lets weeds and ants back in, and it's the single biggest way an inexperienced clean damages block paving.</p>
    </div>
    <div class="feature-card">
      <h3>Natural stone &amp; slabs</h3>
      <p>Sandstone and similar softer stone can etch or lighten unevenly under high pressure. We use a lower pressure and let dwell time do more of the work instead.</p>
    </div>
    <div class="feature-card">
      <h3>Concrete &amp; tarmac</h3>
      <p>More tolerant of higher pressure, but older or already-cracking surfaces still need care around edges and expansion joints.</p>
    </div>
    <div class="feature-card">
      <h3>Decking</h3>
      <p>Timber decking needs the lowest pressure of all — enough to lift algae and grime without fraying the grain or forcing water into the joints between boards.</p>
    </div>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Professional-grade equipment</h2>
  <div class="split">
    <div class="split-media">
      {img("hero-pressure-washing.jpg", "Professional pressure washing equipment in use", 880, 1092)}
    </div>
    <div class="split-text">
      <p>Domestic pressure washers are usually fixed at one setting. Our equipment allows pressure and nozzle angle to be adjusted per surface, which is what makes it possible to safely clean block paving joints and delicate stone with the same visit as a tougher concrete driveway.</p>
    </div>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Frequently asked</h2>
  <div class="faq-list">
    <details>
      <summary>Will pressure washing damage my block paving?</summary>
      <p>Not when the pressure and nozzle are matched to the surface. The risk with block paving is using too high a pressure too close to the joints, which blasts out the sand and lets weeds and ants back in — that's why we re-sand as a follow-up where needed.</p>
    </details>
    <details>
      <summary>How often should a driveway be pressure washed?</summary>
      <p>Most driveways in this part of Dorset benefit from a clean every 12–18 months. South-facing or heavily shaded driveways under trees can need it more often because they hold more moisture and organic debris.</p>
    </details>
    <details>
      <summary>Do you offer patio and driveway cleaning together?</summary>
      <p>Yes — most customers get their driveway, patio and paths done in the same visit. Mention everything you'd like quoted on the form and we'll price it as one job.</p>
    </details>
    <details>
      <summary>What's the cost of pressure washing a driveway?</summary>
      <p>It depends on surface type, size, condition and access — see our full <a href="/guides/pressure-washing-driveway-cost-guide-uk/">driveway pressure washing cost guide</a> for what actually drives the price, or request a free quote for an exact figure.</p>
    </details>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("pressure-washing")}
</section>
""",
)

page(
    "/gutter-and-fascia-cleaning/",
    title="Gutter & Fascia Cleaning, Poole & Bournemouth | PB Softwash",
    description="Gutter clearing and fascia & soffit washing across Poole, Bournemouth and Christchurch, done safely from ground level with a vacuum system. Free quotes.",
    h1="Gutter & Fascia Cleaning",
    breadcrumbs=[("Home", "/"), ("Gutter & Fascia Cleaning", None)],
    og_image="/images/gutter-cleaning-service.jpg",
    body_html=f"""
{page_hero("gutter-cleaning-service.jpg", "Residential gutter being cleared of moss and debris",
            "Gutter & Fascia Cleaning", "Gutter & Fascia Cleaning",
            "Blocked gutters are one of the most common causes of damp and fascia rot on UK homes. We clear the gutter, flush the downpipes, and wash down the fascias and soffits.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {escape(PHONE_DISPLAY)}</a></div>')}

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What's included</h2>
    <ul class="checklist">
      <li>Clearing leaves, moss and silt from the gutter run</li>
      <li>Checking and flushing downpipes for blockages</li>
      <li>Washing down fascias and soffits to remove algae and black streaking</li>
      <li>A before/after check so you can see the debris that's been cleared</li>
    </ul>
  </div>
</section>

<section class="wrap section split reverse reveal">
  <div class="split-media">
    {img("roofer-guttering.jpg", "A worker accessing guttering safely at height against a clear sky", 624, 1092)}
  </div>
  <div class="split-text">
    <h2>Why it matters</h2>
    <p>A blocked gutter overflows at the weakest point — usually straight down the wall behind it. Over a winter that can mean a damp patch inside, staining on the render, or water finding its way behind the fascia board and rotting it from the back, which is far more expensive to fix than a clean. Bournemouth and Christchurch in particular have a lot of mature tree cover, which means gutters here fill with leaf litter faster than in more open areas.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Signs your gutters are already blocked</h2>
  <ul class="checklist">
    <li>Water visibly overflowing the edge in heavy rain, rather than running through the downpipe</li>
    <li>Plants or grass growing in the gutter — a sign silt has built up enough to hold moisture and seeds</li>
    <li>Damp patches on an internal wall below roof level after rain</li>
    <li>Staining or green streaking down external render below a gutter joint</li>
  </ul>
</section>

<section class="band band-dark">
  <div class="band-inner reveal split">
    <div class="split-text">
      <p class="eyebrow">Often overlooked</p>
      <h2>Fascias and soffits</h2>
      <p>The fascia is the board running along the roofline that the gutter is fixed to; the soffit is the panel underneath it, closing off the roof void. Both sit directly below where debris and run-off collect, so they pick up algae and black streaking even when the gutter itself looks fine — and a fascia that's staying damp behind a blocked gutter is the most common way rot starts.</p>
    </div>
    <div class="split-media">
      {img("gutter-downpipe.jpg", "A downpipe fixed to the exterior wall of a house", 1057, 705)}
    </div>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Frequently asked</h2>
  <div class="faq-list">
    <details>
      <summary>Do you need to put a ladder against my house?</summary>
      <p>For most standard two-storey homes we clear and vacuum gutters using extendable pole systems from ground level, which is safer and doesn't rest a ladder on your guttering or render. Taller or more complex properties are assessed on a case-by-case basis.</p>
    </details>
    <details>
      <summary>How often do gutters need clearing in the UK?</summary>
      <p>Once or twice a year is typical — once for most properties, twice a year if you're under trees. Read our full <a href="/guides/how-often-should-you-clean-your-gutters-uk/">guide to gutter cleaning frequency</a>.</p>
    </details>
    <details>
      <summary>Can you tell if my gutters are actually damaged, not just blocked?</summary>
      <p>We'll flag anything we spot while clearing — cracked joints, sagging brackets, or a fascia that's starting to go soft — so you know about it, even though repairs aren't something we carry out ourselves.</p>
    </details>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("gutter-and-fascia-cleaning")}
</section>
""",
)

page(
    "/roof-cleaning/",
    title="Roof Cleaning (Soft Wash) Poole & Bournemouth | PB Softwash",
    description="Soft-wash roof cleaning removes moss, algae and lichen from tiled and slate roofs across Poole, Bournemouth and Christchurch. Low-pressure, roof-safe method.",
    h1="Roof Cleaning (Soft Washing)",
    breadcrumbs=[("Home", "/"), ("Roof Cleaning", None)],
    og_image="/images/moss-covered-roof.jpg",
    body_html=f"""
{page_hero("moss-covered-roof.jpg", "Close-up of a moss-covered tiled roof before cleaning",
            "Roof Cleaning", "Roof Cleaning (Soft Washing)",
            "Moss holds moisture against roof tiles and works its way under them over time. We use a low-pressure soft-wash method rather than a high-pressure jet, which is what most roofing manufacturers recommend.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {escape(PHONE_DISPLAY)}</a></div>')}

<section class="wrap section reveal">
  <h2>Why soft washing, not high-pressure jetting</h2>
  <p>High-pressure jet washing a roof can strip the protective granules off tiles and force water up under them — which is how a roof clean ends up causing the leak it was meant to prevent. Soft washing uses low pressure and a biodegradable treatment to kill moss, algae and lichen at the root, then it's rinsed away. It takes longer to show the full result (the treatment keeps working for a few days) but it doesn't put the roof covering at risk. Read more in our <a href="/guides/roof-moss-soft-wash-vs-pressure-wash/">soft wash vs pressure wash guide</a>.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What we clean</h2>
    <ul class="checklist">
      <li>Concrete and clay tiled roofs</li>
      <li>Natural slate roofs</li>
      <li>Conservatory and outbuilding roofs</li>
      <li>Render and cladding affected by roof run-off staining</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Signs your roof needs attention</h2>
  <ul class="checklist">
    <li>Visible moss along the ridge line or in the valleys between roof slopes</li>
    <li>Green or black streaking running down from the ridge or ends of the tiles</li>
    <li>Moss or grit debris collecting in the gutters below the roofline</li>
    <li>North-facing or heavily shaded slopes noticeably darker than the rest of the roof</li>
  </ul>
</section>

<section class="wrap section split reveal">
  <div class="split-media">
    {img("roofer-guttering.jpg", "A worker safely accessing a roofline for a roof cleaning job", 624, 1092)}
  </div>
  <div class="split-text">
    <h2>A note on older and softer roofs</h2>
    <p>Christchurch's town centre and parts of Poole Old Town have a number of older cottages, some with thatch or soft, weathered tile. We assess the roof type before quoting — thatch isn't something we treat the same way as a standard tiled roof, and we'll say so upfront rather than take on a job that's the wrong fit.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Frequently asked</h2>
  <div class="faq-list">
    <details>
      <summary>Is soft washing safe for my roof tiles?</summary>
      <p>Yes — that's the point of using low pressure rather than a jet wash. The treatment does the work of killing the moss and algae; the rinse is gentle, not a blast.</p>
    </details>
    <details>
      <summary>How long until the moss is fully gone?</summary>
      <p>You'll see an immediate difference in staining, but the treatment continues killing moss and algae over the following one to two weeks as it dies back and washes off naturally in the rain.</p>
    </details>
    <details>
      <summary>Do you work at height on steep roofs?</summary>
      <p>Access and roof pitch are assessed as part of every quote. If a roof isn't safe to access with our equipment, we'll tell you rather than take the job on.</p>
    </details>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("roof-cleaning")}
</section>
""",
)

# ===========================================================================
# AREAS HUB
# ===========================================================================
page(
    "/areas/",
    title="Areas We Cover Across Poole & Bournemouth | PB Softwash",
    description="Pressure washing, gutter and roof cleaning across Poole, Bournemouth, Christchurch and the surrounding BH postcode area of Dorset. Find your area below.",
    h1="Areas We Cover",
    breadcrumbs=[("Home", "/"), ("Areas We Cover", None)],
    og_image="/images/bournemouth-pier.jpg",
    body_html=f"""
{page_hero("bournemouth-pier.jpg", "Bournemouth Pier and seafront",
            "Areas We Cover", "Areas We Cover Across Dorset",
            "We work across the BH postcode area of Dorset. Each town below has its own page with the specific things we see most often in that area.")}

<section class="wrap section reveal">
  <div class="card-grid reveal-stagger">
    <a class="service-card" href="/areas/poole/">
      <div class="img-wrap">{img("poole-harbour.jpg", "Fishing boat in Poole Harbour, Dorset", 400, 270)}</div>
      <h3>Poole</h3>
      <p>Sandbanks, Canford Cliffs, Parkstone, Broadstone and Poole town.</p>
      <span class="card-link">View Poole page &rarr;</span>
    </a>
    <a class="service-card" href="/areas/bournemouth/">
      <div class="img-wrap">{img("bournemouth-pier.jpg", "Bournemouth Pier and seafront", 400, 270)}</div>
      <h3>Bournemouth</h3>
      <p>Talbot Woods, Alum Chine, Southbourne, Westbourne and central Bournemouth.</p>
      <span class="card-link">View Bournemouth page &rarr;</span>
    </a>
    <a class="service-card" href="/areas/christchurch/">
      <div class="img-wrap">{img("christchurch-priory.jpg", "Christchurch Priory tower, Dorset", 400, 270)}</div>
      <h3>Christchurch</h3>
      <p>Christchurch town centre, Mudeford, Highcliffe and Burton.</p>
      <span class="card-link">View Christchurch page &rarr;</span>
    </a>
  </div>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Why we cover it this way</h2>
    <p>Each area page below isn't just this page with the town name swapped in — it covers what's actually different about cleaning exteriors there: how close it is to the coast, how much tree cover there is, and the kind of properties that are common locally. If you're just outside these three towns, get in touch anyway — we cover a fair amount of the surrounding BH postcode area too.</p>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("areas-hub")}
</section>
""",
)

page(
    "/areas/poole/",
    title="Pressure Washing & Gutter Cleaning in Poole | PB Softwash",
    description="Driveway pressure washing, gutter clearing and roof cleaning for Poole, Sandbanks, Canford Cliffs, Parkstone and Broadstone. Free, no-obligation quotes.",
    h1="Pressure Washing, Gutter & Roof Cleaning in Poole",
    breadcrumbs=[("Home", "/"), ("Areas We Cover", "/areas/"), ("Poole", None)],
    og_image="/images/poole-harbour.jpg",
    body_html=f"""
{page_hero("poole-harbour.jpg", "Fishing boat with lobster pots in Poole Harbour",
            "Poole", "Pressure Washing, Gutter & Roof Cleaning in Poole",
            "Covering Poole town, Sandbanks, Canford Cliffs, Parkstone, Broadstone and the harbourside areas.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>')}

<section class="wrap section reveal">
  <h2>What's different about cleaning exteriors in Poole</h2>
  <p>Poole sits directly on one of the largest natural harbours in the world, and a lot of the town — Sandbanks, Lilliput, Canford Cliffs, Parkstone — is close enough to the water that salt-laden air is a real factor. Salt spray accelerates algae growth on render and roof tiles and can leave a dull, chalky residue on paving that plain rain doesn't shift. Properties within a mile or so of the harbour or Poole Bay generally need exterior cleaning more often than inland areas.</p>
  <p>Poole also has a lot of 1930s and post-war render bungalows, particularly around Parkstone and Broadstone, where render staining from roof run-off is one of the most common jobs we're asked to quote.</p>
  <p>Broadly covering postcodes BH12–BH15 and BH18 — if you're near the edge of that, ask when you request a quote.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Services in Poole</h2>
    <div class="card-grid">
      <a class="service-card" href="/pressure-washing/"><h3>Pressure Washing</h3><p>Driveways and patios across Poole and Sandbanks.</p><span class="card-link">Learn more &rarr;</span></a>
      <a class="service-card" href="/gutter-and-fascia-cleaning/"><h3>Gutter &amp; Fascia Cleaning</h3><p>Clearing gutters affected by coastal debris and tree litter.</p><span class="card-link">Learn more &rarr;</span></a>
      <a class="service-card" href="/roof-cleaning/"><h3>Roof Cleaning</h3><p>Soft washing for salt-and-algae staining on Poole roofs.</p><span class="card-link">Learn more &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("areas-poole")}
</section>
""",
)

page(
    "/areas/bournemouth/",
    title="Exterior Cleaning Services in Bournemouth | PB Softwash",
    description="Pressure washing, gutter clearing and roof cleaning for Bournemouth, including Talbot Woods, Alum Chine, Westbourne and Southbourne. Free quotes.",
    h1="Pressure Washing, Gutter & Roof Cleaning in Bournemouth",
    breadcrumbs=[("Home", "/"), ("Areas We Cover", "/areas/"), ("Bournemouth", None)],
    og_image="/images/bournemouth-pier.jpg",
    body_html=f"""
{page_hero("bournemouth-pier.jpg", "Bournemouth Pier and seafront with the beach in view",
            "Bournemouth", "Pressure Washing, Gutter & Roof Cleaning in Bournemouth",
            "Covering central Bournemouth, Talbot Woods, Westbourne, Alum Chine and Southbourne.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>')}

<section class="wrap section reveal">
  <h2>What's different about cleaning exteriors in Bournemouth</h2>
  <p>Bournemouth's chines — the wooded valleys that run down to the seafront at Alum Chine, Middle Chine and Boscombe Chine — put a lot of mature tree cover right up against nearby homes. That means more leaf litter and pollen ending up in gutters, and more roof slopes kept in permanent shade, which is exactly the damp, low-light condition moss needs to establish. Victorian and Edwardian terraces around the town centre and Westbourne also tend to have more complex roof lines with valleys and parapets, which collect debris that a simple pitched roof wouldn't.</p>
  <p>Broadly covering postcodes BH1–BH10 — if you're near the edge of that, ask when you request a quote.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Services in Bournemouth</h2>
    <div class="card-grid">
      <a class="service-card" href="/pressure-washing/"><h3>Pressure Washing</h3><p>Driveways and patios across Bournemouth's residential streets.</p><span class="card-link">Learn more &rarr;</span></a>
      <a class="service-card" href="/gutter-and-fascia-cleaning/"><h3>Gutter &amp; Fascia Cleaning</h3><p>Clearing gutters loaded with leaf litter from chine-side tree cover.</p><span class="card-link">Learn more &rarr;</span></a>
      <a class="service-card" href="/roof-cleaning/"><h3>Roof Cleaning</h3><p>Soft washing for shaded, moss-prone roof slopes.</p><span class="card-link">Learn more &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("areas-bournemouth")}
</section>
""",
)

page(
    "/areas/christchurch/",
    title="Exterior Cleaning Services in Christchurch | PB Softwash",
    description="Pressure washing, gutter clearing and careful roof cleaning for Christchurch, Mudeford, Highcliffe and Burton, including older and thatched properties.",
    h1="Pressure Washing, Gutter & Roof Cleaning in Christchurch",
    breadcrumbs=[("Home", "/"), ("Areas We Cover", "/areas/"), ("Christchurch", None)],
    og_image="/images/christchurch-priory.jpg",
    body_html=f"""
{page_hero("christchurch-priory.jpg", "Christchurch Priory tower with clock",
            "Christchurch", "Pressure Washing, Gutter & Roof Cleaning in Christchurch",
            "Covering Christchurch town centre, Mudeford, Highcliffe and Burton.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>')}

<section class="wrap section reveal">
  <h2>What's different about cleaning exteriors in Christchurch</h2>
  <p>Christchurch sits where the River Avon meets the River Stour before they reach the sea at Mudeford — low-lying, close to water on more than one side, and noticeably more humid than areas further inland. That's ideal growing conditions for moss and algae, which is why roofs and north-facing walls here often need attention more often than the regional average.</p>
  <p>The town centre and parts of Mudeford also have a number of older cottages, some with thatched or soft, aged roofing. We assess roof type and condition before quoting rather than treating every roof the same way — see our <a href="/roof-cleaning/">roof cleaning page</a> for how we approach older and more delicate roofs.</p>
  <p>Broadly covering postcode BH23 — if you're near the edge of that, ask when you request a quote.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Services in Christchurch</h2>
    <div class="card-grid">
      <a class="service-card" href="/pressure-washing/"><h3>Pressure Washing</h3><p>Driveways and patios across Christchurch and Mudeford.</p><span class="card-link">Learn more &rarr;</span></a>
      <a class="service-card" href="/gutter-and-fascia-cleaning/"><h3>Gutter &amp; Fascia Cleaning</h3><p>Clearing gutters in a river-valley climate that stays damp longer.</p><span class="card-link">Learn more &rarr;</span></a>
      <a class="service-card" href="/roof-cleaning/"><h3>Roof Cleaning</h3><p>Careful, assessed-first cleaning for older and more delicate roofs.</p><span class="card-link">Learn more &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("areas-christchurch")}
</section>
""",
)

print(f"Built {len(PAGES)} pages so far...")

# ===========================================================================
# ABOUT
# ===========================================================================
page(
    "/about/",
    title="About Us: Exterior Cleaning Specialists | PB Softwash",
    description="Poole & Bournemouth Softwash provides pressure washing, gutter and roof cleaning across Dorset. Here's how we work and what to expect from a booking.",
    h1="About Poole & Bournemouth Softwash",
    breadcrumbs=[("Home", "/"), ("About", None)],
    og_image="/images/garden-path.jpg",
    body_html=f"""
{page_hero("garden-path.jpg", "A clean, curved brick driveway",
            "About Us", "About Poole & Bournemouth Softwash",
            "We're a local exterior cleaning operation covering Poole, Bournemouth, Christchurch and the surrounding Dorset area, specialising in three things: pressure washing, gutter &amp; fascia cleaning, and roof cleaning.")}

<section class="wrap section split reveal">
  <div class="split-media">
    {img("hero-pressure-washing.jpg", "Professional cleaning equipment being used correctly and carefully", 880, 1092)}
  </div>
  <div class="split-text">
    <h2>How we work</h2>
    <ul class="checklist">
      <li>Every job is quoted from what you tell us and, where useful, a photo — no call-out fee just to get a price.</li>
      <li>Pressure and method are matched to the surface: block paving, natural stone, render, tile and slate all get treated differently.</li>
      <li>We say no to jobs that aren't a good fit — a thatched roof, for example — rather than take them on anyway.</li>
      <li>You get told what we found (a cracked gutter joint, a soft fascia board) even though we don't carry out repairs ourselves.</li>
    </ul>
  </div>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What we don't do</h2>
    <div class="feature-grid">
      <div class="feature-card"><h3>No invented reviews</h3><p>We won't publish star ratings or testimonials we haven't genuinely received. This site has none for exactly that reason — real ones will be added once we have them.</p></div>
      <div class="feature-card"><h3>No fixed-pressure "one setting fits all"</h3><p>Running the same pressure over block paving, render and tarmac is the fastest way to damage a surface. We adjust job to job.</p></div>
      <div class="feature-card"><h3>No pushy upselling</h3><p>You'll be told about anything we spot, but the decision on repairs or extra work is always yours.</p></div>
    </div>
  </div>
</section>

<!-- TODO: replace the equipment photo above with real before/after photos of completed jobs once available — genuine job photos will do more for conversion than any stock image. -->

<section class="wrap section reveal">
  <h2>Get in touch</h2>
  <p>Call <a href="{PHONE_TEL}">{escape(PHONE_DISPLAY)}</a> or use the quote form on any page and we'll get back to you, usually the same day.</p>
</section>
""",
)

# ===========================================================================
# CONTACT
# ===========================================================================
page(
    "/contact/",
    title="Contact Us for a Free Cleaning Quote in Dorset | PB Softwash",
    description="Get in touch for a free pressure washing, gutter cleaning or roof cleaning quote in Poole, Bournemouth or Christchurch. Call, email or use the form.",
    h1="Contact Us",
    breadcrumbs=[("Home", "/"), ("Contact", None)],
    body_html=f"""
{simple_hero("Get in touch", "Contact Us", "The quickest way to get a price is the form below. Prefer to talk? Call or email and we'll do the same thing over the phone.")}

<section class="wrap section contact-grid reveal">
  <div class="contact-details">
    <h2>Direct contact</h2>
    <p><strong>Phone:</strong> <a href="{PHONE_TEL}">{escape(PHONE_DISPLAY)}</a></p>
    <p><strong>Email:</strong> <a href="mailto:leads@eapionageseo.co.uk">leads@eapionageseo.co.uk</a></p>
    <p><strong>Areas covered:</strong> Poole, Bournemouth, Christchurch and the surrounding BH postcode area.</p>
  </div>
  <div class="contact-form">
    {lead_form("contact")}
  </div>
</section>
""",
)

# ===========================================================================
# FAQ (visible Q&A -> FAQPage schema)
# ===========================================================================
FAQS = [
    ("Do I need to be home while you work?", "No, as long as we can access the driveway, gutters or roof safely and there's access to an outdoor water tap. Many customers aren't in during the job."),
    ("How do you price a job?", "From the details on the quote form — surface type and rough size for pressure washing, property size and storeys for gutters and roofs. We confirm the price before any work starts; nothing is charged without you agreeing to it first."),
    ("What areas do you cover?", "Poole, Bournemouth, Christchurch and the surrounding BH postcode area of Dorset. If you're just outside that, ask — we cover some neighbouring areas too."),
    ("Do you use harsh chemicals?", "Roof and render treatments use biodegradable products designed for the job, applied at the concentration needed and rinsed as required. We're happy to talk through exactly what's used if you ask."),
    ("What if it rains on the day?", "Light rain doesn't usually stop pressure washing or gutter clearing. Roof soft-washing is more weather-dependent since the treatment needs time to work — we'll reschedule if conditions aren't right rather than do a job that won't hold."),
    ("Is the work guaranteed?", "If something about the finished job isn't right, tell us and we'll come back to sort it. We don't publish guarantee terms we haven't actually agreed with a client, so ask for specifics when you book."),
    ("How quickly can you fit me in?", "It varies by season — pressure washing and gutters are busiest in spring and autumn. Get in touch and we'll give you a realistic date, not just a hopeful one."),
    ("Do you clean commercial premises?", "Yes, for pressure washing and gutter clearing in particular — forecourts, car parks and commercial guttering. Mention it's a commercial enquiry on the form."),
]

_faq_items_html = "".join(
    f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS
)
_faq_schema_items = ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
    % (q.replace('"', "'"), a.replace('"', "'"))
    for q, a in FAQS
)
_faq_schema = (
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
    + _faq_schema_items + "]}</script>"
)

page(
    "/faq/",
    title="Frequently Asked Questions About Our Services | PB Softwash",
    description="Answers to common questions about booking pressure washing, gutter cleaning and roof cleaning in Poole, Bournemouth and Christchurch. Read before booking.",
    h1="Frequently Asked Questions",
    breadcrumbs=[("Home", "/"), ("FAQ", None)],
    extra_schema=_faq_schema,
    body_html=f"""
{simple_hero("Questions", "Frequently Asked Questions", "Straight answers before you book — not marketing copy.")}
<div class="wrap section reveal">
<div class="faq-list">
{_faq_items_html}
</div>
</div>
<section class="section quote-section" id="quote">
  {lead_form("faq")}
</section>
""",
)

# ===========================================================================
# GUIDES HUB
# ===========================================================================
page(
    "/guides/",
    title="Exterior Cleaning Guides for Homeowners | PB Softwash",
    description="Practical guides on gutter maintenance and pressure washing costs for homeowners in Poole, Bournemouth, Christchurch and the wider UK. No sales pitch.",
    h1="Guides",
    breadcrumbs=[("Home", "/"), ("Guides", None)],
    body_html=f"""
{simple_hero("Learn", "Guides", "Practical, honest information — not just a reason to call us.")}
<div class="wrap section reveal">
<div class="card-grid">
  <a class="service-card" href="/guides/how-often-should-you-clean-your-gutters-uk/">
    <div class="img-wrap">{img("gutter-downpipe.jpg", "A downpipe fixed to the exterior wall of a house", 400, 270)}</div>
    <h3>How Often Should You Clean Your Gutters?</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/pressure-washing-driveway-cost-guide-uk/">
    <div class="img-wrap">{img("clean-house-driveway.jpg", "A clean paved driveway in front of a house", 400, 270)}</div>
    <h3>Pressure Washing a Driveway: UK Cost Guide</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/roof-moss-soft-wash-vs-pressure-wash/">
    <div class="img-wrap">{img("moss-covered-roof.jpg", "A moss-covered tiled roof", 400, 270)}</div>
    <h3>Roof Moss: Soft Wash vs Pressure Wash</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
</div>
</div>
""",
)

_article_schema_gutter = (
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
    '"headline":"How Often Should You Clean Your Gutters?",'
    '"datePublished":"2026-08-18","author":{"@type":"Organization","name":"Poole & Bournemouth Softwash"},'
    '"publisher":{"@type":"Organization","name":"Poole & Bournemouth Softwash"}}</script>'
)

page(
    "/guides/how-often-should-you-clean-your-gutters-uk/",
    title="How Often Should You Clean Your Gutters? | PB Softwash",
    description="A practical guide to gutter cleaning frequency in the UK: what affects it, the warning signs of a blocked gutter, and why it matters more under trees.",
    h1="How Often Should You Clean Your Gutters?",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Gutter Cleaning Frequency", None)],
    extra_schema=_article_schema_gutter,
    og_image="/images/gutter-downpipe.jpg",
    body_html=f"""
{simple_hero("Guide &middot; Published 18 August 2026", "How Often Should You Clean Your Gutters?", "What actually affects the schedule, and the signs it needs doing now rather than later.")}

<section class="wrap section reveal">
  <h2>The general rule</h2>
  <p>Most UK guidance settles on once or twice a year: once in areas with little tree cover, twice — typically once in late spring after blossom and pollen, and once in late autumn after leaf fall — for properties under or near trees. That's a starting point, not a fixed schedule; the right frequency depends on what's actually near your roofline.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What makes gutters block up faster</h2>
    <ul class="checklist">
      <li><strong>Overhanging trees.</strong> Leaves, seed pods and pollen are the single biggest cause of blockages.</li>
      <li><strong>A shallow gutter pitch.</strong> Gutters that don't fall towards the downpipe steeply enough silt up even without much debris.</li>
      <li><strong>Moss and lichen from the roof above.</strong> This washes down into the gutter and builds up at the downpipe outlet, which is usually the first place a blockage forms.</li>
      <li><strong>Nearby building work or render dust</strong>, which can wash into gutters and set almost like cement.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Signs your gutters need attention now, not on a schedule</h2>
  <ul class="checklist">
    <li>Water visibly overflowing over the edge of the gutter in heavy rain, rather than running through the downpipe</li>
    <li>Plants or grass growing in the gutter — a sign silt has built up enough to hold moisture and seeds</li>
    <li>Damp patches on an internal wall below roof level after rain</li>
    <li>Staining or green streaking down external render below a gutter joint</li>
  </ul>
  <p>If you're seeing any of these, it's worth having gutters checked regardless of when they were last done. See our <a href="/gutter-and-fascia-cleaning/">gutter &amp; fascia cleaning page</a> for how we go about it.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-gutter-frequency")}
</section>
""",
)

_article_schema_pw = (
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
    '"headline":"Pressure Washing a Driveway: UK Cost Guide",'
    '"datePublished":"2026-08-18","author":{"@type":"Organization","name":"Poole & Bournemouth Softwash"},'
    '"publisher":{"@type":"Organization","name":"Poole & Bournemouth Softwash"}}</script>'
)

page(
    "/guides/pressure-washing-driveway-cost-guide-uk/",
    title="Pressure Washing a Driveway: UK Cost Guide | PB Softwash",
    description="What affects the cost of pressure washing a UK driveway: surface type, size, condition and access. General market guidance, not a fixed price list.",
    h1="Pressure Washing a Driveway: UK Cost Guide",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Driveway Cost Guide", None)],
    extra_schema=_article_schema_pw,
    og_image="/images/clean-house-driveway.jpg",
    body_html=f"""
{simple_hero("Guide &middot; Published 18 August 2026", "Pressure Washing a Driveway: UK Cost Guide", "What actually drives the price — and why the cheapest quote isn't always the best one.")}

<section class="wrap section reveal">
  <h2>What actually drives the price</h2>
  <ul class="checklist">
    <li><strong>Surface type.</strong> Block paving takes longer than a flat concrete or tarmac driveway because of the jointing, and may need re-sanding afterwards.</li>
    <li><strong>Size.</strong> Priced by area — a single-car driveway is a different job to a long, wide double driveway.</li>
    <li><strong>Condition.</strong> A driveway that hasn't been cleaned in several years, with established moss and black spot algae, takes longer than an annual maintenance clean.</li>
    <li><strong>Access.</strong> Whether we can get equipment and a water/power supply close to the surface, or need to run hose a long distance.</li>
  </ul>
  <p>Independent UK marketplace data for pressure washing jobs generally shows a range of roughly £100–£350 per visit for a typical residential driveway, with an average job landing around the middle of that range — but that's market-wide data, not a quote, and it moves with the factors above. The only way to get an accurate figure for your driveway is to request a free quote and tell us the size and surface type.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Is a cheap price actually a good deal?</h2>
    <p>A very low quote is sometimes a sign the pressure is set too high to work fast, which is exactly what damages block paving joints and softer stone. Ask what pressure and nozzle setup will be used, and whether re-sanding is included for block paving — it often isn't unless you ask. See our <a href="/pressure-washing/">pressure washing page</a> for how we approach different surfaces.</p>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-pw-cost")}
</section>
""",
)

_article_schema_roof = (
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
    '"headline":"Roof Moss: Soft Wash vs Pressure Wash",'
    '"datePublished":"2026-08-18","author":{"@type":"Organization","name":"Poole & Bournemouth Softwash"},'
    '"publisher":{"@type":"Organization","name":"Poole & Bournemouth Softwash"}}</script>'
)

page(
    "/guides/roof-moss-soft-wash-vs-pressure-wash/",
    title="Roof Moss: Soft Wash vs Pressure Wash | PB Softwash",
    description="The difference between soft washing and high-pressure jet washing a mossy roof, why manufacturers recommend soft washing, and what to ask a contractor.",
    h1="Roof Moss: Soft Wash vs Pressure Wash",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Roof Moss: Soft Wash vs Pressure Wash", None)],
    extra_schema=_article_schema_roof,
    og_image="/images/moss-covered-roof.jpg",
    body_html=f"""
{simple_hero("Guide &middot; Published 18 August 2026", "Roof Moss: Soft Wash vs Pressure Wash", "Two different methods get called “roof cleaning” — they don't carry the same risk to your tiles.")}

<section class="wrap section reveal">
  <h2>The core difference</h2>
  <p>High-pressure jet washing uses mechanical force — a concentrated jet — to physically blast moss and algae off the roof surface. Soft washing uses a biodegradable treatment applied at low pressure to kill moss, algae and lichen at the root; the dead growth is then rinsed away gently, or washes off naturally in the rain over the following one to two weeks.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Why pressure is the risk, not the cleaning itself</h2>
    <ul class="checklist">
      <li><strong>Granule loss.</strong> A concentrated high-pressure jet can strip the protective granules off concrete and asphalt-type tiles, shortening their lifespan.</li>
      <li><strong>Forced water ingress.</strong> Blasting water at close range can push water up and under tiles at the overlap, which is a common way a roof clean causes the leak it was meant to prevent.</li>
      <li><strong>Slate and older tile risk.</strong> Older or more brittle roofing is more easily cracked or dislodged by direct high-pressure contact than by a low-pressure rinse.</li>
    </ul>
    <p>This is why most roofing manufacturers and trade bodies recommend soft washing over pressure washing for roofs specifically, even though pressure washing is perfectly appropriate for driveways and patios.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>What to ask a contractor before booking a roof clean</h2>
  <ul class="checklist">
    <li>Is this a soft wash or a high-pressure jet wash?</li>
    <li>What treatment is being used, and is it biodegradable?</li>
    <li>How will they access the roof, and is the pitch/condition being assessed first?</li>
    <li>How long before the full result is visible?</li>
  </ul>
  <p>See our <a href="/roof-cleaning/">roof cleaning page</a> for how we approach this, or request a free quote below.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-roof-moss")}
</section>
""",
)

# ===========================================================================
# LEGAL
# ===========================================================================
page(
    "/privacy-policy/",
    title="Privacy Policy: How We Handle Your Data | PB Softwash",
    description="How Poole & Bournemouth Softwash collects, uses and stores personal data submitted through this website's quote request form. Read before you submit.",
    h1="Privacy Policy",
    breadcrumbs=[("Home", "/"), ("Privacy Policy", None)],
    body_html=f"""
{h1("Privacy Policy")}
<p class="lead">Last updated 18 August 2026.</p>
<section class="section legal-copy">
  <h2>What we collect</h2>
  <p>When you submit the quote request form on this site, we collect the information you provide: name, phone number, and optionally your email address, postcode and any details you add about the job.</p>
  <h2>How it's used</h2>
  <p>Your details are used solely to respond to your enquiry — to call, email or text you back about the job you asked about. Form submissions are delivered to <a href="mailto:leads@eapionageseo.co.uk">leads@eapionageseo.co.uk</a> via our form provider.</p>
  <h2>Who it's shared with</h2>
  <p><!-- TODO: confirm and state explicitly here whether leads are ever shared with, or sold to, other businesses (e.g. a rank-and-rent / lead-resale arrangement). If leads will be passed to a third-party tradesperson or business, this section must say so plainly before the form goes live — this is a legal requirement under UK GDPR, not just good practice. --></p>
  <h2>How long we keep it</h2>
  <p><!-- TODO: state your actual retention period once decided. --></p>
  <h2>Your rights</h2>
  <p>Under UK GDPR you can ask what data we hold about you, ask us to correct it, or ask us to delete it. Contact <a href="mailto:leads@eapionageseo.co.uk">leads@eapionageseo.co.uk</a> to do so.</p>
</section>
""",
)

page(
    "/terms/",
    title="Terms & Conditions for Using This Website | PB Softwash",
    description="Terms and conditions for using the Poole & Bournemouth Softwash website and quote request form. These terms do not cover the price of completed work.",
    h1="Terms &amp; Conditions",
    breadcrumbs=[("Home", "/"), ("Terms", None)],
    body_html=f"""
{h1("Terms & Conditions")}
<p class="lead">Last updated 18 August 2026.</p>
<section class="section legal-copy">
  <h2>Website use</h2>
  <p>This website provides information about our services and a way to request a quote. Submitting the form does not create a contract — a job is only confirmed once a price has been agreed directly with you.</p>
  <h2>Quotes</h2>
  <p>Prices given in response to a quote request are estimates based on the information you provide and may change if the actual job differs once assessed in person.</p>
  <h2>Content</h2>
  <p>Photographs used on this site to illustrate our services are a mix of representative stock photography and, where marked, our own work. See our <a href="/about/">About page</a>.</p>
  <p><!-- TODO: add your actual trading terms — cancellation policy, payment terms, and liability/insurance details — once confirmed. Do not publish invented policy details. --></p>
</section>
""",
)

# ===========================================================================
# THANK YOU (post-submission, kept out of the index)
# ===========================================================================
page(
    "/thank-you/",
    title="Thanks — We've Received Your Quote Request | PB Softwash",
    description="Your quote request has been received. We'll be in touch by phone or email shortly. In the meantime, feel free to browse our services or read our guides.",
    h1="Thanks — we've got your request",
    breadcrumbs=None,
    noindex=True,
    body_html=f"""
{h1("Thanks — we've got your request")}
<p class="lead">We'll be in touch by phone or email shortly, usually the same day.</p>
<p><a class="btn btn-secondary btn-on-light" href="/">Back to homepage</a></p>
""",
)

print(f"Built {len(PAGES)} pages total.")
