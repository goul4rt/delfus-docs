# Moderação e punições

O Delfus oferece um sistema completo de moderação para o seu servidor: advertências (warns) com gatilhos automáticos, silenciamento, expulsão e banimento — tudo registrado em um histórico permanente e consultável. Cada punição valida a hierarquia de cargos antes de agir, pode notificar o usuário punido por mensagem direta (DM) com link de apelação, avisar o canal de logs da staff e ainda alimenta um registro de auditoria (action log) de tudo o que acontece no servidor. Para o dono do servidor, isso significa moderação consistente, rastreável e em grande parte automática.

![Configuração de moderação no painel do Delfus](../assets/dashboard/moderacao.png){ .dx-shot loading=lazy }

*Configuração de moderação no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

Toda punição parte de um comando de barra da staff e segue um fluxo padronizado, com validações de segurança em cada etapa.

### Fluxo de uma punição

1. **A staff executa o comando** (`/warn`, `/mute`, `/ban`, `/kick`, `/unmute`, `/unwarn`) informando o **usuário**, um **motivo** (opcional) e, para `/mute` e `/ban`, uma **duração** (opcional).
2. **O bot valida o alvo**: não é possível punir **a si mesmo**, e `/ban`, `/kick`, `/mute` e `/unmute` **recusam outros bots**. Se o usuário não estiver mais no servidor, o comando avisa e para.
3. **O bot valida a hierarquia de cargos** antes de qualquer ação. A regra (em `PermissionUtils.canPunish`) é rígida:
   - O **cargo mais alto do bot** precisa estar **acima** do cargo mais alto do alvo.
   - O **cargo mais alto de quem executou** precisa estar **acima** do cargo do alvo — **estar acima, não igual**. Ter permissão de Administrador **não** dispensa essa regra: você não pode punir alguém com cargo igual ou maior que o seu.
   - Se a checagem falha, o bot explica o motivo (ex.: "Você não pode punir alguém com o mesmo cargo que você") e nada é aplicado.
4. **Banimento, silêncio e expulsão pedem confirmação.** O bot mostra um resumo da punição (usuário, motivo, duração) com botões **Confirmar** / **Cancelar**, evitando ações acidentais. No momento de confirmar, a checagem de hierarquia é **refeita** (proteção contra mudanças de cargo entre o comando e o clique). **Advertência (`/warn`), remoção de advertência (`/unwarn`) e remoção de silêncio (`/unmute`) são aplicadas direto**, sem confirmação.
5. **A punição é aplicada** usando os recursos nativos do Discord:
   - **Silêncio (`/mute`)** usa o *timeout* do Discord. O limite máximo é **28 dias**; um silêncio "permanente" (sem duração) é aplicado como **28 dias**.
   - **Banimento (`/ban`)** apaga as **mensagens das últimas 24 horas** do usuário ao banir.
   - **Expulsão (`/kick`)** remove o usuário (ele pode voltar com um novo convite).
6. **O usuário punido recebe um aviso por DM** — desde que esse aviso esteja ativado para aquele tipo de punição (veja [Configuração](#configuracao)). A DM é **sempre enviada antes** da expulsão/ban (senão o usuário sairia do servidor e perderia o canal de DM com o bot). Se você tiver configurado um **link de apelação**, ele é incluído como um campo na DM. O bot tenta entregar a DM **até 2 vezes**; se o usuário estiver com as DMs fechadas, ele detecta isso, **não falha a punição** e informa o estado da DM para a staff no resultado do comando.
7. **Um aviso pode ser enviado ao canal de logs da staff**, se essa opção estiver ativada e um canal estiver configurado.
8. **Tudo fica registrado no histórico** do usuário: quem puniu, o tipo, o motivo, a duração e o resultado da tentativa de DM. Esse histórico é permanente e visível pelo `/warnlist`.

### Estados da notificação por DM

No resultado dos comandos, a staff vê uma linha indicando o que aconteceu com a DM do usuário:

- **Enviada** — a DM foi entregue.
- **Desativada** — o aviso por DM está desligado para aquele tipo de punição (não é um erro).
- **DMs fechadas** — o usuário bloqueia DMs ou não compartilha servidor com o bot.
- **Erro** — falha temporária mesmo após a segunda tentativa.

### Advertências com gatilhos automáticos

As advertências (warns) acumulam um **contador por usuário**, mantido em cache rápido para responder na hora (sincronizado com o histórico do banco). Você pode configurar **gatilhos**: ao atingir um número **exato** de warns, o bot executa **automaticamente** uma ação. As ações possíveis de um gatilho são:

- **Silenciar** (com uma duração — padrão de 1 hora se não definida)
- **Expulsar**
- **Banir** (com uma duração — padrão de 24 horas se não definida)
- **Adicionar um cargo**
- **Remover um cargo**

O gatilho dispara quando a contagem do usuário **bate exatamente** o número configurado (ex.: um gatilho em "3 warns" age no 3º warn). Ao advertir, a staff vê uma **barra de progresso** indicando quantos warns o usuário tem, quantos faltam para o próximo gatilho e qual ação ele dispara — por exemplo: `Avisos: ▓▓░ 2/3 → mute 1h`. Se a ação automática foi executada, o resultado do `/warn` também avisa qual foi (ex.: "Ação Automática Executada: MUTE"). A ação automática é registrada no histórico marcada como auto-ação.

### Expiração automática de warns ("bom comportamento")

Se ativada, uma rotina periódica do bot **expira advertências antigas** depois do período que você definir (em dias, semanas ou meses — meses são contados como 30 dias). Quando os warns de um usuário expiram:

1. Os warns que ultrapassaram o período são marcados como **expirados** e deixam de contar.
2. O **contador do usuário é recalculado** (o cache é limpo para refletir o novo valor).
3. **Reversão de cargo automática**: se um gatilho de **adicionar cargo** tinha sido disparado e a contagem agora caiu **abaixo** do número daquele gatilho, o cargo é **removido automaticamente**. Gatilhos de **remover cargo não são revertidos** (o bot não devolve um cargo retirado, para evitar reconceder algo privilegiado por engano). Cada reversão é registrada no histórico.
4. **Reconhecimento de bom comportamento**: se a notificação por canal estiver ativada e houver um canal de logs configurado, o bot publica uma mensagem reconhecendo que as advertências do usuário expiraram.

### Histórico e registro de ações da staff

- **`/warnlist`** mostra o histórico de punições de um usuário: ID de cada registro (útil para o `/unwarn`), tipo, staff responsável, data (absoluta e relativa), motivo, canal, duração e — se aplicável — se foi uma auto-ação ou se já foi removido (e por quem). A lista é **paginada em 5 registros por página**, com botões de navegação que ficam ativos por **5 minutos**. Apenas quem executou o comando pode usar os botões.
- **Registro de ações (action log)**: além do histórico de punições, comandos de moderação e dezenas de eventos do servidor podem ser publicados em um canal de auditoria. Esse registro cobre, entre outros: mensagens apagadas/editadas/em massa, entradas e saídas de membros, bans/unbans, timeouts, mudanças de apelido, adição/remoção de cargos, criação/edição/exclusão de cargos, canais, threads e emojis, eventos de voz, convites e mudanças no servidor. Para identificar **quem** fez cada ação, o bot cruza o evento com o **log de auditoria do Discord**. Eventos que costumam acontecer em rajada (arrastar cargos, sincronizar permissões de canais, importações em massa) são **agrupados** para não poluir o canal, respeitando os limites de envio do Discord.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/warn` | Adverte um usuário (com motivo opcional). Incrementa o contador, mostra a barra de progresso e dispara gatilhos automáticos se a contagem bater um gatilho configurado. |
| `/unwarn` | Remove uma advertência: pela opção `warn_id` (ID exibido no `/warnlist`) ou, se nenhum ID for informado, a **mais recente**. Aceita motivo opcional. |
| `/warnlist` | Mostra o histórico de punições de um usuário, paginado (5 por página). Você pode ver o seu próprio histórico; ver o de outra pessoa exige cargo maior que o dela. |
| `/mute` | Silencia um usuário usando o *timeout* do Discord. Aceita `duration` opcional (ex.: `30s`, `5min`, `2h`); sem duração, aplica o máximo de 28 dias. Pede confirmação. |
| `/unmute` | Remove o silêncio (timeout) de um usuário. Avisa se o usuário não estava silenciado. |
| `/ban` | Bane um usuário. Aceita `duration` opcional para ban temporário; sem duração, é permanente. Apaga as mensagens das últimas 24h. Pede confirmação. |
| `/kick` | Expulsa um usuário do servidor (com motivo opcional). Pede confirmação. |

**Opções dos comandos:**

- **usuário** — obrigatório em todos. O alvo da ação.
- **motivo** — opcional. Aparece na DM, no histórico e no log; se omitido, é registrado como "sem motivo".
- **duração** (`/mute` e `/ban`) — opcional. Formato `número + unidade`: `s` (segundos), `m`/`min` (minutos), `h` (horas) — por exemplo `30s`, `5min`, `2h`. Um número sem unidade é interpretado como **segundos**. Outras unidades (dias, semanas) **não** são aceitas neste campo; sem duração, `/mute` aplica o máximo de 28 dias e `/ban` fica permanente.
- **id_advertencia** (`/unwarn`) — opcional. ID específico do warn a remover (visto no `/warnlist`).

## Configuração

As **punições em si** são aplicadas pelos comandos de barra dentro do Discord. A **configuração** do comportamento é feita pelo **Dashboard** em [https://admin.delfus.app](https://admin.delfus.app), na seção de **Moderação**. As opções principais:

### Notificações
- **Aviso por DM por tipo de punição** — ligue/desligue a DM para advertência, silêncio, expulsão, banimento e suas reversões (unban, unmute, remoção de advertência), de forma independente. Por padrão, **advertência e remoção de advertência avisam por DM**; silêncio, expulsão e banimento vêm **desligados** (você os ativa se quiser).
- **Aviso no canal** — ative para que advertências e o reconhecimento de bom comportamento sejam publicados no canal de logs.
- **Canal de logs** — defina o canal onde as notificações da staff e o reconhecimento de bom comportamento são enviados.
- **Link de apelação** — uma URL incluída como campo nas DMs de punição, para o usuário contestar.
- **Textos/embeds personalizados** — personalize o embed enviado ao usuário em cada tipo de punição (título, descrição, cor, imagem, campos, etc.). Há um embed padrão e a possibilidade de um embed específico por tipo (advertência, silêncio, ban, kick e reversões). Os textos suportam variáveis como `{user}`, `{staff}`, `{reason}`, `{duration}` e `{guild}`.

### Gatilhos automáticos de warns
- Cadastre regras no formato **"ao atingir X warns → execute uma ação"**. Para cada gatilho você escolhe:
  - **contagem** de warns que dispara (número inteiro maior que 0);
  - **ação**: silenciar, expulsar, banir, adicionar cargo ou remover cargo;
  - **duração** (para silenciar/banir) e **cargo** (obrigatório para adicionar/remover cargo).
- Não há um limite fixo de quantidade de gatilhos; eles são avaliados pela contagem exata de warns.

### Expiração automática de warns
- **Ative a expiração** e defina a **duração** e a **unidade** (dias, semanas ou meses). A partir daí, a rotina periódica expira warns mais antigos que esse período, recalcula a contagem, reverte cargos de gatilhos de "adicionar cargo" quando aplicável e (se configurado) publica o reconhecimento de bom comportamento.

### Registro de ações (action log)
- **Ativar/desativar** o registro como um todo.
- **Modo de canal**: um **único canal** para todos os eventos, ou **um canal por tipo de evento**.
- **Eventos a registrar**: escolha quais eventos publicar (mensagens, membros, cargos, canais/threads, emojis, voz, servidor, comandos de moderação, etc.), com ajustes por evento (ex.: apenas mensagens deletadas que contenham imagem).
- **Filtros de ruído**: **canais ignorados**, **cargos ignorados** (eventos de membros com esses cargos não são logados) e **ignorar bots** (ligado por padrão).

## Exemplos de uso

- **Punição em escada, sem decisão manual a cada caso:** configure gatilhos como "3 warns → silenciar 1h", "5 warns → silenciar 12h", "7 warns → banir". A staff só precisa usar `/warn`; o bot escala a punição sozinho e mostra a barra de progresso a cada advertência.
- **Segunda chance para quem se comporta:** ative a expiração automática em "30 dias". Quem ficar 30 dias sem novas advertências tem os warns antigos zerados; se a queda na contagem desfizer um gatilho de "adicionar cargo" (ex.: um cargo de "observação"), o bot remove o cargo automaticamente e pode reconhecer o bom comportamento no canal de logs.
- **Banimento temporário com aviso e apelação:** rode `/ban usuario:@Fulano duracao:2h motivo:flood`, confirme no botão. O usuário recebe uma DM (se ativada) com o motivo e o link de apelação **antes** de ser banido, as mensagens das últimas 24h dele são apagadas, e a staff vê no resultado se a DM foi entregue.
- **Trilha de auditoria completa:** ative o action log apontando para um canal só da staff, ignore os bots e os canais de comandos, e passe a ver quem apagou mensagens, alterou cargos ou baniu membros — com o autor identificado pelo log de auditoria do Discord.

## Requisitos

- **Permissões do bot por ação**: **Moderar Membros** (para `/warn`, `/unwarn`, `/mute`, `/unmute` e `/warnlist`), **Expulsar Membros** (`/kick`) e **Banir Membros** (`/ban`). Os comandos também exigem que **quem executa** tenha a permissão correspondente.
- **Hierarquia de cargos**: o cargo mais alto do **bot** e o de **quem executa** precisam estar **acima** do cargo mais alto do alvo. Ter Administrador **não** dispensa essa regra — não é possível punir alguém com cargo igual ou superior ao seu.
- **Para as DMs**: o usuário precisa aceitar mensagens diretas; se as DMs estiverem fechadas, a punição ainda acontece, só o aviso não é entregue.
- **Para o registro de ações**: no canal de logs, o bot precisa de **Ver Canal**, **Enviar Mensagens**, **Inserir Links** e **Anexar Arquivos**, além de acesso ao **log de auditoria** do servidor para identificar os autores das ações.

## Perguntas frequentes

**Por que o silêncio "permanente" desaparece depois de um tempo?**
O `/mute` usa o *timeout* nativo do Discord, que tem teto de 28 dias. Um silêncio sem duração é aplicado como 28 dias. Para algo realmente permanente, use cargo de "mutado" via gatilho de cargo ou um banimento.

**Posso usar `2d` ou `1w` na duração de um `/ban` ou `/mute`?**
Não. O campo de duração aceita apenas segundos (`s`), minutos (`m`/`min`) e horas (`h`) — por exemplo `30s`, `5min`, `2h`. Um número sem unidade é lido como segundos.

**O usuário foi expulso/banido mas a DM diz "DMs fechadas". A punição valeu?**
Sim. A entrega da DM é independente da punição. Se o usuário bloqueia DMs, o bot apenas registra isso e segue com a expulsão ou banimento normalmente.

**O `/unwarn` remove qual advertência?**
Se você informar o `id_advertencia` (visível no `/warnlist`), remove aquela específica; sem ID, remove a **mais recente**. A remoção atualiza a contagem do usuário e fica registrada no histórico, com aviso por DM ao usuário (se ativado).

!!! tip "Dica"
    Combine **gatilhos automáticos** com a **expiração de warns**: defina a escada de punições (ex.: 3 → mute, 5 → ban) e ative a expiração em 30 dias. Assim a staff só precisa advertir, a punição vira consistente e quem se comporta ganha o histórico limpo — inclusive com remoção automática de cargos de "observação" quando a contagem cai.

