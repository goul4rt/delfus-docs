#!/usr/bin/env python3
"""Gera as og-images (1200x630) de todas as páginas a partir de tools/og/template.html.

Uso:  .venv/bin/python tools/og/generate.py [--only slug]
Saída: docs/assets/og/<slug>.jpg  (slug = caminho do .md com "/" virando "-")

Requer: playwright instalado no venv (playwright install chromium).
Fontes (Sora / Instrument Sans) vêm do Google Fonts — precisa de rede.
"""

import argparse
import html
import re
import sys
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OUT = DOCS / "assets" / "og"
TEMPLATE = Path(__file__).parent / "template.html"
SITE_HOST = "docs.delfus.app"


def load_nav():
    """Lê a nav do mkdocs.yml ignorando tags !!python."""
    class Loader(yaml.SafeLoader):
        pass

    Loader.add_multi_constructor("tag:yaml.org,2002:python/name:", lambda l, s, n: None)
    config = yaml.load((ROOT / "mkdocs.yml").read_text(), Loader=Loader)
    return config["nav"]


def walk_nav(items, trail=()):
    """Gera (src_uri, trilha de seções) para cada página da nav."""
    for item in items:
        for title, value in item.items():
            if isinstance(value, str):
                yield value, trail
            else:
                yield from walk_nav(value, trail + (title,))


def front_matter(md_path):
    text = md_path.read_text()
    meta = {}
    if text.startswith("---"):
        end = text.index("---", 3)
        meta = yaml.safe_load(text[3:end]) or {}
        text = text[end + 3:]
    return meta, text


def first_h1(body):
    m = re.search(r"^# (.+)$", body, re.M)
    return m.group(1).strip() if m else None


def title_size(title):
    n = len(title)
    return "46px" if n > 46 else "54px" if n > 30 else "64px"


def build_pages():
    pages = []
    for src, trail in walk_nav(load_nav()):
        md = DOCS / src
        meta, body = front_matter(md)
        title = first_h1(body)
        eyebrow = trail[-1] if trail else "Documentação"
        if src == "index.md":
            title = "Documentação do Delfus"
        elif src == "suporte.md":
            title = "Precisa de uma mão?"
            eyebrow = "Suporte"
        url = SITE_HOST + "/" + re.sub(r"(index)?\.md$", "", src).rstrip("/")
        pages.append({
            "slug": src.replace("/", "-").removesuffix(".md"),
            "eyebrow": eyebrow,
            "title": title,
            "description": meta.get("description", ""),
            "url": url.rstrip("/") if url.endswith(SITE_HOST + "/") is False else SITE_HOST,
        })
    return pages


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="gerar apenas o slug informado")
    args = parser.parse_args()

    pages = build_pages()
    if args.only:
        pages = [p for p in pages if p["slug"] == args.only]
        if not pages:
            sys.exit(f"slug não encontrado: {args.only}")

    OUT.mkdir(parents=True, exist_ok=True)
    template = TEMPLATE.read_text()

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630})
        for p in pages:
            filled = (
                template
                .replace("__EYEBROW__", html.escape(p["eyebrow"]))
                .replace("__TITLE__", html.escape(p["title"]))
                .replace("__TITLE_SIZE__", title_size(p["title"]))
                .replace("__DESCRIPTION__", html.escape(p["description"]))
                .replace("__URL__", html.escape(p["url"]))
            )
            tmp = TEMPLATE.parent / f"_render-{p['slug']}.html"
            tmp.write_text(filled)
            page.goto(tmp.as_uri())
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(250)
            out = OUT / f"{p['slug']}.jpg"
            page.screenshot(path=str(out), type="jpeg", quality=85)
            tmp.unlink()
            print(f"{out.relative_to(ROOT)}  ({p['eyebrow']} · {p['title']})")
        browser.close()

    print(f"\n{len(pages)} cards gerados em {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
