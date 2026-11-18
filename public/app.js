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
  };
  if (!['n', 'p', 'pg'].includes(st.sort.k)) st.sort = { k: 'pg', dir: 1 };
  let R = [];
  let lock = null;

  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const md = (s, foot) => {
    const m = foot && /^(\*+)/.exec(s); const pre = m ? m[1] : ''; let t = esc(s.slice(pre.length));
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

  // ---------- list ----------
  function home() {
    release();
    document.title = 'Bread';
    const rows = [...R].sort((a, b) => {
      const k = st.sort.k, x = a[k], y = b[k];
      return (x < y ? -1 : x > y ? 1 : a.pg - b.pg) * st.sort.dir;
    });
    const th = (k, label) => {
      const s = st.sort.k === k ? ` aria-sort="${st.sort.dir > 0 ? 'ascending' : 'descending'}"` : '';
      return `<th data-k="${k}"${s}>${label}</th>`;
    };
    app.innerHTML = `
      <table class="list">
        <thead><tr>${th('n', 'Recipe')}${th('p', 'Program')}</tr></thead>
        <tbody>${rows.map(r => `<tr data-id="${r.id}">
          <td>${esc(r.n)}</td><td class="mute">${esc(r.p)}</td></tr>`).join('')}</tbody>
      </table>`;

    app.querySelectorAll('th[data-k]').forEach(h => h.onclick = () => {
      const k = h.dataset.k;
      st.sort = { k, dir: st.sort.k === k ? -st.sort.dir : 1 }; store.set('sort', st.sort); home();
    });
    app.querySelectorAll('tbody tr').forEach(tr => tr.onclick = () => { location.hash = '/' + tr.dataset.id; });
  }

  // ---------- recipe ----------
  function recipe(r, keepScroll) {
    document.title = r.n;
    const c = col(r);
    const when = r.meta.add ? `<span class="when">+${r.meta.add}</span>` : '';
    const head = !c.label ? '<th></th>' : r.sz.length > 1
      ? `<th><button class="size${c.off ? ' off' : ''}">${esc(c.label)}</button></th>`
      : `<th>${esc(c.label)}</th>`;
    const table = (rows, pick, name) => rows.map(it =>
      `<tr class="${it.a ? 'add' : ''}"><td>${md(name(it.n))}${it.a ? when : ''}</td><td>${esc(pick(it))}</td></tr>`).join('');
    const ing = r.sec.map((s, k) => `${s.t ? `<h3>${esc(secTitle(s.t))}</h3>` : ''}
      <table class="ing">${k === 0 ? `<thead><tr><th></th>${head}</tr></thead>` : ''}<tbody>${table(s.i, it => it.g[c.i], short)}</tbody></table>`).join('');
    const shownWarn = r.sec.some(s => s.i.some(it => (it.g[c.i] || '').includes('⚠️')));
    const pct = v => (v >= 10 ? Math.round(v) : v.toFixed(1)) + '%';
    const merged = new Map();
    r.sec.filter(s => s.bp).flatMap(s => s.i).filter(it => !it.top).forEach(it => {
      const g = it.gn[Math.min(c.i, it.gn.length - 1)];
      if (g == null) return;
      const n = short(it.n).replace(/, cool$/, '').replace(/\*+$/, '');
      const m = merged.get(n) || { n, fl: it.fl === 1 ? 1 : 0, g: 0 };
      m.g += g; merged.set(n, m);
      if (it.fl === 0.5) merged.set('Flour in starter', { n: 'Flour in starter', fl: 1, g: g / 2 });
    });
    const bpItems = [...merged.values()].sort((a, b) => (b.fl === 1) - (a.fl === 1) || b.g - a.g);
    const flour = bpItems.reduce((a, it) => a + it.fl * it.g, 0);
    const bakers = flour ? `<details><summary>Baker's %</summary><table><tbody>${bpItems.map(it =>
      `<tr><td>${md(short(it.n))}</td><td>${pct(it.g / flour * 100)}</td></tr>`).join('')}</tbody></table></details>` : '';
    const orig = r.sec.map(s => `${s.t ? `<h3>${esc(s.t)}</h3>` : ''}
      <table><tbody>${table(s.i, it => it.o[Math.min(c.i, it.o.length - 1)], n => n)}</tbody></table>`).join('');

    app.innerHTML = `
      <a class="back" href="#" aria-label="Back"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg></a>
      <h1>${esc(r.n)}</h1>
      ${ing}
      ${shownWarn ? r.w.map(w => `<p class="note">⚠️ ${md(w)}</p>`).join('') : ''}
      <ol>${r.st.map(s => `<li>${md(s)}</li>`).join('')}</ol>
      ${r.no.map(n => `<p class="note">${md(n, true)}</p>`).join('')}
      ${r.uf ? `<details><summary>Ultra-Fast</summary><p>Rapid-rise yeast: <b>5.4 g</b> (1 lb) · <b>7.8 g</b> (1½ lb). Program Ultra-Fast (1:53 / 2:03), then step 3 on. Add-ins 0:13 · paddle 0:18.</p></details>` : ''}
      ${bakers}
      <details><summary>Original</summary>${orig}</details>`;
    const btn = app.querySelector('button.size');
    if (btn) btn.onclick = () => {
      const avail = SIZES.filter(s => r.cols.includes(s));
      st.size = avail[(avail.indexOf(r.cols[c.i]) + 1) % avail.length]; store.set('size', st.size); recipe(r, true);
    };
    if (!keepScroll) window.scrollTo(0, 0);
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
