# Moderação e punições

Manter um servidor saudável dá trabalho — e é exatamente aí que o Delfus entra. Ele te dá warns, mutes, kicks e bans num fluxo único, com regras de segurança automáticas e um histórico permanente de tudo. Você foca em decidir; o resto (avisar o usuário, registrar, escalar punições) o bot cuida.

![Configuração de moderação no painel do Delfus](../assets/dashboard/moderacao.png){ .dx-shot loading=lazy }

*Configuração de moderação no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

Toda punição começa com um comando da staff e segue sempre o mesmo caminho, com checagens de segurança no meio para você não dar tiro no pé.

O bot primeiro confere o alvo: ninguém pune a si mesmo, e mute/ban/kick não funcionam em outros bots. Depois valida a **hierarquia de cargos** — tanto o cargo do bot quanto o seu precisam estar **acima** do cargo da pessoa. E sim, isso vale até pra quem é Administrador: você não pune alguém com cargo igual ou maior que o seu.

Ban, mute e kick ainda pedem um **Confirmar / Cancelar** antes de agir, pra evitar acidente. Warn, unwarn e unmute vão direto. Aplicada a punição, a pessoa pode receber um aviso por DM (se você ativou), o canal da staff pode ser notificado, e tudo fica gravado no histórico.

!!! example "Exemplo"
    Alguém posta um print de golpe no chat. Você roda `/ban`, confirma no botão e pronto: o Delfus apaga as mensagens das últimas 24h do autor, manda uma DM avisando o motivo (com link de apelação, se você configurou) e registra tudo no histórico. A staff vê no resultado se a DM chegou.

### Punições que se escalam sozinhas

A grande sacada são os **gatilhos automáticos**. Cada warn soma um ponto no contador da pessoa, e você define o que acontece ao bater um número exato: silenciar, expulsar, banir, dar ou tirar um cargo.

A staff só precisa usar `/warn` — o bot escala a punição sozinho. Inclusive ele mostra uma barrinha de progresso a cada advertência, tipo `Avisos: ▓▓░ 2/3 → mute 1h`, então todo mundo enxerga o que vem pela frente.

### Segunda chance pra quem se comporta

Se você ativar a **expiração de warns**, advertências antigas deixam de contar depois do prazo que você escolher (ex.: 30 dias sem novas confusões). O contador é recalculado e, se a queda desfizer um gatilho de "adicionar cargo" (tipo um cargo de observação), o Delfus tira o cargo de volta automaticamente. Se quiser, ele ainda publica um reconhecimento de bom comportamento no canal de logs.

!!! note "Detalhe"
    Gatilhos de **remover** cargo não são revertidos — o bot não devolve um cargo retirado, pra não reconceder algo privilegiado por engano.

### Histórico e auditoria

Nada se perde. O `/warnlist` mostra o histórico completo de uma pessoa: quem puniu, tipo, motivo, data, duração e se foi auto-ação. Além disso, o **registro de ações (action log)** pode publicar num canal de auditoria praticamente tudo que rola no servidor — mensagens apagadas, entradas e saídas, mudanças de cargo, bans — sempre identificando o autor pelo log de auditoria do Discord.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/warn` | Adverte alguém, soma no contador, mostra a barra de progresso e dispara gatilhos automáticos quando bate o número configurado. |
| `/unwarn` | Remove uma advertência — pela `id_advertencia` (vista no `/warnlist`) ou, sem ID, a mais recente. |
| `/warnlist` | Mostra o histórico de punições, 5 por página. Ver o seu é livre; ver o de outra pessoa exige cargo maior que o dela. |
| `/mute` | Silencia usando o timeout do Discord. `duration` opcional (ex.: `30s`, `5min`, `2h`); sem duração, vai no máximo de 28 dias. Pede confirmação. |
| `/unmute` | Tira o silêncio. Avisa se a pessoa não estava silenciada. |
| `/ban` | Bane. `duration` opcional pra ban temporário; sem ela, é permanente. Apaga as mensagens das últimas 24h. Pede confirmação. |
| `/kick` | Expulsa do servidor (a pessoa pode voltar com novo convite). Pede confirmação. |

!!! note "Opções"
    Todos os comandos pedem o **usuário**. O **motivo** é sempre opcional (aparece na DM, no histórico e no log). A **duração** de `/mute` e `/ban` aceita só segundos (`s`), minutos (`m`/`min`) e horas (`h`) — número sem unidade vira segundos.

## Configuração

As punições acontecem pelos comandos dentro do Discord. Já o **comportamento** delas você ajusta no [Dashboard](https://admin.delfus.app), na seção **Moderação**.

O essencial pra deixar pronto:

1. **Avisos por DM** — ligue ou desligue a DM por tipo de punição. Por padrão, warn e unwarn avisam; mute, kick e ban vêm desligados.
2. **Canal de logs** — escolha onde caem as notificações da staff e o reconhecimento de bom comportamento.
3. **Link de apelação** — uma URL incluída nas DMs pra pessoa contestar.
4. **Gatilhos automáticos** — cadastre regras "ao atingir X warns → ação" (silenciar, expulsar, banir, dar ou tirar cargo).
5. **Expiração de warns** — ative e defina o prazo em dias, semanas ou meses.
6. **Action log** — ative o registro, escolha um canal (ou um por tipo de evento) e use os filtros pra ignorar bots, canais e cargos.

!!! tip "Personalização"
    Dá pra customizar o embed enviado em cada tipo de punição — título, cor, imagem, campos — usando variáveis como `{user}`, `{staff}`, `{reason}`, `{duration}` e `{guild}`.

## Exemplos

!!! example "Punição em escada, sem decidir caso a caso"
    Configure "3 warns → mute 1h", "5 warns → mute 12h", "7 warns → ban". A staff só usa `/warn`; o Delfus escala a punição sozinho e mostra a barra de progresso a cada aviso. Ninguém precisa lembrar de cabeça qual é o próximo passo.

!!! example "Segunda chance automática"
    Ative a expiração em 30 dias. Quem passar um mês sem novas advertências tem o histórico zerado. Se a queda desfizer um cargo de "observação" que tinha sido dado por gatilho, o bot remove o cargo sozinho e reconhece o bom comportamento no canal de logs.

!!! example "Ban temporário com aviso e apelação"
    Rode `/ban usuario:@Fulano duracao:2h motivo:flood` e confirme. Antes de sair do servidor, a pessoa recebe a DM com o motivo e o link de apelação, as mensagens das últimas 24h dela somem, e você vê no resultado se a DM foi entregue.

## Perguntas frequentes

**Por que o silêncio "permanente" some depois de um tempo?**
O `/mute` usa o timeout do Discord, que tem teto de 28 dias — então um mute sem duração vira 28 dias. Pra algo realmente permanente, use um cargo de "mutado" via gatilho de cargo, ou um ban.

**Posso usar `2d` ou `1w` na duração?**
Não. O campo aceita só segundos (`s`), minutos (`m`/`min`) e horas (`h`), tipo `30s`, `5min`, `2h`. Número sem unidade é lido como segundos.

**A DM diz "DMs fechadas". A punição valeu mesmo assim?**
Valeu. A DM é independente da punição. Se a pessoa bloqueia DMs, o bot só registra isso e segue com o kick ou ban normalmente.

**O `/unwarn` remove qual advertência?**
Com o `id_advertencia` (visto no `/warnlist`), remove aquela específica; sem ID, remove a mais recente. Em ambos os casos a contagem é atualizada e fica tudo registrado.

!!! tip "Dica"
    Combine **gatilhos** com **expiração de warns**: monte a escada de punições (3 → mute, 5 → ban) e ative a expiração em 30 dias. A staff só precisa advertir, a punição fica consistente e quem se comporta ganha histórico limpo — inclusive com a remoção automática de cargos de "observação" quando a contagem cai.
