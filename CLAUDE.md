# CLAUDE.md — delfus-docs

Documentação de usuário do Delfus. MkDocs Material → GitHub Pages em https://docs.delfus.app.
Repo separado do bot (`../discord-bot`) e do painel (`../front-end`).

## Comandos

```bash
source .venv/bin/activate            # venv já criado
mkdocs serve -a 127.0.0.1:8001       # preview local
mkdocs build --strict                # build (zero links quebrados)
```

Plugins: search, social (og-images), glightbox (zoom em imagem), git-revision-date.

## Gotchas (não-óbvios)

- **Build local quebra sem libs de imagem.** O social plugin usa Cairo/Pango. Prefixe:
  `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib mkdocs build`. No CI o workflow instala via apt.
- **og-image: `background_color: transparent`** é obrigatório no `cards_layout_options` — senão
  o plugin pinta a cor opaca POR CIMA do `background_image` (fundo da marca em `docs/assets/og-bg.png`).
- **`git push` falha** (identidade SSH errada). Pushe via:
  `git -c credential.helper='!gh auth git-credential' push https://github.com/goul4rt/delfus-docs.git main`.
  Nunca force-push.
- **Deploy**: push em `main` → Actions roda `mkdocs gh-deploy`. CDN do Pages demora ~1-3 min; ao
  verificar use cache-bust (`?cb=$RANDOM`) e tenha paciência (o index cacheia mais).
- **Domínio**: `docs/CNAME` (= docs.delfus.app) + `site_url` no mkdocs.yml. Não remover o CNAME.

## Home (docs/index.md)

- É **HTML puro** (sem atributo `markdown` no `<div class="dx-home">`) — com `markdown`, o md_in_html
  ejeta filhos do flex e quebra o hero. Estilos em `docs/stylesheets/extra.css` (classes `.dxh-*`).
- Ícones são **SVG inline do Lucide** (mesmo DS do front-end), não emoji.
- Mascote: PNGs já transparentes em `Delfus/` (ex.: `image 24.png` → `docs/assets/mascote-hero.png`).

## Screenshots do painel (via demo mode do front-end)

Telas em `docs/assets/dashboard/*.png` vêm do `../front-end` em demo mode:

1. Patchar `../front-end/src/middleware.ts` (comentar redirect de `/dashboard`) — **REVERTER depois**
   com `git checkout`.
2. Subir `bun run dev` com `DATABASE_URL`/`REDIS_HOST`/`BOT_API_URL` neutralizados p/ localhost
   (`REDIS_PASSWORD` não-vazio). O `.env.local` aponta p/ PRODUÇÃO — sempre neutralizar.
3. Playwright: `localStorage['theme']='dark'`, cookie `active_theme=blue`,
   `localStorage['dashboard-storage']={state:{selectedGuildId:'demo-guild',isDemoModeActive:true,hasSeenWelcome:true}}`.
4. **Modais de criação ficam `disabled` no demo** — só dá pra capturar navegação/abas, não dialogs.

## Conteúdo

19 páginas de feature geradas/revisadas por workflow (lê o código do bot em `../discord-bot`).
Escrita: direta, enxuta, sem cacoetes de IA. Re-inserir screenshots após reescrever (script anexa o
print antes de `## Como funciona`).
