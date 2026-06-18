# Moderação e punições

Warns, mutes, kicks e bans num fluxo único, com checagens de segurança automáticas e histórico permanente. Você decide a punição; o bot avisa o usuário, registra e escala.

![Configuração de moderação no painel do Delfus](../assets/dashboard/moderacao.png){ .dx-shot loading=lazy }

*Configuração de moderação no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

Toda punição começa com um comando da staff e passa pelas mesmas checagens antes de agir.

Primeiro o bot confere o alvo: ninguém pune a si mesmo, e mute, ban e kick não funcionam em outros bots. Depois valida a hierarquia de cargos. O cargo do bot e o seu precisam estar acima do cargo da pessoa. Isso vale até para Administradores: você não pune alguém com cargo igual ou maior que o seu.

Ban, mute e kick pedem **Confirmar / Cancelar** antes de agir. Warn, unwarn e unmute vão direto. Aplicada a punição, a pessoa pode receber um aviso por DM (se você ativou), o canal da staff pode ser notificado e tudo fica gravado no histórico.

!!! example "Exemplo"
    Alguém posta um print de golpe no chat. Você roda `/ban`, confirma no botão e pronto: o Delfus apaga as mensagens das últimas 24h do autor, manda uma DM com o motivo (e link de apelação, se você configurou) e registra tudo no histórico. A staff vê no resultado se a DM chegou.

### Punições que se escalam sozinhas

Cada warn soma um ponto no contador da pessoa. Você define o que acontece ao bater um número exato: silenciar, expulsar, banir, dar ou tirar um cargo.

A staff só usa `/warn` e o bot escala a punição sozinho. Ele ainda mostra uma barra de progresso a cada advertência, tipo `Avisos: ▓▓░ 2/3 → mute 1h`, então todo mundo enxerga o que vem pela frente.

### Segunda chance pra quem se comporta

Com a **expiração de warns** ativada, advertências antigas deixam de contar depois do prazo que você escolher (ex.: 30 dias sem novas confusões). O contador é recalculado. Se a queda desfizer um gatilho de "adicionar cargo" (tipo um cargo de observação), o Delfus tira o cargo de volta automaticamente. Se quiser, ele publica um reconhecimento de bom comportamento no canal de logs.

!!! note "Detalhe"
    Gatilhos de **remover** cargo não são revertidos. O bot não devolve um cargo retirado, para não reconceder algo privilegiado por engano.

### Histórico e auditoria

O `/warnlist` mostra o histórico completo de uma pessoa: quem puniu, tipo, motivo, data, duração e se foi auto-ação. O **registro de ações (action log)** pode publicar num canal de auditoria quase tudo que rola no servidor: mensagens apagadas, entradas e saídas, mudanças de cargo, bans. Sempre identificando o autor pelo log de auditoria do Discord.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/warn` | Adverte alguém, soma no contador, mostra a barra de progresso e dispara gatilhos automáticos ao bater o número configurado. |
| `/unwarn` | Remove uma advertência pela `id_advertencia` (vista no `/warnlist`) ou, sem ID, a mais recente. |
| `/warnlist` | Mostra o histórico de punições, 5 por página. Ver o seu é livre; ver o de outra pessoa exige cargo maior que o dela. |
| `/mute` | Silencia via timeout do Discord. `duration` opcional (ex.: `30s`, `5min`, `2h`); sem duração, vai no máximo de 28 dias. Pede confirmação. |
| `/unmute` | Tira o silêncio. Avisa se a pessoa não estava silenciada. |
| `/ban` | Bane. `duration` opcional para ban temporário; sem ela, é permanente. Apaga as mensagens das últimas 24h. Pede confirmação. |
| `/kick` | Expulsa do servidor (a pessoa pode voltar com novo convite). Pede confirmação. |

!!! note "Opções"
    Todos os comandos pedem o **usuário**. O **motivo** é sempre opcional (aparece na DM, no histórico e no log). A **duração** de `/mute` e `/ban` aceita segundos (`s`), minutos (`m`/`min`) e horas (`h`). Número sem unidade vira segundos.

## Configuração

As punições rodam pelos comandos no Discord. O **comportamento** delas você ajusta no [Dashboard](https://admin.delfus.app), na seção **Moderação**.

O essencial para deixar pronto:

1. **Avisos por DM** — ligue ou desligue a DM por tipo de punição. Por padrão, warn e unwarn avisam; mute, kick e ban vêm desligados.
2. **Canal de logs** — escolha onde caem as notificações da staff e o reconhecimento de bom comportamento.
3. **Link de apelação** — uma URL incluída nas DMs para a pessoa contestar.
4. **Gatilhos automáticos** — cadastre regras "ao atingir X warns → ação" (silenciar, expulsar, banir, dar ou tirar cargo).
5. **Expiração de warns** — ative e defina o prazo em dias, semanas ou meses.
6. **Action log** — ative o registro, escolha um canal (ou um por tipo de evento) e use os filtros para ignorar bots, canais e cargos.

!!! tip "Personalização"
    Dá pra customizar o embed de cada tipo de punição (título, cor, imagem, campos) usando variáveis como `{user}`, `{staff}`, `{reason}`, `{duration}` e `{guild}`.

## Exemplos

!!! example "Punição em escada, sem decidir caso a caso"
    Configure "3 warns → mute 1h", "5 warns → mute 12h", "7 warns → ban". A staff só usa `/warn`; o Delfus escala a punição sozinho e mostra a barra de progresso a cada aviso. Ninguém precisa lembrar de cabeça qual é o próximo passo.

!!! example "Segunda chance automática"
    Ative a expiração em 30 dias. Quem passar um mês sem novas advertências tem o histórico zerado. Se a queda desfizer um cargo de "observação" dado por gatilho, o bot remove o cargo sozinho e reconhece o bom comportamento no canal de logs.

!!! example "Ban temporário com aviso e apelação"
    Rode `/ban usuario:@Fulano duracao:2h motivo:flood` e confirme. Antes de sair do servidor, a pessoa recebe a DM com o motivo e o link de apelação, as mensagens das últimas 24h dela somem, e você vê no resultado se a DM foi entregue.

## Perguntas frequentes

**Por que o silêncio "permanente" some depois de um tempo?**
O `/mute` usa o timeout do Discord, com teto de 28 dias. Um mute sem duração vira 28 dias. Para algo realmente permanente, use um cargo de "mutado" via gatilho de cargo, ou um ban.

**Posso usar `2d` ou `1w` na duração?**
Não. O campo aceita só segundos (`s`), minutos (`m`/`min`) e horas (`h`), tipo `30s`, `5min`, `2h`. Número sem unidade é lido como segundos.

**A DM diz "DMs fechadas". A punição valeu mesmo assim?**
Valeu. A DM é independente da punição. Se a pessoa bloqueia DMs, o bot só registra isso e segue com o kick ou ban normalmente.

**O `/unwarn` remove qual advertência?**
Com o `id_advertencia` (visto no `/warnlist`), remove aquela específica; sem ID, remove a mais recente. Nos dois casos a contagem é atualizada e fica tudo registrado.

!!! tip "Dica"
    Combine **gatilhos** com **expiração de warns**: monte a escada (3 → mute, 5 → ban) e ative a expiração em 30 dias. A staff só precisa advertir, a punição fica consistente e quem se comporta ganha histórico limpo, incluindo a remoção automática de cargos de "observação" quando a contagem cai.

