"""Hooks de SEO do build.

- FAQPage JSON-LD: extrai as Q&A da seção "Perguntas frequentes" do HTML
  renderizado de cada página (o template não consegue — page.toc só tem os
  títulos, não as respostas) e guarda em page.meta pro overrides/main.html emitir.
- llms-full.txt: concatena o markdown de todas as páginas num arquivo único
  pra ingestão direta por LLMs (complementa o docs/llms.txt).
"""

import html
import json
import re
from pathlib import Path

# h2 "Perguntas frequentes" até o próximo h2 (ou fim)
_FAQ_SECTION = re.compile(
    r'<h2 id="perguntas-frequentes">.*?(?=<h2 |$)', re.S
)
# cada h3 (pergunta) e o que vem até o próximo h3/h2 (resposta)
_QA = re.compile(
    r'<h3 id="[^"]*">(.*?)</h3>(.*?)(?=<h3 |<h2 |$)', re.S
)
_TAGS = re.compile(r"<[^>]+>")


def _text(fragment: str) -> str:
    return html.unescape(_TAGS.sub("", fragment)).replace("¶", "").strip()


def on_page_content(html_content, page, config, files):
    section = _FAQ_SECTION.search(html_content)
    if not section:
        return html_content
    qas = [
        {
            "@type": "Question",
            "name": _text(q),
            "acceptedAnswer": {"@type": "Answer", "text": _text(a)},
        }
        for q, a in _QA.findall(section.group(0))
        if _text(q) and _text(a)
    ]
    if qas:
        page.meta["faq_jsonld"] = json.dumps(
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qas},
            ensure_ascii=False,
        )
    return html_content


def on_post_build(config):
    docs = Path(config["docs_dir"])
    site = Path(config["site_dir"])
    parts = []
    for md in sorted(docs.rglob("*.md")):
        body = md.read_text(encoding="utf-8")
        # remove frontmatter
        body = re.sub(r"\A---\n.*?\n---\n", "", body, flags=re.S)
        parts.append(f"<!-- {md.relative_to(docs)} -->\n\n{body.strip()}\n")
    (site / "llms-full.txt").write_text("\n\n---\n\n".join(parts), encoding="utf-8")
