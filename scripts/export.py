"""Builds public/recipes.json from data.py using the single density table in build.py."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import R
from build import grams, TIMES, render

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
            g, wi = [], None
            if tag.startswith('warn:'):
                _, rest = tag.split(':', 1)
                col, msg, ovr = rest.split('|')
                wi = sizes.index('1 lb'); warns.append(msg)
            for i, a in enumerate(amts):
                g.append(grams(ovr, key) + ' ⚠️' if i == wi else grams(a, key))
            o = [orig] if orig and len(amts) == 1 else amts
            rows.append({'n': label, 'g': g, 'o': [x or '—' for x in o], 'a': tag == 'addin'})
        secs.append({'t': title, 'i': rows})
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
        'sec': secs, 'st': r['steps'], 'no': r.get('notes', []), 'w': warns,
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
