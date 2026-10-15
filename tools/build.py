#!/usr/bin/env python3
"""Builds the static site: <lang>/{index,privacy,support}.html for ten languages, the language pickers at the root
and the stylesheet. Texts live in tools/content_*.py (landing page and support) and tools/privacy/<lang>.html (the privacy policy).

Usage (from the repo root):  python3 tools/build.py [--policies ../kwity-ios/Kwity/Resources]
With --policies the privacy policies of the languages the app has (all ten) are re-read from the app's
`<lang>.lproj/PrivacyPolicy.html` first, so the site and the app never say different things.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_de_fr_es import DE, ES, FR  # noqa: E402
from content_it_uk_ru import IT, RU, UK  # noqa: E402
from content_ja_zh import JA, ZH  # noqa: E402
from content_pl_en import EN, PL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://haker.dev/kwity-public"
LANGS = [PL, EN, DE, FR, ES, IT, UK, RU, JA, ZH]
MAIL = "marcin.polak@ideaapps.io"
FORM = "https://forms.gle/NSWuiSGS5Xyxgx7UA"
APP_STORE = "https://apps.apple.com/app/id6820909795"
APP_FOLDER = {"pl": "pl", "en": "en", "es": "es", "it": "it", "de": "de", "ru": "ru", "zh": "zh-Hans", "fr": "fr", "uk": "uk", "ja": "ja"}

STYLE = """\
:root{color-scheme:dark;--bg:#14102E;--surface:rgba(255,255,255,.08);--ink:#FFFFFF;--soft:#B9BDD0;--accent:#C6F24E;--border:rgba(255,255,255,.18);--on:#17132E}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Manrope",-apple-system,BlinkMacSystemFont,"Helvetica Neue","Hiragino Sans","PingFang SC",Arial,sans-serif;font-size:17px;line-height:1.6;-webkit-text-size-adjust:100%}
body:before{content:"";position:fixed;inset:0;z-index:-1;background:radial-gradient(60% 40% at 90% -5%,rgba(120,80,230,.34),transparent 70%),radial-gradient(60% 45% at -5% 105%,rgba(20,150,140,.26),transparent 70%)}
.wrap{max-width:720px;margin:0 auto;padding:28px 20px 56px}
nav{display:flex;gap:6px 18px;flex-wrap:wrap;align-items:center;margin-bottom:36px;font-weight:800}
nav a{color:var(--ink);text-decoration:none}nav a:hover,nav a[aria-current]{color:var(--accent)}
nav .brand{margin-right:auto;font-size:20px;display:flex;align-items:center;gap:10px}
.mark{width:30px;height:30px;border-radius:9px;background:var(--accent);color:var(--on);display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:18px;line-height:1}
.langs{position:relative}
.langs summary{cursor:pointer;list-style:none;color:var(--soft);font-weight:700;font-size:15px;padding:4px 0}
.langs summary::-webkit-details-marker{display:none}
.langs summary::after{content:" \\25BE"}
.langs ul{position:absolute;right:0;top:100%;z-index:5;margin:6px 0 0;padding:6px;list-style:none;background:#241E55;border:1px solid var(--border);border-radius:14px;min-width:170px}
.langs li{margin:0}.langs li a{display:block;padding:7px 12px;border-radius:9px;font-weight:600}
.langs li a:hover,.langs li a[aria-current]{background:rgba(255,255,255,.1);color:var(--accent)}
@media (max-width:560px){.langs{width:100%}.langs ul{position:static}}
h1{font-size:clamp(30px,7vw,44px);line-height:1.12;margin:0 0 10px;letter-spacing:-.01em;text-wrap:balance;color:var(--accent)}
h2{font-size:21px;margin:34px 0 8px}
p,li{color:var(--ink)}p{margin:0 0 14px}ul{padding-left:22px;margin:0 0 14px}li{margin-bottom:6px}
.lead{font-size:19px;color:var(--soft);margin-bottom:26px}
.updated{font-size:13px;font-weight:700;color:var(--soft);margin:0 0 24px}
.card,.callout{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:18px 20px;margin:0 0 20px}
.card strong,.callout strong{color:var(--accent)}
a{color:var(--accent)}
.btn{display:inline-block;padding:13px 26px;border-radius:999px;background:var(--accent);color:var(--on);font-weight:800;text-decoration:none}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin:0 0 22px}
.btn.ghost{background:var(--surface);color:var(--ink);border:1px solid var(--border)}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));margin:0 0 24px}
.grid .card{margin:0}.grid h3{margin:0 0 6px;font-size:17px;color:var(--accent)}.grid p{margin:0;color:var(--soft);font-size:15px}
details.q{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:14px 18px;margin:0 0 10px}
details.q summary{cursor:pointer;font-weight:800}details.q p{margin:10px 0 0;color:var(--soft)}
.pick{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin:0 0 24px}
.pick a{display:block;padding:14px 18px;border-radius:16px;background:var(--surface);border:1px solid var(--border);color:var(--ink);text-decoration:none;font-weight:800}
.pick a:hover{border-color:var(--accent);color:var(--accent)}.pick small{display:block;color:var(--soft);font-weight:600}
footer{margin-top:44px;color:var(--soft);font-size:13px;display:flex;gap:16px;flex-wrap:wrap}
footer a{color:var(--soft)}
"""


def esc(text):
    return html.escape(text, quote=False)


def mail_link():
    return f'<a href="mailto:{MAIL}">{MAIL}</a>'


def head(lang, page, title, description, depth="../"):
    alternates = "".join(
        f'<link rel="alternate" hreflang="{l["html_lang"]}" href="{BASE}/{l["folder"]}/{page}">' for l in LANGS)
    return f"""<!doctype html>
<html lang="{lang['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="stylesheet" href="{depth}style.css">
{alternates}
</head>
"""


def nav(lang, page):
    items = "".join(
        f'<li><a href="../{l["folder"]}/{page}" hreflang="{l["html_lang"]}" lang="{l["html_lang"]}"'
        f'{" aria-current=\"true\"" if l is lang else ""}>{l["label"]}</a></li>' for l in LANGS)
    cur = lambda name: ' aria-current="page"' if page == name else ""  # noqa: E731
    return (f'<nav><a class="brand" href="index.html"><span class="mark">K</span>Kwity</a>'
            f'<a href="privacy.html"{cur("privacy.html")}>{esc(lang["nav_privacy"])}</a>'
            f'<a href="support.html"{cur("support.html")}>{esc(lang["nav_support"])}</a>'
            f'<details class="langs"><summary>{lang["label"]}</summary><ul>{items}</ul></details></nav>')


def foot(lang):
    return (f'<footer><span>{lang["footer_copy"]}</span><a href="privacy.html">{esc(lang["nav_privacy"])}</a>'
            f'<a href="support.html">{esc(lang["nav_support"])}</a></footer>')


def wrap(lang, page, title, description, body):
    return (head(lang, page, title, description) + '<body>\n<div class="wrap">\n  ' + nav(lang, page) + "\n\n" + body
            + "\n  " + foot(lang) + "\n</div>\n</body>\n</html>\n")


def index_page(lang):
    c = lang["index"]
    cards = "\n".join(f'    <div class="card"><h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for t, p in c["cards"])
    body = f"""  <h1>{esc(c['h1'])}</h1>
  <p class="lead">{esc(c['lead'])}</p>
  <div class="btns">
    <a class="btn" href="{APP_STORE}">{esc(c['download'])}</a>
    <a class="btn ghost" href="support.html">{esc(c['support_btn'])}</a>
    <a class="btn ghost" href="privacy.html">{esc(c['privacy_btn'])}</a>
  </div>
  <div class="grid">
{cards}
  </div>
  <p class="updated">{esc(c['note'])}</p>"""
    return wrap(lang, "index.html", c["title"], c["description"], body)


def support_page(lang):
    c = lang["support"]
    faq = "\n".join(f'  <details class="q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in c["qa"])
    body = f"""  <h1>{esc(c['h1'])}</h1>
  <p class="lead">{esc(c['lead'])}</p>
  <div class="btns">
    <a class="btn" href="{FORM}">{esc(c['report'])}</a>
    <a class="btn ghost" href="mailto:{MAIL}?subject=Kwity">{esc(c['mail'])}</a>
    <a class="btn ghost" href="privacy.html">{esc(c['privacy'])}</a>
  </div>
  <p>{esc(c['mail_line']).replace('{mail}', mail_link())}</p>

  <h2>{esc(c['faq'])}</h2>
{faq}"""
    return wrap(lang, "support.html", c["title"], c["description"], body)


def privacy_page(lang):
    fragment = (ROOT / "tools" / "privacy" / f"{lang['folder']}.html").read_text(encoding="utf-8").rstrip()
    title = re.search(r"<h1>(.*?)</h1>", fragment).group(1)
    summary = re.search(r"<strong>.*?</strong>(.*?)\n", fragment, re.S)
    description = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", summary.group(1))).strip()[:200] if summary else title
    return wrap(lang, "privacy.html", f"{title} | Kwity", description, fragment)


def root_page(page):
    """The page at the root of the site: sends the browser to its language and lists them all."""
    links = "".join(
        f'<a href="{l["folder"]}/{page}" hreflang="{l["html_lang"]}" lang="{l["html_lang"]}">{l["label"]}<small>{esc(l["pick"])}</small></a>'
        for l in LANGS)
    mapping = ",".join(f'"{l["folder"]}":"{l["folder"]}"' for l in LANGS)
    alternates = "".join(f'<link rel="alternate" hreflang="{l["html_lang"]}" href="{BASE}/{l["folder"]}/{page}">' for l in LANGS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kwity</title>
<meta name="description" content="Kwity: receipts and warranties. Choose a language.">
<link rel="stylesheet" href="style.css">
{alternates}
<script>
(function () {{
  var known = {{{mapping}}};
  var prefs = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || "en"];
  for (var i = 0; i < prefs.length; i++) {{
    var code = String(prefs[i]).toLowerCase().split("-")[0];
    if (known[code]) {{ location.replace(known[code] + "/{page}" + location.hash); return; }}
  }}
  location.replace("en/{page}" + location.hash);
}})();
</script>
</head>
<body>
<div class="wrap">
  <nav><span class="brand"><span class="mark">K</span>Kwity</span></nav>
  <div class="pick">{links}</div>
</div>
</body>
</html>
"""


def main():
    if "--policies" in sys.argv:
        source = Path(sys.argv[sys.argv.index("--policies") + 1])
        for folder, app in APP_FOLDER.items():
            text = (source / f"{app}.lproj" / "PrivacyPolicy.html").read_text(encoding="utf-8")
            body = re.search(r"<body>\n(.*)\n</body>", text, re.S).group(1)
            (ROOT / "tools" / "privacy" / f"{folder}.html").write_text(body.rstrip() + "\n", encoding="utf-8")
    (ROOT / "style.css").write_text(STYLE, encoding="utf-8")
    for lang in LANGS:
        folder = ROOT / lang["folder"]
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(index_page(lang), encoding="utf-8")
        (folder / "privacy.html").write_text(privacy_page(lang), encoding="utf-8")
        (folder / "support.html").write_text(support_page(lang), encoding="utf-8")
    for page in ("index.html", "privacy.html", "support.html"):
        (ROOT / page).write_text(root_page(page), encoding="utf-8")
    print("built", ", ".join(l["folder"] for l in LANGS))


if __name__ == "__main__":
    main()
