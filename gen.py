import os

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">'

STYLE = """<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root { --cream: #f9f7f3; --ink: #1a1a18; --muted: #7a7a72; --border: #e0ddd8; --accent: #8b3a2a; }
  body { font-family: 'Jost', sans-serif; background: var(--cream); color: var(--ink); font-weight: 300; }
  nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; display: flex; justify-content: space-between; align-items: center; padding: 1.4rem 3rem; background: rgba(249,247,243,0.92); backdrop-filter: blur(8px); border-bottom: 1px solid var(--border); }
  .nav-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; text-decoration: none; color: var(--ink); }
  .nav-links { display: flex; gap: 2.5rem; list-style: none; }
  .nav-links a { font-size: 0.75rem; letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none; color: var(--muted); transition: color 0.2s; }
  .nav-links a:hover { color: var(--ink); }
  .hero { padding-top: 120px; padding-bottom: 3rem; max-width: 900px; margin: 0 auto; padding-left: 2rem; padding-right: 2rem; }
  .back-link { font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem; margin-bottom: 2.5rem; }
  .back-link:hover { color: var(--ink); }
  .trip-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(2.5rem, 7vw, 5.5rem); font-weight: 300; line-height: 1; letter-spacing: -0.01em; margin-bottom: 0.75rem; }
  .trip-meta { font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted); margin-bottom: 1.5rem; }
  .route { font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-style: italic; color: var(--muted); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 1rem 0; margin-bottom: 3rem; }
  .route span { color: var(--accent); }
  .content { max-width: 900px; margin: 0 auto; padding: 0 2rem 5rem; }
  .city-section { margin-bottom: 4rem; padding-bottom: 4rem; border-bottom: 1px solid var(--border); }
  .city-section:last-child { border-bottom: none; }
  .city-name { font-family: 'Cormorant Garamond', serif; font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 400; margin-bottom: 1.5rem; }
  .takeaways { background: #fff; border: 1px solid var(--border); padding: 1.5rem 2rem; margin-bottom: 2rem; }
  .takeaways-title { font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--accent); margin-bottom: 1rem; }
  .takeaways ul { list-style: none; }
  .takeaways li { font-size: 0.95rem; line-height: 1.7; padding: 0.5rem 0; border-bottom: 1px solid var(--border); padding-left: 1rem; position: relative; }
  .takeaways li::before { content: '—'; position: absolute; left: 0; color: var(--accent); }
  .takeaways li:last-child { border-bottom: none; }
  .city-text { font-size: 1rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--ink); }
  .placeholder-note { font-size: 0.85rem; color: var(--muted); font-style: italic; padding: 2rem; background: #f0ede8; border: 1px dashed var(--border); text-align: center; }
  footer { text-align: center; padding: 2.5rem; font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); border-top: 1px solid var(--border); }
  @media (max-width: 600px) { nav { padding: 1rem 1.5rem; } .hero { padding-left: 1.5rem; padding-right: 1.5rem; } .content { padding-left: 1.5rem; padding-right: 1.5rem; } }
</style>"""

NAV = """<nav>
  <a class="nav-brand" href="../index.html">Brodie Trips</a>
  <ul class="nav-links">
    <li><a href="../index.html">Home</a></li>
    <li><a href="../index.html#trips">Trips</a></li>
    <li><a href="../cocktails/index.html">Cocktails</a></li>
  </ul>
</nav>"""

def page(title, year, meta, route, body, filename):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Brodie Trips</title>
{FONTS}
{STYLE}
</head>
<body>
{NAV}
<div class="hero">
  <a class="back-link" href="../index.html">← All Trips</a>
  <h1 class="trip-title">{title}</h1>
  <div class="trip-meta">{meta}</div>
  {f'<div class="route">{route}</div>' if route else ''}
</div>
<div class="content">
{body}
</div>
<footer>&copy; The Brodies &nbsp;&middot;&nbsp; Adventures around the world</footer>
</body>
</html>"""
    path = f"/home/claude/brodies/trips/{filename}"
    with open(path, 'w') as f:
        f.write(html)
    print(f"Created {filename}")

def city(name, takeaways=None, text=None):
    out = f'<div class="city-section">\n<h2 class="city-name">{name}</h2>\n'
    if takeaways:
        items = ''.join(f'<li>{t}</li>' for t in takeaways)
        out += f'<div class="takeaways"><div class="takeaways-title">Quick Takeaways</div><ul>{items}</ul></div>\n'
    if text:
        for p in text:
            out += f'<p class="city-text">{p}</p>\n'
    out += '</div>\n'
    return out

def placeholder(name):
    return f'<div class="city-section"><h2 class="city-name">{name}</h2><div class="placeholder-note">Photos and notes coming soon.</div></div>\n'

# ---- LONDON 2022 ----
london_body = city("London", takeaways=[
    "Stay in Covent Garden — great neighborhood especially for your first time in the city",
    "Take a bicycle tour — we booked the Classic London Landmarks Bicycle Tour with Viator",
    "Eat at one of Ottolenghi's restaurants (book way in advance) — we loved NOPI",
    "Dishoom in Covent Garden: gorgeous restaurant, great food, book reservation way in advance",
    "Visit Sky Garden — it's free but you need reservations (skygarden.london)",
    "Portobello Market is a must, and so is The Distillery where they make Portobello Gin (the-distillery.london)",
    "Take advantage of the free museums",
    "No need for a metro card — use your credit card to get in and out of the subway for the same cost",
    "Fentiman Arms (64 Fentiman Road) — best pub food ever, great atmosphere",
    "Seven Dials Market (35 Earlham St) — fun multi-level food court with dozens of micro-restaurants",
    "Anita Gelato (4 Upper St. Martins Lane) — really good gelato",
    "Cafe Nata (25 Old Compton St) — a little taste of Portugal",
    "Maison Bertaux (28 Greek St) — amazing scones",
    "Cocktail making class at The Alchemist — so fun!",
    "SUSHISAMBA — highest outdoor dining terrace in Europe, 38th & 39th floors of Heron Tower",
    "Black Friar (174 Queen Victoria St) — stumbled across it, very cool interior and exterior",
    "Tower of London: take a free Beefeater tour, use the Middle Drawbridge entrance to avoid crowds",
], text=[
    "We stayed in an Airbnb in Covent Garden — a great neighborhood especially for a first visit to the city.",
    "Our guide on the Viator bike tour was fantastic. Best way to see the city — we caught the Changing of the Guards along the way.",
    "Charlotte's friend who lived in London shared a great insider list: <a href='https://docs.google.com/document/d/1r7wTG2aMWiRx9oNS9619ifqgbh4QW5tGO8A5Cef-KgA/edit' style='color:var(--accent)'>view it here</a>.",
    "Ottolenghi's restaurant NOPI: amazing food, drinks, and a crazy mirrored bathroom. Book way in advance.",
    "The Distillery at Portobello Market — Roger our bartender taught us everything about gin and lined up shots for taste testing.",
    "Our Beefeater at the Tower was the first woman to hold that position. She was fabulous!",
])

page("London", "2022", "England · 2022", "", london_body, "london-2022.html")

# ---- SPAIN & PORTUGAL 2022 ----
sp_body = city("Madrid", text=[
    "Church of Saint Jerome the Royal is situated beautifully between the Prado and Retiro Park.",
    "Bodega de los Secretos — a cool wine cellar transformed into a restaurant near our Airbnb. In the 17th century it was at the border of Madrid; restorers found 3 clandestine passageways used to smuggle goods and escape troops during the Napoleonic Wars and Spanish Civil War. The duck was amazing!",
    "Mercado San Miguel — so fun! We are not beer drinkers but LOVED cerveza limón.",
])
sp_body += city("Toledo", takeaways=[
    "If driving to Toledo, stop at the Mirador del Valle overlook on Carretera de Circunvalación — fabulous view of the city, and there's a restaurant for drinks and snacks",
    "The cathedral and audio guide are a must — there are two lines, one for tickets and one for the free audio guide. Bring headphones or they charge you",
    "You MUST eat at Botero — best meal ever! Make reservations early, it books up quickly",
], text=[
    "Toledo Cathedral was begun in 1226 under Ferdinand III and built on top of a Muslim mosque. A magnificent example of medieval Gothic architecture.",
    "We stayed at 'The Cave' Airbnb — an incredible spot in the old city.",
])
sp_body += city("Granada", takeaways=[
    "Om Kalsum at C. Jardines, 17 — wonderful small restaurant serving Moroccan & Middle Eastern tapas. Order the meatballs!",
    "Only city left in Spain where you get a free tapa with each drink you order",
    "Stayed at 'The Lover's Workshop' at C. San Juan de los Reyes, 80 in the old Moorish quarter near the Alhambra — getting there with luggage was tough through the winding cobblestone streets",
])
sp_body += city("Cordoba", text=["Photos and notes — beautiful historic city center."])
sp_body += city("Ardales", text=["A stunning natural park — photos tell the story."])
sp_body += city("Ronda", takeaways=[
    "Our favorite small city in Spain",
    "Las Maravillas at Carrera Espanel, 12 — yummy paella, view from our back deck was incredible",
    "Tragatá at Calle Nueva, 4 — highly recommended but closed the night we were there. Will have to go back!",
])
sp_body += city("Sevilla", takeaways=[
    "Alcazar — a must see, bring a bag lunch to eat in the gardens. We thought it was even more impressive than the one in Granada",
    "Mercado El Postigo — an art market on C. Arfe, perfect place to buy gifts",
    "La Brunilda Restaurant — be sure to make a reservation",
    "Bar Alfalfa — tiny restaurant on C. Candilejo with great vibe and good food",
    "You must see a flamenco show — we got tickets to La Casa de Flamenco, a 15th-century home-turned flamenco theater",
    "SEEBYBIKE Tours — a bike tour is a great way to cover a lot of ground in this big city, our guide was fantastic",
])
sp_body += city("Algarve, Portugal", takeaways=[
    "Boat ride of caves is a must — make sure the boat is small with rubber sides so you can go inside the caves, or better yet kayak. We used AllBoats",
    "Albufeira was convenient (walk to the marina) but touristy — wouldn't strongly recommend the town itself",
    "If you end up in Albufeira, have a meal at Prazeres",
    "Tavira is a small town on the coast definitely worth a visit",
    "Bar Portas da Villa — fun place to stop for a drink, owner decorated exterior and interior with shells collected from the beach",
])
sp_body += city("Lisboa", text=[
    "The end point of a spectacular road trip through Spain and Portugal. Lisboa (Lisbon) deserves its own extended stay.",
])

route_sp = "Madrid <span>··</span> Toledo <span>··</span> Granada <span>··</span> Córdoba <span>··</span> Ardales <span>··</span> Ronda <span>··</span> Sevilla <span>··</span> Albufeira <span>··</span> Lisboa"
page("Spain & Portugal", "2022", "2022", route_sp, sp_body, "spain-portugal-2022.html")

# ---- SPAIN 2019 ----
sp19_body = city("Madrid", takeaways=[
    "Stayed at the Generator Hostal — stylish hostal with a rooftop deck at the corner of Calle de Silva and Calle de San Bernardo",
    "Mercado de San Miguel — a must",
    "Chocolatería San Ginés (Pasadizo de San Ginés, 5) — great churros",
    "Tapas everywhere: Iberian ham, croquetas (deep fried cheese)",
])
sp19_body += city("Segovia", text=["The famous Roman aqueduct, the Alcázar, and incredible roast suckling pig — a stunning day trip from Madrid."])
sp19_body += city("Salamanca", text=["One of the most beautiful university cities in Spain. The golden sandstone buildings glow at sunset."])
sp19_body += city("The Castle — Castillo del Buen Amor", text=["Our hotel: the remarkable Castillo del Buen Amor, a 15th-century castle turned luxury hotel between Salamanca and the Portuguese border."])
sp19_body += city("Picos de Europa", text=["Spectacular mountain national park in northern Spain — incredible hiking and scenery."])
sp19_body += city("Alquezar", text=["A stunning medieval village perched above a river gorge in Aragon. One of Spain's most picturesque hidden gems."])

route_sp19 = "Madrid <span>··</span> Segovia <span>··</span> Salamanca <span>··</span> Picos de Europa <span>··</span> Alquézar"
page("Spain", "2019", "2019", route_sp19, sp19_body, "spain-2019.html")

# ---- THAILAND & CAMBODIA 2023 ----
tc_body = city("Bangkok", takeaways=[
    "Hire a tuk tuk driver for the day — have them take you to the different temples and wait while you explore",
    "Don't shy away from using the SkyTrain — it's really easy to figure out",
])
tc_body += city("Chiang Mai", takeaways=[
    "Do not miss hiking the Monk's Trail to Wat Pha Lat",
    "If you arrive on Sunday, don't miss the Sunday Night Market (Tha Pae Walking Market) — the largest of the week, starts at 4pm until 10:30pm",
    "Smaller market Saturday nights; the Night Bazaar takes place every night",
])
tc_body += city("Elephant Nature Park", text=[
    "Elephant Nature Park is truly a magical place and a must see! Located about an hour north of Chiang Mai, it's home to not only elephants but hundreds of other animals in need of rescue.",
    "It was established by Saengduean Chailert (Lek), a famous elephant rights advocate — we even got to meet and talk with her while there!",
    "The park has rescued elephants who were once subjected to cruel practices such as street begging, riding, and circus shows. It felt like we were in Jurassic Park as the elephants and other animals wander free.",
    "We did the overnight stay and highly recommend it. Rooms were clean (fans, no A/C), food was good. The second day was the best — we hiked into the mountains, just the three of us and our guide, and saw many elephants in their natural habitat.",
])

route_tc = "Bangkok <span>··</span> Chiang Mai <span>··</span> Elephant Nature Park"
page("Thailand & Cambodia", "2023", "Southeast Asia · 2023", route_tc, tc_body, "thailand-cambodia-2023.html")

# ---- GREECE 2014 ----
greece_body = '<div class="placeholder-note">Photos and notes from Greece 2014 coming soon.</div>'
page("Greece", "2014", "2014", "", greece_body, "greece-2014.html")

# ---- NEW TRIPS (placeholders) ----
new_trips = [
    ("Oxford", "2026", "England · 2026", "", "oxford-2026.html"),
    ("Memphis", "2026", "Tennessee · 2026", "", "memphis-2026.html"),
    ("London, Oxford & Paris", "2025", "UK & France · 2025", "London <span>··</span> Oxford <span>··</span> Paris", "london-oxford-paris-2025.html"),
    ("Florence & Rome", "2025", "Italy · 2025", "Florence <span>··</span> Rome", "florence-rome-2025.html"),
    ("Girls Trip — Utah", "2025", "USA · 2025", "", "utah-2025.html"),
    ("Switzerland & Sweden", "2025", "Europe · 2025", "Switzerland <span>··</span> Sweden", "switzerland-sweden-2025.html"),
    ("Charleston", "2025", "South Carolina · 2025", "", "charleston-2025.html"),
    ("Cambodia", "2024", "Southeast Asia · 2024", "", "cambodia-2024.html"),
    ("Ireland", "2024", "2024", "", "ireland-2024.html"),
    ("Puerto Rico", "2023", "2023", "", "puerto-rico-2023.html"),
]

for title, year, meta, route, filename in new_trips:
    body = f'<div class="placeholder-note">Notes and photos from {title} {year} coming soon. Check back!</div>'
    page(title, year, meta, route, body, filename)

print("All pages generated!")
