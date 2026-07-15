# delfus-docs

Documentação oficial do [Delfus](https://delfus.app), bot para Discord com moderação,
anti-raid, cargos automáticos, VIP, starboard e análise de comunidade — construída com
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

**📖 Leia em: https://docs.delfus.app**

Seções principais: [Primeiros passos](https://docs.delfus.app/comecar/adicionar/) ·
[Funcionalidades](https://docs.delfus.app/funcionalidades/) ·
[Moderação](https://docs.delfus.app/funcionalidades/moderacao/) ·
[Anti-raid](https://docs.delfus.app/funcionalidades/anti-raid/) ·
[VIP](https://docs.delfus.app/funcionalidades/vip/) ·
[Suporte](https://docs.delfus.app/suporte/)

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
