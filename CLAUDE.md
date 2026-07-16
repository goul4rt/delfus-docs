# CLAUDE.md — delfus-docs

Documentação de usuário do Delfus. MkDocs Material → GitHub Pages em https://docs.delfus.app.
Repo separado do bot (`../discord-bot`) e do painel (`../front-end`).

## Comandos

```bash
source .venv/bin/activate            # venv já criado
mkdocs serve -a 127.0.0.1:8001       # preview local
mkdocs build --strict                # build (zero links quebrados)
```

Plugins: search, glightbox (zoom em imagem), git-revision-date.

## Gotchas (não-óbvios)

- **og-images NÃO usam o plugin social** (removido). São estáticas: `tools/og/generate.py`
  renderiza `tools/og/template.html` via Playwright → `docs/assets/og/<slug>.jpg` (slug =
  caminho do .md com `/`→`-`). Meta og/twitter emitidas em `overrides/main.html`. Ao criar
  página nova ou mudar `description:`/H1, rode
  `.venv/bin/python tools/og/generate.py [--only slug]` e commite o jpg.
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
4. Esconder overlay do Next antes do screenshot: inserir `<style>nextjs-portal,[data-nextjs-toast]{display:none!important}</style>`.
5. **Modais de criar/editar ABREM no demo** (desde a branch `demo-completeness` em `delfus-v2`): mutações viram no-op (`src/lib/demo-noop.ts`), nada persiste. Clicar "Novo Plano"/"Criar" e printar o dialog.

Classificar OK/vazio: olhar o texto do `<main>` (NÃO o body inteiro — o seletor de guild renderiza "Nenhum servidor" e dá falso-positivo). Procurar `Erro ao carregar` / a mensagem de vazio própria da feature.

## Conteúdo

Páginas de feature geradas/revisadas por workflow (lê o código do bot em `../discord-bot` + front-end).
Escrita: direta, enxuta, sem cacoetes de IA. Re-inserir screenshots após reescrever (script anexa o
print antes de `## Como funciona`).

## Expandir cobertura (demo + docs) — fluxo repetível

Spec/plan da rodada original: `specs/2026-06-18-docs-completeness-*`. Estado: ver memória `project_demo_completeness`.

Para cobrir uma feature nova do dashboard:

1. **Auditar de verdade** (não estático): subir o front em demo, abrir a rota, ler o `<main>`.
   "Tem `isDemoMode` check?" NÃO garante que renderiza — a análise estática super-estima gaps.
   Só é gap se a tela der erro ou mostrar o vazio próprio dela.
2. **Demo data** (se vazio): criar `src/features/<feat>/utils/demo-<feat>-generator.ts` tipado
   aos tipos reais (espelhar `demo-vip-generator.ts`), e ramificar a read em
   `if (isDemoMode()) { const {gen}=await import(...); return gen(); }` (ver `starboard/api.ts`).
   `bun run tsc --noEmit` limpo. Commit na branch `demo-completeness` (NUNCA na main do front; é prod).
3. **Polish**: nomes BR variados + @handles, avatares Discord (`cdn.discordapp.com/embed/avatars/0..5.png`),
   números não-redondos, embeds com título+emoji, descrição com `{{user}}/{{server}}/{{memberCount}}`, cor da marca.
4. **Screenshot** (seção acima) em dark+azul.
5. **Doc**: workflow gera a página (fundamentada no código), embed do print, adicionar à `nav` do mkdocs.yml.
6. **Push**: front via gh helper (`https://github.com/goul4rt/delfus-v2.git demo-completeness`); docs na main.
   Branch do front fica em PR — repo de produção, merge é decisão do usuário.

Telas sem doc de propósito (internas/triviais): `changelog`, `getting-started`, `product`, `bot-config`.
