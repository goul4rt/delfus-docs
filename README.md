# delfus-docs

Documentação oficial do [Delfus](https://delfus.app) — construída com
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Rodar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Abra http://127.0.0.1:8000.

## Build

```bash
mkdocs build   # gera o site estático em site/
```

## Deploy

Push para `main` dispara o workflow `.github/workflows/deploy.yml`, que publica no
GitHub Pages via `mkdocs gh-deploy`.
