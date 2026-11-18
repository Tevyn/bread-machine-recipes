(() => {
  const app = document.getElementById('app');
  const SIZES = ['1 lb', '1½ lb', '2 lb'];
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
  };
  const st = {
    size: store.get('size', '1½ lb'),
    sort: store.get('sort', { k: 'pg', dir: 1 }),
    f: store.get('f', { p: '', t: '', d: '' }),
  };
  let R = [];
  let lock = null;

  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const md = s => {
    const m = /^(\*+)/.exec(s); const pre = m ? m[1] : ''; let t = esc(s.slice(pre.length));
    t = t.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\*(.+?)\*/g, '<i>$1</i>');
    return pre + t;
  };

  const short = n => n
    .replace(/,? room temperature/g, '').replace(/, cut into ½-inch pieces/, '').replace(/,? (and )?cubed/, '')
    .replace(/ \(active dry, instant or bread machine\)/, '').replace(/^Unbleached all-purpose/, 'All-purpose')
    .replace(/, pitted, drained, patted dry, halved/, '').replace(/, seeded and finely chopped/, '');
  const secTitle = t => t.replace(/ \(.*\)$/, '');

  // which column of a recipe to show for the chosen size
  function col(r) {
    if (!r.sz.length) return { i: 0, label: '', off: false };
    let i = r.cols.indexOf(st.size);
    if (i >= 0) return { i, label: st.size, off: false };
    const want = SIZES.indexOf(st.size);
    let best = 0, bd = 9;
    r.cols.forEach((c, j) => { const d = Math.abs(SIZES.indexOf(c) - want); if (d < bd) { bd = d; best = j; } });
    return { i: best, label: r.cols[best], off: true };
  }
  function time(r) {
    const t = r.meta.time;
    return t[st.size] || t['*'] || Object.values(t)[0] || '';
  }

  const hm = r => {
    if (!r.m) return '—';
    const t = time(r);
    return /^\d+:\d\d$/.test(t) ? t : `${Math.floor(r.m / 60)}:${String(r.m % 60).padStart(2, '0')}`;
  };

  // ---------- list ----------
  function home() {
    release();
    document.title = 'Bread';
    const opts = (k, label, vals) =>
      `<select data-f="${k}"><option value="">${label}</option>${vals.map(v =>
        `<option${st.f[k] === v ? ' selected' : ''}>${esc(v)}</option>`).join('')}</select>`;
    const uniq = a => [...new Set(a)];
    const progs = uniq(R.map(r => r.p));
    const types = uniq(R.map(r => r.t));
    const diets = ['Gluten-free', 'Egg-free', 'Dairy-free', 'Vegan'];

    const rows = R.filter(r =>
      (!st.f.p || r.p === st.f.p) && (!st.f.t || r.t === st.f.t) && (!st.f.d || r.d.includes(st.f.d)))
      .sort((a, b) => {
        const k = st.sort.k; let x = a[k], y = b[k];
        if (k === 'm') { x = x ?? 1e9; y = y ?? 1e9; }
        return (x < y ? -1 : x > y ? 1 : a.pg - b.pg) * st.sort.dir;
      });

    const th = (k, label, cls = '') => {
      const s = st.sort.k === k ? ` aria-sort="${st.sort.dir > 0 ? 'ascending' : 'descending'}"` : '';
      return `<th data-k="${k}" class="${cls}"${s}>${label}</th>`;
    };
    app.innerHTML = `
      <div class="bar">
        <div class="seg">${SIZES.map(s =>
          `<button data-s="${s}" aria-pressed="${s === st.size}">${s}</button>`).join('')}</div>
      </div>
      <div class="bar">${opts('p', 'Program', progs)}${opts('t', 'Type', types)}${opts('d', 'Diet', diets)}</div>
      <table class="list">
        <thead><tr>${th('n', 'Recipe')}${th('p', 'Program')}${th('m', 'Time', 'num')}</tr></thead>
        <tbody>${rows.map(r => `<tr data-id="${r.id}">
          <td>${esc(r.n)}</td><td class="mute">${esc(r.p)}</td>
          <td class="num mute">${hm(r)}</td></tr>`).join('')}</tbody>
      </table>`;

    app.querySelectorAll('[data-s]').forEach(b => b.onclick = () => { st.size = b.dataset.s; store.set('size', st.size); home(); });
    app.querySelectorAll('[data-f]').forEach(s => s.onchange = () => { st.f[s.dataset.f] = s.value; store.set('f', st.f); home(); });
    app.querySelectorAll('th[data-k]').forEach(h => h.onclick = () => {
      const k = h.dataset.k;
      st.sort = { k, dir: st.sort.k === k ? -st.sort.dir : 1 }; store.set('sort', st.sort); home();
    });
    app.querySelectorAll('tbody tr').forEach(tr => tr.onclick = () => { location.hash = '/' + tr.dataset.id; });
  }

  // ---------- recipe ----------
  function recipe(r) {
    document.title = r.n;
    const c = col(r);
    const meta = [r.p === 'No machine' ? null : r.p, time(r),
      r.meta.add && `add-ins ${r.meta.add}`, r.meta.paddle && `paddle ${r.meta.paddle}`,
      r.meta.delay === 'Yes' ? 'delay ok' : r.meta.delay.startsWith('Yes') ? 'delay ok (be there for add-ins)' : null,
      r.y && !r.sz.length ? r.y : null].filter(Boolean);
    const head = c.label ? `<th class="${c.off ? 'off' : ''}">${esc(c.label)}</th>` : '<th></th>';
    const table = (rows, pick, name) => rows.map(it =>
      `<tr class="${it.a ? 'add' : ''}"><td>${it.a ? '⏰ ' : ''}${md(name(it.n))}</td><td>${esc(pick(it))}</td></tr>`).join('');
    const ing = r.sec.map((s, k) => `${s.t ? `<h3>${esc(secTitle(s.t))}</h3>` : ''}
      <table class="ing">${k === 0 ? `<thead><tr><th></th>${head}</tr></thead>` : ''}<tbody>${table(s.i, it => it.g[c.i], short)}</tbody></table>`).join('');
    const shownWarn = r.sec.some(s => s.i.some(it => (it.g[c.i] || '').includes('⚠️')));
    const orig = r.sec.map(s => `${s.t ? `<h3>${esc(s.t)}</h3>` : ''}
      <table><tbody>${table(s.i, it => it.o[Math.min(c.i, it.o.length - 1)], n => n)}</tbody></table>`).join('');

    app.innerHTML = `
      <a class="back" href="#" aria-label="Back">←</a>
      <h1>${esc(r.n)}</h1>
      <p class="meta">${meta.map(esc).join(' · ')}</p>
      ${ing}
      ${shownWarn ? r.w.map(w => `<p class="note">⚠️ ${md(w)}</p>`).join('') : ''}
      <ol>${r.st.map(s => `<li>${md(s)}</li>`).join('')}</ol>
      ${r.no.map(n => `<p class="note">${md(n)}</p>`).join('')}
      ${r.uf ? `<details><summary>Ultra-Fast</summary><p>Rapid-rise yeast: <b>5.4 g</b> (1 lb) · <b>7.8 g</b> (1½ lb). Program Ultra-Fast (1:53 / 2:03), then step 3 on. Add-ins 0:13 · paddle 0:18.</p></details>` : ''}
      <details><summary>Original</summary>${orig}</details>`;
    window.scrollTo(0, 0);
    acquire();
  }

  // ---------- screen wake lock ----------
  async function acquire() {
    try { if ('wakeLock' in navigator && !lock) { lock = await navigator.wakeLock.request('screen'); lock.addEventListener('release', () => { lock = null; }); } } catch {}
  }
  function release() { if (lock) { lock.release().catch(() => {}); lock = null; } }
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && location.hash.length > 2) acquire();
  });

  function route() {
    const id = location.hash.replace(/^#\/?/, '');
    const r = id && R.find(x => x.id === id);
    r ? recipe(r) : home();
  }
  window.addEventListener('hashchange', route);
  fetch('recipes.json').then(r => r.json()).then(d => { R = d; route(); });
})();
