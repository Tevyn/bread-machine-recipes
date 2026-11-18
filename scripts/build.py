import json, math, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import R

# ---------- density table: grams per US cup (King Arthur chart unless noted) ----------
CUP = {
    'water': 227, 'milk': 227, 'buttermilk': 227, 'cream': 227, 'sour_cream': 227, 'yogurt': 227,
    'butter': 227, 'olive_oil': 200, 'veg_oil': 198, 'honey': 336, 'maple': 312, 'molasses': 340,
    'sugar': 198, 'brown_sugar': 213, 'powdered_sugar': 113,
    'salt': 256,                      # Morton kosher: 16 g/tbsp
    'ap_flour': 120, 'bread_flour': 120, 'ww_flour': 113, 'rye_flour': 106, 'semolina': 163, 'oat_flour': 92,
    'brown_rice_flour': 128, 'white_rice_flour': 142, 'arrowroot': 128, 'tapioca': 113, 'quinoa_flour': 110,
    'cornstarch': 112, 'gf_blend': 131,  # booklet DIY blend weight
    'psyllium': 144,                  # 9 g/tbsp (NOW Foods label)
    'pectin': 196,                    # 12.25 g/tbsp (1.75 oz box ≈ 4 tbsp)
    'yeast': 148.8,                   # 3.1 g/tsp (KA: 2¼ tsp = 7 g)
    'baking_powder': 192, 'baking_soda': 288,
    'dry_milk': 112, 'cocoa': 84, 'potato_flakes': 86, 'flax': 100, 'wheat_germ': 112, 'wheat_bran': 64, 'oats': 89,
    'walnuts': 113, 'choc_chips': 170, 'choc_chopped': 170, 'raisins': 149, 'dried_cherries': 142, 'dried_fruit': 149,
    'cheddar': 113, 'parmesan': 100, 'olives': 142, 'mixed_nuts': 130, 'cereal_flakes': 40,
    'zucchini': 135, 'banana': 227, 'blueberries': 155, 'raspberries': 120,
    'strawberries': 113.4,            # booklet: 4 cups = 1 lb
    'jam': 340, 'sesame': 142, 'starter': 227,
    'lemon_juice': 227, 'lime_juice': 227, 'vanilla': 224, 'hot_sauce': 230,
}
TSP = {k: v / 48 for k, v in CUP.items()}
TSP.update({
    'cinnamon': 2.6, 'nutmeg': 2.2, 'anise': 2.1, 'fennel': 2.0, 'caraway': 2.1, 'pepper': 2.3, 'paprika': 2.3,
    'garlic_powder': 3.1, 'italian_herbs': 1.0, 'herbes_provence': 1.0, 'basil_dried': 0.7, 'oregano_dried': 1.0,
    'red_pepper': 1.8, 'orange_zest': 2.0, 'lime_zest': 2.0, 'ginger_fresh': 2.0, 'candied_ginger': 3.0,
    'rosemary': 0.6, 'fresh_herbs': 0.67, 'basil_fresh': 0.5, 'allspice': 1.9, 'onion_flakes': 2.0,
})
EACH = {'egg': 50, 'jalapeno': 14, 'garlic_clove': 5}
APPROX = {'cereal_flakes', 'mixed_nuts', 'olives', 'zucchini', 'blueberries', 'dried_fruit', 'choc_chopped',
          'starter', 'rosemary', 'fresh_herbs', 'basil_fresh', 'jalapeno', 'garlic_clove', 'candied_ginger',
          'ginger_fresh', 'gf_blend'}
UNIT_TSP = {'teaspoon': 1, 'tablespoon': 3, 'cup': 48}
WEIGHT = {'ounce': 28.35, 'pound': 453.6}
FR = {'½': .5, '¼': .25, '¾': .75, '⅓': 1/3, '⅔': 2/3, '⅛': .125}

def num(s):
    s = s.strip()
    total = 0.0
    m = re.match(r'^(\d+)?\s*([½¼¾⅓⅔⅛])?$', s)
    if m and (m.group(1) or m.group(2)):
        if m.group(1): total += int(m.group(1))
        if m.group(2): total += FR[m.group(2)]
        return total
    m = re.match(r'^(?:(\d+)\s+)?(\d+)/(\d+)$', s)
    if m:
        return (int(m.group(1)) if m.group(1) else 0) + int(m.group(2)) / int(m.group(3))
    raise ValueError(f"bad number {s!r}")

TERM = re.compile(r'^\s*([\d½¼¾⅓⅔⅛ /]+?)\s*(teaspoons?|tablespoons?|cups?|ounces?|pounds?|eggs?|chiles?)?\s*\*?\s*$')

def term_grams(t, key):
    m = TERM.match(t)
    if not m:
        return None
    n = num(m.group(1)); unit = (m.group(2) or '').rstrip('s')
    if unit in WEIGHT:
        return n * WEIGHT[unit]
    if unit in ('egg', 'chile', '') and key in EACH:
        return n * EACH[key]
    if unit in UNIT_TSP:
        if key not in TSP:
            raise KeyError(f"no density for {key}")
        return n * UNIT_TSP[unit] * TSP[key]
    return None

def fmt(g, approx=False):
    # Round half up (Python's round() goes half-to-even, so 12.5 showed as 12).
    tenths = math.floor(g * 10 + 0.5) / 10
    s = f"{tenths:.1f} g" if tenths < 10 else f"{math.floor(g + 0.5)} g"
    return ("~" + s) if approx else s

def grams(amt, key):
    """returns display string for the gram column"""
    a = amt.strip()
    if key == 'none':
        return 'as needed' if not a else ('all of it' if a == 'all' else a)
    if not a:
        return '—'
    low = a.lower()
    if 'pinch' in low:
        return low.replace(' to ', '–')
    # ranges: "1 to 2 tablespoons"
    m = re.match(r'^(\S+) to (\S+) (.+)$', a)
    if m:
        g1 = term_grams(f"{m.group(1)} {m.group(3)}", key); g2 = term_grams(f"{m.group(2)} {m.group(3)}", key)
        if g1 is None:
            return a.replace(' to ', '–')
        return f"{fmt(g1).replace(' g','')}–{fmt(g2)}"
    parts = re.split(r'\s*(?:\+|plus)\s*', a)
    tot = 0.0
    for p in parts:
        g = term_grams(p, key)
        if g is None:
            return a  # leave as text (e.g. "1 loaf", "1 recipe")
        tot += g
    s = fmt(tot, key in APPROX)
    if key == 'egg':
        n = round(tot / 50)
        return f"{n} egg{'s' if n != 1 else ''} · {s}"
    if key == 'jalapeno':
        return f"{a} · {s}"
    if key == 'garlic_clove':
        return f"{a} cloves · {s}"
    return s

def note_esc(n):
    m = re.match(r'^(\*+)(.*)$', n, re.S)
    return ('\\*' * len(m.group(1)) + m.group(2)) if m else n

def esc(s):
    return s.replace('*', '\\*')

# ---------- program metadata ----------
TIMES = {
    'White': ({'2 lb': '3:30', '1½ lb': '3:25', '1 lb': '3:18'}, 210, '≈40 min in', '≈1 h 15 min in'),
    'French': ({'2 lb': '4:20', '1½ lb': '4:15', '1 lb': '4:05'}, 260, '≈1 h 15 min in', '≈1 h 55 min in'),
    'Whole Wheat': ({'2 lb': '4:10', '1½ lb': '4:05', '1 lb': '3:57'}, 250, '≈50 min in', '≈1 h 35 min in'),
    'Sweet': ({'1½ lb': '3:20', '1 lb': '3:15'}, 200, '30 min in', '1 h 10 min in'),
    'Gluten Free': ({'1½ lb': '2:15', '2 lb dough': '2:15'}, 135, '20 min in', '35 min in'),
    'Artisan Dough': ({'1½ lb': '5:05'}, 305, None, None),
    'Dough': ({'Batch': '1:30'}, 90, None, None),
    'Jam': ({'Batch': '1:20'}, 80, None, None),
    'Cake': ({'Batch': '1:52'}, 112, None, None),
    'No machine': ({}, None, None, None),
}
ICON = {
    'Basic White Bread': '🍞', 'Oatmeal Bread': '🥣', 'Cinnamon Swirl Bread': '🌀', 'Rye Bread': '🍞',
    'Jalapeño Cheddar Bread': '🌶️', 'French Bread Loaf': '🥖', 'King Arthur-Style French Bread': '🥖', 'Rustic Italian Loaf': '🥖',
    'Country French Bread with Olives & Rosemary': '🫒', 'Parmesan Peppercorn French Bread': '🧀',
    'Semolina Bread with Fennel & Golden Raisins': '🌾', 'Basic Whole Wheat Bread': '🌾',
    'Multigrain Cereal Wheat Bread': '🌾', 'Nutty Whole Wheat Bread': '🥜', 'Wheat Bran Bread': '🌾',
    'Challah Loaf': '🍞', 'Brioche Loaf': '🧈', 'Panettone Loaf': '🍊', 'Chocolate Cherry Loaf': '🍒',
    'Babka': '🍫', 'Gluten-Free Sandwich Bread': '🥪', 'Gluten-Free Multigrain Bread': '🌱',
    'Gluten-Free Cinnamon Swirl Bread': '🌀', 'Gluten-Free Pizza Dough': '🍕', 'Sourdough Starter': '🫙',
    'Sourdough Loaf and Boule': '🥖', 'Ciabatta': '🥖', 'French Baguettes': '🥖', 'Cheddar Breadsticks': '🧀',
    'Pizza Dough': '🍕', 'Herb Focaccia': '🌿', 'Pretzels': '🥨', 'Whole Wheat Kalamata Rolls': '🫒',
    'Garlic, Herb and Cheese Knots': '🧄', 'Cinnamon Swirl Rolls': '🌀', 'Basic Sweet Dough': '🥐',
    'Raspberry Cheese Danish': '🥮', 'Strawberry Rhubarb Jam': '🍓', 'Pear & Ginger Preserves': '🍐',
    'Blueberry Lime Jam': '🫐', 'Mixed Berry Jam': '🍇', 'Banana Walnut Bread': '🍌',
    'Sour Cream Chocolate Bread': '🍫', 'Zucchini Bread': '🥒', 'Breadcrumbs': '🍞', 'Croutons': '🥗',
    'Challah French Toast': '🍳', 'Berry Brioche Bread Pudding': '🍮', 'Pizza Margherita': '🍕',
}
DAIRY = {'milk', 'buttermilk', 'cream', 'sour_cream', 'yogurt', 'butter', 'dry_milk', 'cheddar', 'parmesan',
         'cream_cheese', 'mozzarella', 'choc_chopped', 'choc_chips', 'ref_white', 'ref_challah', 'ref_brioche', 'ref_sweet_dough'}
EGG = {'egg', 'ref_challah', 'ref_brioche', 'ref_sweet_dough'}
HONEY = {'honey', 'ref_pizza'}
GLUTEN = {'ap_flour', 'bread_flour', 'ww_flour', 'rye_flour', 'semolina', 'wheat_bran', 'wheat_germ', 'cereal_flakes',
          'ref_white', 'ref_challah', 'ref_brioche', 'ref_sweet_dough', 'ref_pizza', 'starter', 'oats'}

def render(r, urls):
    sizes = r['sizes']; multi = len(sizes) > 1
    prog = r['program']
    times, mins, addin_t, paddle_t = TIMES[prog]
    keys = {it[1] for _, items in r['sections'] for it in items}

    # ----- summary callout -----
    lines = []
    if prog == 'No machine':
        lines.append(f"**No bread machine needed** · Yield: {r.get('yield_')}")
    else:
        head = f"**{prog} program**"
        if prog in ('White', 'Whole Wheat', 'Sweet'):
            head += " · choose crust + size"
        elif prog == 'French':
            head += " · choose size (no crust setting)"
        head += f" · Delay start: {r['delay']}"
        lines.append(head)
        if multi:
            tt = " · ".join(f"{times[s]} ({s})" for s in sizes if s in times)
        else:
            tt = r.get('machine_note') or times.get(sizes[0], list(times.values())[0])
            y = r.get('yield_') or ''
            if y.startswith('One '): y = 'one ' + y[4:]
            tt = f"{tt}" + (f" · makes {y}" if y else "")
        lines.append(f"Machine time: {tt}")
        if addin_t and ('Add-ins at beep' in r['attention'] or 'Fill & roll at paddle beep' in r['attention'] or prog in ('White','French','Whole Wheat','Sweet','Gluten Free')):
            bits = []
            if 'Add-ins at beep' in r['attention']:
                bits.append(f"add-in beep {addin_t}")
            bits.append(f"paddle beep {paddle_t}")
            lines.append("Beeps: " + " · ".join(bits))
    links = r.get('links', [])
    if links:
        ms = []
        for n in links:
            u = urls.get(n)
            ms.append(f'<mention url="{u}">{n}</mention>' if u else n)
        lines.append("Uses: " + ", ".join(ms))
    out = [f'<callout icon="⚙️" color="gray_bg">\n' + "\\\n".join(lines) + "\n</callout>", ""]

    # ----- gram tables -----
    out.append("## Ingredients (grams)")
    out.append("")
    if prog not in ('No machine', 'Jam', 'Cake') and r['typ'] != 'Starter':
        out.append("Load in this order: liquids first, then dry, then yeast last in a small well in the flour.")
        out.append("")
    warns = []
    has_addin = False
    for title, items in r['sections']:
        if title:
            out.append(f"### {title}")
            out.append("")
        if multi:
            out.append("| Ingredient | " + " | ".join(sizes) + " |")
            out.append("|---" * (len(sizes) + 1) + "|")
        else:
            out.append("| Ingredient | Grams |")
            out.append("|---|---|")
        for label, key, amts, tag, orig in items:
            cells = []
            wcol = None; woverride = None
            if tag.startswith('warn:'):
                _, rest = tag.split(':', 1)
                col, msg, ovr = rest.split('|')
                wcol = sizes.index({'1lb': '1 lb', '1.5lb': '1½ lb', '2lb': '2 lb'}[col]); woverride = ovr
                warns.append(msg)
            for i, a in enumerate(amts):
                if i == wcol:
                    cells.append(grams(woverride, key) + " ⚠️")
                else:
                    cells.append(grams(a, key))
            lab = esc(label)
            if tag == 'addin':
                has_addin = True
                lab = f"⏰ **{lab}**"
            out.append(f"| {lab} | " + " | ".join(cells) + " |")
        out.append("")
    if has_addin:
        out.append(f"⏰ = hold back; add at the **add-in beep** ({addin_t}).")
        out.append("")
    for w in warns:
        out.append(f'<callout icon="⚠️" color="yellow_bg">\n{w}\n</callout>')
        out.append("")

    # ----- steps -----
    out.append("## Steps")
    out.append("")
    for i, s in enumerate(r['steps'], 1):
        out.append(f"{i}. {s}")
    out.append("")

    if r.get('ultrafast'):
        out.append("<toggle>⚡ Ultra-Fast version (1 lb & 1½ lb loaves only)\n\n"
                   "Use the 1 lb or 1½ lb amounts, but swap the yeast for **rapid-rise yeast**: **5.4 g** (1¾ tsp) for 1 lb, or **7.8 g** (2½ tsp) for 1½ lb. "
                   "Select **Ultra-Fast** (1:53 for 1 lb, 2:03 for 1½ lb), press START/STOP, then continue from step 3. "
                   "The beeps come much sooner: add-ins ≈13 min in, paddle ≈18 min in.\n</toggle>")
        out.append("")

    notes = r.get('notes', [])
    if notes:
        out.append('<callout icon="📝" color="blue_bg">\n' + "\\\n".join(note_esc(n) for n in notes) + "\n</callout>")
        out.append("")

    # ----- original drawer -----
    out.append("---")
    out.append("")
    dr = ["<toggle>📏 Original measurements (cups & spoons" + ("" if r.get('source') else ", as printed in the booklet") + ")", ""]
    for title, items in r['sections']:
        if title:
            dr.append(f"**{esc(title)}**")
            dr.append("")
        if multi:
            dr.append("| Ingredient | " + " | ".join(sizes) + " |")
            dr.append("|---" * (len(sizes) + 1) + "|")
            for label, key, amts, tag, orig in items:
                dr.append(f"| {esc(label)} | " + " | ".join(amts) + " |")
        else:
            dr.append("| Ingredient | Amount |")
            dr.append("|---|---|")
            for label, key, amts, tag, orig in items:
                amt = esc(orig) if orig else (amts[0] if amts[0] else "as needed")
                dr.append(f"| {esc(label)} | {amt} |")
        dr.append("")
    if r.get('orig_extra'):
        dr.append(r['orig_extra']); dr.append("")
    dr.append(f"Nutrition: {r['nutrition']}")
    dr.append("")
    dr.append(f"Source: {r['source']}" if r.get('source') else f"Source: Cuisinart CBK-110 Instruction & Recipe Booklet, p. {r['page']}.")
    dr.append("</toggle>")
    out.append("\n".join(dr))
    content = "\n".join(out)

    # ----- properties -----
    diet = []
    if not (keys & GLUTEN): diet.append('Gluten-free')
    if not (keys & EGG): diet.append('Egg-free')
    if not (keys & DAIRY): diet.append('Dairy-free')
    if not (keys & (EGG | DAIRY | HONEY)): diet.append('Vegan')
    loaf = [s for s in sizes if s in ('1 lb', '1½ lb', '2 lb')]
    props = {
        'Name': r['name'],
        'Program': prog,
        'Type': r['typ'],
        'Loaf sizes': loaf,
        'Yield': r.get('yield_') or ("Loaf: " + ", ".join(sizes)),
        'Delay start': r['delay'],
        'Ultra-Fast option': '__YES__' if r.get('ultrafast') else '__NO__',
        'Hands-on': r['attention'],
        'Flavor': r['flavor'],
        'Key ingredients': r['keyings'],
        'Dietary': diet,
        'Booklet page': None if r.get('source') else r['page'],
    }
    mins = r.get('machine_min', mins)
    if mins: props['Machine time (min)'] = mins
    return {'name': r['name'], 'icon': ICON[r['name']], 'properties': props, 'content': content}

if __name__ == '__main__':
    urls = {}
    up = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'urls.json')
    if os.path.exists(up):
        urls = json.load(open(up, encoding='utf-8'))
    pages = [render(r, urls) for r in R]
    od = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
    os.makedirs(od, exist_ok=True)
    json.dump(pages, open(os.path.join(od, 'pages.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for p in pages:
        open(os.path.join(od, re.sub(r'[^A-Za-z0-9]+', '_', p['name']) + '.md'), 'w', encoding='utf-8').write(p['content'])
    print(len(pages), "pages;", sum(len(p['content']) for p in pages), "chars")
