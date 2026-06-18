# VIP, assinaturas e recompensas

Defina os benefícios uma vez e o Delfus cuida do resto: ativa o VIP, controla o prazo, avisa o membro antes de acabar e remove tudo na hora certa, sem trabalho manual.

![Planos VIP no painel do Delfus](../assets/dashboard/vip.png){ .dx-shot loading=lazy }

*Planos VIP no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O VIP tem três peças, nesta ordem: benefícios, níveis e entrega.

1. **Benefícios (recompensas)**: as vantagens individuais. Um cargo, XP em dobro, mais chances em sorteios, bônus no `/daily` ou um slot de família.
2. **Níveis (tiers)**: você junta vários benefícios num pacote, tipo "Ouro" ou "Diamante", e dá uma prioridade. Quanto maior o número, mais alto o nível.
3. **Entrega**: você passa o nível pro membro de duas formas. Gerando um código que ele resgata, ou concedendo direto pra alguém.

A partir daí o Delfus assume. Aplica os benefícios na hora, marca quando expira, avisa o membro antes do prazo, remove tudo quando acaba e devolve sozinho cargos VIP que sumiram.

!!! example "Exemplo"
    Você cria um cargo "VIP Ouro" e um bônus de XP em dobro. Junta os dois num nível "Ouro". Gera um código e vende. O membro digita `/vip resgatar`, o código é validado e ele já fica com o cargo e ganhando XP dobrado. Daqui a 30 dias o bot tira tudo automaticamente, depois de avisá-lo antes.

### Os tipos de benefício

Cada recompensa é de um tipo:

- **Cargo**: dá um cargo automático ao membro VIP e tira quando expira.
- **Multiplicador de XP**: multiplica o XP que ele ganha, de 1x a 5x.
- **Sorteios**: mais entradas nos sorteios, de 1 a 10 chances.
- **Bônus diário**: moedas extras no `/daily`, fixas ("+50") ou em percentual ("+25%").
- **Família**: libera um slot pro membro criar uma família com cargo próprio, via `/familia criar`.

### O que acontece nos bastidores

Você não precisa se preocupar com isso, mas é bom saber que o bot:

- **Calcula a expiração** e cria a assinatura quando o VIP é ativado.
- **Avisa de hora em hora** quem está perto de perder o VIP. Por padrão, 3 dias antes.
- **Expira sozinho**: tira os cargos, para os bônus e congela famílias vinculadas àquele VIP.
- **Conserta cargos a cada 6 horas**: devolve cargo VIP que alguém tirou na mão e remove cargo que sobrou.

!!! note "Já tem VIP e ganha outro?"
    Se o novo nível for mais alto, o bot faz upgrade e troca o nível. Se for igual ou menor, ele soma os dias ao VIP atual em vez de recomeçar, ótimo pra quem renovou. Um VIP permanente continua permanente.

## Comandos

### Para os membros: `/vip`

| Comando | O que faz |
| --- | --- |
| `/vip status` | Mostra seu VIP atual: nível, quando expira e seus benefícios. |
| `/vip info [tier]` | Lista os níveis disponíveis, ou os detalhes de um nível específico. |
| `/vip resgatar codigo:<código>` | Resgata um código VIP (também funciona como `/vip redeem`). |

### Para administradores: `/vip-admin`

Restrito a admins. Os comandos estão organizados em grupos:

| Comando | O que faz |
| --- | --- |
| `/vip-admin reward create` | Cria uma recompensa (cargo, XP, sorteio, bônus diário ou família). |
| `/vip-admin reward list` / `delete` | Lista ou remove recompensas. |
| `/vip-admin tier create` | Monta um nível com nome, prioridade e recompensas. |
| `/vip-admin tier list` / `info` / `edit` / `delete` | Lista, detalha, edita ou apaga um nível. |
| `/vip-admin code create` | Gera um código: nível, duração, máximo de usos e validade opcional. |
| `/vip-admin code list` / `delete` | Lista ou remove códigos. |
| `/vip-admin user give` | Concede VIP direto a um membro. |
| `/vip-admin user remove` / `time` / `list` | Remove o VIP, ajusta dias ou lista quem tem VIP. |
| `/vip-admin config ...` | Configura canal de avisos, DMs, dias de antecedência e mais. |

!!! tip "Como escrever a duração"
    Aceita `30d` (dias), `2w` (semanas), `1m` (mês = 30 dias) ou só um número (`30` = 30 dias). Use `0` para deixar o VIP permanente. Vale só ao conceder ou criar código.

## Configuração

Configure tudo pelos comandos `/vip-admin config` ou pelo [Dashboard](https://admin.delfus.app). Dá no mesmo.

O caminho mais tranquilo:

1. **Crie os benefícios** primeiro (`reward create`).
2. **Monte os níveis** juntando os benefícios e definindo a prioridade (`tier create`). Cada nível precisa de pelo menos um benefício, e nome e prioridade não podem repetir.
3. **Distribua**: gere códigos pra vender ou sortear (`code create`), ou conceda direto (`user give`).
4. **Ajuste os avisos** no grupo `config`: canal de notificações, DMs e quantos dias antes avisar.

!!! note "Bom saber"
    Cada servidor pode ter até 10 níveis, 20 benefícios por nível e 100 códigos ativos. Detalhe das DMs: se o membro está com as mensagens do servidor fechadas, o aviso não chega, mas o VIP ativa normalmente.

## Exemplos

!!! example "Vender um plano mensal"
    Crie um cargo "VIP Ouro" e um XP em dobro, junte num nível "Ouro" e gere códigos com `/vip-admin code create tier:Ouro duracao:30d`. Venda cada código. O membro resgata com `/vip resgatar` e ganha cargo + XP dobrado por 30 dias. Quando acabar, o bot tira tudo sozinho.

!!! example "Recompensar staff ou apoiador na hora"
    Sem código nenhum: `/vip-admin user give usuario:@membro tier:Diamante duracao:0` dá um VIP permanente direto. Ideal pra quem você quer premiar pra sempre.

!!! example "Quem renovou ganha mais tempo, não recomeça"
    Um membro já tem "Ouro" e compra outro mês? Entregue outro código do mesmo nível. O bot soma 30 dias à assinatura atual em vez de zerar o relógio.

!!! example "Família com cargo próprio"
    Inclua um benefício de família num nível. Os assinantes montam a própria família com `/familia criar`, com cargo e tudo. Se o VIP expirar, a família é congelada automaticamente.

## Perguntas frequentes

**Um membro pode usar o mesmo código duas vezes?**
Não. Cada pessoa resgata um código só uma vez. Mas o mesmo código pode ser usado por vários membros, até bater o limite de usos que você definiu.

**E se o membro já tem VIP e resgata outro código?**
Se for de um nível mais alto, vira upgrade. Se for do mesmo nível ou menor, o bot soma os dias ao VIP atual (com a extensão habilitada, que é o padrão).

**Tirei o cargo VIP de alguém na mão. O bot devolve?**
Devolve. A cada 6 horas ele confere e restaura cargos VIP que sumiram. É só esperar o próximo ciclo.

**Posso apagar um nível que ainda tem assinantes?**
Não. O bot bloqueia enquanto houver VIP ativo naquele nível. Espere os VIPs expirarem ou remova-os antes.

!!! tip "Dica"
    Códigos podem ter validade própria, separada da duração do VIP. Use isso em promoções: `duracao:30d expira:7d` cria um código que dá 30 dias de VIP, mas só pode ser resgatado nos próximos 7 dias. Se você não escolher um código, o bot gera um automático no formato `VIP-XXXXXX`.
