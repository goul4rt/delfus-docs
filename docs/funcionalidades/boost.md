# Recompensas de boost

Reage automaticamente quando alguém impulsiona (boost) o seu servidor: envia uma mensagem de agradecimento personalizada no canal que você escolher e, opcionalmente, concede um plano VIP ao membro que impulsionou — renovando esse VIP sozinho enquanto o boost continuar ativo. É uma forma simples de reconhecer publicamente quem apoia o servidor e de premiar esses membros com benefícios automáticos, sem nenhum trabalho manual da moderação.

![Recompensas de boost no painel do Delfus](../assets/dashboard/boost.png){ .dx-shot loading=lazy }

*Recompensas de boost no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O bot observa os boosts do servidor em tempo real. Sempre que o Discord avisa que um membro **começou** ou **deixou** de impulsionar, o bot reage na hora. Além disso, um job em segundo plano revisa periodicamente quem ainda está impulsionando para manter as recompensas VIP em dia.

### Quando alguém começa a impulsionar

1. **O bot detecta o início do boost.** Internamente, ele percebe que o membro passou de "não-booster" para "booster" (o Discord marca a data em que a pessoa começou a impulsionar).
2. **Mensagem de agradecimento (se ativada).** Se você ativou a mensagem de boost, o bot publica no canal que você configurou a mensagem que você montou. Ela pode ser:
   - **Texto simples** — uma mensagem de texto pura; ou
   - **Embed (Rich Embed)** — um cartão estilizado com título, descrição, cor, imagem, miniatura (thumbnail), rodapé com ícone, autor, carimbo de data/hora e campos.
   
   Você ainda pode anexar uma **imagem** e adicionar até **3 botões de link** (cada um com um texto e uma URL que abre fora do Discord).
3. **VIP automático (se ativado).** Se você ativou a recompensa VIP e escolheu um plano (tier), o membro que impulsionou recebe automaticamente esse plano VIP, válido pela quantidade de dias que você definir (padrão de **30 dias**). Quem concede o VIP é o próprio bot.
4. As duas coisas — mensagem e VIP — são independentes: o bot pode mandar a mensagem, conceder o VIP, ou ambos, conforme você ativar cada um.

### Variáveis (placeholders) nas mensagens

Em qualquer campo de texto da mensagem (conteúdo, e também título, descrição, rodapé, autor e campos do embed) você pode usar variáveis que o bot substitui na hora do envio:

| Variável | Substituída por |
| --- | --- |
| `{{@user}}` | Menção do membro que impulsionou (notifica a pessoa) |
| `{{user}}` | Nome de exibição do membro no servidor |
| `{{server}}` | Nome do servidor |
| `{{memberCount}}` | Total de membros do servidor |
| `{{boostCount}}` | Total de boosts ativos no servidor |
| `{{boostTier}}` | Nível de boost do servidor, de 0 a 3 |
| `{{boostTierName}}` | Nome do nível (`Nenhum`, `Tier 1`, `Tier 2` ou `Tier 3`) |

### Renovação automática enquanto o boost continuar

A cada **6 horas**, o bot revisa todos os servidores que têm a recompensa VIP ativada e percorre todos os membros que ainda estão impulsionando. Para cada um:

1. Verifica se o membro **ainda tem VIP ativo**.
2. Se o membro continua impulsionando mas o VIP **já venceu**, o bot **renova o VIP automaticamente** (concede de novo o mesmo plano, pela mesma duração configurada).

Isso resolve um detalhe do Discord: quando alguém renova o boost sem deixar passar tempo entre um e outro, o Discord **não** dispara um novo aviso de boost. Sem essa revisão periódica, o membro poderia perder o VIP mesmo continuando a impulsionar. Na prática, **o membro mantém o benefício VIP pelo tempo em que continuar com o boost ativo**.

### Quando alguém deixa de impulsionar

O bot também detecta quando um membro remove o boost (passa de booster para não-booster) e pode enviar uma mensagem de "unboost" no canal configurado, com as mesmas opções de personalização da mensagem de boost.

> Observação: a mensagem de boost, a mensagem de unboost e a recompensa VIP são totalmente independentes — você pode ativar só uma, duas ou todas. Atualmente o painel disponibiliza a configuração das abas **Boost** e **VIP**; a configuração de unboost existe no bot, mas não está aberta na interface do dashboard no momento.

## Comandos

Esta feature é configurada apenas pelo painel. Não há comandos de barra próprios — toda a configuração é feita pelo Dashboard.

## Configuração

Tudo é configurado pelo Dashboard, na seção **Boost do Servidor** ([admin.delfus.app](https://admin.delfus.app)), por servidor. A tela tem duas abas: **Boost** e **VIP**.

### Pré-requisito no Discord

Para que as mensagens de boost funcionem, ative no Discord, em **Configurações do Servidor → Visão geral / Sistema**, a opção **"Enviar uma mensagem quando alguém impulsionar este servidor"** e selecione um canal. Sem isso, o evento de boost pode não chegar de forma confiável.

### Aba Boost (mensagem de agradecimento)

1. Ligue o interruptor **Ativo** no topo do cartão da mensagem de boost.
2. **Canal** — escolha em qual canal de texto a mensagem será publicada.
3. **Estilo da mensagem** — escolha entre **Texto Simples** ou **Rich Embed**.
   - No estilo **Texto**, escreva o conteúdo livremente no campo de texto.
   - No estilo **Embed**, use o editor visual de embed para montar título, descrição, cor, campos, rodapé etc.
4. **Imagem (opcional)** — informe a URL de uma imagem. No estilo embed, ela aparece dentro do embed; no estilo texto, é enviada como anexo.
5. **Botões de Link (máx. 3)** — adicione até três botões; cada um tem um **Label** (texto do botão) e uma **URL**. Eles funcionam como links externos.
6. Use as variáveis da tabela acima em qualquer campo de texto. A caixa de "Placeholders disponíveis" no painel lista todas elas.

### Aba VIP (recompensa automática)

1. Ligue o interruptor **Ativo** no cartão **VIP por Boost**.
2. **Tier VIP** — selecione qual plano VIP será concedido a quem impulsionar. É preciso já ter pelo menos um plano VIP criado no servidor para que apareça na lista.
3. **Duração (dias)** — quantos dias o VIP dura a cada concessão. Aceita valores de **1 a 365** dias; o padrão é **30 dias** (próximo da duração de um boost no Discord, que é de aproximadamente 30 dias).

Ao terminar, clique em **Salvar**. Há também um botão **Deletar**, que remove toda a configuração de boost (mensagens e VIP) — depois disso, nenhuma mensagem de boost/unboost é mais enviada.

## Exemplos de uso

- **Agradecer publicamente cada novo boost:** ative a aba Boost, escolha o canal de avisos e use um texto como `{{@user}} acabou de dar boost! Agora temos {{boostCount}} boosts e estamos no {{boostTierName}} 🚀`. Toda vez que alguém impulsionar, o servidor inteiro vê o agradecimento e a pessoa é mencionada.
- **Premiar boosters com VIP automático:** crie um plano VIP exclusivo para boosters, vá à aba VIP, selecione esse plano e deixe a duração em 30 dias. Quem impulsionar ganha o VIP na hora, e o bot renova sozinho a cada 6 horas enquanto o boost continuar — sem a moderação precisar acompanhar manualmente quem ainda está impulsionando.
- **Mensagem rica com botões:** monte a mensagem como embed, com cor da marca do servidor e uma imagem comemorativa, e adicione botões de link como "Saiba mais sobre boost" ou "Entrar no canal VIP" apontando para uma página ou canal de regras.

## Requisitos

- O bot precisa ter acesso ao canal escolhido e **permissão de enviar mensagens** (e, para embeds, **incorporar links**) nesse canal — caso contrário a mensagem não é publicada.
- Para a recompensa VIP, é preciso ter **pelo menos um plano (tier) VIP criado** no servidor, já que você seleciona qual plano será concedido.
- No Discord, mantenha ativada a opção de **enviar mensagem ao impulsionar** (citada na seção de configuração), para que os eventos de boost cheguem de forma confiável.

## Perguntas frequentes

**O membro perde o VIP assim que o VIP "vence", mesmo continuando a impulsionar?**
Não. A cada 6 horas o bot revisa quem ainda está impulsionando e renova o VIP de quem continua com o boost ativo, mesmo que a concessão anterior já tenha vencido. O benefício só termina quando o VIP vence **e** o boost não está mais ativo.

**Posso usar texto e embed ao mesmo tempo?**
Você escolhe um estilo por mensagem. No estilo embed, se você também preencher o campo de conteúdo de texto, o bot envia o texto junto com o embed; no estilo texto, vai apenas o texto (com a imagem como anexo, se houver).

**Por que o membro recebeu a menção mas eu não queria notificá-lo?**
A variável `{{@user}}` cria uma menção real e notifica a pessoa. Se preferir só exibir o nome sem notificar, use `{{user}}` no lugar.

**Existe comando de barra para configurar isso?**
Não. Toda a configuração — mensagens e recompensa VIP — é feita pelo Dashboard, sem comandos no Discord.

!!! tip "Dica"
    Deixe a recompensa VIP ativa e use uma duração próxima de 30 dias: como o bot renova o VIP automaticamente a cada 6 horas enquanto o boost estiver ativo, o membro nunca fica sem o benefício no meio do caminho — e só o perde quando realmente para de impulsionar. Isso transforma o VIP num incentivo contínuo para manter o boost.

