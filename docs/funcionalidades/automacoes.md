# Automações de canal

As automações de canal aplicam regras automáticas a cada mensagem enviada em um canal: você define o que aquele canal aceita (só mídia, só comandos, só arquivos), faz o bot publicar anúncios sozinho ou abrir um tópico de discussão para cada post. O bot age na hora, sem precisar de moderador online — e tudo fica registrado para você acompanhar pelo painel.

## Como funciona

Cada canal pode ter **uma ou mais** automações configuradas. Sempre que alguém envia uma mensagem nesse canal, o bot avalia as regras na ordem que você definiu e age conforme o tipo de cada uma. Se um canal não tem nenhuma automação, nada acontece — as regras só rodam onde você configurou.

### O que o bot ignora sempre

Antes de avaliar qualquer regra, o bot descarta automaticamente algumas mensagens, independente da configuração:

- Mensagens de sistema do Discord (entrou no servidor, fixou mensagem, etc.).
- Mensagens enviadas por **webhooks**.
- As próprias mensagens do bot (inclusive o aviso temporário que ele acabou de mandar — assim ele nunca se autoapaga).

### Quem passa livre pelas regras

Para cada automação você pode definir exceções:

- **Ignorar bots** — quando ligado, mensagens de outros bots não são afetadas pela regra. (Vem ligado por padrão.)
- **Cargos que ignoram a regra** (lista de exceções) — qualquer membro que tenha pelo menos um dos cargos da lista passa livre por aquela automação. Ideal para a equipe postar à vontade no canal sem ser barrada.

> Observação: nas automações de **Tópico automático** e **Publicação automática**, a exceção que vale é apenas a de "ignorar bots". A lista de cargos liberados tem efeito prático nas regras que apagam mensagem (mídia, comandos, arquivos). No caso da **Publicação automática**, a lista de cargos funciona como um *filtro de quem é publicado* (explicado abaixo), não como exceção.

### Ordem e prioridade

Quando o mesmo canal tem várias automações, o bot as executa **da menor prioridade para a maior** — o número **menor roda primeiro**. Assim que uma regra **apaga** a mensagem, as regras seguintes deixam de ser aplicadas (a mensagem já não existe). Regras que não apagam (como reagir, criar tópico ou publicar) não interrompem a sequência. Se o canal tem só uma automação, a prioridade não importa — pode deixar em 0.

### Avisos temporários

Quando uma mensagem é apagada (ou só recebe um aviso), o bot envia uma mensagem curta no canal explicando o motivo e a **apaga sozinho cerca de 8 segundos depois**, para não poluir o canal. Esses avisos têm proteções importantes:

- **Nunca mencionam** @everyone, @here, cargos ou usuários — mesmo que o texto que você configurou contenha menções, elas são neutralizadas.
- **Limite anti-flood**: se o mesmo membro envia várias mensagens em sequência no mesmo canal, os avisos são limitados a no máximo um a cada 10 segundos por pessoa. **A remoção das mensagens continua acontecendo em todas as vezes** — só o aviso de texto é segurado para o bot não virar spam.

### Registro de ações (auditoria)

Cada ação automática do bot é registrada: mensagem apagada, aviso enviado, tópico criado e publicação feita. O registro guarda apenas identificadores (do servidor, do canal, da mensagem e do autor) e o motivo — **nunca o conteúdo da mensagem**. O painel usa esses registros para mostrar estatísticas por servidor (quantas mensagens foram apagadas, quantos tópicos criados, quantas publicações, quantos avisos).

### Os cinco tipos de automação

#### 1. Somente mídia (`MEDIA_ONLY`)

O canal aceita apenas os tipos de mídia que você escolher: **imagens**, **GIFs**, **vídeos** e/ou **figurinhas** (cada um pode ser ligado/desligado separadamente). O fluxo de avaliação:

1. Se a mensagem não traz nenhuma das mídias permitidas, ela é **apagada** com o aviso configurado.
2. Você pode exigir um **tamanho mínimo de imagem** (largura e altura em pixels). Imagens menores que esse limite são tratadas como não aceitas — útil para barrar emojis salvos e miniaturas minúsculas. (O limite vale para imagens; GIFs, vídeos e figurinhas não são medidos.)
3. Você pode **bloquear legendas**: se "permitir legenda" estiver desligado e a mensagem tiver mídia válida mas vier acompanhada de texto, ela é apagada.
4. Quando a mídia é aceita, se você configurou **reações automáticas**, o bot reage com aqueles emojis na mídia, em ordem — já abrindo as votações/curtidas do post.

#### 2. Somente comandos (`COMMAND_ONLY`)

O canal só aceita comandos. Uma mensagem é aceita quando:

- É um **comando de barra (slash)** nativo do Discord; ou
- Começa com um dos **prefixos** que você definiu (por exemplo `/`, `!`, `?`).

Qualquer outra mensagem é **apagada**, e o bot manda o aviso de redirecionamento que você configurou. Se você apontar um **canal de conversa**, o aviso inclui um link para ele (ex.: "Aqui é só para comandos. Use o canal de conversa #bate-papo").

#### 3. Somente arquivos (`FILE_ONLY`)

O canal só aceita anexos válidos. Um arquivo é aceito quando atende a **duas** condições ao mesmo tempo:

- **Extensão permitida** — se você definiu uma lista de extensões (ex.: `.pdf`, `.zip`, `.docx`), só elas passam. Lista vazia = qualquer extensão.
- **Tamanho dentro do intervalo** — o arquivo precisa ter pelo menos o tamanho mínimo e, se houver máximo, não ultrapassá-lo. Tamanho máximo em 0 significa "sem limite máximo".

Mensagens sem nenhum arquivo válido (sem anexo, extensão errada ou tamanho fora do intervalo) são **apagadas** com o aviso configurado.

#### 4. Tópico automático (`AUTO_THREAD`)

Para cada mensagem nova no canal, o bot abre um **tópico (thread)** atrelado a ela. O nome do tópico vem de um **modelo** que você escreve, com etiquetas que o bot substitui:

- `{author}` — nome de exibição de quem postou.
- `{date}` — a data atual (formato brasileiro, ex.: 17/06/2026).

O tópico tem um **tempo de arquivamento automático** que você escolhe (1 hora, 1 dia, 3 dias ou 1 semana). É ideal para canais de sugestões, dúvidas ou divulgações, onde cada post vira sua própria discussão.

#### 5. Publicação automática (`AUTO_PUBLISH`)

Em **canais de anúncio**, o bot publica (faz o *crosspost*) as mensagens automaticamente para os servidores que seguem o canal — sem ninguém precisar clicar em "Publicar". Antes de publicar, a mensagem precisa passar por alguns filtros que você define:

1. **Filtro de cargos** — se você informou cargos, só são publicadas as mensagens de quem tem pelo menos um deles. Vazio = todo mundo é publicado.
2. **Exigir conteúdo rico** — se ligado, mensagens sem imagem/GIF e sem embed não são publicadas (evita republicar coisas como "ok").
3. **Tamanho mínimo de texto** — mensagens com menos caracteres que o mínimo não são publicadas.

Quando a mensagem passa em todos os filtros, o bot publica. Você pode configurar um **atraso** (em minutos): publicar imediatamente (0) ou aguardar um tempo, dando uma janela para você editar ou apagar antes da republicação. **Este tipo só funciona em canais de anúncio** — em um canal de texto normal, a publicação é simplesmente ignorada.

## Comandos

Esta feature é configurada apenas pelo painel.

## Configuração

A configuração é feita inteiramente pelo Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção de **Automações de canal**. Cada automação tem campos comuns e campos específicos do tipo escolhido.

### Campos comuns a todas as automações

- **Canal** — onde a regra vale.
- **Tipo de automação** — Somente mídia, Somente comandos, Somente arquivos, Tópico automático ou Publicação automática.
- **Ativado** — liga/desliga a regra sem precisar apagá-la.
- **Ignorar bots** — quando ligado, não aplica a regra a mensagens de bots (padrão: ligado).
- **Cargos que ignoram a regra** — lista de cargos que ficam livres da automação (até 50 cargos).
- **Ordem de execução (prioridade)** — número de 0 a 100; menor roda primeiro. Só importa quando o mesmo canal tem mais de uma automação.

### Campos por tipo

**Somente mídia**
- Tipos permitidos: Imagens, GIFs, Vídeos, Figurinhas (cada um liga/desliga).
- Permitir legenda — aceita texto junto da mídia.
- Tamanho mínimo de imagem — em pixels (0 a 4096).
- Mensagem de aviso — texto enviado quando uma mensagem é apagada (até 500 caracteres).
- Reações automáticas — até **10 emojis**, incluindo emojis personalizados do servidor.

**Somente comandos**
- Prefixos de comando — lista separada por vírgula (de 1 a 10 prefixos, cada um até 5 caracteres). Padrão: `/`.
- Mensagem de redirecionamento — texto do aviso (até 500 caracteres).
- Canal de conversa — opcional; quando definido, o aviso vira um link para ele.

**Somente arquivos**
- Extensões permitidas — lista separada por vírgula (até 50; vazio = todas).
- Tamanho mínimo (KB) e Tamanho máximo (KB) — máximo em 0 significa "sem limite".
- Mensagem de aviso — texto do aviso (até 500 caracteres).

**Tópico automático**
- Modelo do nome do tópico — texto com as etiquetas `{author}` e `{date}` (até 100 caracteres). Padrão: `{author} — {date}`.
- Arquivar automaticamente após — 1 hora, 1 dia, 3 dias ou 1 semana.

**Publicação automática**
- Aguardar antes de publicar — atraso em minutos (0 a 1440; 0 = imediato).
- Publicar apenas mensagens destes cargos — filtro de cargos (vazio = todos).
- Exigir imagem ou conteúdo rico — só publica mensagens com mídia/embed.
- Tamanho mínimo do texto — em caracteres (0 = sem mínimo).

A página também mostra uma aba de **estatísticas** com a quantidade de automações por tipo e os totais acumulados de mensagens apagadas, tópicos criados, publicações e avisos do servidor.

## Exemplos de uso

- **Canal de memes só com imagens e votação automática**: crie uma automação de *Somente mídia* no canal, deixe ligadas Imagens/GIFs/Vídeos, defina um tamanho mínimo de imagem (ex.: 100px) para barrar miniaturas, e adicione as reações 👍 e 👎. Cada print postado já abre a votação sozinho, e textos soltos são removidos.

- **Canal de comandos do bot sem bate-papo**: configure *Somente comandos* com o prefixo `/`, aponte o canal `#bate-papo` como redirecionamento e escreva um aviso amigável. Quem mandar conversa nesse canal tem a mensagem removida e é convidado a ir para o canal certo. Adicione o cargo da staff à lista de exceções se quiser que a equipe possa escrever livre.

- **Canal de sugestões onde cada post vira discussão**: crie uma automação de *Tópico automático* com o modelo `{author} — {date}` e arquivamento de 3 dias. Toda sugestão postada ganha seu próprio tópico, onde a comunidade discute sem bagunçar o canal principal.

- **Canal de anúncios que se propaga sozinho**: em um canal de anúncio seguido por outros servidores, ative *Publicação automática* exigindo conteúdo rico e limitando aos cargos da equipe. Cada anúncio oficial é publicado automaticamente para todos os servidores seguidores.

## Requisitos

Para as automações funcionarem, o bot precisa das permissões adequadas no canal, conforme a ação:

- **Gerenciar mensagens** — para apagar mensagens nas regras de Somente mídia / Somente comandos / Somente arquivos.
- **Enviar mensagens** — para mandar os avisos temporários.
- **Adicionar reações** — para as reações automáticas do Somente mídia.
- **Criar tópicos públicos** — para o Tópico automático (o canal precisa permitir tópicos).
- **Publicar / Gerenciar mensagens em canal de anúncio** — para a Publicação automática. Esse tipo só funciona em **canais de anúncio**; em canais normais ele é ignorado.

Além disso, para reações automáticas com emojis personalizados, o bot precisa ter acesso aos emojis (em geral, estar no servidor de origem deles).

## Perguntas frequentes

**A regra apaga as mensagens da minha equipe também?**
Não, se você adicionar os cargos da equipe à lista de "cargos que ignoram a regra". Quem tiver um desses cargos passa livre pela automação. Bots também são ignorados por padrão.

**Posso ter mais de uma automação no mesmo canal?**
Sim. Elas rodam por ordem de prioridade (menor primeiro). Lembre-se de que, assim que uma regra apaga a mensagem, as seguintes não rodam — então coloque regras de remoção com a prioridade certa.

**Por que minha mensagem de aviso não menciona o cargo que coloquei nela?**
Por segurança, os avisos automáticos nunca disparam menções a @everyone, cargos ou usuários, mesmo que o texto contenha essas menções. Isso evita pings indevidos a cada remoção.

**A publicação automática não está funcionando no meu canal. Por quê?**
Esse tipo só funciona em **canais de anúncio**. Verifique também se a mensagem passou nos filtros (cargo permitido, conteúdo rico exigido e tamanho mínimo de texto) e se o bot tem permissão para publicar no canal.

!!! tip "Dica"
    Em canais de mídia muito ativos, ligue o **tamanho mínimo de imagem** (ex.: 64–100px) na automação "Somente mídia". Isso barra emojis salvos e miniaturas minúsculas que tecnicamente são "imagens", mantendo o canal só com prints e fotos de verdade.
