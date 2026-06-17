# Análise e insights

O Delfus coleta automaticamente dados de atividade do seu servidor — mensagens, entradas e saídas de membros, uso de voz e emojis — e transforma tudo em gráficos e rankings que você consulta tanto no Discord quanto no painel web.

## Como funciona

O bot está sempre observando a atividade do servidor em segundo plano e acumulando contagens para montar as estatísticas. O fluxo é o seguinte:

1. **Coleta contínua.** A cada mensagem enviada, o bot soma uma contagem para aquele canal, autor e hora. A cada emoji usado (seja dentro de uma mensagem ou como reação) e a cada vez que alguém atualiza o perfil, ele também registra. Membros entrando e saindo são contabilizados pelos eventos de entrada/saída.
2. **Acúmulo em memória.** Para não sobrecarregar o banco de dados, essas contagens ficam acumuladas em memória em vez de serem gravadas uma a uma. O bot junta tudo por hora, canal, usuário e emoji.
3. **Gravação periódica.** Cerca de uma vez por minuto o bot descarrega esse acúmulo no banco, consolidando os números. Por isso as estatísticas refletem a atividade quase em tempo real, com um pequeno atraso de poucos minutos — emojis recém-usados, por exemplo, podem levar um instante até aparecer nos rankings.
4. **Consulta no Discord.** Quando você usa um comando de estatística, o bot lê esses dados consolidados e responde. Os gráficos (`/grafico`) são gerados como uma imagem com a identidade do servidor, mostrando linhas de evolução e os destaques do período. Logo abaixo da imagem aparecem botões para **recarregar** o gráfico e **trocar o período** (1 dia, 7 dias ou 30 dias) — ao clicar, o próprio gráfico é regerado na mesma mensagem.
5. **Consulta no painel.** Os mesmos dados alimentam as telas de visão geral, insights e emojis do Dashboard, onde você vê tudo de forma navegável sem precisar abrir o Discord.

O que você obtém no fim:

- **`/grafico overview`** — visão geral do servidor (mensagens dos últimos 30 dias, atividade de voz, membros e os canais e membros mais ativos).
- **`/grafico membros`** — evolução de entradas, saídas e total de membros ao longo do período.
- **`/grafico canal`** — evolução de mensagens de um canal específico.
- **`/guildstats`** — um resumo rápido do servidor (data de criação, dono, total de membros, quantidade de canais de texto e voz, banner).
- **`/emoji-stats top`** — ranking dos emojis mais usados, separando uso em mensagens e em reações, e marcando emojis externos ao servidor.
- **`/emoji-stats sem-uso`** — lista os emojis do servidor que ainda não foram usados nenhuma vez.
- **`/emoji-stats nomes-estranhos`** — aponta emojis com nomes pouco descritivos (números, nomes muito curtos ou genéricos), úteis para uma faxina na lista de emojis.

## Configuração

Não há nada a ativar: a coleta de estatísticas roda sozinha assim que o bot está no servidor. Você consulta os dados de duas formas:

- **Pelo Discord**, com os comandos `/grafico`, `/guildstats` e `/emoji-stats`.
- **Pelo Dashboard** em [admin.delfus.app](https://admin.delfus.app), nas telas de visão geral, insights e emojis.

## Requisitos

- Os comandos `/grafico`, `/guildstats` e `/emoji-stats` só funcionam dentro de um servidor.
- O `/emoji-stats` exige a permissão **Gerenciar Servidor** para ser usado.
- Como as estatísticas dependem de dados coletados ao longo do tempo, um servidor recém-adicionado pode mostrar pouca ou nenhuma informação até o bot acumular atividade.

!!! tip
    Os números aparecem com um pequeno atraso (alguns minutos) porque o bot consolida a atividade periodicamente. Se um emoji ou mensagem recente ainda não apareceu no ranking, use o botão **Reload** do gráfico ou aguarde um instante.
