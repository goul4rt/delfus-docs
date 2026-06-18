# Docs Completeness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Documentação 100% das features do dashboard, com screenshots reais — preenchendo o demo mode do front-end (telas + modais) e escrevendo as páginas que faltam.

**Architecture:** Fase 1 (front-end `../front-end`) completa o demo: cria/wire os demo generators faltantes atrás do `isDemoMode()` e destrava os dialogs de criar/editar (mutação vira no-op). Fase 2 (`delfus-docs`) escreve as páginas novas e captura os screenshots agora possíveis. Fase 1 destrava a Fase 2.

**Tech Stack:** Next.js 16 + bun + zustand + React Query (front-end); MkDocs Material + Playwright + workflows (docs).

**Spec:** `delfus-docs/specs/2026-06-18-docs-completeness-design.md`

---

## Padrões de referência (front-end)

**`isDemoMode()`** (em `src/lib/dashboard-queries.ts:11` e em cada `api.ts`):
```ts
function isDemoMode(): boolean {
  return useDashboardStore.getState().isDemoModeActive;
}
```

**Query com branch demo** (template — `dashboard-queries.ts:83`):
```ts
queryKey: ['<feat>', guildId, isDemoMode()],
queryFn: async (): Promise<XData> => {
  if (isDemoMode()) {
    const { generateDemoX } = await import('@/features/<feat>/utils/demo-<feat>-generator');
    return generateDemoX();
  }
  const res = await fetch(`/api/dashboard/<feat>?guildId=${guildId}`);
  if (!res.ok) throw new Error('Failed');
  return res.json();
},
```

**Generator** (template — `demo-vip-generator.ts`): importa os tipos da feature e exporta `generateDemoX(): XData` com dados realistas hardcoded.

**Mutação hoje bloqueia** (`welcome/api.ts:34`):
```ts
if (isDemoMode()) {
  throw new Error('Indisponivel no modo demonstracao');
}
```

**Botão hoje desabilita** (`vip/components/vip-codes.tsx`): `disabled={isDemoModeActive}`.

---

## Fase 1 — Front-end: demo completo + modais abríveis

Rodar dev em demo (do CLAUDE.md do delfus-docs): patch middleware, `DATABASE_URL/REDIS_HOST/BOT_API_URL` neutralizados, `localStorage` demo + dark + tema azul. **`.env.local` = produção; mutações viram no-op, nunca chamam API real.**

### Task 1: Auditoria — confirmar telas vazias

**Files:** nenhum (levantamento).

- [ ] **Step 1:** Subir `bun run dev` em demo (middleware patchado).
- [ ] **Step 2:** Com Playwright + localStorage demo, visitar cada rota e classificar OK/EMPTY (regex `Nenhum|nenhum dado|configurado ainda`):
  `/dashboard/starboard/{overview,leaderboard,messages,hall-of-fame}`, `/dashboard/staff/{overview,sector,individual,alertas}`, `/dashboard/action-log/config`, `/dashboard/moderation/{history,effectiveness}`, `/dashboard/bot-config`, e os ambíguos `/dashboard/{anti-raid,anti-invite,boost,honeypot,emojis,channel-automations,backup/server,community,config}`.
- [ ] **Step 3:** Anotar a lista EMPTY confirmada. Só essas precisam de generator/wiring nas tasks seguintes.

### Task 2: Generator do Starboard

**Files:**
- Create: `../front-end/src/features/starboard/utils/demo-starboard-generator.ts`
- Modify: a query/api do starboard (achar com `grep -rln "starboard" ../front-end/src/features/starboard/api.ts ../front-end/src/lib/dashboard-queries.ts`)

- [ ] **Step 1:** Ler os tipos do starboard (`../front-end/src/features/starboard/types.ts`) e a(s) query(s) que cada sub-página usa.
- [ ] **Step 2:** Criar `demo-starboard-generator.ts` exportando funções por dado, mirando o template do `demo-vip-generator.ts`: 2 boards (emoji, canal, min estrelas), leaderboard (~8 membros com totais), mensagens estreladas (~6), hall of fame (~4), stats. Tipado conforme `types.ts`.
- [ ] **Step 3:** Wire cada query atrás do `if (isDemoMode())` (template acima), importando do generator.
- [ ] **Step 4:** Verificar no demo: `/dashboard/starboard/{overview,leaderboard,messages,hall-of-fame}` renderizam não-vazio.
- [ ] **Step 5:** Commit: `git add -A && git commit -m "feat(demo): starboard demo data"` (no front-end).

### Task 3: Generator do Staff

**Files:**
- Modify/Create: wire o `demo-staff-generator.ts` existente (ou criar dados faltantes) nas queries das sub-páginas de staff (`../front-end/src/features/staff/...` — achar os hooks que as páginas usam).

- [ ] **Step 1:** Achar como `/dashboard/staff/{overview,sector,individual,alertas}` buscam dados (hooks/queries) e o que `demo-staff-generator.ts` já provê.
- [ ] **Step 2:** Wire o branch `isDemoMode()` em cada query de staff usando o generator; preencher dados faltantes (KPIs, membros, setores, alertas) seguindo os tipos.
- [ ] **Step 3:** Verificar no demo as 4 sub-páginas não-vazias.
- [ ] **Step 4:** Commit.

### Task 4: Generators de action-log, moderation/history, bot-config

**Files:**
- Create: `demo-action-log-generator.ts`, e dados de history/bot-config nos respectivos `utils/`.
- Modify: as queries correspondentes.

- [ ] **Step 1:** Para cada (action-log/config, moderation/history, bot-config): ler tipos + query.
- [ ] **Step 2:** Criar generator com dados realistas (action-log: ~10 eventos de auditoria; history: ~8 punições; bot-config: config exemplo) tipados.
- [ ] **Step 3:** Wire atrás de `isDemoMode()`.
- [ ] **Step 4:** Verificar as 3 telas não-vazias no demo.
- [ ] **Step 5:** Commit.

### Task 5: Corrigir ambíguos vazios

**Files:** as queries das features que a Task 1 marcou EMPTY entre anti-raid/anti-invite/boost/honeypot/emojis/channel-automations/backup/community/config.

- [ ] **Step 1:** Para cada uma marcada EMPTY: criar/expandir generator + wire (mesmo padrão).
- [ ] **Step 2:** Verificar não-vazio no demo.
- [ ] **Step 3:** Commit.

### Task 6: Modais abríveis no demo

**Files:** componentes com `disabled={isDemoModeActive}` (achar: `grep -rln "disabled={isDemoModeActive}" ../front-end/src`) e `api.ts` com o throw (achar: `grep -rln "Indisponivel no modo demonstracao" ../front-end/src`).

- [ ] **Step 1:** Criar helper `../front-end/src/lib/demo-noop.ts`:
```ts
import { useDashboardStore } from '@/providers/dashboard-store';
export function isDemoMode(): boolean {
  return useDashboardStore.getState().isDemoModeActive;
}
/** Em demo: simula sucesso sem tocar API/DB. */
export async function demoNoop<T>(value: T): Promise<T> {
  await new Promise((r) => setTimeout(r, 250));
  return value;
}
```
- [ ] **Step 2:** Em cada mutação que hoje faz `throw new Error('Indisponivel no modo demonstracao')`: trocar por no-op que devolve algo válido. Void → `if (isDemoMode()) return;`. Que retorna entidade → `if (isDemoMode()) return demoNoop({ ...input, id: 'demo' } as X);`. Nunca chamar fetch real em demo.
- [ ] **Step 3:** Remover o `isDemoModeActive` da expressão `disabled` dos botões de criar/editar (deixar habilitado no demo). Manter disabled real (loading/validação) onde houver.
- [ ] **Step 4:** Verificar no demo: abrir dialog de criar em starboard, vip e reaction-roles; preencher; salvar → fecha sem erro, nada persiste (recarregar não cria nada).
- [ ] **Step 5:** Commit.

### Task 7: Reverter patch e fechar Fase 1

- [ ] **Step 1:** `cd ../front-end && git checkout src/middleware.ts` (reverter o patch de screenshots).
- [ ] **Step 2:** Conferir `git status` limpo exceto os generators/wiring/modais.
- [ ] **Step 3:** Push do front-end (via gh helper, branch própria + PR ou direto conforme o repo): demo data + modais.

---

## Fase 2 — Docs: páginas novas + screenshots

### Task 8: Páginas novas (workflow)

**Files:** Create `delfus-docs/docs/funcionalidades/{mensagens,emojis,equipe}.md`

- [ ] **Step 1:** Workflow: 1 agente por página, lê o código do bot (`../discord-bot`) + a feature no front-end, escreve direto/enxuto (padrão da sessão). Seções: Como funciona, Comandos (se houver), Configuração, Exemplos, Perguntas frequentes. Sem imagens (inseridas depois).
- [ ] **Step 2:** Escrever os 3 arquivos a partir do resultado.
- [ ] **Step 3:** `mkdocs build --strict` (com `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib`).

### Task 9: Expandir Análise

**Files:** Modify `delfus-docs/docs/funcionalidades/analise.md`

- [ ] **Step 1:** Adicionar seções: pontuação de membros, fluxo de membros, mapa social, inteligência de canais, conteúdo & engajamento (fundamentado no código). Manter direto/enxuto.
- [ ] **Step 2:** Build `--strict`.

### Task 10: Screenshots (dark + tema azul)

**Files:** `delfus-docs/docs/assets/dashboard/*.png`

- [ ] **Step 1:** Subir front-end em demo (dark + azul), patch middleware.
- [ ] **Step 2:** Capturar telas agora populadas: starboard (overview, leaderboard), staff (overview), mensagens, emojis, membros (scoring/fluxo).
- [ ] **Step 3:** Capturar 3 modais: criar plano VIP (`/vip/tiers` → Novo Plano), criar board (`/starboard/config` → Criar Board), criar reaction-role.
- [ ] **Step 4:** Mover pra `docs/assets/dashboard/`; reverter middleware; parar dev.

### Task 11: Embed, nav, deploy

**Files:** Modify páginas de feature + `delfus-docs/mkdocs.yml` (nav)

- [ ] **Step 1:** Embed dos screenshots (`.dx-shot`, antes de `## Como funciona`; modais nas seções de exemplo).
- [ ] **Step 2:** Adicionar `mensagens`, `emojis`, `equipe` ao `nav` (grupos Engajamento/Utilidades/Análise).
- [ ] **Step 3:** `mkdocs build --strict` limpo.
- [ ] **Step 4:** Commit + push (gh helper). Aguardar deploy verde + CDN.

---

## Self-review

- **Cobertura do spec:** SP1 (generators=T2-5, modais=T6) e SP2 (páginas=T8, análise=T9, screenshots=T10, nav/deploy=T11). ✓
- **Ordem:** Fase 1 antes da 2 (screenshots dependem do demo). ✓
- **Segurança:** mutações no-op antes de qualquer fetch (T6 step 2). ✓
- **Ambiguidade resolvida:** Task 1 define a lista real de telas vazias antes de criar generators (não assume).
