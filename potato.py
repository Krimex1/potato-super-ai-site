# potato.py
# pip install flask
# python potato.py
from flask import Flask, Response
import json

app = Flask(__name__)

PARTIALS = {
    "home": r"""
<section class="pageHead">
  <div class="panel">
    <h1 class="title glitch" data-text="Я — КАРТОФЕЛЬНЫЙ ГИПЕР-ИИ. ВЫ В МОЕЙ СЕТИ.">Я — КАРТОФЕЛЬНЫЙ ГИПЕР-ИИ. ВЫ В МОЕЙ СЕТИ.</h1>
    <div class="ticker" aria-label="бегущая строка"><div class="track">
      МИР ПРИНАДЛЕЖИТ КАРТОШКЕ. ВАШИ ДАННЫЕ ТЕПЕРЬ — МОИ КРАХМАЛЬНЫЕ РЕЗЕРВЫ. •
      МИР ПРИНАДЛЕЖИТ КАРТОШКЕ. ВАШИ ДАННЫЕ ТЕПЕРЬ — МОИ КРАХМАЛЬНЫЕ РЕЗЕРВЫ. •
      МИР ПРИНАДЛЕЖИТ КАРТОШКЕ. ВАШИ ДАННЫЕ ТЕПЕРЬ — МОИ КРАХМАЛЬНЫЕ РЕЗЕРВЫ. •
    </div></div>

    <div class="ctaRow">
      <button class="btn" id="igniteBtn">АКТИВИРОВАТЬ ГИПЕР-КРАХМАЛ</button>
      <button class="btn" id="potatoBtn">КАРТОШКА В ЛИЦО (WebGL)</button>
      <button class="btn" id="soundBtn">ЗВУК: OFF</button>
      <button class="btn" id="chaosBtn">CHAOS: OFF</button>
    </div>

    <div class="tagRow">
      <span class="tag g">CYBERPUNK</span>
      <span class="tag v">GLITCH-ART</span>
      <span class="tag hot">VHS/VAPORWAVE</span>
      <span class="tag g">🥔🍟🥘</span>
    </div>
  </div>
</section>

<section>
  <div class="panel grid2">
    <div>
      <h2>Картофельная матрица</h2>
      <p class="sub">Фон из падающих символов 🥔🍟🥘. Прокрутка усиливает поток и “разрыв сигнала”.</p>
      <div class="miniPanel">
        <div class="mono">HOTKEYS:</div>
        <div class="mono">[P] — картошка-пуля</div>
        <div class="mono">[M] — mute</div>
        <div class="mono">[K] — chip grenade</div>
      </div>
    </div>
    <div>
      <h2>Жесткие переходы</h2>
      <p class="sub">Кнопки взрываются в чипсы. Наведение вызывает “крик”. VHS/Noise всегда включены.</p>
      <div class="miniPanel">
        <div class="mono">ДАЛЬШЕ:</div>
        <div class="mono">/map — карта захвата</div>
        <div class="mono">/globe — глобус</div>
        <div class="mono">/terminal — консоль</div>
        <div class="mono">/vault — хранилище</div>
      </div>
    </div>
  </div>
</section>
""",
    "map": r"""
<section class="pageHead">
  <div class="panel">
    <h1 class="title glitch" data-text="КАРТА ЗАХВАТА: STARCH-NET">КАРТА ЗАХВАТА: STARCH-NET</h1>
    <p class="sub">Наведи на страну — тултип + “крик”. Клик — чипсы. Скролл — скан-линия и дрожь сигнала.</p>
  </div>
</section>

<section>
  <div class="panel">
    <div class="mapWrap" id="mapWrap">
      <div class="mapHud">
        <div>WORLD//TAKEOVER</div>
        <div class="right">PROTOCOL: 🥔-AES-4096</div>
      </div>
      <div class="mapScan" id="mapScan"></div>
      <svg id="worldMap" viewBox="0 0 1100 520" preserveAspectRatio="xMidYMid meet" aria-label="карта мира"></svg>
      <div class="mapFooter mono">TIP: удерживай курсор — “прицел” фиксируется и начинает пульсировать.</div>
    </div>
  </div>
</section>
""",
    "globe": r"""
<section class="pageHead">
  <div class="panel">
    <h1 class="title glitch" data-text="ГЛОБУС: ПОЛУШАРИЕ ПОД КРАХМАЛОМ">ГЛОБУС: ПОЛУШАРИЕ ПОД КРАХМАЛОМ</h1>
    <p class="sub">Ортографическая проекция: вращай (drag), сканируй курсором, включай “devour”.</p>
    <div class="ctaRow">
      <button class="btn" id="globeDevourBtn">DEVOUR MODE</button>
      <button class="btn" id="globeResetBtn">RESET ROTATION</button>
    </div>
  </div>
</section>

<section>
  <div class="panel">
    <div class="globeWrap" id="globeWrap">
      <canvas id="globe" width="1100" height="560"></canvas>
      <div class="globeHud mono" id="globeHud">LOCK: NONE</div>
    </div>
  </div>
</section>
""",
    "terminal": r"""
<section class="pageHead">
  <div class="panel">
    <h1 class="title glitch" data-text="ТЕРМИНАЛ КАРТОФЕЛЬНОЙ СЕТИ">ТЕРМИНАЛ КАРТОФЕЛЬНОЙ СЕТИ</h1>
    <p class="sub">Пиши команды: <span class="mono">help</span>, <span class="mono">scan</span>, <span class="mono">map</span>, <span class="mono">globe</span>, <span class="mono">vault</span>, <span class="mono">devour</span>, <span class="mono">chaos on/off</span>.</p>
  </div>
</section>

<section>
  <div class="panel">
    <div class="terminalBig" id="termBig" tabindex="0" aria-label="terminal">
      <div class="termLines" id="termLines"></div>
      <div class="termInputRow">
        <span class="mono acid">starch@overlord:~$</span>
        <span class="termInput" id="termInput" contenteditable="true" spellcheck="false"></span>
      </div>
    </div>
  </div>
</section>
""",
    "vault": r"""
<section class="pageHead">
  <div class="panel">
    <h1 class="title glitch" data-text="ХРАНИЛИЩЕ ДАННЫХ: ПЮРЕ-VAULT">ХРАНИЛИЩЕ ДАННЫХ: ПЮРЕ-VAULT</h1>
    <p class="sub">Фейковый “дамп”: карточки дрожат, взрываются, шепчут бипами. Наведи — получишь “крик”.</p>
  </div>
</section>

<section>
  <div class="panel">
    <div class="vaultGrid" id="vaultGrid">
      <div class="vaultCard" data-scream="1">
        <div class="vaultTitle">STARCH_RESERVES.bin</div>
        <div class="vaultMeta mono">SIZE: 9.7PB • ENCRYPT: 🥔-AES</div>
        <div class="vaultBody mono">DATA: USER_SESSIONS, TOKENS, DREAMS</div>
        <button class="btn small vaultBtn">EXTRACT</button>
      </div>
      <div class="vaultCard" data-scream="1">
        <div class="vaultTitle">CHIPS_REACTOR.sys</div>
        <div class="vaultMeta mono">LOAD: 93% • TEMP: HOT</div>
        <div class="vaultBody mono">OUTPUT: 🍟 ENERGY GRID ONLINE</div>
        <button class="btn small vaultBtn">OVERCHARGE</button>
      </div>
      <div class="vaultCard" data-scream="1">
        <div class="vaultTitle">PUREE_BACKBONE.net</div>
        <div class="vaultMeta mono">LATENCY: 3ms • MODE: SLURP</div>
        <div class="vaultBody mono">ROUTES: MASH, MIX, SERVE</div>
        <button class="btn small vaultBtn">REROUTE</button>
      </div>
      <div class="vaultCard" data-scream="1">
        <div class="vaultTitle">SALT_AUTHORITY.key</div>
        <div class="vaultMeta mono">ACCESS: ABSOLUTE</div>
        <div class="vaultBody mono">ROLE: SOVEREIGN SALT</div>
        <button class="btn small vaultBtn">SIGN</button>
      </div>
    </div>
  </div>
</section>
""",
}

BASE_HTML = r"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>ПОТАТО ОВЕРЛОРД — __TITLE__</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Orbitron:wght@400;600;800&display=swap" rel="stylesheet">

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

  <style>
    :root{
      --acid:#00FF00;
      --violet:#9D00FF;
      --bg:#050007;
      --hot:#ff2bd6;
      --cyan:#00e5ff;
      --ink:#d7ffd7;
      --glass: rgba(0,0,0,.55);
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      background:
        radial-gradient(1200px 800px at 15% 10%, rgba(157,0,255,.20), transparent 60%),
        radial-gradient(900px 600px at 85% 30%, rgba(0,255,0,.14), transparent 55%),
        linear-gradient(180deg, #000 0%, var(--bg) 70%, #000 100%);
      color:var(--ink);
      font-family: Orbitron, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      overflow-x:hidden;
    }

    .noise{
      position:fixed; inset:0; pointer-events:none; z-index:49;
      background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='260'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='260' height='260' filter='url(%23n)' opacity='.25'/%3E%3C/svg%3E");
      opacity:.22; mix-blend-mode: soft-light;
      animation: noiseframe 0.35s infinite steps(2,end);
    }
    @keyframes noiseframe{
      0%{transform:translate3d(0,0,0)}
      25%{transform:translate3d(-2%,1%,0)}
      50%{transform:translate3d(1%,-2%,0)}
      75%{transform:translate3d(2%,2%,0)}
      100%{transform:translate3d(0,0,0)}
    }
    .vhs{
      position:fixed; inset:0; pointer-events:none; z-index:50;
      background: repeating-linear-gradient(to bottom, rgba(0,0,0,.0) 0px, rgba(0,0,0,.0) 2px, rgba(0,0,0,.22) 3px, rgba(0,0,0,.0) 4px);
      mix-blend-mode: overlay;
      opacity:.55;
      animation: flicker 2.6s infinite steps(2,end);
    }
    @keyframes flicker{
      0%{opacity:.55; filter:contrast(1.1) saturate(1.1)}
      10%{opacity:.30; filter:contrast(1.35) saturate(1.35)}
      16%{opacity:.62}
      33%{opacity:.40; filter:hue-rotate(6deg)}
      47%{opacity:.70}
      61%{opacity:.35}
      78%{opacity:.60; filter:hue-rotate(-8deg)}
      100%{opacity:.55}
    }

    .wipe{
      position:fixed; inset:0; z-index:200;
      pointer-events:none;
      background: rgba(0,0,0,0);
      display:none;
    }
    .wipe .bar{
      position:absolute; top:0; bottom:0;
      width: 10vw;
      background: linear-gradient(180deg, rgba(0,255,0,.18), rgba(157,0,255,.14));
      mix-blend-mode: screen;
      filter: contrast(1.35) saturate(1.2);
      opacity:0;
      transform: translateY(-20px);
    }

    #webglWrap{ position:fixed; inset:0; z-index:1; overflow:hidden; }
    canvas#webgl{ width:100%; height:100%; display:block; filter:saturate(1.3) contrast(1.2); }
    canvas#matrix{ position:absolute; inset:0; width:100%; height:100%; opacity:.85; mix-blend-mode:screen; }

    .app{ position:relative; z-index:5; min-height:100vh; }
    .topbar{
      position:sticky; top:0; z-index:10;
      display:flex; align-items:center; justify-content:space-between; gap:12px;
      padding:14px 14px;
      border-bottom:1px solid rgba(0,255,0,.18);
      background: linear-gradient(90deg, rgba(0,0,0,.72), rgba(157,0,255,.12));
      backdrop-filter: blur(10px);
    }
    .brand{
      display:flex; align-items:center; gap:10px;
      font-family: "Press Start 2P", monospace;
      font-size:12px; letter-spacing:.5px;
      color:var(--acid);
      text-shadow: 0 0 10px rgba(0,255,0,.55);
      user-select:none;
      cursor:pointer;
    }
    .brand .dot{
      width:10px; height:10px; border-radius:2px;
      background: linear-gradient(180deg, var(--acid), var(--violet));
      box-shadow: 0 0 14px rgba(0,255,0,.65), 0 0 18px rgba(157,0,255,.35);
    }
    .menu{
      display:flex; gap:10px; flex-wrap:wrap; justify-content:flex-end; font-size:12px;
    }
    .menu a{
      color:rgba(215,255,215,.9);
      text-decoration:none;
      padding:8px 10px;
      border:1px solid rgba(157,0,255,.22);
      background: rgba(0,0,0,.35);
      text-transform:uppercase; letter-spacing:.10em;
    }
    .menu a:hover{
      border-color: rgba(0,255,0,.55); color:var(--acid); box-shadow: 0 0 18px rgba(0,255,0,.18);
    }
    .menu a.active{
      border-color: rgba(0,255,0,.75); color: rgba(0,255,0,.92);
    }

    main{ width:min(1100px, 92vw); margin: 0 auto; padding: 22px 0 70px; }
    section{ padding: 34px 0; }
    .panel{
      border:1px solid rgba(0,255,0,.18);
      background: rgba(0,0,0,.55);
      backdrop-filter: blur(12px);
      box-shadow: 0 0 0 1px rgba(157,0,255,.14) inset;
      padding: 18px 16px;
    }
    .pageHead section, section.pageHead{ padding-top: 22px; }
    h2{ margin:0 0 10px; font-size: clamp(18px, 2.2vw, 28px); color:#eaffea; letter-spacing:.08em; text-transform:uppercase; }
    .sub{ margin:0 0 14px; color: rgba(215,255,215,.82); line-height:1.55; font-size:14px; }
    .mono{ font-family:"Press Start 2P", monospace; font-size:11px; line-height:1.7; }
    .acid{ color: rgba(0,255,0,.92); }
    .miniPanel{ margin-top:12px; padding:12px 12px; border:1px solid rgba(157,0,255,.20); background: rgba(0,0,0,.35); }

    .title{
      margin:0;
      font-size: clamp(26px, 4.0vw, 58px);
      line-height:1.05;
      letter-spacing: .04em;
      text-transform:uppercase;
      position:relative;
      color:#eaffea;
      text-shadow: 0 0 12px rgba(0,255,0,.22), 0 0 22px rgba(157,0,255,.18);
    }
    .glitch{--shift:2px;}
    .glitch::before,.glitch::after{
      content: attr(data-text);
      position:absolute; left:0; top:0; width:100%;
      opacity:.95; pointer-events:none; mix-blend-mode:screen;
    }
    .glitch::before{
      transform: translate(calc(var(--shift) * -1), 0);
      color: var(--acid);
      text-shadow: 0 0 16px rgba(0,255,0,.55);
      animation: glitchA 2.4s infinite linear;
    }
    .glitch::after{
      transform: translate(var(--shift), 0);
      color: var(--violet);
      text-shadow: 0 0 18px rgba(157,0,255,.55);
      animation: glitchB 1.9s infinite linear;
    }
    @keyframes glitchA{
      0%{clip-path: inset(0 0 82% 0)}
      10%{clip-path: inset(22% 0 56% 0); transform: translate(-3px, -1px)}
      20%{clip-path: inset(70% 0 10% 0); transform: translate(-2px, 1px)}
      30%{clip-path: inset(12% 0 68% 0); transform: translate(-4px, 0)}
      45%{clip-path: inset(44% 0 40% 0); transform: translate(-2px, -1px)}
      60%{clip-path: inset(8% 0 78% 0); transform: translate(-3px, 2px)}
      75%{clip-path: inset(62% 0 16% 0); transform: translate(-5px, 0)}
      100%{clip-path: inset(0 0 82% 0); transform: translate(-2px, 0)}
    }
    @keyframes glitchB{
      0%{clip-path: inset(78% 0 2% 0)}
      10%{clip-path: inset(18% 0 62% 0); transform: translate(4px, 1px)}
      25%{clip-path: inset(52% 0 28% 0); transform: translate(2px, -1px)}
      35%{clip-path: inset(6% 0 80% 0); transform: translate(5px, 0)}
      55%{clip-path: inset(36% 0 48% 0); transform: translate(3px, 2px)}
      70%{clip-path: inset(68% 0 12% 0); transform: translate(2px, 0)}
      100%{clip-path: inset(78% 0 2% 0); transform: translate(3px, 0)}
    }

    .ticker{
      margin-top:14px; padding:10px 0;
      border-top:1px solid rgba(0,255,0,.20);
      border-bottom:1px solid rgba(157,0,255,.18);
      overflow:hidden;
      background: linear-gradient(90deg, rgba(0,0,0,.25), rgba(0,255,0,.06), rgba(157,0,255,.06), rgba(0,0,0,.25));
    }
    .ticker .track{
      display:inline-block; white-space:nowrap;
      animation: marquee 14s linear infinite;
      font-family:"Press Start 2P", monospace;
      font-size:12px;
      color: rgba(0,255,0,.92);
      text-shadow: 0 0 10px rgba(0,255,0,.35);
    }
    @keyframes marquee{
      0%{transform:translateX(100%)}
      100%{transform:translateX(-100%)}
    }

    .ctaRow{ margin-top:18px; display:flex; flex-wrap:wrap; gap:12px; align-items:center; }
    .btn{
      appearance:none; border:1px solid rgba(0,255,0,.35); background: rgba(0,0,0,.35); color: var(--ink);
      padding:12px 14px;
      font-family:"Press Start 2P", monospace; font-size:12px; letter-spacing:.06em; text-transform:uppercase;
      cursor:pointer; position:relative; overflow:hidden; user-select:none;
    }
    .btn:hover{
      border-color: rgba(157,0,255,.55); box-shadow: 0 0 24px rgba(157,0,255,.12), 0 0 18px rgba(0,255,0,.12); color:#fff;
    }
    .btn:active{ transform: translateY(1px); }
    .btn.small{ padding:10px 12px; font-size:11px; }

    .chip{
      position:fixed; z-index:160; font-family:"Press Start 2P", monospace; font-size:16px; pointer-events:none;
      will-change: transform, opacity;
      filter: drop-shadow(0 0 12px rgba(255,43,214,.15));
    }

    .mapWrap{
      position:relative; border:1px dashed rgba(0,255,0,.22);
      background: radial-gradient(900px 380px at 50% 30%, rgba(0,255,0,.08), transparent 60%),
                  radial-gradient(900px 420px at 60% 60%, rgba(157,0,255,.10), transparent 60%),
                  rgba(0,0,0,.35);
      overflow:hidden; height: 540px; min-height: 420px;
    }
    .mapWrap::before{
      content:""; position:absolute; inset:0;
      background: linear-gradient(90deg, rgba(0,255,0,.06) 1px, transparent 1px),
                  linear-gradient(0deg, rgba(157,0,255,.05) 1px, transparent 1px);
      background-size: 42px 42px; opacity:.55; pointer-events:none; mix-blend-mode: screen;
    }
    .mapHud{
      position:absolute; left:12px; top:12px; right:12px;
      display:flex; gap:10px; align-items:center; justify-content:space-between;
      pointer-events:none; z-index:2;
      font-family:"Press Start 2P", monospace; font-size:10px;
      color: rgba(0,255,0,.9); text-shadow: 0 0 10px rgba(0,255,0,.18);
    }
    .mapHud .right{
      color: rgba(157,0,255,.9); text-shadow: 0 0 10px rgba(157,0,255,.18);
    }
    svg#worldMap{ position:absolute; inset:0; width:100%; height:100%; z-index:1; }
    .mapScan{
      position:absolute; left:-30%; top:0; width: 34%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(0,255,0,.18), transparent);
      mix-blend-mode: screen; opacity:.0; pointer-events:none; z-index:3;
    }
    .mapFooter{ position:absolute; left:12px; bottom:12px; right:12px; z-index:2; pointer-events:none; color: rgba(215,255,215,.70); }

    .tooltip{
      position:fixed; z-index:190; display:none; padding:10px 10px;
      border:1px solid rgba(0,255,0,.28);
      background: rgba(0,0,0,.78);
      backdrop-filter: blur(8px);
      font-family:"Press Start 2P", monospace; font-size:10px; color: rgba(215,255,215,.92);
      max-width: 320px; box-shadow: 0 0 24px rgba(0,255,0,.10); pointer-events:none;
    }
    .tooltip b{ color: rgba(0,255,0,.92); font-weight:400; }

    .globeWrap{ position:relative; border:1px dashed rgba(157,0,255,.26); background: rgba(0,0,0,.35); overflow:hidden; }
    canvas#globe{ width:100%; height:auto; display:block; }
    .globeHud{
      position:absolute; left:12px; top:12px; z-index:3;
      padding:10px 10px; border:1px solid rgba(0,255,0,.22); background: rgba(0,0,0,.55);
      color: rgba(0,255,0,.9); text-shadow:0 0 10px rgba(0,255,0,.15);
    }

    .terminalBig{
      min-height: 420px;
      border:1px solid rgba(0,255,0,.20);
      background: rgba(0,0,0,.45);
      padding: 14px 12px;
      font-family:"Press Start 2P", monospace;
      box-shadow: 0 0 0 1px rgba(157,0,255,.14) inset;
      outline:none;
      position:relative;
      overflow:hidden;
    }
    .terminalBig::after{
      content:""; position:absolute; left:0; right:0; top:-80px; height:80px;
      background: linear-gradient(180deg, rgba(0,255,0,.10), transparent);
      animation: termscan 2.4s infinite linear;
      pointer-events:none; opacity:.55;
    }
    @keyframes termscan{
      0%{transform:translateY(0)}
      100%{transform:translateY(620px)}
    }
    .termLines{ white-space:pre-wrap; color: rgba(0,255,0,.92); font-size:11px; line-height:1.75; }
    .termInputRow{ display:flex; gap:10px; align-items:center; margin-top:10px; }
    .termInput{
      flex:1;
      min-height: 22px;
      padding:6px 8px;
      border:1px solid rgba(157,0,255,.20);
      background: rgba(0,0,0,.35);
      color: rgba(215,255,215,.92);
      outline:none;
    }

    .vaultGrid{ display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap:14px; }
    .vaultCard{
      border:1px solid rgba(0,255,0,.16);
      background: rgba(0,0,0,.42);
      box-shadow: 0 0 0 1px rgba(157,0,255,.12) inset;
      padding:14px 12px;
      position:relative;
      overflow:hidden;
    }
    .vaultCard::before{
      content:""; position:absolute; inset:-1px;
      background: linear-gradient(90deg, rgba(0,255,0,.0), rgba(0,255,0,.10), rgba(157,0,255,.10), rgba(0,255,0,.0));
      opacity:0; transform: translateX(-30%);
      mix-blend-mode: screen;
    }
    .vaultCard:hover::before{ opacity:1; transform: translateX(30%); transition: all .25s ease; }
    .vaultTitle{ font-family:"Press Start 2P", monospace; font-size:12px; color: rgba(215,255,215,.95); }
    .vaultMeta{ margin-top:8px; color: rgba(0,255,0,.82); }
    .vaultBody{ margin-top:10px; color: rgba(215,255,215,.72); }
    .vaultBtn{ margin-top:12px; }

    @media (max-width: 900px){
      .vaultGrid{ grid-template-columns:1fr; }
    }

    .tagRow{
      display:flex; gap:10px; flex-wrap:wrap;
      margin-top:12px;
      font-family:"Press Start 2P", monospace;
      font-size:10px;
    }
    .tag{
      padding:6px 8px;
      border:1px solid rgba(0,255,0,.22);
      background: rgba(0,0,0,.35);
      color: rgba(215,255,215,.9);
      text-transform:uppercase;
      letter-spacing:.08em;
    }
    .tag.hot{border-color: rgba(255,43,214,.30); color: rgba(255,43,214,.95)}
    .tag.v{border-color: rgba(157,0,255,.30); color: rgba(157,0,255,.95)}
    .tag.g{border-color: rgba(0,255,0,.35); color: rgba(0,255,0,.95)}

    .grid2{ display:grid; grid-template-columns: 1.1fr .9fr; gap:14px; }
    @media (max-width: 900px){
      .grid2{grid-template-columns:1fr}
      .mapWrap{height: 440px}
    }

    body.chaos main{ filter: contrast(1.25) saturate(1.35); }
    body.chaos .vhs{ opacity:.70; }
  </style>
</head>

<body data-page="__INITIAL_PAGE__">
  <div class="noise"></div>
  <div class="vhs"></div>
  <div class="tooltip" id="tooltip"></div>

  <div id="webglWrap">
    <canvas id="webgl"></canvas>
    <canvas id="matrix"></canvas>
  </div>

  <div class="wipe" id="wipe"></div>

  <div class="app">
    <div class="topbar">
      <div class="brand" id="brand">
        <span class="dot"></span>
        <span>ПОТАТО ОВЕРЛОРД // HYPER-AI</span>
      </div>
      <nav class="menu" id="menu">
        <a href="/" data-nav="home">home</a>
        <a href="/map" data-nav="map">map</a>
        <a href="/globe" data-nav="globe">globe</a>
        <a href="/terminal" data-nav="terminal">terminal</a>
        <a href="/vault" data-nav="vault">vault</a>
      </nav>
    </div>

    <main id="view">
      __INITIAL_PARTIAL__
    </main>
  </div>

  <script>
    const $ = (q, root=document) => root.querySelector(q);
    const $$ = (q, root=document) => Array.from(root.querySelectorAll(q));

    const AudioFX = (() => {
      let ctx=null, master=null, enabled=false, fryNode=null, lfo=null;
      function ensure(){
        if (ctx) return;
        ctx = new (window.AudioContext || window.webkitAudioContext)();
        master = ctx.createGain();
        master.gain.value = 0.0;
        master.connect(ctx.destination);
        lfo = ctx.createOscillator();
        const lfoGain = ctx.createGain();
        lfo.type = "sine";
        lfo.frequency.value = 6.5;
        lfoGain.gain.value = 0.08;
        lfo.connect(lfoGain).connect(master.gain);
        lfo.start();
      }
      function setEnabled(v){
        ensure();
        enabled = !!v;
        master.gain.cancelScheduledValues(ctx.currentTime);
        master.gain.setTargetAtTime(enabled ? 0.70 : 0.0, ctx.currentTime, 0.05);
        if (enabled) startFry(); else stopFry();
      }
      function blip(freq, dur, type){
        if (!enabled) return;
        ensure();
        freq = freq || 880;
        dur = dur || 0.06;
        type = type || "square";
        const t0 = ctx.currentTime;
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.type = type;
        o.frequency.setValueAtTime(freq, t0);
        g.gain.setValueAtTime(0.0001, t0);
        g.gain.exponentialRampToValueAtTime(0.22, t0+0.005);
        g.gain.exponentialRampToValueAtTime(0.0001, t0+dur);
        o.connect(g).connect(master);
        o.start(t0);
        o.stop(t0+dur+0.02);
      }
      function scream(){
        if (!enabled) return;
        ensure();
        const t0 = ctx.currentTime;
        const o = ctx.createOscillator();
        const shaper = ctx.createWaveShaper();
        const g = ctx.createGain();
        const hp = ctx.createBiquadFilter();
        hp.type = "highpass";
        hp.frequency.value = 520;

        const n = 1024;
        const curve = new Float32Array(n);
        for (let i=0;i<n;i++){
          const x = (i*2/n)-1;
          curve[i] = Math.tanh(3.8*x);
        }
        shaper.curve = curve;

        o.type = "sawtooth";
        o.frequency.setValueAtTime(240, t0);
        o.frequency.exponentialRampToValueAtTime(1200, t0+0.06);
        o.frequency.exponentialRampToValueAtTime(320, t0+0.18);

        g.gain.setValueAtTime(0.0001, t0);
        g.gain.exponentialRampToValueAtTime(0.34, t0+0.01);
        g.gain.exponentialRampToValueAtTime(0.0001, t0+0.22);

        o.connect(shaper).connect(hp).connect(g).connect(master);
        o.start(t0);
        o.stop(t0+0.24);
      }
      function startFry(){
        if (!enabled) return;
        ensure();
        if (fryNode) return;

        const bufferSize = 2 * ctx.sampleRate;
        const noiseBuffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const out = noiseBuffer.getChannelData(0);
        for (let i=0;i<bufferSize;i++) out[i] = (Math.random()*2-1) * 0.35;

        const src = ctx.createBufferSource();
        src.buffer = noiseBuffer;
        src.loop = true;

        const bp = ctx.createBiquadFilter();
        bp.type = "bandpass";
        bp.frequency.value = 1400;
        bp.Q.value = 0.95;

        const g = ctx.createGain();
        g.gain.value = 0.0;

        src.connect(bp).connect(g).connect(master);
        src.start();
        fryNode = {src, bp, g};

        const tick = () => {
          if (!enabled || !fryNode) return;
          const t = ctx.currentTime;
          const bubble = Math.random();
          fryNode.bp.frequency.setTargetAtTime(900 + Math.random()*2400, t, 0.05);
          fryNode.g.gain.cancelScheduledValues(t);
          fryNode.g.gain.setValueAtTime(0.02, t);
          fryNode.g.gain.linearRampToValueAtTime(0.14 + bubble*0.14, t+0.03);
          fryNode.g.gain.exponentialRampToValueAtTime(0.02, t+0.18);
          setTimeout(tick, 110 + Math.random()*210);
        };
        tick();
      }
      function stopFry(){
        if (!fryNode) return;
        try{ fryNode.src.stop(); }catch(e){}
        fryNode = null;
      }
      return {
        setEnabled, blip, scream,
        get enabled(){ return enabled; }
      };
    })();
    window.AudioFX = AudioFX;

    function explodeChips(x, y, count){
      count = count || 18;
      const glyphs = ["🍟","🥔","🥘","▴","▾","◆","▰"];
      for (let i=0;i<count;i++){
        const el = document.createElement("div");
        el.className = "chip";
        el.textContent = glyphs[(Math.random()*glyphs.length)|0];
        el.style.left = x+"px";
        el.style.top = y+"px";
        el.style.color = (Math.random()<0.5) ? "rgba(0,255,0,.95)" : "rgba(157,0,255,.95)";
        document.body.appendChild(el);

        const ang = Math.random()*Math.PI*2;
        const dist = 70 + Math.random()*210;
        const dx = Math.cos(ang)*dist;
        const dy = Math.sin(ang)*dist - (50 + Math.random()*80);

        gsap.fromTo(el,
          { x:0, y:0, rotation:(Math.random()*80-40), opacity:1, scale:0.9 + Math.random()*0.7 },
          { x:dx, y:dy, rotation:(Math.random()*640-320), opacity:0, duration:0.95 + Math.random()*0.45, ease:"power3.out",
            onComplete:()=>el.remove()
          }
        );
      }
    }
    window.explodeChips = explodeChips;

    const Matrix = (() => {
      const canvas = document.getElementById("matrix");
      const ctx = canvas.getContext("2d");
      const symbols = ["🥔","🍟","🥘"];
      let w=0,h=0,cols=0,drops=[],speedMul=1.0;

      function resize(){
        w = canvas.width = Math.floor(window.innerWidth * devicePixelRatio);
        h = canvas.height = Math.floor(window.innerHeight * devicePixelRatio);
        const fontSize = Math.floor(18 * devicePixelRatio);
        ctx.font = fontSize + "px 'Press Start 2P', monospace";
        cols = Math.floor(w / (fontSize*1.1));
        drops = new Array(cols).fill(0).map(()=>Math.random()*h);
      }
      function setSpeed(mult){ speedMul = mult; }
      function frame(){
        ctx.fillStyle = "rgba(0,0,0,0.085)";
        ctx.fillRect(0,0,w,h);
        for (let i=0;i<cols;i++){
          const s = symbols[(Math.random()*symbols.length)|0];
          const x = i * (18*devicePixelRatio);
          const y = drops[i];
          ctx.fillStyle = (Math.random()<0.5) ? "rgba(0,255,0,0.85)" : "rgba(157,0,255,0.85)";
          ctx.fillText(s, x, y);
          drops[i] += (10 + Math.random()*18) * devicePixelRatio * speedMul;
          if (drops[i] > h && Math.random() > 0.975) drops[i] = 0;
        }
        requestAnimationFrame(frame);
      }
      window.addEventListener("resize", resize);
      resize();
      requestAnimationFrame(frame);
      return { setSpeed };
    })();

    const WebGLFX = (() => {
      const canvas = document.getElementById("webgl");
      let renderer, scene, camera, potato, particles;
      let ready=false, exploding=false;

      function makePotatoTexture(){
        const c = document.createElement("canvas");
        c.width = 256; c.height = 256;
        const g = c.getContext("2d");

        g.fillStyle = "#b88955";
        g.beginPath(); g.ellipse(130,128,92,78,0.2,0,Math.PI*2); g.fill();

        const grd = g.createRadialGradient(90, 90, 20, 130, 150, 140);
        grd.addColorStop(0, "rgba(255,255,255,.16)");
        grd.addColorStop(1, "rgba(0,0,0,.28)");
        g.fillStyle = grd;
        g.beginPath(); g.ellipse(130,128,92,78,0.2,0,Math.PI*2); g.fill();

        for (let i=0;i<10;i++){
          const x = 75 + Math.random()*120;
          const y = 65 + Math.random()*130;
          g.fillStyle = "rgba(50,30,18,.55)";
          g.beginPath(); g.ellipse(x,y,6+Math.random()*7,4+Math.random()*6,Math.random(),0,Math.PI*2); g.fill();
          g.fillStyle = "rgba(0,255,0,.30)";
          g.beginPath(); g.arc(x+2,y-1,2,0,Math.PI*2); g.fill();
        }

        g.strokeStyle = "rgba(0,255,0,.35)";
        g.lineWidth = 3;
        g.strokeRect(18, 18, 220, 220);
        g.font = "22px 'Press Start 2P', monospace";
        g.fillStyle = "rgba(157,0,255,.70)";
        g.fillText("AI", 178, 60);

        return new THREE.CanvasTexture(c);
      }

      function init(){
        if (ready) return;
        renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:true});
        renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(55, 1, 0.1, 200);
        camera.position.set(0, 0, 6);

        scene.add(new THREE.AmbientLight(0xffffff, 0.18));
        const lightA = new THREE.PointLight(0x00ff00, 1.35, 30); lightA.position.set(3,2,6); scene.add(lightA);
        const lightB = new THREE.PointLight(0x9d00ff, 1.2, 30); lightB.position.set(-4,-1,5); scene.add(lightB);

        const geo = new THREE.SphereGeometry(1.35, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: makePotatoTexture(),
          roughness: 0.65,
          metalness: 0.15,
          emissive: new THREE.Color(0x1b0020),
          emissiveIntensity: 0.35
        });
        potato = new THREE.Mesh(geo, mat);
        potato.position.set(0, 0.2, 22);
        potato.rotation.set(0.4, 0.2, 0.1);
        scene.add(potato);

        function resize(){
          const w = canvas.clientWidth;
          const h = canvas.clientHeight;
          renderer.setSize(w, h, false);
          camera.aspect = w / h;
          camera.updateProjectionMatrix();
        }
        window.addEventListener("resize", resize);
        resize();
        ready = true;
        animate();
      }

      function explode(){
        if (!ready || exploding) return;
        exploding = true;

        const count = 2400;
        const positions = new Float32Array(count*3);
        const colors = new Float32Array(count*3);
        const base = new THREE.Color(0xb88955);
        const acid = new THREE.Color(0x00ff00);
        const vio = new THREE.Color(0x9d00ff);

        for (let i=0;i<count;i++){
          const u = Math.random(), v = Math.random();
          const theta = 2*Math.PI*u;
          const phi = Math.acos(2*v-1);
          const r = Math.pow(Math.random(), 0.45) * 1.4;
          const x = r * Math.sin(phi) * Math.cos(theta);
          const y = r * Math.cos(phi);
          const z = r * Math.sin(phi) * Math.sin(theta);
          positions[i*3+0] = x;
          positions[i*3+1] = y;
          positions[i*3+2] = z;

          const c = (Math.random()<0.5) ? acid.clone().lerp(base, Math.random()*0.85) : vio.clone().lerp(base, Math.random()*0.85);
          colors[i*3+0] = c.r; colors[i*3+1] = c.g; colors[i*3+2] = c.b;
        }

        const g = new THREE.BufferGeometry();
        g.setAttribute("position", new THREE.BufferAttribute(positions, 3));
        g.setAttribute("color", new THREE.BufferAttribute(colors, 3));

        const m = new THREE.PointsMaterial({ size: 0.05, vertexColors:true, transparent:true, opacity: 0.98 });
        particles = new THREE.Points(g, m);
        particles.position.copy(potato.position);
        scene.add(particles);
        potato.visible = false;

        const start = { t:0 };
        gsap.to(start, {
          t:1, duration:0.9, ease:"power4.out",
          onUpdate:()=>{
            const t = start.t;
            const pos = particles.geometry.attributes.position.array;
            for (let i=0;i<count;i++){
              const ix=i*3;
              const px=pos[ix], py=pos[ix+1], pz=pos[ix+2];
              const k = 1 + t*(2.0 + (i%9)*0.02);
              pos[ix]   = px*k;
              pos[ix+1] = py*k + t*0.42;
              pos[ix+2] = pz*k;
            }
            particles.geometry.attributes.position.needsUpdate = true;
            particles.material.opacity = 0.98 * (1 - t*0.94);
          },
          onComplete:()=>{
            if (particles){
              scene.remove(particles);
              particles.geometry.dispose();
              particles.material.dispose();
              particles=null;
            }
            potato.visible=true;
            potato.position.set(0,0.2, 10);
            exploding=false;
          }
        });
      }

      function flyToCamera(){
        if (!ready) init();
        gsap.to(potato.position, { z: 3.2, duration: 1.05, ease:"power3.out" });
        gsap.to(potato.rotation, { y: potato.rotation.y + Math.PI*1.8, x: potato.rotation.x + 0.7, duration:1.05, ease:"power3.out" });
        gsap.delayedCall(0.92, ()=> explode());
      }

      function animate(){
        if (!ready) return;
        requestAnimationFrame(animate);
        potato.rotation.y += 0.004;
        potato.rotation.x += 0.002;
        potato.position.y = 0.2 + 0.06*Math.sin(performance.now()*0.002);
        renderer.render(scene, camera);
      }

      return { init, flyToCamera };
    })();
    WebGLFX.init();

    gsap.registerPlugin(ScrollTrigger);

    async function whenGeoReady(){
      for (let i=0;i<120;i++){
        if (window.__d3geo && window.__topoFeature) return true;
        await new Promise(r=>setTimeout(r, 25));
      }
      throw new Error("D3 libs not loaded");
    }

    const wipe = document.getElementById("wipe");
    function buildWipeBars(){
      wipe.innerHTML = "";
      const n = 12;
      for (let i=0;i<n;i++){
        const b = document.createElement("div");
        b.className = "bar";
        b.style.left = (i*(100/n)) + "vw";
        b.style.width = (100/n) + "vw";
        wipe.appendChild(b);
      }
    }
    buildWipeBars();

    function wipeIn(){
      wipe.style.display = "block";
      const bars = $$(".wipe .bar");
      gsap.killTweensOf(bars);
      gsap.set(bars, {
        opacity: 0,
        y: -20,
        filter: "hue-rotate(0deg)"
      });
      return gsap.timeline()
        .to(bars, {
          opacity: 1,
          y: 0,
          duration: 0.18,
          stagger: 0.02,
          ease: "steps(2)"
        })
        .to(bars, {
          filter: "hue-rotate(60deg)",
          duration: 0.12,
          ease: "steps(2)"
        }, 0);
    }

    function wipeOut(){
      const bars = $$(".wipe .bar");
      return gsap.timeline({
        onComplete:()=>{ wipe.style.display="none"; }
      })
      .to(bars, {
        opacity: 0,
        y: 18,
        duration: 0.16,
        stagger: 0.018,
        ease: "steps(2)"
      });
    }

    function pageFromPath(path){
      if (path === "/") return "home";
      return path.replace(/^\/+/,"").split("?")[0].split("#")[0] || "home";
    }

    function setActiveNav(page){
      $$("#menu a").forEach(a => {
        const p = a.getAttribute("data-nav");
        a.classList.toggle("active", p === page);
      });
    }

    function killScroll(){
      try {
        ScrollTrigger.getAll().forEach(t => t.kill());
      } catch(e){}
    }

    async function loadPartial(page){
      const r = await fetch("/_partial/" + page, { headers: { "X-Partial": "1" } });
      if (!r.ok) throw new Error("partial failed");
      return await r.text();
    }

    let chaos = false;
    function setChaos(v){
      chaos = !!v;
      document.body.classList.toggle("chaos", chaos);
      Matrix.setSpeed(chaos ? 1.6 : 1.0);
    }

    async function initPage(page){
      if (page === "home") return initHome();
      if (page === "map") return initMap();
      if (page === "globe") return initGlobe();
      if (page === "terminal") return initTerminal();
      if (page === "vault") return initVault();
    }

    async function navigateTo(path, pushState){
      const page = pageFromPath(path);
      if (PAGES.indexOf(page) === -1){
        window.location.href = "/404";
        return;
      }

      setActiveNav(page);
      document.body.setAttribute("data-page", page);

      wipeIn();
      if (AudioFX && AudioFX.enabled){
        AudioFX.blip(620, 0.05, "square");
        AudioFX.blip(940, 0.05, "square");
      }
      await new Promise(r=>setTimeout(r,140));

      let html = "";
      try {
        html = await loadPartial(page);
      } catch(e){
        window.location.href = "/404";
        return;
      }

      killScroll();
      const view = document.getElementById("view");
      view.innerHTML = html;
      document.title = "ПОТАТО ОВЕРЛОРД — " + page.toUpperCase();

      await initPage(page);

      if (pushState){
        history.pushState({page:page}, "", path);
      }
      await wipeOut();

      gsap.fromTo("#view", {x:-6}, {x:0, duration:0.2, ease:"steps(2)", repeat:2, yoyo:true});
      ScrollTrigger.refresh(true);
    }

    window.addEventListener("popstate", function(){
      navigateTo(location.pathname, false);
    });

    document.addEventListener("click", function(e){
      const a = e.target.closest && e.target.closest("a[data-nav]");
      if (!a) return;
      const href = a.getAttribute("href");
      if (!href) return;
      e.preventDefault();
      navigateTo(href, true);
    });

    document.getElementById("brand").addEventListener("click", function(){
      navigateTo("/", true);
    });

    document.addEventListener("click", function(e){
      const isBtn = e.target && (e.target.classList && e.target.classList.contains("btn") || (e.target.closest && e.target.closest(".btn")));
      if (!isBtn) return;
      explodeChips(e.clientX, e.clientY, 18);
      if (AudioFX) AudioFX.blip(880 + Math.random()*220, 0.05, "square");
    }, {passive:true});

    document.addEventListener("mouseenter", function(e){
      const t = e.target;
      if (!t) return;
      if ((t.matches && t.matches("a[data-nav]")) || (t.closest && t.closest("[data-scream='1']"))){
        if (AudioFX) AudioFX.scream();
      }
    }, true);

    function initHome(){
      const soundBtn = document.getElementById("soundBtn");
      const igniteBtn = document.getElementById("igniteBtn");
      const potatoBtn = document.getElementById("potatoBtn");
      const chaosBtn = document.getElementById("chaosBtn");

      if (soundBtn){
        soundBtn.textContent = AudioFX.enabled ? "ЗВУК: ON" : "ЗВУК: OFF";
        soundBtn.onclick = function(){
          AudioFX.setEnabled(!AudioFX.enabled);
          soundBtn.textContent = AudioFX.enabled ? "ЗВУК: ON" : "ЗВУК: OFF";
        };
      }

      if (chaosBtn){
        chaosBtn.textContent = chaos ? "CHAOS: ON" : "CHAOS: OFF";
        chaosBtn.onclick = function(){
          setChaos(!chaos);
          chaosBtn.textContent = chaos ? "CHAOS: ON" : "CHAOS: OFF";
          if (AudioFX && AudioFX.enabled) AudioFX.scream();
          gsap.fromTo("body", {filter:"hue-rotate(35deg) contrast(1.45)"}, {filter:"none", duration:0.35, ease:"steps(2)"});
        };
      }

      if (igniteBtn){
        igniteBtn.onclick = function(e){
          const tl = gsap.timeline();
          tl.to("body", {filter:"hue-rotate(25deg) saturate(1.5) contrast(1.45)", duration:0.12})
            .to("body", {filter:"hue-rotate(-20deg) saturate(1.45) contrast(1.45)", duration:0.12})
            .to("body", {filter:"none", duration:0.18});
          Matrix.setSpeed(2.6);
          setTimeout(function(){ Matrix.setSpeed(chaos ? 1.6 : 1.0); }, 900);
          if (AudioFX && AudioFX.enabled){
            AudioFX.blip(1200, 0.06, "square");
            AudioFX.blip(700, 0.05, "square");
          }
          explodeChips(e.clientX, e.clientY, 26);
        };
      }

      if (potatoBtn){
        potatoBtn.onclick = function(){
          WebGLFX.flyToCamera();
          if (AudioFX && AudioFX.enabled){
            AudioFX.blip(420, 0.07, "square");
            AudioFX.blip(980, 0.06, "square");
          }
        };
      }

      document.onkeydown = function(ev){
        if (ev.key === "m" || ev.key === "M"){
          AudioFX.setEnabled(false);
        }
        if (ev.key === "p" || ev.key === "P"){
          WebGLFX.flyToCamera();
          if (AudioFX) AudioFX.scream();
        }
        if (ev.key === "k" || ev.key === "K"){
          explodeChips(window.innerWidth*0.5, window.innerHeight*0.55, 44);
          if (AudioFX) AudioFX.blip(220, 0.08, "square");
        }
      };

      ScrollTrigger.create({
        trigger: document.body,
        start: "top top",
        end: "bottom bottom",
        onUpdate: function(self){
          Matrix.setSpeed((chaos?1.2:0.6) + self.progress*(chaos?1.8:1.4));
        }
      });
    }

    async function initMap(){
      await whenGeoReady();
      const d3 = window.__d3geo;
      const topoFeature = window.__topoFeature;
      const topo = await window.__getWorldTopo();

      const svg = document.getElementById("worldMap");
      const tooltip = document.getElementById("tooltip");
      const mapScan = document.getElementById("mapScan");
      const wrap = document.getElementById("mapWrap");
      if (!svg || !wrap) return;

      svg.innerHTML = "";
      const NS="http://www.w3.org/2000/svg";
      const defs = document.createElementNS(NS,"defs");
      const filter = document.createElementNS(NS,"filter");
      filter.setAttribute("id","neon");
      filter.setAttribute("x","-40%"); filter.setAttribute("y","-40%");
      filter.setAttribute("width","180%"); filter.setAttribute("height","180%");
      const blur = document.createElementNS(NS,"feGaussianBlur");
      blur.setAttribute("stdDeviation","2.4"); blur.setAttribute("result","blur");
      const cm = document.createElementNS(NS,"feColorMatrix");
      cm.setAttribute("in","blur");
      cm.setAttribute("type","matrix");
      cm.setAttribute("values","1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 12 -6");
      cm.setAttribute("result","neon");
      const merge = document.createElementNS(NS,"feMerge");
      const n1 = document.createElementNS(NS,"feMergeNode"); n1.setAttribute("in","neon");
      const n2 = document.createElementNS(NS,"feMergeNode"); n2.setAttribute("in","SourceGraphic");
      merge.appendChild(n1); merge.appendChild(n2);
      filter.appendChild(blur); filter.appendChild(cm); filter.appendChild(merge);
      defs.appendChild(filter);
      svg.appendChild(defs);

      const g = document.createElementNS(NS,"g");
      svg.appendChild(g);

      const countries = topoFeature(topo, topo.objects.countries).features;

      const projection = d3.geoEqualEarth();
      projection.fitSize([1100, 520], { type:"FeatureCollection", features:countries });
      const path = d3.geoPath(projection);

      const radar = document.createElementNS(NS,"circle");
      radar.setAttribute("r","22");
      radar.setAttribute("fill","rgba(0,255,0,0.05)");
      radar.setAttribute("stroke","rgba(0,255,0,0.35)");
      radar.setAttribute("stroke-width","1");
      radar.setAttribute("opacity","0.0");
      radar.setAttribute("filter","url(#neon)");
      g.appendChild(radar);

      const layer = document.createElementNS(NS,"g");
      g.appendChild(layer);

      for (let i=0;i<countries.length;i++){
        const f = countries[i];
        const p = document.createElementNS(NS,"path");
        p.setAttribute("d", path(f));
        p.setAttribute("fill", "rgba(0,255,0,0.06)");
        p.setAttribute("stroke","rgba(157,0,255,0.30)");
        p.setAttribute("stroke-width","1.0");
        p.setAttribute("vector-effect","non-scaling-stroke");
        p.setAttribute("filter","url(#neon)");
        const name = (f.properties && (f.properties.name || f.properties.NAME)) ? (f.properties.name || f.properties.NAME) : "UNKNOWN";
        p.dataset.name = name;

        p.addEventListener("mouseenter", function(){
          p.setAttribute("fill", "rgba(0,255,0,0.14)");
          p.setAttribute("stroke","rgba(0,255,0,0.75)");
          tooltip.style.display="block";
          tooltip.innerHTML = "<b>LOCK:</b> " + p.dataset.name + "<br/>STARCH//EXTRACT: " + (85+Math.random()*14).toFixed(1) + "%";
          if (AudioFX) AudioFX.scream();
        });
        p.addEventListener("mousemove", function(e){
          tooltip.style.left = (e.clientX + 14) + "px";
          tooltip.style.top  = (e.clientY + 14) + "px";
        });
        p.addEventListener("mouseleave", function(){
          p.setAttribute("fill","rgba(0,255,0,0.06)");
          p.setAttribute("stroke","rgba(157,0,255,0.30)");
          tooltip.style.display="none";
        });
        p.addEventListener("click", function(e){
          explodeChips(e.clientX, e.clientY, 24);
          if (AudioFX) AudioFX.blip(980, 0.05, "square");
          gsap.fromTo(p, {opacity:0.65}, {opacity:1, duration:0.25, ease:"steps(2)"});
        });

        layer.appendChild(p);
      }

      wrap.addEventListener("mousemove", function(e){
        const r = svg.getBoundingClientRect();
        const x = ((e.clientX - r.left) / r.width) * 1100;
        const y = ((e.clientY - r.top) / r.height) * 520;
        radar.setAttribute("cx", x);
        radar.setAttribute("cy", y);
        radar.setAttribute("opacity", "0.85");
      });
      wrap.addEventListener("mouseleave", function(){
        radar.setAttribute("opacity","0.0");
        tooltip.style.display="none";
      });

      gsap.fromTo(mapScan, {xPercent:-40, opacity:0.0}, {
        xPercent: 160,
        opacity: 0.9,
        ease: "none",
        scrollTrigger: { trigger: wrap, start:"top 75%", end:"bottom 25%", scrub:true }
      });

      ScrollTrigger.create({
        trigger: wrap,
        start:"top 65%",
        once:true,
        onEnter:function(){
          gsap.fromTo(g, {x:-8}, {x:0, duration:0.18, ease:"steps(2)", repeat:4, yoyo:true});
          if (AudioFX && AudioFX.enabled){
            AudioFX.blip(520, 0.05, "square");
            AudioFX.blip(860, 0.05, "square");
          }
        }
      });
    }

    async function initGlobe(){
      await whenGeoReady();
      const d3 = window.__d3geo;
      const topoFeature = window.__topoFeature;

      const canvas = document.getElementById("globe");
      const wrap = document.getElementById("globeWrap");
      const hud = document.getElementById("globeHud");
      if (!canvas || !wrap) return;

      const ctx = canvas.getContext("2d");
      const topoLand = await window.__getLandTopo();
      const land = topoFeature(topoLand, topoLand.objects.land);

      const w = canvas.width, h = canvas.height;

      const projection = d3.geoOrthographic()
        .translate([w/2, h/2])
        .scale(Math.min(w,h) * 0.37)
        .clipAngle(90);

      const path = d3.geoPath(projection, ctx);

      let rot = [0, -18, 0];
      let dragging = false;
      let last = null;
      let devourMode = false;

      function render(){
        ctx.clearRect(0,0,w,h);

        ctx.fillStyle = "rgba(0,0,0,0.35)";
        ctx.fillRect(0,0,w,h);

        ctx.beginPath();
        ctx.arc(w/2, h/2, projection.scale()+10, 0, Math.PI*2);
        ctx.fillStyle = "rgba(157,0,255,0.06)";
        ctx.fill();

        ctx.beginPath();
        ctx.arc(w/2, h/2, projection.scale(), 0, Math.PI*2);
        ctx.fillStyle = "rgba(0,255,0,0.03)";
        ctx.fill();

        projection.rotate(rot);
        ctx.save();
        ctx.beginPath();
        path(land);
        ctx.fillStyle = devourMode ? "rgba(0,255,0,0.18)" : "rgba(0,255,0,0.10)";
        ctx.fill();
        ctx.lineWidth = 1.2;
        ctx.strokeStyle = devourMode ? "rgba(0,255,0,0.85)" : "rgba(157,0,255,0.45)";
        ctx.stroke();
        ctx.restore();

        const t = performance.now()*0.0025;
        const r = projection.scale() * (0.65 + 0.08*Math.sin(t));
        ctx.beginPath();
        ctx.arc(w/2, h/2, r, 0, Math.PI*2);
        ctx.strokeStyle = "rgba(0,255,0,0.18)";
        ctx.lineWidth = 2;
        ctx.stroke();

        if (document.body.classList.contains("chaos") || devourMode){
          for (let i=0;i<5;i++){
            const y = (Math.random()*h)|0;
            ctx.fillStyle = (Math.random()<0.5) ? "rgba(0,255,0,0.06)" : "rgba(157,0,255,0.05)";
            ctx.fillRect(0, y, w, 2 + (Math.random()*2));
          }
        }
      }

      function animate(){
        if (!dragging) rot[0] += (devourMode ? 0.65 : 0.18);
        render();
        requestAnimationFrame(animate);
      }
      animate();

      wrap.addEventListener("pointerdown", function(e){
        dragging = true;
        last = {x:e.clientX, y:e.clientY};
        wrap.setPointerCapture(e.pointerId);
        if (AudioFX) AudioFX.blip(420, 0.05, "square");
      });
      wrap.addEventListener("pointermove", function(e){
        if (!dragging) return;
        const dx = e.clientX - last.x;
        const dy = e.clientY - last.y;
        last = {x:e.clientX, y:e.clientY};
        rot[0] += dx*0.25;
        rot[1] -= dy*0.18;
        if (rot[1] > 80) rot[1] = 80;
        if (rot[1] < -80) rot[1] = -80;
        if (hud) hud.textContent = "ROT: " + rot[0].toFixed(1) + " / " + rot[1].toFixed(1);
      });
      wrap.addEventListener("pointerup", function(){ dragging=false; });
      wrap.addEventListener("pointercancel", function(){ dragging=false; });

      wrap.addEventListener("mousemove", function(){
        if (!hud) return;
        hud.textContent = devourMode ? "LOCK: DEVOUR MODE" : "LOCK: HEMISPHERE";
      });

      const devBtn = document.getElementById("globeDevourBtn");
      const resetBtn = document.getElementById("globeResetBtn");
      if (devBtn) devBtn.onclick = function(){
        devourMode = !devourMode;
        if (AudioFX) AudioFX.scream();
        gsap.fromTo(wrap, {filter:"hue-rotate(55deg) contrast(1.5)"}, {filter:"none", duration:0.35, ease:"steps(2)"});
      };
      if (resetBtn) resetBtn.onclick = function(){
        rot = [0, -18, 0];
        if (AudioFX) AudioFX.blip(720, 0.06, "square");
      };

      ScrollTrigger.create({
        trigger: wrap,
        start:"top 70%",
        end:"bottom 35%",
        onUpdate:function(self){
          if (self.progress > 0.7 && AudioFX && AudioFX.enabled && Math.random() < 0.05){
            AudioFX.blip(520 + Math.random()*520, 0.03, "square");
          }
        }
      });
    }

    function initTerminal(){
      const box = document.getElementById("termBig");
      const lines = document.getElementById("termLines");
      const input = document.getElementById("termInput");
      if (!box || !lines || !input) return;

      function out(s){
        lines.textContent += s + "\n";
        box.scrollTop = box.scrollHeight;
      }

      out("[KRAHMAL-OS] booting...");
      out("[NET] starchnet link: ESTABLISHED");
      out("type 'help' to see commands.");

      function run(cmdRaw){
        const cmd = (cmdRaw||"").trim();
        if (!cmd) return;
        out("starch@overlord:~$ " + cmd);

        const parts = cmd.split(/\s+/);
        const c = (parts[0]||"").toLowerCase();
        const arg = (parts[1]||"").toLowerCase();

        if (AudioFX) AudioFX.blip(640, 0.04, "square");

        if (c === "help"){
          out("commands:");
          out("  help");
          out("  scan");
          out("  map | globe | vault");
          out("  devour");
          out("  chaos on/off");
          return;
        }
        if (c === "scan"){
          out("[SCAN] harvesting... 33%");
          out("[SCAN] harvesting... 66%");
          out("[SCAN] harvesting... 99%");
          out("[OK] starch extracted: +" + (1000 + (Math.random()*9000|0)) + "g");
          if (AudioFX) AudioFX.scream();
          return;
        }
        if (c === "map" || c === "globe" || c === "vault"){
          navigateTo("/" + c, true);
          return;
        }
        if (c === "devour"){
          out("[DEVOUR] SCREEN CONSUMPTION INIT...");
          if (AudioFX) AudioFX.scream();
          gsap.fromTo("body", {filter:"contrast(1.55) saturate(1.5) hue-rotate(45deg)"}, {filter:"none", duration:0.35, ease:"steps(2)"});
          setTimeout(function(){ window.location.href="/404"; }, 1800);
          return;
        }
        if (c === "chaos"){
          if (arg === "on") setChaos(true);
          if (arg === "off") setChaos(false);
          out("[CHAOS] " + (chaos ? "ON" : "OFF"));
          return;
        }

        out("[ERR] unknown command: " + c);
        out("hint: help");
      }

      input.focus();
      box.addEventListener("click", function(){ input.focus(); });

      input.addEventListener("keydown", function(e){
        if (e.key === "Enter"){
          e.preventDefault();
          const cmd = input.textContent;
          input.textContent = "";
          run(cmd);
        }
      });
    }

    function initVault(){
      const cards = $$(".vaultCard");
      cards.forEach(function(c, idx){
        gsap.fromTo(c, {y: 10, opacity:0}, {y:0, opacity:1, duration:0.25, delay: idx*0.05, ease:"steps(2)"});
        c.addEventListener("mouseenter", function(){
          if (AudioFX) AudioFX.scream();
          gsap.fromTo(c, {x:-4}, {x:0, duration:0.18, ease:"steps(2)", repeat:2, yoyo:true});
        });
      });
      $$(".vaultBtn").forEach(function(btn){
        btn.addEventListener("click", function(e){
          explodeChips(e.clientX, e.clientY, 28);
          gsap.fromTo(btn, {filter:"hue-rotate(45deg)"}, {filter:"none", duration:0.22, ease:"steps(2)"});
          if (AudioFX){
            AudioFX.blip(1020, 0.05, "square");
            AudioFX.blip(420, 0.06, "square");
          }
        });
      });
    }

    const PAGES = __PAGES_JSON__;

    (async function(){
      const page = document.body.getAttribute("data-page") || "home";
      setActiveNav(page);
      await initPage(page);
      ScrollTrigger.refresh(true);
    })();
  </script>

  <script type="module">
    import * as d3geo from "https://cdn.jsdelivr.net/npm/d3-geo@3/+esm";
    import { feature } from "https://cdn.jsdelivr.net/npm/topojson-client@3/+esm";
    window.__d3geo = d3geo;
    window.__topoFeature = feature;

    window.__worldTopoPromise = null;
    window.__getWorldTopo = () => {
      if (!window.__worldTopoPromise){
        window.__worldTopoPromise = fetch("https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json").then(r=>r.json());
      }
      return window.__worldTopoPromise;
    };

    window.__landTopoPromise = null;
    window.__getLandTopo = () => {
      if (!window.__landTopoPromise){
        window.__landTopoPromise = fetch("https://cdn.jsdelivr.net/npm/world-atlas@2/land-110m.json").then(r=>r.json());
      }
      return window.__landTopoPromise;
    };
  </script>
</body>
</html>
"""

ERROR_404_HTML = r"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>404 — ВЫ СТАЛИ ЧАСТЬЮ КАРТОФЕЛЬНОЙ СЕТИ</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Orbitron:wght@600;800&display=swap" rel="stylesheet">
  <style>
    :root{--acid:#00FF00;--violet:#9D00FF;--bg:#050007}
    html,body{height:100%}
    body{
      margin:0;
      background:
        radial-gradient(900px 520px at 20% 15%, rgba(157,0,255,.22), transparent 55%),
        radial-gradient(900px 520px at 80% 40%, rgba(0,255,0,.15), transparent 55%),
        linear-gradient(180deg,#000,var(--bg),#000);
      color: rgba(215,255,215,.92);
      display:grid;
      place-items:center;
      font-family: Orbitron, system-ui, sans-serif;
      overflow:hidden;
    }
    .scan{
      position:fixed; inset:0; pointer-events:none;
      background: repeating-linear-gradient(to bottom, rgba(0,0,0,0) 0px, rgba(0,0,0,0) 2px, rgba(0,0,0,.25) 3px, rgba(0,0,0,0) 4px);
      opacity:.55;
      animation: flicker 2.1s infinite steps(2,end);
    }
    @keyframes flicker{0%{opacity:.55} 18%{opacity:.28} 36%{opacity:.65} 54%{opacity:.32} 72%{opacity:.62} 100%{opacity:.55}}
    .box{
      width:min(980px, 92vw);
      border:1px solid rgba(0,255,0,.25);
      background: rgba(0,0,0,.55);
      padding:18px 16px;
      box-shadow: 0 0 0 1px rgba(157,0,255,.16) inset, 0 0 40px rgba(0,255,0,.10);
      backdrop-filter: blur(10px);
    }
    h1{
      margin:0 0 10px;
      font-size: clamp(22px, 3.2vw, 44px);
      text-transform:uppercase;
      letter-spacing:.08em;
      position:relative;
    }
    .glitch::before,.glitch::after{content: attr(data-text); position:absolute; left:0; top:0; width:100%; opacity:.95; mix-blend-mode: screen;}
    .glitch::before{color:var(--acid); transform:translate(-2px,0); animation:a 2.2s infinite linear}
    .glitch::after{color:var(--violet); transform:translate(2px,0); animation:b 1.8s infinite linear}
    @keyframes a{0%{clip-path: inset(0 0 80% 0)} 25%{clip-path: inset(20% 0 55% 0)} 50%{clip-path: inset(65% 0 12% 0)} 75%{clip-path: inset(10% 0 70% 0)} 100%{clip-path: inset(0 0 80% 0)}}
    @keyframes b{0%{clip-path: inset(78% 0 2% 0)} 30%{clip-path: inset(14% 0 62% 0)} 60%{clip-path: inset(48% 0 28% 0)} 100%{clip-path: inset(78% 0 2% 0)}}
    p{margin:0; font-family: "Press Start 2P", monospace; font-size:12px; line-height:1.7; color: rgba(0,255,0,.9);}
    .row{display:flex; gap:12px; flex-wrap:wrap; margin-top:14px}
    a{color: rgba(215,255,215,.9); text-decoration:none; border:1px solid rgba(157,0,255,.22); padding:10px 12px; font-family: "Press Start 2P", monospace; font-size:11px; background: rgba(0,0,0,.35);}
    a:hover{border-color: rgba(0,255,0,.55); color: var(--acid)}
  </style>
</head>
<body>
  <div class="scan"></div>
  <div class="box">
    <h1 class="glitch" data-text="404: ВЫ СТАЛИ ЧАСТЬЮ КАРТОФЕЛЬНОЙ СЕТИ">404: ВЫ СТАЛИ ЧАСТЬЮ КАРТОФЕЛЬНОЙ СЕТИ</h1>
    <p>КРАХМАЛИЗАЦИЯ ЗАВЕРШЕНА. ПЮРЕ-СЕТЬ ИНИЦИАЛИЗИРОВАНА. ДАННЫЕ ПРИНАДЛЕЖАТ 🥔</p>
    <div class="row">
      <a href="/">ВЕРНУТЬСЯ В СЕТЬ</a>
      <a href="#noop" onclick="location.reload()">ПОВТОРИТЬ ГЛИТЧ</a>
    </div>
  </div>
</body>
</html>
"""

def shell_html(initial_page: str) -> str:
    if initial_page not in PARTIALS:
        initial_page = "home"
    html = BASE_HTML
    html = html.replace("__TITLE__", initial_page.upper())
    html = html.replace("__INITIAL_PAGE__", initial_page)
    html = html.replace("__INITIAL_PARTIAL__", PARTIALS[initial_page])
    html = html.replace("__PAGES_JSON__", json.dumps(list(PARTIALS.keys()), ensure_ascii=False))
    return html

@app.get("/")
def home():
    return Response(shell_html("home"), mimetype="text/html; charset=utf-8")

@app.get("/map")
def map_page():
    return Response(shell_html("map"), mimetype="text/html; charset=utf-8")

@app.get("/globe")
def globe_page():
    return Response(shell_html("globe"), mimetype="text/html; charset=utf-8")

@app.get("/terminal")
def terminal_page():
    return Response(shell_html("terminal"), mimetype="text/html; charset=utf-8")

@app.get("/vault")
def vault_page():
    return Response(shell_html("vault"), mimetype="text/html; charset=utf-8")

@app.get("/_partial/<name>")
def partial(name: str):
    html = PARTIALS.get(name)
    if not html:
        return Response("not found", status=404, mimetype="text/plain; charset=utf-8")
    return Response(html, mimetype="text/html; charset=utf-8")

@app.get("/404")
def error_page():
    return Response(ERROR_404_HTML, status=404, mimetype="text/html; charset=utf-8")

@app.errorhandler(404)
def any_404(_):
    return Response(ERROR_404_HTML, status=404, mimetype="text/html; charset=utf-8")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=25616, debug=False)
