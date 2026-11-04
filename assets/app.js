/* LIFE SIMUL LAB — 사이트 동작 (검색, 태그 필터, 다크 모드, 목차) */
(function () {
  'use strict';
  var root = document.documentElement;

  /* ---------- 저장소 (사생활 보호 모드 등에서 실패해도 동작하게) ---------- */
  function load(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
  function save(key, v) { try { localStorage.setItem(key, v); } catch (e) {} }

  /* ---------- 다크 모드 ---------- */
  function isDark() {
    var t = root.getAttribute('data-theme');
    if (t) return t === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  document.getElementById('theme-toggle').addEventListener('click', function () {
    var next = isDark() ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    save('theme', next);
    renderMermaid();
  });

  /* ---------- 모바일 목차 ---------- */
  var navBtn = document.getElementById('nav-toggle');
  navBtn.addEventListener('click', function () {
    var open = document.body.classList.toggle('nav-open');
    navBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.addEventListener('click', function (e) {
    if (!document.body.classList.contains('nav-open')) return;
    if (e.target.closest('#sidebar') || e.target.closest('#nav-toggle')) return;
    document.body.classList.remove('nav-open');
    navBtn.setAttribute('aria-expanded', 'false');
  });

  /* ---------- 표 감싸기 (좁은 화면에서 표만 가로 스크롤) ---------- */
  document.querySelectorAll('article table').forEach(function (t) {
    if (t.parentElement.classList.contains('table-wrap')) return;
    var w = document.createElement('div');
    w.className = 'table-wrap';
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });

  /* ---------- 현재 읽는 소제목 표시 ---------- */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[decodeURIComponent(a.getAttribute('href').slice(1))] = a; });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          tocLinks.forEach(function (a) { a.classList.remove('on'); });
          map[en.target.id].classList.add('on');
        }
      });
    }, { rootMargin: '-60px 0px -70% 0px' });
    document.querySelectorAll('article h2[id], article h3[id]').forEach(function (h) { obs.observe(h); });
  }

  /* ---------- 태그 필터 ---------- */
  var article = document.querySelector('article');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip[data-filter]'));
  var hint = document.querySelector('.filter-hint');
  var active = new Set((load('filters') || '').split(',').filter(Boolean));
  // 필터 대상: 문단, 목록 항목, 표 행, 태그 모아보기 항목
  var units = Array.prototype.slice.call(article.querySelectorAll('.claim, .card, .content p, .content li, .content tbody tr')).filter(function (el) {
    return !el.closest('.filter-bar, .page-head, .toc-mobile, .pager, .claim-body') && !(el.closest('.card') && !el.classList.contains('card'));
  });

  function tagsOf(el) {
    var set = new Set();
    if (el.dataset.tags) el.dataset.tags.split(' ').forEach(function (t) { set.add(t); });
    el.querySelectorAll('[data-tag]').forEach(function (s) { set.add(s.dataset.tag); });
    return set;
  }
  function applyFilter() {
    chips.forEach(function (c) { c.setAttribute('aria-pressed', active.has(c.dataset.filter) ? 'true' : 'false'); });
    var on = active.size > 0;
    article.classList.toggle('is-filtered', on);
    var shown = 0;
    units.forEach(function (el) {
      el.classList.remove('f-hide', 'f-hit');
      if (!on) return;
      var tags = tagsOf(el);
      var hit = false;
      active.forEach(function (t) { if (tags.has(t)) hit = true; });
      // 하위 목록 중 하나라도 맞으면 부모 항목은 남긴다
      if (!hit && el.querySelector) {
        el.querySelectorAll('li, p').forEach(function (child) {
          var ct = tagsOf(child);
          active.forEach(function (t) { if (ct.has(t)) hit = true; });
        });
      }
      if (hit) { el.classList.add('f-hit'); shown++; } else { el.classList.add('f-hide'); }
    });
    // 태그 모아보기에서는 하이라이트 대신 숨김만
    document.querySelectorAll('.claim.f-hit').forEach(function (el) { el.classList.remove('f-hit'); });
    // 걸러진 결과가 없는 소제목 구역은 접는다
    document.querySelectorAll('article section.sec').forEach(function (sec) {
      var any = !on || sec.querySelector('.f-hit') || sec.classList.contains('claim');
      sec.classList.toggle('f-hide', !any);
    });
    if (hint) hint.textContent = on ? ('맞는 항목 ' + shown + '개') : '';
    save('filters', Array.from(active).join(','));
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var k = c.dataset.filter;
      if (active.has(k)) active.delete(k); else active.add(k);
      applyFilter();
    });
  });
  var clear = document.querySelector('[data-filter-clear]');
  if (clear) clear.addEventListener('click', function () { active.clear(); applyFilter(); });
  applyFilter();

  /* ---------- 체크리스트 (이 브라우저에만 저장) ---------- */
  var boxes = Array.prototype.slice.call(document.querySelectorAll('.task-box'));
  if (boxes.length) {
    var key = 'checks:' + location.pathname;
    var saved = (load(key) || '').split(',');
    boxes.forEach(function (b, i) {
      b.checked = saved.indexOf(String(i)) >= 0;
      b.addEventListener('change', function () {
        save(key, boxes.map(function (x, j) { return x.checked ? j : -1; }).filter(function (j) { return j >= 0; }).join(','));
      });
    });
  }

  /* ---------- 검색 ---------- */
  var input = document.getElementById('search-input');
  var box = document.getElementById('search-results');
  var data = window.SEARCH_INDEX || [];
  var sel = -1;
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function highlight(text, terms) {
    var out = esc(text);
    terms.forEach(function (t) {
      if (!t) return;
      var re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      out = out.replace(re, '<mark>$1</mark>');
    });
    return out;
  }
  function search(q) {
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) { box.hidden = true; return; }
    var res = [];
    data.forEach(function (d) {
      var hay = (d.h + ' ' + d.t + ' ' + d.p).toLowerCase();
      var ok = terms.every(function (t) { return hay.indexOf(t) >= 0; });
      if (!ok) return;
      var score = 0;
      terms.forEach(function (t) { if (d.h.toLowerCase().indexOf(t) >= 0) score += 5; if (d.p.toLowerCase().indexOf(t) >= 0) score += 1; });
      res.push({ d: d, s: score });
    });
    res.sort(function (a, b) { return b.s - a.s; });
    res = res.slice(0, 20);
    sel = -1;
    if (!res.length) { box.innerHTML = '<div class="empty">결과가 없습니다.</div>'; box.hidden = false; return; }
    box.innerHTML = res.map(function (r) {
      var t = r.d.t, i = t.toLowerCase().indexOf(terms[0]);
      var snip = i < 0 ? t.slice(0, 90) : (i > 40 ? '…' : '') + t.slice(Math.max(0, i - 40), i + 80) + '…';
      return '<a href="' + r.d.u + '"><div class="r-path">' + esc(r.d.p) + '</div><div>' + highlight(r.d.h, terms) + '</div><div class="r-snip">' + highlight(snip, terms) + '</div></a>';
    }).join('');
    box.hidden = false;
  }
  input.addEventListener('input', function () { search(input.value.trim()); });
  input.addEventListener('keydown', function (e) {
    var links = box.querySelectorAll('a');
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (!links.length) return;
      sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length;
      links.forEach(function (a, i) { a.classList.toggle('sel', i === sel); });
      links[sel].scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter' && links.length) {
      location.href = links[Math.max(sel, 0)].getAttribute('href');
    } else if (e.key === 'Escape') { box.hidden = true; input.blur(); }
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.search')) box.hidden = true; });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); input.focus(); }
  });

  /* ---------- Mermaid 다이어그램 ---------- */
  var mermaidSrc = [];
  document.querySelectorAll('pre.mermaid').forEach(function (el, i) { mermaidSrc[i] = el.textContent; });
  function renderMermaid() {
    var m = window.__mermaid;
    if (!m) return;
    m.initialize({ startOnLoad: false, theme: isDark() ? 'dark' : 'neutral', securityLevel: 'strict', fontFamily: 'Pretendard Variable, sans-serif', flowchart: { htmlLabels: true, curve: 'basis' } });
    document.querySelectorAll('pre.mermaid').forEach(function (el, i) {
      el.removeAttribute('data-processed');
      el.textContent = mermaidSrc[i];
    });
    m.run({ querySelector: 'pre.mermaid' }).catch(function (err) { console.warn('mermaid', err); });
  }
  if (window.__mermaid) renderMermaid(); else window.addEventListener('mermaid-ready', renderMermaid);
})();
