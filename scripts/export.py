"""Builds public/recipes.json from data.py using the single density table in build.py."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import R
from build import grams, TIMES, render, term_grams
from steps import STEPS, WARN, ULTRA

FLOUR = {'ap_flour', 'bread_flour', 'ww_flour', 'rye_flour', 'semolina', 'oat_flour', 'brown_rice_flour',
         'white_rice_flour', 'arrowroot', 'tapioca', 'quinoa_flour', 'gf_blend'}
NOT_DOUGH = ('swirl', 'filling', 'glaze', 'topping', 'frosting', 'rolled in', 'seasoning', 'shaping', 'dip',
             'assembly', 'pan', 'daily feed', 'refresh', 'seasoned')

def gnum(amt, key):
    a = amt.strip()
    if not a or key == 'none' or 'pinch' in a.lower() or ' to ' in a:
        return None
    tot = 0.0
    for p in re.split(r'\s*(?:\+|plus)\s*', a):
        g = term_grams(p, key)
        if g is None:
            return None
        tot += g
    return round(tot, 2)

def dough_section(title):
    # Ignore parenthetical asides so "Dough (goes in the pan)" isn't caught by 'pan'.
    head = re.sub(r'\s*\(.*?\)', '', title or '').lower()
    return not title or not any(w in head for w in NOT_DOUGH)

WARN_COL = {'1lb': '1 lb', '1.5lb': '1½ lb', '2lb': '2 lb'}

BEEPS = {  # elapsed h:mm
    'White': ('0:40', '1:15'), 'French': ('1:15', '1:55'), 'Whole Wheat': ('0:50', '1:35'),
    'Sweet': ('0:30', '1:10'), 'Gluten Free': ('0:20', '0:35'),
}

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower().replace('ñ', 'n')).strip('-')

def recipe(r):
    sizes = r['sizes']
    times, mins, _, _ = TIMES[r['program']]
    secs, warns = [], []
    for title, items in r['sections']:
        rows = []
        for label, key, amts, tag, orig in items:
            g, ovr = [], {}
            if tag.startswith('warn:'):
                # warn:<col>[;<col>...]|<msg>|<override>[;<override>...]
                _, rest = tag.split(':', 1)
                cols, msg, ovrs = rest.split('|')
                ovr = {sizes.index(WARN_COL[c]): v for c, v in zip(cols.split(';'), ovrs.split(';'), strict=True)}
                w = WARN[r['name']]
                warns += [x for x in ([w] if isinstance(w, str) else w) if x not in warns]
            for i, a in enumerate(amts):
                g.append(grams(ovr[i], key) + ' †' if i in ovr else grams(a, key))
            o = [orig] if orig and len(amts) == 1 else amts
            gn = [gnum(ovr.get(i, a), key) for i, a in enumerate(amts)]
            fl = 1 if key in FLOUR else 0.5 if key == 'starter' else 0
            rows.append({'n': label, 'g': g, 'o': [x or '—' for x in o], 'a': tag == 'addin',
                         'gn': gn, 'fl': fl, 'top': tag == 'top'})
        secs.append({'t': title, 'i': rows, 'bp': dough_section(title)})
    keys = {it[1] for _, items in r['sections'] for it in items}
    lb = [s for s in sizes if s in ('1 lb', '1½ lb', '2 lb')]
    att = r['attention']
    b = BEEPS.get(r['program'])
    meta = {
        'time': {s: times[s] for s in sizes if s in times} or ({'*': list(times.values())[0]} if times else {}),
        'add': b[0] if b and 'Add-ins at beep' in att else None,
        'paddle': b[1] if b and 'Fill & roll at paddle beep' in att else None,
        'delay': r['delay'],
    }
    if r.get('machine_note'):
        meta['time'] = {'*': r['machine_note']}
    return {
        'id': slug(r['name']), 'n': r['name'], 'p': r['program'], 't': r['typ'],
        'm': r.get('machine_min', mins), 'pg': r['page'], 'y': r.get('yield_'),
        'sz': lb, 'cols': sizes, 'meta': meta, 'uf': bool(r.get('ultrafast')),
        'sec': secs, 'st': STEPS[r['name']], 'ux': ULTRA if r.get('ultrafast') else None, 'no': r.get('notes', []), 'w': warns,
        'h': att, 'f': r['flavor'], 'd': render(r, {})['properties']['Dietary'],
    }

if __name__ == '__main__':
    out = [recipe(r) for r in R]
    ids = [x['id'] for x in out]
    assert len(ids) == len(set(ids)), 'duplicate ids'
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public', 'recipes.json')
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(',', ':'))
    print(len(out), 'recipes ->', os.path.normpath(p), os.path.getsize(p), 'bytes')
