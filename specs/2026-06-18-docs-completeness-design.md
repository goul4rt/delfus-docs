# Docs completeness — demo mocks + páginas faltantes

**Data:** 2026-06-18
**Repos:** `front-end` (demo) e `delfus-docs` (docs). Spec mora em `delfus-docs/specs/` (fora de `docs/`, não vai pro site).

## Objetivo

Documentação 100% das features do dashboard, com screenshots reais. Hoje faltam páginas
e várias telas renderizam vazias no demo mode (sem screenshot possível).

## Decisões (brainstorming)

- Escopo: front-end (demo) + docs.
- Demo mode: toda tela renderiza com dados **e** os dialogs de criar/editar abrem no demo
  (preenchidos, sem persistir).
- Estrutura docs: páginas novas só para features distintas (Mensagens/Embeds, Emojis,
  Gestão de equipe). Visões analíticas viram seções dentro de `analise.md`.
- Bot-only (vídeo, correio, família) ficam como estão — sem tela de dashboard, sem mudança.

## SP1 — Front-end: demo completo + modais abríveis

Repo `../front-end`. Commit/PR coordenado. `.env.local` aponta p/ produção — demo é
client-side (leitura via generator, escrita vira no-op), sem escrita em prod.

### 1. Demo generators faltantes

Padrão existente: `src/features/<feat>/utils/demo-<feat>-generator.ts` (ou em
`src/features/welcome/utils/`), retornando dados realistas, chamado atrás de `isDemoMode()`
em `src/lib/dashboard-queries.ts` ou `src/features/<feat>/api.ts`.

Criar + wire para:

| Feature | Rotas | Dados demo |
| --- | --- | --- |
| starboard | `/dashboard/starboard/{overview,leaderboard,config,messages,hall-of-fame}` | 2 boards, ranking de membros, mensagens estreladas, hall of fame, stats |
| staff | `/dashboard/staff/{overview,sector,individual,alertas}` | KPIs, membros da equipe, métricas por setor, alertas (já existe `demo-staff-generator.ts` — wire/expandir) |
| action-log | `/dashboard/action-log/config` | eventos recentes de auditoria + config |
| moderation/history | `/dashboard/moderation/history` | registros de punição |
| bot-config | `/dashboard/bot-config` | config exemplo |

### 2. Auditar ambíguos

Verificar que renderizam com dados (e corrigir wiring se vazio): anti-raid, anti-invite,
boost, honeypot, emojis, channel-automations, backup, community/config.

### 3. Modais abríveis no demo

Hoje: botões `disabled={isDemoModeActive}`; mutações dão `throw 'Indisponível no modo
demonstração'` (ver `welcome/api.ts` e `vip/components/*`).

Mudança:
- Remover o `disabled={isDemoModeActive}` dos botões de criar/editar.
- Trocar o `throw` por um **no-op de demo**: helper único (ex.: `demoNoop()` /
  `isDemoMode()` retornando sucesso sem chamar API/DB) + toast "Demonstração — nada foi salvo".

Invariante: em demo, nenhuma mutação real é chamada. O no-op é o primeiro statement da função
de mutação, antes de qualquer fetch.

### Teste SP1

Rodar `bun run dev` em demo (localStorage demo + dark + tema azul), visitar cada rota e
confirmar não-vazio; abrir um dialog de criar em starboard, vip e reaction-roles.

## SP2 — Docs: páginas novas + screenshots

Repo `delfus-docs`. Depois do SP1 (precisa do demo populado).

### 1. Páginas novas

Geradas por workflow (1 agente/página, lê o código do bot em `../discord-bot` + front-end):
- `mensagens.md` — embeds e mensagens.
- `emojis.md` — gestão e estatísticas de emojis.
- `equipe.md` — gestão de equipe (staff): desempenho, setores, alertas.

Tom: direto, enxuto, sem cacoetes de IA (padrão da sessão). Seções: Como funciona,
Comandos (se houver), Configuração, Exemplos, Perguntas frequentes.

### 2. Análise expandida

Adicionar seções a `analise.md`: pontuação de membros, fluxo de membros (entradas/saídas),
mapa social, inteligência de canais, conteúdo & engajamento.

### 3. Screenshots (dark + tema azul)

Via demo (harness Playwright da sessão). Capturar as telas agora populadas: starboard
(overview/leaderboard), staff, mensagens, emojis, membros. Mais alguns **modais**: criar
plano VIP, criar board do starboard, criar reaction-role. Salvar em
`docs/assets/dashboard/`, embed nas páginas (`.dx-shot`), re-inserir antes de
`## Como funciona`.

### 4. Nav + deploy

Adicionar as páginas novas ao `nav` do `mkdocs.yml` (grupos Engajamento/Utilidades/Análise).
Build `--strict`, commit, push, deploy.

### Teste SP2

`mkdocs build --strict` limpo; checagem visual de 1 página nova + 1 modal.

## Ordem

SP1 → screenshots dependem dele. SP2 depois. Cada um com seu commit/push.

## Não-objetivos

- Não documentar telas que são puramente internas/dev (changelog, getting-started, product).
- Não reorganizar a nav inteira; só acrescentar.
- Não mexer em vídeo/correio/família.
