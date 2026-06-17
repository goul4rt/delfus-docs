# Automações de canal

As automações de canal aplicam regras automáticas a cada mensagem enviada num canal: você define o que aquele canal aceita (só mídia, só comandos, só arquivos), faz o bot publicar anúncios sozinho, ou abrir um tópico de discussão para cada mensagem. O bot age na hora, sem precisar de moderador online.

## Como funciona

Cada canal pode ter uma ou mais automações configuradas. Sempre que alguém envia uma mensagem nesse canal, o bot avalia as regras na ordem definida e age conforme o tipo. Se um canal não tem nenhuma automação, nada acontece — as regras só rodam onde você configurou.

Os tipos disponíveis são:

1. **Somente mídia** — o canal aceita apenas imagens, GIFs, vídeos ou figurinhas (você escolhe quais). Mensagens que não trazem a mídia permitida são apagadas na hora. Você pode exigir um tamanho mínimo de imagem (para barrar emojis e miniaturas minúsculas), bloquear legendas de texto junto da mídia, e fazer o bot reagir automaticamente com emojis nas mídias aceitas (para já abrir as votações/curtidas).
2. **Somente comandos** — o canal só aceita comandos de barra (slash) ou mensagens que começam com os prefixos que você definir. Qualquer outra mensagem é apagada, com um aviso que pode apontar para o canal correto de conversa.
3. **Somente arquivos** — o canal só aceita anexos com as extensões permitidas e dentro de um intervalo de tamanho (mínimo e máximo). Mensagens sem arquivo válido são apagadas.
4. **Tópico automático** — para cada mensagem nova, o bot abre um tópico (thread) atrelado a ela, com um nome baseado num modelo (pode incluir o autor e a data) e um tempo de arquivamento automático que você escolhe. Bom para canais de sugestões, dúvidas ou divulgações onde cada post vira sua própria discussão.
5. **Publicação automática** — em canais de anúncio, o bot publica (crosspost) as mensagens automaticamente para os servidores que seguem o canal. Você pode restringir a quais cargos isso se aplica, exigir que a mensagem tenha imagem/embed ou um tamanho mínimo de texto, e adicionar um atraso antes de publicar.

Pontos importantes do comportamento:

- **Quem é ignorado**: você pode definir que bots sejam ignorados e que certos cargos (lista de exceções) passem livres por qualquer regra — útil para staff postar o que quiser.
- **Avisos temporários**: quando uma mensagem é apagada (ou só recebe aviso), o bot manda uma mensagem curta explicando o motivo e a apaga sozinho poucos segundos depois, para não poluir o canal. Esse aviso nunca menciona @everyone, cargos ou usuários. Se alguém enviar muitas mensagens em sequência, os avisos são limitados para evitar flood (mas a remoção das mensagens continua acontecendo todas as vezes).
- **Ordem e prioridade**: se um canal tem várias regras, elas rodam por prioridade. Assim que uma regra apaga a mensagem, as seguintes deixam de ser aplicadas (a mensagem já não existe).
- **Registro de ações**: cada ação do bot (mensagem apagada, aviso enviado, tópico criado, publicação feita) fica registrada, e o painel mostra estatísticas com esses totais por servidor.

## Configuração

A configuração é feita inteiramente pelo Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção de automações de canal. Lá você escolhe o canal, o tipo de automação, ativa/desativa, define a prioridade, as exceções (bots e cargos liberados) e os ajustes específicos de cada tipo (extensões, tamanhos, emojis de reação, modelo de nome de tópico, etc.). Não há comando de barra para essa configuração — tudo passa pelo painel.

## Requisitos

Para as automações funcionarem, o bot precisa de permissões no canal de acordo com a ação:

- **Gerenciar mensagens** — para apagar mensagens nas regras de "somente mídia / comandos / arquivos".
- **Enviar mensagens** — para mandar os avisos temporários.
- **Adicionar reações** — para o auto-reação do "somente mídia".
- **Criar tópicos públicos** — para o "tópico automático".
- **Gerenciar mensagens / publicar** num canal de anúncio — para a "publicação automática" (esse tipo só funciona em canais de anúncio; em canais normais ele é ignorado).

!!! tip
    Adicione o cargo da sua equipe à lista de exceções da regra para que a staff possa postar livremente sem ser barrada pela automação do canal.
