/* Plot Atlas — client layer for the pre-rendered site.
   Everything here is progressive enhancement: every page is complete HTML
   before this file runs. */
(function () {
  'use strict';
  var ROOT = document.documentElement.getAttribute('data-root') || '';
  var esc = function (s) {
    return (s || '').replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };

  /* ---------- 1. legacy hash routes ----------
     The site used to be a hash-routed SPA. Map the old URLs onto the new ones
     so that links people already have keep working. */
  (function () {
    var h = location.hash;
    if (!h || h.slice(0, 2) !== '#/') return;
    var path = h.slice(2).split('?')[0];
    var qs = h.slice(2).split('?')[1] || '';
    var p = path.split('/').filter(Boolean);
    var to = null;
    if (!p.length) to = '';
    else if (p[0] === 'plot' && p[1]) to = 'plot/' + p[1] + '/';
    else if (p[0] === 'shape' && p[1]) to = 'shape/' + p[1] + '/';
    else if (p[0] === 'area' && p[1]) to = 'area/' + p[1] + '/';
    else if (p[0] === 'shapes') to = 'shapes/';
    else if (p[0] === 'areas') to = 'subjects/';
    else if (p[0] === 'origins') to = 'origins/';
    else if (p[0] === 'about') to = 'about/';
    else if (p[0] === 'browse') to = 'browse/' + (qs ? '?' + qs : '');
    if (to === null) return;
    location.replace(ROOT + to);
  })();

  /* ---------- 2. theme toggle ---------- */
  var btn = document.getElementById('themebtn');
  if (btn) {
    var LBL = { light: 'Light', dark: 'Dark', system: 'System' };
    var apply = function (t) {
      if (t === 'system') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', t);
      btn.textContent = LBL[t];
      btn.setAttribute('aria-label', 'Theme: ' + LBL[t] + '. Click to change.');
    };
    var cur = 'system';
    try { cur = localStorage.getItem('atlas-theme') || 'system'; } catch (e) {}
    apply(cur);
    btn.hidden = false;
    btn.addEventListener('click', function () {
      var order = ['system', 'light', 'dark'];
      cur = order[(order.indexOf(cur) + 1) % 3];
      apply(cur);
      try { localStorage.setItem('atlas-theme', cur); } catch (e) {}
    });
  }

  /* ---------- 3. search index ---------- */
  var IDX = null, waiting = [];
  function load(cb) {
    if (IDX) { cb(IDX); return; }
    waiting.push(cb);
    if (waiting.length > 1) return;
    fetch(ROOT + 'assets/search-index.json')
      .then(function (r) { return r.json(); })
      .then(function (j) {
        IDX = j;
        IDX.e.forEach(function (e) { e._h = (e.n + ' ' + (e.a || '') + ' ' + j.fam[e.f]).toLowerCase(); });
        waiting.forEach(function (f) { f(IDX); });
        waiting = [];
      })
      .catch(function () { waiting = []; });
  }

  var qEl = document.getElementById('q'), sg = document.getElementById('sugg');
  if (qEl && sg) {
    var sel = -1;
    qEl.addEventListener('focus', function () { load(function () {}); });
    qEl.addEventListener('input', function () {
      var v = qEl.value.trim().toLowerCase();
      if (window.__browse__) window.__browse__.setQuery(qEl.value.trim());
      if (v.length < 2) { sg.classList.remove('open'); return; }
      load(function (D) {
        if (qEl.value.trim().toLowerCase() !== v) return;
        var hits = D.e.filter(function (e) { return e._h.indexOf(v) >= 0; }).slice(0, 12);
        sel = -1;
        sg.innerHTML = hits.map(function (e, i) {
          return '<a href="' + ROOT + 'plot/' + e.s + '/" data-i="' + i + '">' +
            '<span class="sid">' + e.i + '</span>' + esc(e.n) +
            '<span class="sm">' + e.sh + ' · ' + D.origin[e.o] + '</span></a>';
        }).join('') + '<a href="' + ROOT + 'browse/" style="color:var(--series-1)">See all results in browse →</a>';
        sg.classList.add('open');
      });
    });
    qEl.addEventListener('keydown', function (ev) {
      var links = [].slice.call(sg.querySelectorAll('a'));
      if (ev.key === 'ArrowDown') { ev.preventDefault(); sel = Math.min(sel + 1, links.length - 1); }
      else if (ev.key === 'ArrowUp') { ev.preventDefault(); sel = Math.max(sel - 1, 0); }
      else if (ev.key === 'Enter' && sel >= 0) { ev.preventDefault(); links[sel].click(); sg.classList.remove('open'); qEl.blur(); return; }
      else if (ev.key === 'Escape') { sg.classList.remove('open'); qEl.blur(); return; }
      else return;
      links.forEach(function (l, i) { l.classList.toggle('sel', i === sel); });
    });
    document.addEventListener('click', function (e) {
      if (!sg.contains(e.target) && e.target !== qEl) sg.classList.remove('open');
    });
    sg.addEventListener('click', function () { sg.classList.remove('open'); });
  }

  /* ---------- 4. browse facets ----------
     The full 812-row table is already in the HTML. JS only takes over once a
     filter is touched. */
  var facetBox = document.getElementById('facets');
  if (facetBox) {
    var F = { q: '', origin: {}, area: {}, tier: {}, shape: {} };
    var TIERLBL = { universal: 'Universal', 'cross-domain': 'Cross-domain', 'domain-signature': 'Domain signature', niche: 'Niche' };
    var pre = new URLSearchParams(location.search);
    var famFilter = pre.get('fam') || '', tagFilter = pre.get('tag') || '';
    var touched = false;
    var size = function (o) { var n = 0; for (var k in o) if (o[k]) n++; return n; };
    var has = function (o) { for (var k in o) if (o[k]) return true; return false; };

    function match(D, e) {
      if (has(F.origin) && !F.origin[e.o]) return false;
      if (has(F.tier) && !F.tier[e.t]) return false;
      if (has(F.shape) && !F.shape[e.sh]) return false;
      if (has(F.area) && !e.ar.some(function (a) { return F.area[a]; })) return false;
      if (famFilter && D.fam[e.f] !== famFilter) return false;
      if (tagFilter && e.tg.indexOf(tagFilter) < 0) return false;
      if (F.q && e._h.indexOf(F.q.toLowerCase()) < 0) return false;
      return true;
    }

    function rows(D, list) {
      if (!list.length) return '<p style="color:var(--muted)">Nothing matches those filters.</p>';
      return '<div class="tablewrap"><table><thead><tr><th>#</th><th>Plot</th><th>Shape</th>' +
        '<th>Origin</th><th>Subject areas</th></tr></thead><tbody>' +
        list.map(function (e) {
          return '<tr><td class="tid">' + e.i + '</td><td class="tname">' +
            '<span class="dot d-' + e.d + '" title="' + e.d + '"></span>' +
            '<a href="' + ROOT + 'plot/' + e.s + '/">' + esc(e.n) + '</a>' +
            (e.a ? '<span class="al">' + esc(e.a) + '</span>' : '') + '</td>' +
            '<td><a href="' + ROOT + 'shape/' + e.sh + '/" class="pill">' + e.sh + '</a></td>' +
            '<td><span class="pill o-' + e.o + '">' + D.origin[e.o] + '</span></td>' +
            '<td style="color:var(--muted);font-size:12.6px">' + (e.ar.length ? e.ar.join(' · ') : '—') + '</td></tr>';
        }).join('') + '</tbody></table></div>' +
        '<div class="legend"><span><span class="dot d-deep"></span> deep entry</span>' +
        '<span><span class="dot d-standard"></span> standard</span>' +
        '<span><span class="dot d-stub"></span> stub</span></div>';
    }

    function render(D) {
      var list = D.e.filter(function (e) { return match(D, e); });
      var active = size(F.origin) + size(F.area) + size(F.tier) + size(F.shape) +
        (F.q ? 1 : 0) + (famFilter ? 1 : 0) + (tagFilter ? 1 : 0);
      var lbl = '';
      if (famFilter) lbl += ' · ' + esc(famFilter.replace(/^F\d+\s/, ''));
      if (tagFilter) lbl += ' · ' + esc(D.tags[tagFilter] || tagFilter);
      document.getElementById('results').innerHTML =
        '<div class="resbar"><b>' + list.length + '</b><span style="color:var(--muted);font-size:13px">of ' +
        D.e.length + lbl + '</span>' + (active ? '<button id="clr">Clear filters</button>' : '') + '</div>' +
        rows(D, list);
      var c = document.getElementById('clr');
      if (c) c.onclick = function () {
        F = { q: '', origin: {}, area: {}, tier: {}, shape: {} };
        famFilter = ''; tagFilter = '';
        if (qEl) qEl.value = '';
        history.replaceState(null, '', location.pathname);
        facets(D); render(D);
      };
    }

    function facets(D) {
      var n = function (fn) { var k = 0; D.e.forEach(function (e) { if (fn(e)) k++; }); return k; };
      var mk = function (title, items, set, key) {
        return '<div class="facet"><h4>' + title + '</h4>' + items.map(function (it) {
          return '<label><input type="checkbox" data-k="' + key + '" value="' + it[0] + '"' +
            (set[it[0]] ? ' checked' : '') + '><span>' + esc(it[1]) + '</span>' +
            '<span class="cnt">' + it[2] + '</span></label>';
        }).join('') + '</div>';
      };
      var shapeItems = Object.keys(D.shapes).sort().map(function (s) {
        return [s, s + ' ' + D.shapes[s].replace(/\s*\(.*/, ''), n(function (e) { return e.sh === s; })];
      }).filter(function (x) { return x[2]; });
      facetBox.innerHTML =
        mk('Origin', Object.keys(D.origin).map(function (c) { return [c, D.origin[c], n(function (e) { return e.o === c; })]; }), F.origin, 'origin') +
        mk('Subject area', Object.keys(D.areas).map(function (c) { return [c, D.areas[c], n(function (e) { return e.ar.indexOf(c) >= 0; })]; }), F.area, 'area') +
        mk('Breadth', Object.keys(TIERLBL).map(function (c) { return [c, TIERLBL[c], n(function (e) { return e.t === c; })]; }), F.tier, 'tier') +
        mk('Data shape', shapeItems, F.shape, 'shape');
      [].slice.call(facetBox.querySelectorAll('input')).forEach(function (i) {
        i.onchange = function () { F[i.dataset.k][i.value] = i.checked; touched = true; render(D); };
      });
    }

    window.__browse__ = {
      setQuery: function (v) { F.q = v; load(function (D) { touched = true; render(D); }); }
    };
    load(function (D) {
      if (pre.get('origin')) F.origin[pre.get('origin')] = true;
      if (pre.get('area')) F.area[pre.get('area')] = true;
      if (pre.get('shape')) F.shape[pre.get('shape')] = true;
      facets(D);
      if (pre.get('origin') || pre.get('area') || pre.get('shape') || famFilter || tagFilter) render(D);
    });
  }
})();
