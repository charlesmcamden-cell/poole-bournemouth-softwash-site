#!/usr/bin/env python3
from html import escape
from generate_site import (
    page, img, lead_form, h1, page_hero, simple_hero,
    PAGES, BASE_URL, BRAND, PHONE_DISPLAY, PHONE_TEL,
    local_business_schema, service_schema, article_schema, bar_chart_svg, stat_row,
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
    extra_schema=local_business_schema(),
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
      <p>Regular exterior cleaning is maintenance, not vanity — and it's cheaper than the fascia, render or roofing repairs that come from ignoring it. Bournemouth alone sees roughly 800mm of rain a year spread fairly evenly across the seasons, which is exactly the sustained damp that lets moss and algae keep establishing rather than drying out and dying back the way they would somewhere drier.</p>
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
    extra_schema=service_schema(
        "Driveway and patio pressure washing",
        "Pressure washing for driveways, patios, block paving and pathways, with pressure and nozzle matched to the surface to avoid stripping jointing sand or etching stone.",
    ),
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
        <p>Debris and run-off contained where the job requires it, particularly near drains — see our <a href="/guides/why-we-contain-run-off-near-drains/">explainer on why that matters</a>.</p>
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
      <p>The most common driveway type we quote for in this area. Pressure is kept low enough to protect the jointing sand — stripping it out is what lets weeds and ants back in, and it's the single biggest way an inexperienced clean damages block paving. See our <a href="/guides/block-paving-re-sanding-guide/">block paving re-sanding guide</a> for why that matters.</p>
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
    <details>
      <summary>How do I know if a quote is actually a good one?</summary>
      <p>Pressure and technique matter more than price alone — see our guide on <a href="/guides/how-to-spot-a-bad-pressure-washing-quote/">how to spot a bad pressure washing quote</a> for the questions worth asking before you book with anyone.</p>
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
    extra_schema=service_schema(
        "Gutter and fascia cleaning",
        "Gutter clearing, downpipe flushing and fascia/soffit washing, carried out safely from ground level with pole and vacuum systems.",
    ),
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
    <p>A blocked gutter overflows at the weakest point — usually straight down the wall behind it. Over a winter that can mean a damp patch inside, staining on the render, or water finding its way behind the fascia board and rotting it from the back, which is far more expensive to fix than a clean. Bournemouth and Christchurch in particular have a lot of mature tree cover, which means gutters here fill with leaf litter faster than in more open areas. Not every stain on render is a sign of a problem though — see our guide on <a href="/guides/render-staining-vs-damp-warning-signs/">render staining vs damp</a> for how to tell the difference.</p>
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
    <details>
      <summary>What does gutter cleaning typically cost in the UK?</summary>
      <p>Published UK trade pricing generally scales with the length of guttering and the property's storeys — a small terraced house sits at the low end, a taller three-storey property at the high end. The chart below shows the general shape of that range; it's market-wide data, not a quote, so the only way to get an exact figure for your property is to request one.</p>
    </details>
  </div>
  {bar_chart_svg(
      "Typical UK gutter cleaning cost by property type (market-wide guidance, not a fixed price list)",
      "",
      [("Small terrace", 85), ("Semi-detached", 125), ("4-bed detached", 148), ("3-storey townhouse", 230)],
      highlight_label=None,
  )}
</section>

<section class="wrap section reveal">
  <h2>Why twice a year is the general rule</h2>
  <p>Most UK guidance settles on clearing gutters once or twice a year — once for properties with little overhead tree cover, twice for anywhere under or near trees, generally timed for after autumn leaf fall and again before the wetter spring months. That's a starting point rather than a fixed schedule: a gutter running under a mature oak or sycamore can silt up well inside six months, while one on an exposed, tree-free roofline might comfortably go longer. Read the full breakdown in our <a href="/guides/how-often-should-you-clean-your-gutters-uk/">gutter cleaning frequency guide</a>.</p>
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
    extra_schema=service_schema(
        "Roof soft washing",
        "Low-pressure soft-wash roof cleaning to remove moss, algae and lichen from tiled and slate roofs without stripping protective granules or forcing water under tiles.",
    ),
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
  <p>That last one isn't a coincidence — see our guide on <a href="/guides/north-facing-shaded-roofs-moss/">why north-facing roofs need cleaning more often</a> for why shade matters as much as rainfall.</p>
</section>

<section class="wrap section split reveal">
  <div class="split-media">
    {img("roofer-guttering.jpg", "A worker safely accessing a roofline for a roof cleaning job", 624, 1092)}
  </div>
  <div class="split-text">
    <h2>A note on older and softer roofs</h2>
    <p>Christchurch's town centre and parts of Poole Old Town have a number of older cottages, some with thatch or soft, weathered tile. We assess the roof type before quoting — thatch isn't something we treat the same way as a standard tiled roof, and we'll say so upfront rather than take on a job that's the wrong fit. If the property is listed or in a conservation area, see our guide on <a href="/guides/cleaning-an-older-or-listed-property/">cleaning an older or listed property</a> for what's worth checking first.</p>
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

<section class="wrap section reveal">
  <h2>Why spring is generally the best time to book</h2>
  <p>Moss is dormant and easiest to kill effectively when it's actively growing rather than dried out, and it grows most vigorously in cool, damp conditions — which is why UK roofing guidance generally points to spring, roughly March to May, as the best window. Treating it then also gives the roof the rest of spring and summer to dry out fully before the next wet season, rather than going into autumn already damp. Bournemouth's own rainfall pattern (below) shows why: the driest run of months is early-to-mid summer, so a spring treatment gets ahead of both the wettest, moss-friendliest months and the driest window to let everything dry properly afterwards.</p>
  {bar_chart_svg(
      "Average monthly rainfall in Bournemouth (mm) — the wetter months either side of winter are when moss grows fastest",
      "mm",
      [("Jan", 78), ("Feb", 60), ("Mar", 53), ("Apr", 58), ("May", 57), ("Jun", 57),
       ("Jul", 52), ("Aug", 67), ("Sep", 59), ("Oct", 86), ("Nov", 90), ("Dec", 81)],
      highlight_label="Nov",
  )}
  <p class="chart-source">Source: <a href="https://en.climate-data.org/europe/united-kingdom/england/bournemouth-6564/">climate averages for Bournemouth, en.climate-data.org</a>. That doesn't mean spring is the only time we'll quote — a roof that's visibly heavy with moss shouldn't wait for a specific month if it's already holding moisture against the tiles.</p>
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

<section class="wrap section reveal">
  <h2>What actually varies from town to town</h2>
  <p>The three areas we cover sit within a few miles of each other, but the conditions that dictate how fast a driveway, roof or gutter gets dirty again aren't the same across all of them. Distance from open salt water is the biggest single factor: Poole's harbourside and Sandbanks properties deal with salt-laden air that accelerates algae growth on render and leaves a chalky residue plain rain won't shift. Bournemouth's wooded chines put mature tree cover directly over a lot of roofs and gutters, which means more leaf litter and more permanently shaded, moss-prone slopes. Christchurch sits at the confluence of two rivers before they reach the sea, which keeps humidity higher for longer than areas further inland.</p>
  <p>Property age matters too. Poole has a lot of 1930s and post-war render bungalows around Parkstone and Broadstone, where render staining from roof run-off is one of the most common jobs quoted. Christchurch's town centre and parts of Mudeford have older cottages, some with thatched or soft, aged roofing that needs assessing before it's quoted rather than treated like a standard tiled roof. Bournemouth's Victorian and Edwardian terraces tend to have more complex roof lines — valleys, parapets, dormers — that collect debris a simple pitched roof wouldn't.</p>
  <p>None of that changes what we actually do — pressure washing, gutter &amp; fascia cleaning and roof soft washing are the same three services everywhere we work. It changes how often a given property probably needs it, and what we look out for while we're there. Pick a town below for the specifics, or get in touch if you're not sure which side of a boundary you fall on.</p>
  <p>Postcode-wise that's roughly BH1 through BH23, though the coverage genuinely follows where properties actually are rather than a strict postcode map — a road right on the edge of one of these boundaries is still worth asking about, even if it isn't listed by name on any of the three town pages below. When in doubt, the fastest way to find out is simply to ask when you request a quote rather than trying to work it out yourself from a postcode list alone.</p>
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
    extra_schema=service_schema(
        "Exterior cleaning in Poole",
        "Pressure washing, gutter and fascia cleaning and roof soft washing for properties in Poole, Sandbanks, Canford Cliffs, Parkstone and Broadstone.",
        areas=["Poole", "Sandbanks", "Canford Cliffs", "Parkstone", "Broadstone"],
    ),
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

<section class="wrap section reveal">
  <h2>How salt air changes the cleaning schedule</h2>
  <p>Salt spray doesn't just sit on a surface — it's hygroscopic, meaning it pulls moisture from the air and keeps paving, render and roof tiles damp for longer after rain than they would be further inland. That extra dwell time is exactly what algae and black spot need to establish. Properties within roughly a mile of the harbour or Poole Bay, particularly around Sandbanks, Lilliput and the Panorama Road stretch, generally need driveway and render cleaning noticeably more often than the 12–18 month interval that suits most inland Dorset properties — closer to annually is common for the most exposed spots.</p>
  <p>The same logic applies to gutters near the water: salt-laden grit and debris carried on the wind settles in gutter runs alongside the usual leaf litter, so it's worth checking Poole's harbourside properties on the more frequent end of our <a href="/guides/how-often-should-you-clean-your-gutters-uk/">gutter cleaning frequency guide</a>.</p>
  <p>Inland from the water, Broadstone and the northern edges of Poole see less salt exposure but more tree cover, so the driving factor shifts from salt residue to leaf litter and shaded, moss-prone roof slopes — closer to the general Dorset pattern than the harbourside. Whichever side of that you're on, the quote process is the same: tell us the surface or roof details and roughly where you are, and pricing reflects what's actually needed rather than a flat area-wide rate.</p>
  <p>Parkstone in particular sits in between the two — close enough to the water for some salt effect, with enough established tree-lined streets that gutter clearing frequency matters as much as render staining does. It's a good, representative example of why we always ask about the specific property first, not just the town name alone, before pricing anything up for a Poole customer. For more on exactly how salt air affects a property, see our <a href="/guides/coastal-salt-air-property-maintenance/">coastal salt air &amp; property maintenance guide</a>.</p>
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
    extra_schema=service_schema(
        "Exterior cleaning in Bournemouth",
        "Pressure washing, gutter and fascia cleaning and roof soft washing for properties in Bournemouth, Talbot Woods, Alum Chine, Westbourne and Southbourne.",
        areas=["Bournemouth", "Talbot Woods", "Westbourne", "Southbourne"],
    ),
    body_html=f"""
{page_hero("bournemouth-pier.jpg", "Bournemouth Pier and seafront with the beach in view",
            "Bournemouth", "Pressure Washing, Gutter & Roof Cleaning in Bournemouth",
            "Covering central Bournemouth, Talbot Woods, Westbourne, Alum Chine and Southbourne.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>')}

<section class="wrap section reveal">
  <h2>What's different about cleaning exteriors in Bournemouth</h2>
  <p>Bournemouth's chines — the wooded valleys that run down to the seafront at Alum Chine, Middle Chine and Boscombe Chine — put a lot of mature tree cover right up against nearby homes. That means more leaf litter and pollen ending up in gutters, and more roof slopes kept in permanent shade, which is exactly the damp, low-light condition moss needs to establish — see our guide on <a href="/guides/north-facing-shaded-roofs-moss/">why shaded roofs need cleaning more often</a> for the science behind that. Victorian and Edwardian terraces around the town centre and Westbourne also tend to have more complex roof lines with valleys and parapets, which collect debris that a simple pitched roof wouldn't.</p>
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

<section class="wrap section reveal">
  <h2>Why tree cover, not just rain, drives the schedule here</h2>
  <p>It's tempting to assume gutter and roof cleaning frequency comes down to rainfall alone, but shade matters just as much — moss and algae need both moisture and low light to establish, and Bournemouth's chines put a lot of roofs and gutters permanently in the shadow of mature trees. A north-facing slope under tree cover in Alum Chine or Middle Chine can stay damp for days after rain that a similar south-facing, open roof would shrug off within hours. That's why we assess shade and overhang, not just how long it's been since the last clean, when we're asked how often a particular property needs attention.</p>
  <p>For gutters specifically, overhanging trees are the single biggest factor in how often clearing is needed — general UK guidance of once or twice a year assumes moderate exposure, and a heavily tree-lined Bournemouth street can need the more frequent end of that. See our <a href="/guides/how-often-should-you-clean-your-gutters-uk/">gutter cleaning frequency guide</a> for the full breakdown.</p>
  <p>Central Bournemouth and the seafront itself are more exposed and less shaded than the chines, so properties there tend to sit closer to the standard once-a-year gutter interval and the 12–18 month driveway cleaning window that suits most inland Dorset homes. The difference within Bournemouth can be as much about which street you're on as which side of town — which is exactly why we quote from the actual property rather than a blanket area rate.</p>
  <p>Boscombe and the eastern seafront share some of Southbourne's tree-lined character further back from the beach itself, while the immediate town-centre core — around the Square and the Lower Gardens — is more built-up with less overhead cover. Either way, the underlying services are the same three; only the frequency recommendation shifts based on what's actually overhead and how close the property sits to open water — which is exactly what we ask about, street by street, before quoting anywhere in Bournemouth.</p>
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
    extra_schema=service_schema(
        "Exterior cleaning in Christchurch",
        "Pressure washing, gutter and fascia cleaning and careful roof soft washing for properties in Christchurch, Mudeford, Highcliffe and Burton, including older and thatched buildings.",
        areas=["Christchurch", "Mudeford", "Highcliffe", "Burton"],
    ),
    body_html=f"""
{page_hero("christchurch-priory.jpg", "Christchurch Priory tower with clock",
            "Christchurch", "Pressure Washing, Gutter & Roof Cleaning in Christchurch",
            "Covering Christchurch town centre, Mudeford, Highcliffe and Burton.",
            ctas_html=f'<div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get a free quote</a><a class="btn btn-secondary" href="{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>')}

<section class="wrap section reveal">
  <h2>What's different about cleaning exteriors in Christchurch</h2>
  <p>Christchurch sits where the River Avon meets the River Stour before they reach the sea at Mudeford — low-lying, close to water on more than one side, and noticeably more humid than areas further inland. That's ideal growing conditions for moss and algae, which is why roofs and north-facing walls here often need attention more often than the regional average.</p>
  <p>The town centre and parts of Mudeford also have a number of older cottages, some with thatched or soft, aged roofing. We assess roof type and condition before quoting rather than treating every roof the same way — see our <a href="/roof-cleaning/">roof cleaning page</a> for how we approach older and more delicate roofs, or our guide on <a href="/guides/cleaning-an-older-or-listed-property/">cleaning an older or listed property</a> for what's worth checking before booking anything.</p>
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

<section class="wrap section reveal">
  <h2>Assessing older and thatched properties first</h2>
  <p>A standard concrete or clay tiled roof and a soft, weathered thatch aren't the same job, and treating them the same way is how damage happens. Before quoting anywhere in Christchurch's town centre or around Mudeford, where older cottages are common, we ask about roof age and covering type — if it's thatch, that's not something we treat with the same soft-wash method as a standard tiled roof, and we'll say so upfront rather than take on a job that's the wrong fit. See our <a href="/roof-cleaning/">roof cleaning page</a> for how soft washing works on the roofs it is suited to.</p>
  <p>The river confluence at Mudeford also means humidity here tends to run higher for longer after rain than areas further inland, which is worth factoring in if you're deciding between an annual and a twice-yearly gutter clearing schedule — our <a href="/guides/how-often-should-you-clean-your-gutters-uk/">gutter cleaning frequency guide</a> covers what else affects that decision.</p>
  <p>Highcliffe and Burton, further from the immediate river confluence, are somewhat drier and more exposed than the town centre and Mudeford, so they tend to follow the general Dorset pattern more closely. As with the other areas we cover, the roof and property type on your specific street matters more than a single blanket rule for the whole town — tell us what you've got and we'll quote accordingly.</p>
  <p>Mudeford Quay and the harbourside properties closest to the water share some of Poole's salt-air characteristics too, on top of the general river-valley humidity — the combination is part of why we treat Christchurch's coastal fringe as its own case rather than assuming it behaves exactly like the town centre a couple of miles inland. That combination of salt and standing humidity is, if anything, the most demanding set of conditions we're asked to quote for anywhere across the three Dorset towns we cover.</p>
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
    extra_schema=local_business_schema(),
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
  <h2>Why three services, not a long list</h2>
  <p>Pressure washing, gutter &amp; fascia cleaning and roof soft washing aren't three unrelated jobs — they're the same underlying problem attacking a property from different directions. Moss and algae on a roof wash down into the gutters below it; a blocked gutter overflows onto render and paving below that; and coastal damp keeps the whole cycle going faster here than in most of the UK. Specialising in these three, rather than offering a broad menu that also includes window cleaning, driveway sealing or full roof repairs, means the equipment and technique for each job gets used often enough to actually be good at it, and it's easier to say no to a job that's outside what we do properly rather than take it on anyway.</p>
  <p>That also means there are things we deliberately don't do: structural roof repairs, guttering replacement, or full render restoration are all trades of their own. Where a job needs one of those, we'll say so during the quote rather than attempt it.</p>
  <p>It also means we turn down jobs outside Poole, Bournemouth, Christchurch and the immediate surrounding area, rather than travelling a long distance and pricing it accordingly — being local to the area we work in is part of how the pricing and scheduling stays realistic. If you're just outside that radius, ask anyway; the boundary isn't a hard line, it's a reflection of where we can turn quotes around quickly.</p>
  <p>If you're weighing up whether it's worth booking before selling a property, our guide on <a href="/guides/does-cleaning-help-when-selling-a-house/">whether cleaning actually helps when selling a house</a> covers the real UK research on that, rather than the usual assumption.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>How a typical booking goes</h2>
    <div class="process-grid">
      <div class="process-step">
        <div class="step-num">1</div>
        <h3>You describe the job</h3>
        <p>Surface type or roof/gutter details and a rough size, plus a photo if that's quicker than describing it — through the form on any page.</p>
      </div>
      <div class="process-step">
        <div class="step-num">2</div>
        <h3>We confirm a price</h3>
        <p>Usually the same day. Nothing is booked or charged until you've agreed to a figure.</p>
      </div>
      <div class="process-step">
        <div class="step-num">3</div>
        <h3>We turn up and do the job</h3>
        <p>Access to an outdoor tap and, for pressure washing, reasonable vehicle access is generally all we need — you don't have to be home.</p>
      </div>
      <div class="process-step">
        <div class="step-num">4</div>
        <h3>You're shown the result</h3>
        <p>And told about anything we spotted along the way, even things outside what we were booked to do.</p>
      </div>
    </div>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Get in touch</h2>
  <p>Call <a href="{PHONE_TEL}">{escape(PHONE_DISPLAY)}</a> or use the quote form on any page and we'll get back to you, usually the same day. If you'd rather read more before deciding, our <a href="/faq/">FAQ page</a> and <a href="/guides/">guides</a> cover most of what people ask before booking.</p>
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
    extra_schema=local_business_schema(),
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

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What to include for a faster quote</h2>
    <ul class="checklist">
      <li><strong>For pressure washing:</strong> the surface type (block paving, concrete, natural stone) and a rough size — "single driveway", "double driveway plus patio" is enough to start with.</li>
      <li><strong>For gutter &amp; fascia cleaning:</strong> how many storeys the property is and whether there's significant tree cover overhead.</li>
      <li><strong>For roof cleaning:</strong> the roof covering if you know it (tile, slate, thatch) and roughly how visible the moss or staining is.</li>
      <li>A photo, for any of the above — often quicker than describing it, and it's an optional field on the form.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>What happens after you get in touch</h2>
  <p>Enquiries are usually answered the same day, sometimes the next if it comes in late or over a weekend. You'll get a price based on what you've told us — for anything unusual (a large commercial forecourt, an oddly-shaped roof, uncertain access) we may ask a couple of follow-up questions or arrange a quick look before confirming a final figure. Nothing is booked or charged until you've agreed to the price. If you'd rather skip the form entirely, calling {escape(PHONE_DISPLAY)} gets you the same conversation without typing it out.</p>
</section>

<section class="wrap section reveal">
  <h2>Not sure which service you need?</h2>
  <p>That's fine — tell us what you're seeing rather than trying to diagnose it yourself. "Green staining on the driveway" usually points to pressure washing; "water overflowing the gutter in heavy rain" points to a blocked gutter; "dark patches on the roof, especially on shaded slopes" usually means moss and points to roof cleaning. If more than one applies, say so on the form and we'll quote the whole job in one visit rather than sending someone out twice.</p>
  <div class="area-links">
    <a href="/pressure-washing/">Pressure washing</a>
    <a href="/gutter-and-fascia-cleaning/">Gutter &amp; fascia cleaning</a>
    <a href="/roof-cleaning/">Roof cleaning</a>
    <a href="/faq/">Read the FAQ &rarr;</a>
  </div>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Where we cover</h2>
    <p>Based centrally to the Poole/Bournemouth/Christchurch area and working across the wider BH postcode area of Dorset — see our full <a href="/areas/">areas covered</a> breakdown for what's different about cleaning exteriors in each town, or just ask when you get in touch if you're not sure whether your address is covered.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Prefer to read first?</h2>
  <p>If you're not ready to request a quote yet and just want more information, the <a href="/faq/">FAQ page</a> covers the questions we're asked most often, and the <a href="/guides/">guides section</a> goes into more detail on specific topics like gutter cleaning frequency and driveway pressure washing costs — genuinely useful information, not just a longer way of asking you to call. Read as much or as little of it as you want; there's no form to fill in first.</p>
</section>

<section class="wrap section reveal">
  <h2>Email vs the form</h2>
  <p>Both reach the same place, so use whichever is easier — the form just prompts for the details (surface, size, area) that speed up a first response, while email works fine for anything that doesn't fit neatly into those fields, like a longer description or an attached photo.</p>
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
    ("What's the difference between pressure washing and soft washing?", "Pressure washing uses higher water pressure and is right for hard surfaces like driveways, patios and concrete — it physically blasts grime off. Soft washing uses low pressure with a biodegradable treatment that kills moss and algae at the root, which is what we use on roofs and delicate render, since a hard jet can strip roof granules or force water under tiles. See our soft wash vs pressure wash guide for the full comparison."),
    ("Do I need to move anything before you arrive?", "Cars off a driveway that's being cleaned, and garden furniture or planters clear of a patio, make the job quicker — but if something's too heavy to move, mention it on the form and we'll work around it or clean up to it."),
    ("Do you bring your own water supply?", "For most residential jobs we connect to an outdoor tap. If a property doesn't have one accessible, mention it on the form so we can plan for it in advance rather than discover it on the day."),
    ("Is there anything you won't clean?", "Thatched roofs are treated differently to standard tiled or slate roofs and assessed individually — see our roof cleaning page. We also don't carry out repairs (gutters, render, roofing) ourselves; we'll flag anything that needs one and let you arrange it separately."),
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
  <a class="service-card" href="/guides/does-cleaning-help-when-selling-a-house/">
    <div class="img-wrap">{img("clean-house-driveway.jpg", "A clean house with a well-kept driveway", 400, 270)}</div>
    <h3>Does Cleaning Help When Selling a House?</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/coastal-salt-air-property-maintenance/">
    <div class="img-wrap">{img("poole-harbour.jpg", "Fishing boat in Poole Harbour, Dorset", 400, 270)}</div>
    <h3>Coastal Salt Air &amp; Property Maintenance</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/render-staining-vs-damp-warning-signs/">
    <div class="img-wrap">{img("garden-path.jpg", "A clean brick driveway bordered by render walls", 400, 270)}</div>
    <h3>Render Staining vs Damp: What's the Risk?</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/cleaning-an-older-or-listed-property/">
    <div class="img-wrap">{img("christchurch-priory.jpg", "Christchurch Priory tower, an example of a historic Dorset building", 400, 270)}</div>
    <h3>Cleaning an Older or Listed Property</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/why-we-contain-run-off-near-drains/">
    <div class="img-wrap">{img("gutter-downpipe.jpg", "A downpipe fixed to the exterior wall of a house", 400, 270)}</div>
    <h3>Why We Contain Run-off Near Drains</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/block-paving-re-sanding-guide/">
    <div class="img-wrap">{img("pressure-washing-steps.jpg", "Pressure washer being used on outdoor paving", 400, 270)}</div>
    <h3>Block Paving Re-Sanding: Why &amp; How Often</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/north-facing-shaded-roofs-moss/">
    <div class="img-wrap">{img("moss-covered-roof.jpg", "Moss concentrated on a shaded roof slope", 400, 270)}</div>
    <h3>Why North-Facing Roofs Need Cleaning More</h3>
    <span class="card-link">Read the guide &rarr;</span>
  </a>
  <a class="service-card" href="/guides/how-to-spot-a-bad-pressure-washing-quote/">
    <div class="img-wrap">{img("hero-pressure-washing.jpg", "Professional pressure washing equipment in use", 400, 270)}</div>
    <h3>How to Spot a Bad Pressure Washing Quote</h3>
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
{simple_hero("Guide · Published 18 August 2026", "How Often Should You Clean Your Gutters?", "What actually affects the schedule, and the signs it needs doing now rather than later.")}

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

<section class="wrap section reveal">
  <h2>What it typically costs, by property size</h2>
  <p>Published UK trade pricing for gutter clearing scales mainly with the length of guttering to be cleared and how many storeys it's at — a single-storey terrace is a shorter, easier job than a three-storey townhouse. The chart below reflects that general market-wide pattern; it's not a quote for any specific property, since access and condition on the day both affect the final price.</p>
  {bar_chart_svg(
      "Typical UK gutter cleaning cost by property type (market-wide guidance, not a fixed price list)",
      "",
      [("Small terrace", 85), ("Semi-detached", 125), ("4-bed detached", 148), ("3-storey townhouse", 230)],
  )}
  <p>Weighing cost against frequency: a property that needs clearing twice a year because of heavy tree cover will spend roughly double what a once-a-year property does annually — which is sometimes a reason to consider whether overhanging branches can be trimmed back, not just how often the gutter itself gets cleared.</p>
</section>

<section class="wrap section reveal">
  <h2>The bottom line</h2>
  <p>If you genuinely don't know when your gutters were last cleared, that's the strongest signal to get them checked now rather than wait for a fixed date. A quick inspection costs nothing to arrange, and it turns "once or twice a year" from a guess into an actual schedule based on your roofline, not a generic rule of thumb, or on borrowed assumptions from a neighbour's different property. For the service itself — what's included and how it's carried out — see our <a href="/gutter-and-fascia-cleaning/">gutter &amp; fascia cleaning page</a>.</p>
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
{simple_hero("Guide · Published 18 August 2026", "Pressure Washing a Driveway: UK Cost Guide", "What actually drives the price — and why the cheapest quote isn't always the best one.")}

<section class="wrap section reveal">
  <h2>What actually drives the price</h2>
  <ul class="checklist">
    <li><strong>Surface type.</strong> Block paving takes longer than a flat concrete or tarmac driveway because of the jointing, and may need re-sanding afterwards.</li>
    <li><strong>Size.</strong> Priced by area — a single-car driveway is a different job to a long, wide double driveway.</li>
    <li><strong>Condition.</strong> A driveway that hasn't been cleaned in several years, with established moss and black spot algae, takes longer than an annual maintenance clean.</li>
    <li><strong>Access.</strong> Whether we can get equipment and a water/power supply close to the surface, or need to run hose a long distance.</li>
  </ul>
  <p>Independent UK marketplace data for pressure washing jobs generally shows a range of roughly £100–£350 per visit for a typical residential driveway, with an average job landing around the middle of that range — but that's market-wide data, not a quote, and it moves with the factors above. The only way to get an accurate figure for your driveway is to request a free quote and tell us the size and surface type.</p>
  {bar_chart_svg(
      "Typical UK driveway pressure washing cost by size (market-wide guidance, not a fixed price list)",
      "",
      [("Small driveway", 250), ("Medium driveway", 350), ("Large driveway", 400)],
  )}
  <p>Priced per square metre rather than by "small/medium/large", UK market data generally sits around £8.50–£15.50/m² for a clean on its own, rising to roughly £24/m² if joint re-sanding or a protective seal is included afterwards. A single-car driveway (roughly 15–20m²) and a long double driveway (40m² or more) can therefore land at quite different points even within the same "medium" bracket — which is why an accurate quote needs an actual measurement, not just a size category.</p>
</section>

<section class="wrap section reveal">
  <h2>Sealing: worth it, and when</h2>
  <p>A clean removes what's already grown; a sealant slows down how fast it comes back by making the surface less porous, so moss and algae have less to grip. It's a genuinely separate line item, not something bundled into every clean by default — ask for it specifically if you want it quoted alongside the wash.</p>
</section>

<section class="wrap section reveal">
  <h2>Getting an accurate quote instead of guessing</h2>
  <p>Every range in this guide is market-wide UK data, useful for budgeting but not a substitute for an actual measurement of your driveway. Surface type and condition move the price as much as size does — a block-paved driveway with established weeds in the joints costs more to do properly than a similarly sized concrete drive that's just dusty. Tell us the size and surface, ideally with a photo, and we'll give you a real figure specific to your driveway rather than a general range.</p>
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
{simple_hero("Guide · Published 18 August 2026", "Roof Moss: Soft Wash vs Pressure Wash", "Two different methods get called “roof cleaning” — they don't carry the same risk to your tiles.")}

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

<section class="wrap section reveal">
  <h2>Why timing affects which method makes sense</h2>
  <p>Moss is far easier to kill — by either method — while it's actively growing than once it's dried out and gone dormant, which is one more reason soft washing tends to be scheduled for the wetter parts of the year rather than the height of summer. Bournemouth's rainfall pattern below shows the shape of that: the driest months (June–July) are when moss is least vulnerable to treatment, while the wetter months either side of winter are when it's actively growing and most responsive.</p>
  {bar_chart_svg(
      "Average monthly rainfall in Bournemouth (mm)",
      "mm",
      [("Jan", 78), ("Feb", 60), ("Mar", 53), ("Apr", 58), ("May", 57), ("Jun", 57),
       ("Jul", 52), ("Aug", 67), ("Sep", 59), ("Oct", 86), ("Nov", 90), ("Dec", 81)],
      highlight_label="Nov",
  )}
  <p class="chart-source">Source: <a href="https://en.climate-data.org/europe/united-kingdom/england/bournemouth-6564/">climate averages for Bournemouth, en.climate-data.org</a></p>
  <p>This matters more for soft washing than pressure washing specifically, because soft washing relies on the treatment penetrating and killing living moss over the following one to two weeks — treating dormant, dried-out moss in the middle of a dry spell simply gets a slower, less complete result. A high-pressure jet wash doesn't have that dependency, since it's removing moss mechanically rather than biologically — one more reason it's tempting for a quick fix, and one more reason it's still the wrong tool for a roof, regardless of what time of year it's done. Whatever the season, the underlying advice from our <a href="/roof-cleaning/">roof cleaning page</a> stays the same: soft wash, not jet wash.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-roof-moss")}
</section>
""",
)

# ===========================================================================
# NEW GUIDE ARTICLES (batch 2)
# ===========================================================================

page(
    "/guides/does-cleaning-help-when-selling-a-house/",
    title="Does Cleaning Help When Selling a House? | PB Softwash",
    description="What UK kerb-appeal research actually says about buyer decisions, and where driveway, render and roof cleaning fits in before viewings and photos.",
    h1="Does Exterior Cleaning Help When Selling a House?",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Kerb Appeal & Selling", None)],
    extra_schema=article_schema(
        "Does Exterior Cleaning Help When Selling a House?",
        "What UK kerb-appeal research says about buyer decisions, and where driveway, render and roof cleaning fits in before viewings and photos.",
        "/images/clean-house-driveway.jpg",
    ),
    og_image="/images/clean-house-driveway.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Does Exterior Cleaning Help When Selling a House?", "What the research actually says, rather than the usual estate agent truism.")}

<section class="wrap section reveal">
  <h2>What the research says</h2>
  <p>"Kerb appeal matters" is repeated so often it starts to sound like filler, but there's real UK survey data behind it. A 2023 survey of 2,001 UK residents (commissioned by landscaping brand Marshalls) found the numbers below — and they're a lot more specific than the usual advice.</p>
  {stat_row([
      ("60%", "of viewers decide their first impression within one minute of seeing the outside"),
      ("68%", "would be put off buying if the front garden had visible design flaws"),
      ("43%", "say they now care more about their home's front appearance than two years ago"),
  ])}
  <p class="chart-source">Source: <a href="https://www.estateagenttoday.co.uk/breaking-news/2023/12/two-thirds-of-buyers-deterred-if-property-lacks-kerb-appeal-survey/">Estate Agent Today, reporting Marshalls' 2023 kerb appeal survey</a></p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Where cleaning specifically fits in</h2>
    <p>The survey's most-mentioned appeal factors are mostly planting and landscaping — hanging baskets, trees, lawns. But a stained, moss-covered driveway or a roof with visible black streaking undercuts all of that in the same one-minute window the research describes: it reads as "not maintained" before a viewer has processed anything else about the property. Unlike replanting a garden, which takes a season, a driveway or render clean is something that can be booked and completed within days of a first viewing being arranged.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>What's worth doing before viewings, in order</h2>
  <ul class="checklist">
    <li><strong>Driveway and path first.</strong> It's the first surface a viewer walks across and the one most likely to show algae or black spot staining. See our <a href="/pressure-washing/">pressure washing page</a>.</li>
    <li><strong>Render and any visible roof staining next.</strong> Streaking below a gutter joint or along a roofline photographs badly, especially in listing photos taken from the street.</li>
    <li><strong>Gutters, if they're visibly sagging or overflowing.</strong> Less visible day-to-day, but a surveyor will notice it even if a viewer doesn't.</li>
  </ul>
  <p>None of this is a substitute for the property itself being in good condition — cleaning surfaces a house that's already sound, it doesn't disguise one that isn't. See our <a href="/guides/pressure-washing-driveway-cost-guide-uk/">driveway cleaning cost guide</a> for what it typically costs to have done before a sale.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Photos matter as much as viewings</h2>
    <p>Most buyers see a property online before they ever see it in person, and listing photos are usually shot from the street — the exact angle that shows a stained driveway or a mossy roofline most clearly. A clean exterior photographs noticeably better in flat, even light than one with dark algae patches breaking up the surface, which is worth timing deliberately: getting the clean done a few days before listing photos are taken, rather than after the first viewings have already happened, gets the benefit from the very first impression a buyer forms — the online listing, not just the doorstep.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>What this doesn't fix</h2>
  <p>Exterior cleaning is one of the cheapest, fastest kerb-appeal improvements available precisely because it's cosmetic — it makes a well-maintained property look as good as it actually is. It won't disguise genuine issues like render cracking, a sagging gutter, or a roof that needs more than a clean. If anything, a clean can make those issues more visible rather than less, since they're no longer hidden under general grime — which is arguably a better outcome for a seller than papering over a problem a survey will find anyway.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-kerb-appeal")}
</section>
""",
)

page(
    "/guides/coastal-salt-air-property-maintenance/",
    title="Coastal Salt Air & Property Maintenance | PB Softwash",
    description="How salt-laden air from Poole Harbour and Poole Bay affects paving, render and roof tiles, and why coastal properties need more frequent exterior cleaning.",
    h1="Coastal Salt Air & Property Maintenance",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Coastal Salt Air", None)],
    extra_schema=article_schema(
        "Coastal Salt Air & Property Maintenance in Poole",
        "How salt-laden air from Poole Harbour and Poole Bay affects paving, render and roof tiles, and why coastal properties need more frequent exterior cleaning.",
        "/images/poole-harbour.jpg",
    ),
    og_image="/images/poole-harbour.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Coastal Salt Air & Property Maintenance", "Why a harbourside driveway and an inland one age differently, even a few miles apart.")}

<section class="wrap section reveal">
  <h2>Why salt air speeds up staining</h2>
  <p>Salt is hygroscopic — it draws moisture out of the air and holds onto it, rather than letting a surface dry out the way it would after ordinary rain. Airborne salt spray from Poole Harbour and Poole Bay settles on paving, render and roof tiles and keeps them damp for longer after wet weather, and that extended dampness is exactly the condition algae and black spot staining need to establish and spread. It's a physical, measurable effect, not a vague "sea air ages things" claim — surfaces genuinely stay wetter for longer near open salt water than the same surfaces a few miles inland.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What it actually shows up as</h2>
    <ul class="checklist">
      <li><strong>A dull, chalky residue on paving</strong> that plain rain doesn't rinse away, distinct from ordinary dirt.</li>
      <li><strong>Faster algae growth on render</strong>, particularly on north-facing or shaded elevations that already dry slowly.</li>
      <li><strong>Corrosion on metal fixings</strong> — gutter brackets, downpipe clips — well before the guttering itself needs attention.</li>
      <li><strong>Accelerated staining on roof tiles</strong>, especially on exposed, sea-facing slopes.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>How much more often does a coastal property need cleaning?</h2>
  <p>For most inland Dorset properties, a driveway clean every 12–18 months is typical. For properties within roughly a mile of the harbour or Poole Bay — Sandbanks, Lilliput, the Panorama Road stretch, and similar exposed spots — closer to an annual clean is common, and render or roof staining can become visible again within months rather than years in the most exposed locations. That's a general pattern we see, not a fixed rule for every address; a sheltered courtyard a street back from the water behaves differently to an exposed frontage facing straight out to the bay. See our <a href="/areas/poole/">Poole area page</a> for more on how this plays out locally, or our <a href="/pressure-washing/">pressure washing page</a> for how salt residue is treated differently from ordinary dirt.</p>
</section>

<section class="wrap section reveal">
  <h2>What helps between cleans</h2>
  <p>A sealant on paving genuinely slows salt and algae build-up by making the surface less porous, so there's less for residue to bind to — worth asking about specifically if a property is in one of the more exposed spots, since it's not automatically included with a standard clean. For render, there isn't an equivalent quick fix; a well-maintained, intact render finish naturally sheds more moisture than cracked or aged render, so keeping on top of any render repairs matters more near the coast than it does further inland, where the same minor damage would take longer to turn into a visible problem.</p>
  <p>Metal fixings are worth a specific mention: gutter brackets, downpipe clips and similar fittings corrode faster in salt air than the guttering itself typically wears out, so a fitting failing early is more often a coastal-exposure issue than a manufacturing one. It's a small thing to have checked while gutters are being cleared rather than treated as a separate concern, and it costs nothing extra to flag if we notice it during a routine visit.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-salt-air")}
</section>
""",
)

page(
    "/guides/render-staining-vs-damp-warning-signs/",
    title="Render Staining vs Damp: What's the Risk? | PB Softwash",
    description="How to tell whether dirty, algae-stained render is just cosmetic or an early warning sign of penetrating damp, and what actually causes render-related damp.",
    h1="Render Staining vs Damp: Cosmetic or Warning Sign?",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Render Staining vs Damp", None)],
    extra_schema=article_schema(
        "Render Staining vs Damp: What's Cosmetic, What Isn't",
        "How to tell whether dirty, algae-stained render is just cosmetic or an early warning sign of penetrating damp, and what actually causes render-related damp.",
        "/images/garden-path.jpg",
    ),
    og_image="/images/garden-path.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Render Staining vs Damp: Cosmetic or Warning Sign?", "Most render staining is purely cosmetic. Here's how to tell when it isn't.")}

<section class="wrap section reveal">
  <h2>The cosmetic case: algae and general grime</h2>
  <p>Green or black staining spread fairly evenly across a render surface, worse on shaded or north-facing walls, is almost always algae growing on the surface itself — it's cosmetic, and a clean genuinely resolves it without any underlying issue. This is the most common reason render looks dirty, and it's not a sign anything is wrong with the wall underneath.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What actually causes render-related damp</h2>
    <p>Penetrating damp linked to render generally comes from one of a few specific mechanisms, not simply "the render is old":</p>
    <ul class="checklist">
      <li><strong>Cracks and fissures</strong> that let water directly into the wall behind the render.</li>
      <li><strong>Render bridging the damp-proof course</strong> — if render runs down over the DPC line, it can create a path for rising damp that the DPC was meant to block.</li>
      <li><strong>Poor detailing around windows and doors</strong>, where water finds a way in at a joint rather than through the render face itself.</li>
      <li><strong>Non-breathable modern renders on older, solid-wall properties</strong>, which can trap moisture that would otherwise evaporate outward.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Signs it's more than cosmetic</h2>
  <ul class="checklist">
    <li>Staining concentrated around one specific crack, joint or window reveal, rather than spread generally across the wall</li>
    <li>Render that sounds hollow when tapped, or has visibly bulged or blown away from the wall behind it</li>
    <li>A damp patch appearing on the corresponding internal wall, especially after heavy rain</li>
    <li>Staining that returns within weeks of a clean, concentrated in the same spot each time</li>
  </ul>
  <p>General, even algae staining is a cleaning job — see our <a href="/pressure-washing/">pressure washing page</a>, which covers render alongside paving. Anything matching the list above is a job for a render or damp specialist, not a clean; we'll say so if we spot it while working, since it's not something we carry out repairs for ourselves.</p>
</section>

<section class="wrap section reveal">
  <h2>Why a clean sometimes reveals the difference</h2>
  <p>General grime and algae can actually mask the more localised signs above — a wall covered evenly in green staining makes it harder to spot the one patch that's cracked or bulging underneath. That's part of why a proper clean is genuinely useful diagnostically, not just cosmetically: once the surface-level algae is gone, what's left is either a uniformly clean wall, or a specific area that still looks different from the rest — which is exactly the kind of localised issue worth having looked at properly rather than assumed away.</p>
</section>

<section class="wrap section reveal">
  <h2>What we do, and what we don't</h2>
  <p>Our render work is limited to cleaning — removing algae, general grime and roof run-off staining from the surface, using the same pressure-matched approach we use on other surfaces. We're not damp specialists and don't diagnose or treat damp itself; if what we find while cleaning looks like more than a surface issue, the honest answer is to say so and point you toward someone who does that specifically, rather than guess at what it might be.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-render-damp")}
</section>
""",
)

page(
    "/guides/cleaning-an-older-or-listed-property/",
    title="Cleaning an Older or Listed Property | PB Softwash",
    description="What to check before cleaning a listed building or a property in a conservation area in the UK, and why the safe first step is always your local council.",
    h1="Cleaning an Older or Listed Property: What to Check",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Older & Listed Properties", None)],
    extra_schema=article_schema(
        "Cleaning an Older or Listed Property: What to Check",
        "What to check before cleaning a listed building or a property in a conservation area in the UK, and why the safe first step is always your local council.",
        "/images/christchurch-priory.jpg",
    ),
    og_image="/images/christchurch-priory.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Cleaning an Older or Listed Property: What to Check", "Christchurch and parts of Poole Old Town have real numbers of these — here's what's worth knowing first.")}

<section class="wrap section reveal">
  <h2>Why this is worth checking before you book anything</h2>
  <p>If a property is listed or sits in a conservation area, exterior work — including some types of cleaning — can require consent from the local planning authority, and the rules vary by council and by exactly what's listed about the property. This isn't something we can give a blanket answer to on a website, because the specifics genuinely depend on your council and your property's listing. The one reliable first step is checking directly with your local planning department before booking any exterior cleaning on a listed building, rather than assuming a soft, low-pressure method is automatically fine because it's gentler than a jet wash.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What tends to matter most</h2>
    <ul class="checklist">
      <li><strong>Roof covering.</strong> Thatch and very old, soft tile are treated completely differently from standard modern tiles — see our <a href="/roof-cleaning/">roof cleaning page</a> for how we assess this before quoting.</li>
      <li><strong>Original stonework or historic brick.</strong> Softer, older masonry can be more vulnerable to high pressure or aggressive chemical treatments than modern equivalents.</li>
      <li><strong>Whether the property is listed itself, or just within a conservation area.</strong> These carry different rules — a conservation area mainly affects things like alterations and demolition, while listing can cover much more of the fabric of the building.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>How we approach it</h2>
  <p>We ask about roof type, age and any listing status before quoting, and we'll say upfront if a job looks like it needs a specialist heritage cleaner rather than a general soft wash — thatch is the clearest example, and Christchurch's town centre and parts of Mudeford have a genuine number of older cottages where this comes up. See our <a href="/areas/christchurch/">Christchurch area page</a> for more on the local property mix, or get in touch and mention the property's age and any listing status when you request a quote.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Listed vs conservation area: not the same thing</h2>
    <p>The two get conflated, but they're different designations. A conservation area is about the character of a wider street or neighbourhood — alterations, demolitions and some external changes across the whole area can need consent. A listed building is a designation on a specific property, based on its individual architectural or historic interest, and can affect far more of the property's fabric, inside and out. A property can be in a conservation area without being individually listed, or listed without the wider street being a conservation area — which is exactly why checking your specific property's status with the local council, rather than assuming from the general character of the street, is the right first step.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Why "gentle" doesn't automatically mean "permitted"</h2>
  <p>It's tempting to assume that because soft washing uses lower pressure than a jet wash, it must always be fine on a listed or older property — but consent requirements are often about the method and materials used, not just how forceful the clean is. A biodegradable treatment applied to historic stonework can still be the wrong call if the stone type reacts differently to it than modern render does. This is exactly why we treat older and listed properties as their own case rather than assuming our standard soft-wash approach transfers automatically.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-listed-property")}
</section>
""",
)

page(
    "/guides/why-we-contain-run-off-near-drains/",
    title="Why We Contain Run-off Near Drains: A Guide | PB Softwash",
    description="A short explainer on surface water drains versus foul sewers, and why containing pressure washing and roof cleaning run-off near drains is good practice.",
    h1="Why We Contain Run-off Near Drains",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Run-off Near Drains", None)],
    extra_schema=article_schema(
        "Why We Contain Run-off Near Drains: An Explainer",
        "A short explainer on surface water drains versus foul sewers, and why containing pressure washing and roof cleaning run-off near drains is good practice.",
        "/images/gutter-downpipe.jpg",
    ),
    og_image="/images/gutter-downpipe.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Why We Contain Run-off Near Drains", "A quick explainer on something we mention on our service pages without always saying why.")}

<section class="wrap section reveal">
  <h2>Two different kinds of drain</h2>
  <p>Most UK properties have two separate drainage systems: foul sewers, which carry wastewater from sinks and toilets to a treatment works, and surface water drains, which carry rainwater (and anything else that goes down them) straight to a local river, stream or the sea — generally without any treatment in between. A road gully or a drain in a driveway or car park is almost always a surface water drain, not a foul one.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What that means for pressure washing and roof cleaning</h2>
    <p>Water carrying detergent, moss treatment or a concentration of whatever's been washed off a surface shouldn't be allowed to run straight down a surface water drain, because that drain leads directly to a natural watercourse rather than a treatment works. In practice that means being deliberate about where run-off goes on a job — working away from nearby gullies where possible, containing or diverting run-off when a drain is close by, and not treating "it'll wash away" as good enough near a drain specifically.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Where this shows up in how we work</h2>
  <p>It's why our <a href="/pressure-washing/">pressure washing</a> and <a href="/roof-cleaning/">roof cleaning</a> pages both mention run-off being contained where a job requires it, particularly near drains — it's not marketing language, it's a genuinely different way of working a job depending on whether there's a gully a few feet away or not. If you know there's a drain close to the area being cleaned, mentioning it on the quote form helps us plan for it rather than work it out on the day.</p>
</section>

<section class="wrap section reveal">
  <h2>Why the treatment matters too, not just where it goes</h2>
  <p>Containing run-off is one half of it; what's actually in the water is the other. Biodegradable treatments break down over time rather than persisting in a watercourse indefinitely, which is one of the reasons the treatment used matters as much as the method — a soft-wash treatment that isn't biodegradable would make containing run-off near drains even more important, not less, since it would take longer to stop being a concern once it did reach a watercourse. Both things — using a treatment designed to break down, and being careful about where run-off actually goes — are part of the same underlying approach, not separate concerns.</p>
</section>

<section class="wrap section reveal">
  <h2>What this looks like on an ordinary residential job</h2>
  <p>For most driveway or patio cleans, there's no drain close enough for this to change how the job is done at all — it only becomes a practical consideration on properties with a gully or road drain within a few feet of the area being cleaned, or on larger commercial forecourts and car parks where drainage is a bigger part of the site. On those jobs, it can mean working in a particular sequence, using drain covers temporarily, or simply being aware of where water is naturally flowing during the clean rather than treating it as an afterthought once the job is already underway.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-drains")}
</section>
""",
)

page(
    "/guides/block-paving-re-sanding-guide/",
    title="Block Paving Re-Sanding: Why & How Often | PB Softwash",
    description="Why block paving joints need re-sanding after a clean, what happens if you skip it, and roughly how often it needs doing on a typical Dorset driveway.",
    h1="Block Paving Re-Sanding: Why & How Often",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Block Paving Re-Sanding", None)],
    extra_schema=article_schema(
        "Block Paving Re-Sanding: Why & How Often to Do It",
        "Why block paving joints need re-sanding after a clean, what happens if you skip it, and roughly how often it needs doing on a typical Dorset driveway.",
        "/images/pressure-washing-steps.jpg",
    ),
    og_image="/images/pressure-washing-steps.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Block Paving Re-Sanding: Why & How Often", "The step that's easy to skip, and the one most likely to be missed by an inexperienced clean.")}

<section class="wrap section reveal">
  <h2>What the sand in the joints actually does</h2>
  <p>Block paving isn't a solid slab — it's individual blocks with sand-filled joints between them, and that sand is doing real structural work: it locks the blocks together so they don't shift under weight, and it stops water pooling by letting it drain down between blocks rather than sitting on the surface. Pressure washing, especially at too high a setting or held too close to the joints, can blast that sand straight out — which is the single most common way an inexperienced or rushed clean damages block paving.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What happens if joints are left empty</h2>
    <ul class="checklist">
      <li><strong>Weeds and moss move in</strong> — an empty joint is an easy place for seeds to establish, undoing the point of the clean fairly quickly.</li>
      <li><strong>Blocks start to shift</strong> under vehicle weight without sand locking them in place, which can lead to an uneven surface over time.</li>
      <li><strong>Ants and other insects nest in the gaps</strong>, which is a common complaint on driveways that have lost their jointing sand.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>How often it needs doing</h2>
  <p>Re-sanding isn't needed after every single clean — a driveway that's cleaned at a sensible pressure with the joints protected can go multiple cleans before the sand needs topping up. As a general guide, checking the joints every 12–24 months and topping up wherever sand has visibly dropped below the block surface keeps a driveway performing as intended. It's worth asking specifically whether re-sanding is included when you get a pressure washing quote — see our <a href="/guides/pressure-washing-driveway-cost-guide-uk/">driveway cost guide</a> — because it's a genuinely separate step that a lower quote may be skipping rather than including for free.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Is this something to DIY?</h2>
    <p>Kiln-dried jointing sand is available at most builders' merchants, and brushing it into clean, dry joints is genuinely a task most people can do themselves — the sand needs to go into properly clean, dry gaps for it to bind and settle correctly, which is really the only part that takes some care. The more common mistake is topping up sand over joints that still have moss or old, compacted sand in them, which stops the new sand from settling properly and means it washes or blows out again within weeks. If a driveway's just been cleaned, that's the right moment to re-sand — the joints are already clear.</p>
    <p>Some driveways benefit from a polymeric sand instead of plain kiln-dried sand — it sets harder once it's been dampened, which resists weed growth and washout better on a driveway with a slope or heavy vehicle use, though it costs more per bag and is less forgiving if it's applied incorrectly. For a typical flat residential driveway, standard kiln-dried sand topped up every year or two is usually all that's needed, and it's the option we'd suggest starting with unless there's a specific reason not to.</p>
  </div>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-resanding")}
</section>
""",
)

page(
    "/guides/north-facing-shaded-roofs-moss/",
    title="Why North-Facing Roofs Need Cleaning More | PB Softwash",
    description="Why a north-facing or heavily shaded roof slope grows moss faster than a south-facing one, and what that means for how often each side needs attention.",
    h1="Why North-Facing Roofs Need Cleaning More Often",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("North-Facing Roofs & Moss", None)],
    extra_schema=article_schema(
        "Why North-Facing Roofs Need Cleaning More Often",
        "Why a north-facing or heavily shaded roof slope grows moss faster than a south-facing one, and what that means for how often each side needs attention.",
        "/images/moss-covered-roof.jpg",
    ),
    og_image="/images/moss-covered-roof.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "Why North-Facing Roofs Need Cleaning More Often", "The same roof, two different moss problems, depending on which way each slope faces.")}

<section class="wrap section reveal">
  <h2>Shade and moisture, not just rain</h2>
  <p>Moss needs two things to establish: moisture, and enough shade that the surface doesn't dry out quickly between wet spells. Rain falls on every slope of a roof roughly equally, but sun exposure doesn't — in the UK, a north-facing slope receives direct sun for a much smaller part of the day than a south-facing one, especially through autumn and winter when the sun sits low in the sky. That means a north-facing slope can stay damp for days after rain that a south-facing slope on the same roof has already dried out from within hours.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>What this looks like in practice</h2>
    <ul class="checklist">
      <li>Visible moss concentrated on one side of a roof, with the opposite slope noticeably cleaner</li>
      <li>Valleys between roof sections — which get even less direct sun than a flat slope — often the first place moss establishes</li>
      <li>Roofs under mature trees showing the same pattern even more strongly, since shade from the tree compounds the aspect effect</li>
      <li>The effect is more pronounced in built-up or chine-side streets, where neighbouring buildings or tree cover add extra shade on top of the roof's own orientation</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>What it means for scheduling</h2>
  <p>It means a whole-roof clean doesn't need to happen on a single fixed schedule for every slope — a south-facing side might genuinely go two or three years between treatments while a shaded north-facing valley on the same roof needs attention every year. If you've only ever had moss on one side of the roof, that's not unusual, and it's not necessarily a sign the whole roof needs the same frequency of attention. See our <a href="/roof-cleaning/">roof cleaning page</a> for how soft washing handles this, or our <a href="/areas/bournemouth/">Bournemouth area page</a> for how chine-side tree cover adds to the same effect locally.</p>
</section>

<section class="wrap section reveal">
  <h2>Can anything be done structurally?</h2>
  <p>Overhanging branches are the one factor in this that's genuinely within a homeowner's control — trimming back a tree that's shading a roof slope won't change which direction it faces, but it does reduce the extra shade stacking on top of the aspect effect, and it cuts down the leaf litter reaching the gutters below at the same time. Beyond that, aspect itself can't be changed, which is really the point of this guide: it's not something gone wrong, it's a predictable pattern worth planning a cleaning schedule around rather than being surprised by every time.</p>
</section>

<section class="wrap section reveal">
  <h2>What this doesn't mean</h2>
  <p>It doesn't mean a north-facing roof is somehow a worse roof, or a bad sign about a property — it's simply orientation, and every roof has one. It's also not a reason to treat a north-facing slope with a harsher method to "catch up" faster; soft washing at the same low pressure applies regardless of which way a slope faces, since the roof covering itself doesn't become more tolerant of high pressure just because it's growing moss faster than the slope beside it.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-north-facing-roofs")}
</section>
""",
)

page(
    "/guides/how-to-spot-a-bad-pressure-washing-quote/",
    title="How to Spot a Bad Pressure Washing Quote | PB Softwash",
    description="Red flags to watch for in a UK pressure washing quote: pressure that's too high, no mention of re-sanding, vague pricing, and other signs to ask more questions.",
    h1="How to Spot a Bad Pressure Washing Quote",
    breadcrumbs=[("Home", "/"), ("Guides", "/guides/"), ("Spotting a Bad Quote", None)],
    extra_schema=article_schema(
        "How to Spot a Bad Pressure Washing Quote",
        "Red flags to watch for in a UK pressure washing quote: pressure that's too high, no mention of re-sanding, vague pricing, and other signs to ask more questions.",
        "/images/hero-pressure-washing.jpg",
    ),
    og_image="/images/hero-pressure-washing.jpg",
    body_html=f"""
{simple_hero("Guide · Published 18 August 2026", "How to Spot a Bad Pressure Washing Quote", "The cheapest number on the page isn't always the cheapest job in the end.")}

<section class="wrap section reveal">
  <h2>Why the lowest quote isn't automatically the best one</h2>
  <p>Pressure washing is fast to do badly and slower to do properly, and price alone doesn't tell you which one you're being quoted for. A contractor running maximum pressure over everything finishes faster — which can mean a lower price — but it's also the single most common way block paving joints get stripped and softer stone gets etched. The questions below are less about catching someone out and more about finding out which approach you're actually paying for.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Questions worth asking before you book</h2>
    <ul class="checklist">
      <li><strong>"What pressure and nozzle will you use on this surface?"</strong> A contractor who can't answer this, or says "the same on everything," is a warning sign.</li>
      <li><strong>"Is re-sanding included for block paving?"</strong> If it's not mentioned at all, it's worth asking directly — see our <a href="/guides/block-paving-re-sanding-guide/">re-sanding guide</a> for why this matters.</li>
      <li><strong>"How will run-off near drains be handled?"</strong> A contractor with a real answer to this has thought about the job, not just the sale.</li>
      <li><strong>"Is this price fixed, or does it depend on what you find on the day?"</strong> A quote that changes significantly once work starts, without a clear reason, is a common complaint.</li>
    </ul>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Other signs worth noticing</h2>
  <ul class="checklist">
    <li>A price given with no site visit, photo, or size/surface details at all — accurate pricing needs at least one of those</li>
    <li>No willingness to say what happens if something goes wrong (a cracked slab, a damaged plant bed)</li>
    <li>Pressure toward booking immediately rather than answering questions first</li>
  </ul>
  <p>None of this means the cheapest quote is automatically bad, or the most expensive automatically good — it means asking the same handful of questions of every quote you get, so you're comparing like for like rather than just comparing two numbers. See our <a href="/guides/pressure-washing-driveway-cost-guide-uk/">driveway cost guide</a> for what UK market pricing generally looks like, so you've got a baseline to compare against.</p>
</section>

<section class="band band-tint">
  <div class="band-inner reveal">
    <h2>Insurance and accountability</h2>
    <p>It's reasonable to ask whether a contractor carries public liability insurance before work starts on your property — not because damage is likely, but because it tells you what happens if something does go wrong, like a cracked slab or an accidentally soaked plant bed. A contractor who's uncomfortable being asked, or vague about the answer, is telling you something useful in itself. This is a fair question to ask of anyone quoting for exterior work, not just pressure washing.</p>
  </div>
</section>

<section class="wrap section reveal">
  <h2>Trusting your own read of the visit</h2>
  <p>Beyond the specific questions above, a lot comes down to ordinary judgement: did they actually look at the surface before quoting, or price it purely from a phone description? Did they ask what the surface is made of, or assume? A contractor who's genuinely engaging with the specifics of your driveway or roof, rather than reciting a standard pitch, is usually the one who ends up doing a job matched to what you actually have, not a generic version of it.</p>
</section>

<section class="section quote-section" id="quote">
  {lead_form("guide-bad-quotes")}
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
