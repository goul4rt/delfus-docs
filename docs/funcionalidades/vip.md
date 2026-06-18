# VIP, assinaturas e recompensas

O sistema VIP do Delfus permite criar **níveis de assinatura (tiers)** com benefícios automáticos — cargos, bônus de XP, mais entradas em sorteios, bônus extra no `/daily` e slots de família — e distribuí-los aos membros por **código de resgate** ou **concessão manual**. O bot cuida de tudo o que vem depois: ativa os benefícios na hora, controla a expiração, avisa o membro antes do prazo acabar, remove os benefícios quando expira e ainda corrige sozinho cargos VIP que sumiram. Para o dono do servidor, é a base para monetizar ou recompensar a comunidade sem trabalho manual recorrente.

![Planos VIP no painel do Delfus](../assets/dashboard/vip.png){ .dx-shot loading=lazy }

*Planos VIP no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O VIP é montado em três peças que se encaixam nesta ordem: **recompensas** → **tiers** → **códigos** (ou concessão direta). Você cria recompensas (os benefícios individuais), agrupa várias delas dentro de um tier (o nível VIP), e então entrega esse tier aos membros — por um código que eles resgatam, ou concedendo manualmente.

### 1. Você define os benefícios (recompensas)

Cada recompensa é de **um tipo**, e cada tipo tem seu próprio parâmetro e limites validados pelo bot:

- **`ROLE` (cargo)** — atribui automaticamente um cargo ao membro VIP. Ao criar, o bot verifica se o cargo está **abaixo** do cargo mais alto do bot; se estiver acima, recusa a criação porque não conseguiria atribuí-lo. Por padrão o cargo é **removido quando o VIP expira**.
- **`XP_MULTIPLIER` (multiplicador de XP)** — multiplica o XP que o membro ganha. O multiplicador deve ficar entre **1.0 e 5.0**. É exibido como percentual de bônus (ex.: multiplicador 2.0 aparece como "+100% XP"). O sistema de XP consulta esse valor em tempo real.
- **`GIVEAWAY_MULTIPLIER` (entradas em sorteios)** — dá mais entradas em sorteios. O número de entradas deve ficar entre **1 e 10** (ex.: "3x chances em sorteios").
- **`DAILY_BONUS` (bônus diário)** — adiciona moedas extras no comando `/daily`. Pode ser um valor **fixo** (`flat`, ex.: "+50 moedas no daily") ou **percentual** (`percent`, ex.: "+25% no daily"). O comando `/daily` consulta o bônus em tempo real.
- **`FAMILY` (slot de família)** — cada recompensa FAMILY libera **1 slot** para o membro criar uma família com cargo próprio. Define o máximo de membros da família (entre **1 e 50**). As famílias são criadas manualmente pelo membro via `/familia criar`; a recompensa só libera o slot.

Você dá um **nome único** a cada recompensa dentro do servidor (não pode repetir nome).

### 2. Você monta os tiers (níveis VIP)

Um tier agrupa uma ou mais recompensas e tem uma **prioridade** numérica (quanto maior o número, mais "alto" o nível — ex.: prioridade 3 é superior à prioridade 1). Regras na criação:

- Um tier precisa de **pelo menos uma recompensa** vinculada.
- O **nome** e a **prioridade** são únicos por servidor — não dá para ter dois tiers com o mesmo nome nem com a mesma prioridade.
- Cada tier pode ter no máximo **20 recompensas**, e o servidor pode ter no máximo **10 tiers**.

Você pode editar um tier depois (renomear, mudar prioridade, adicionar ou remover recompensas). Um tier só **não pode ser deletado** enquanto houver assinaturas ativas nele.

### 3. O membro recebe o VIP

Há duas formas de entrega:

- **Concessão manual** — um administrador usa `/vip-admin user give` informando o membro, o tier e a duração.
- **Resgate de código** — o membro usa `/vip resgatar` (ou `/vip redeem`) com um código que você gerou.

No resgate, o bot **valida o código em sequência** antes de ativar:

1. O código existe neste servidor?
2. Está dentro da validade? (códigos podem ter data de expiração própria)
3. Ainda tem usos disponíveis? (cada código tem um limite máximo de usos)
4. O membro **já usou este código antes**? Cada membro só pode resgatar o mesmo código **uma vez**.

Se qualquer checagem falhar, o bot responde com a mensagem do erro e nada é ativado.

### 4. O bot ativa e aplica tudo na hora

Ao ativar (manual ou via código), o bot:

1. Calcula a **data de expiração** a partir da duração (ou marca como **permanente** se a duração for `0`).
2. Cria a **assinatura** do membro e registra um evento de auditoria.
3. **Aplica cada benefício do tier**: dá os cargos, registra os multiplicadores de XP/sorteio, libera o bônus diário e os slots de família. Se uma recompensa específica falhar (ex.: cargo bloqueado por hierarquia), o bot registra a falha e **continua** com as outras — a ativação não é abortada por uma recompensa.
4. Se configurado, envia uma **mensagem privada (DM)** de ativação ao membro e uma **notificação no canal** de avisos VIP.

### 5. Upgrade, extensão e downgrade

Quando o membro **já tem um VIP ativo** e recebe outro, o comportamento depende da prioridade e da configuração do servidor:

- **Upgrade** — se o novo tier tem **prioridade maior** que o atual, o bot **cancela** a assinatura anterior e ativa a nova.
- **Mesmo tier ou tier inferior, via código** — se a **extensão de tempo** estiver habilitada (padrão: sim), o bot **soma os dias** do código ao VIP atual em vez de trocar de tier. Um código permanente (duração `0`) transforma o VIP atual em permanente; se o VIP já era permanente, a extensão é ignorada (não há o que somar).
- **Downgrade manual** — pela concessão manual (`/vip-admin user give`), conceder um tier de prioridade **menor ou igual** só é permitido se o servidor tiver o **downgrade habilitado** na configuração; caso contrário o bot recusa, informando que o membro já tem um VIP de prioridade igual ou maior.

### 6. Ajuste manual de tempo

Com `/vip-admin user time` você **adiciona** ou **remove** dias de uma assinatura ativa. Detalhes:

- Não dá para **remover** dias de um VIP **permanente**.
- Se a remoção de dias deixar a expiração no passado, o VIP **expira na hora** (com remoção dos benefícios).
- Adicionar dias a um VIP permanente o converte em temporário com a nova data.

### 7. Aviso de expiração (de hora em hora)

Um job roda **a cada hora** e procura quem está perto de perder o VIP. Por padrão o aviso é enviado **3 dias antes** (configurável por servidor). O membro recebe uma **DM de aviso** — desde que a DM de aviso esteja habilitada na configuração.

### 8. Expiração automática

O mesmo job horário detecta as assinaturas cujo prazo **já acabou** e as desativa. Ao expirar, o bot:

1. **Remove os benefícios**: tira os cargos VIP (os que têm "remover ao expirar" ativo) e para de aplicar os multiplicadores/bônus.
2. **Congela as famílias** vinculadas àquela assinatura (os cargos da família são removidos).
3. Se configurado, envia **DM de expiração** ao membro e **notificação no canal**.

> Quando um VIP é **cancelado para upgrade** (troca de tier), o bot **não** envia DM de expiração — só envia em expiração de fato.

### 9. Reconciliação de cargos (a cada 6 horas)

A cada **6 horas** o bot confere se os cargos VIP de cada membro batem com o que ele deveria ter, e:

- **Restaura** cargos VIP que sumiram (ex.: alguém removeu o cargo manualmente).
- **Remove** cargos VIP que o membro não deveria mais ter.

Isso mantém os cargos consistentes mesmo após edições manuais no Discord.

### O que o membro vê

- **`/vip status`** — mostra o tier atual, quando expira (ou "permanente"), quando foi ativado e a lista de benefícios. Se o membro não tem VIP, lista os tiers disponíveis.
- **`/vip info`** — sem argumento, lista todos os tiers do servidor com seus benefícios; com um tier informado, mostra os detalhes daquele tier.

## Comandos

### Comandos de membro — `/vip`

| Comando | O que faz |
| --- | --- |
| `/vip status` | Mostra o status VIP atual do membro: tier, expiração, data de ativação e benefícios. |
| `/vip info [tier]` | Lista os tiers disponíveis ou mostra os detalhes de um tier específico. |
| `/vip resgatar codigo:<código>` | Resgata um código VIP (também aceito como `/vip redeem`). |

### Comandos de administrador — `/vip-admin`

Restrito a administradores, organizado em grupos:

| Comando | O que faz |
| --- | --- |
| `/vip-admin reward create` | Cria uma recompensa (`ROLE`, `XP_MULTIPLIER`, `GIVEAWAY_MULTIPLIER`, `DAILY_BONUS` ou `FAMILY`) com seu parâmetro. |
| `/vip-admin reward list` | Lista todas as recompensas cadastradas no servidor. |
| `/vip-admin reward delete nome:<nome>` | Remove uma recompensa pelo nome. |
| `/vip-admin tier create` | Cria um tier com nome, prioridade e recompensas (separadas por vírgula). |
| `/vip-admin tier list` | Lista todos os tiers e seus benefícios. |
| `/vip-admin tier info tier:<nome>` | Mostra detalhes de um tier, incluindo quantos VIPs ativos ele tem. |
| `/vip-admin tier edit` | Edita um tier: `novo_nome`, `nova_prioridade`, `adicionar_recompensas`, `remover_recompensas`. |
| `/vip-admin tier delete tier:<nome>` | Deleta um tier (bloqueado se houver assinaturas ativas). |
| `/vip-admin code create` | Gera um código VIP: tier, duração, `max_usos` (padrão 1), código personalizado e validade opcional. |
| `/vip-admin code list` | Lista os códigos e seu status (ativo, usado, expirado). |
| `/vip-admin code delete codigo:<código>` | Remove um código. |
| `/vip-admin user give` | Concede VIP a um membro: usuário, tier e duração. |
| `/vip-admin user remove usuario:<membro>` | Remove o VIP ativo de um membro. |
| `/vip-admin user time` | Adiciona ou remove dias do VIP de um membro (`acao`, `tempo`, `motivo`). |
| `/vip-admin user list` | Lista todos os membros com VIP ativo, agrupados por tier. |
| `/vip-admin config channel canal:<canal>` | Define o canal de notificações VIP. |
| `/vip-admin config dm tipo:<tipo> ativado:<sim/não>` | Liga/desliga as DMs de `activated` (ativação), `expiring` (aviso) ou `expired` (expiração). |
| `/vip-admin config expiring-days dias:<n>` | Define com quantos dias de antecedência avisar o membro. |
| `/vip-admin config view` | Mostra a configuração VIP atual do servidor. |

### Formato de duração

Os campos de duração (`/vip-admin user give`, `user time`, `code create`) aceitam:

- `30d` → 30 dias · `2w` → 2 semanas (14 dias) · `1m` → 1 mês (30 dias)
- Um número puro (ex.: `30`) é interpretado como **dias**.
- `0` (ou `permanente`) = **permanente** — válido apenas para `give` e `code create`; o ajuste de tempo (`user time`) e a validade de código (`expira`) não aceitam `0`.

## Configuração

A configuração do servidor pode ser feita pelos subcomandos `/vip-admin config` **ou** pelo Dashboard em [admin.delfus.app](https://admin.delfus.app) — o efeito é o mesmo.

**Passo a passo recomendado:**

1. **Crie as recompensas** primeiro (`/vip-admin reward create` ou painel). Defina o tipo e o parâmetro de cada benefício.
2. **Monte os tiers** (`/vip-admin tier create`) juntando as recompensas e definindo a prioridade. Lembre: nome e prioridade são únicos, e o tier precisa de pelo menos uma recompensa.
3. **Distribua o VIP**: gere códigos (`/vip-admin code create`) para vender/sortear, ou conceda diretamente (`/vip-admin user give`).
4. **Ajuste as notificações** no grupo `config`.

**Campos de configuração do servidor:**

- **Canal de notificações** (`notification_channel_id`) — onde o bot posta avisos de ativação e expiração.
- **DM ao ativar** (`dm_on_activated`) — mensagem privada quando o VIP é ativado.
- **DM de aviso** (`dm_on_expiring`) — mensagem privada antes de expirar.
- **DM ao expirar** (`dm_on_expired`) — mensagem privada quando o VIP expira.
- **Dias de antecedência do aviso** (`days_before_expiring_warn`) — padrão **3 dias**.
- **Permitir downgrade** (`allow_tier_downgrade`) — se concessões manuais de tier inferior/igual são aceitas.
- **Permitir extensão de tempo** (`allow_time_extension`) — se resgatar um código de tier igual/inferior **soma dias** em vez de recusar (padrão: habilitado).

**Limites por servidor:** até **10 tiers**, **20 recompensas por tier** e **100 códigos ativos**.

## Exemplos de uso

- **Vender um plano VIP mensal:** crie uma recompensa `ROLE` com o cargo "VIP Ouro", monte um tier "Ouro" (prioridade 2) com esse cargo e talvez um `XP_MULTIPLIER` 2.0. Depois gere códigos com `/vip-admin code create tier:Ouro duracao:30d max_usos:1` e venda cada código. O membro resgata com `/vip resgatar` e ganha o cargo + XP em dobro por 30 dias.

- **Recompensar staff ou apoiadores diretamente:** use `/vip-admin user give usuario:@membro tier:Diamante duracao:0` para conceder um VIP **permanente**, sem código.

- **Estender quem renovou:** se um membro já tem "Ouro" e compra outro mês, basta entregar outro código do mesmo tier — com a extensão habilitada, o bot **soma 30 dias** à assinatura atual em vez de reiniciar.

- **Família com cargo próprio:** crie uma recompensa `FAMILY` (ex.: até 10 membros), inclua num tier, e os assinantes poderão montar a família com `/familia criar`. Se o VIP expirar, a família é congelada automaticamente.

## Requisitos

- O bot precisa de permissão para **Gerenciar Cargos**, e o cargo dele deve estar **acima** dos cargos VIP na hierarquia — o bot recusa criar uma recompensa `ROLE` com um cargo posicionado acima do dele.
- Para enviar avisos por DM, o membro precisa **aceitar DMs do servidor**; com as DMs fechadas, o bot apenas registra a falha e segue normalmente (a ativação não é afetada).
- Recompensas do tipo `FAMILY` dependem do **módulo de famílias** estar em uso; as famílias são criadas pelo próprio membro via `/familia criar`.
- Recompensas `XP_MULTIPLIER` e `DAILY_BONUS` só têm efeito prático se o servidor usar os sistemas de XP e o comando `/daily`, respectivamente (o valor é aplicado em tempo real por esses sistemas).

## Perguntas frequentes

**Um membro pode usar o mesmo código duas vezes?**
Não. Cada membro só pode resgatar um código **uma vez**. O código no geral pode ser usado por vários membros até atingir o limite de usos (`max_usos`).

**O que acontece se o membro já tem VIP e resgata outro código?**
Se o código for de um tier de prioridade **maior**, é feito upgrade (troca de tier). Se for do **mesmo** tier ou inferior, o bot **soma os dias** ao VIP atual — desde que a extensão de tempo esteja habilitada. Caso contrário, recusa.

**Removi o cargo VIP de alguém manualmente. O bot vai devolver?**
Sim. A cada 6 horas a reconciliação restaura cargos VIP que sumiram e remove cargos que não deveriam mais existir. Para forçar, basta esperar o próximo ciclo.

**Posso deletar um tier que ainda tem assinantes?**
Não. O bot bloqueia a exclusão enquanto houver assinaturas ativas naquele tier. Remova ou aguarde a expiração dos VIPs primeiro.

!!! tip "Dica"
    Códigos podem ter **validade própria** (`expira`) separada da **duração do VIP** (`duracao`). Use isso para promoções com prazo: por exemplo, `duracao:30d expira:7d` gera um código que dá 30 dias de VIP, mas só pode ser resgatado dentro dos próximos 7 dias. Se você não informar um código personalizado, o bot gera um automático no formato `VIP-XXXXXX`.

