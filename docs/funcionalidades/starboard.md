# Starboard

O Starboard transforma reações em um mural de destaques: quando uma mensagem recebe estrelas (ou qualquer emoji que você definir) suficientes, o Delfus a republica automaticamente em um canal de destaques do servidor. Inclui contagem com pesos e votos negativos, níveis visuais de exibição, ranking de membros com cargos de recompensa, resets periódicos e um Hall da Fama curado pela moderação. É a forma de premiar e dar visibilidade ao melhor conteúdo da sua comunidade — memes, arte, prints, mensagens marcantes — sem trabalho manual.

## Como funciona

O Starboard funciona com base em **murais** (boards). Cada mural tem um nome, um ou mais **emojis de voto**, um **canal de destino** e um número mínimo de estrelas para entrar. Você pode ter **vários murais ao mesmo tempo** no mesmo servidor (por exemplo, um para "melhores memes" e outro para "mensagens em destaque"), e um mesmo emoji pode ser compartilhado por mais de um mural.

### O fluxo por reação, do começo ao fim

1. **Alguém reage** a uma mensagem com um emoji. O Delfus identifica quais murais **ativos** usam aquele emoji naquele servidor. Se nenhum mural usa o emoji, nada acontece. Reações repetidas (vindas de eventos duplicados do Discord) são ignoradas por uma janela curta para evitar contagem dupla.

2. **O voto é validado** contra as regras do mural, nesta ordem:
   - **Reações de bots** são ignoradas (se o filtro de bots estiver ligado), assim como a própria reação que o Delfus dá nos posts.
   - **Auto-voto** (reagir na própria mensagem) é bloqueado quando o mural não permite — e nesse caso a reação é **sempre removida**, mesmo que a remoção automática esteja desligada, porque deixá-la visível confunde. Na primeira vez que um membro tenta dar auto-voto, ele recebe um **aviso por mensagem direta** (apenas uma vez por servidor; o Delfus lembra disso por cerca de 30 dias).
   - **Limite anti-spam (cooldown)**: se configurado, cada membro só pode dar um número máximo de votos naquele mural dentro de uma janela de tempo. Votos acima do limite são descartados.
   - **Listas de bloqueio/permissão**: o mural pode bloquear ou permitir por **usuário, cargo ou canal**, aplicando a regra a quem reage, a quem é autor da mensagem, ou a ambos. Regras mais específicas vencem as mais gerais (usuário > cargo > canal). Se houver qualquer regra de "permitir (apenas estes)", quem não estiver na lista é bloqueado.
   - **Filtros de mensagem**: idade mínima/máxima da mensagem e tamanho mínimo de texto.
   - Reações que falham em qualquer dessas checagens podem ser **removidas automaticamente** se a opção "remover reações inválidas" estiver ligada.

3. **A pontuação é contada**. Cada emoji tem um **peso** (por padrão 1), e você pode marcar emojis como **voto negativo**, que **descontam** pontos. A pontuação é acumulada de forma eficiente em memória e gravada periodicamente, então um pico de reações não sobrecarrega o servidor.

4. **Ao atingir o mínimo de estrelas**, a mensagem é **republicada no canal de destaques** com um cartão (embed) mostrando:
   - O autor (apelido, nome de exibição ou usuário, conforme a configuração) e o avatar.
   - O conteúdo do texto (truncado pelos limites configurados).
   - A primeira imagem como destaque e imagens extras como embeds adicionais (respeitando os limites de mídia).
   - Um trecho da mensagem respondida, se a original era uma resposta (opcional).
   - Um **link para a mensagem original** (como botão, no rodapé ou como menção, conforme a configuração).
   - Uma linha de cabeçalho no formato `⭐ 5 | #canal` indicando a pontuação atual e o canal de origem.
   - Anexos não-imagem (vídeos, documentos) podem ser **reenviados** junto, se você quiser.

   Conforme mais votos chegam, o cartão é **atualizado** com a nova pontuação. O mural também pode **reagir no próprio post** com o emoji de voto, para facilitar votar a partir do canal de destaques.

### Níveis de exibição (tiers)

Murais com **níveis de exibição** trocam o **emoji e a cor** do cartão conforme a pontuação sobe. Os padrões do sistema são `⭐` (a partir de 0), `🌟` (a partir de 10), `💫` (a partir de 20) e `✨` (a partir de 30), mas você pode definir seus próprios limiares, emojis e cores. O cartão sempre mostra o nível de maior limiar que a pontuação já alcançou.

### Quando a pontuação cai

Se a pontuação cair **igual ou abaixo do limite de remoção** (porque pessoas tiraram a reação ou houve votos negativos), o destaque é **removido do canal**. O limite de remoção é separado do limite de entrada — assim você cria uma "zona de histerese" (ex.: entra com 5, só sai abaixo de 3) para evitar que o post fique piscando perto da borda.

### Edição e exclusão da mensagem original

- **Sincronizar edições**: se ligado, editar a mensagem original atualiza o cartão no destaque.
- **Sincronizar exclusões**: se ligado, apagar a mensagem original remove o cartão do destaque.
- **Quando o post do destaque é apagado** manualmente, o mural segue um dos comportamentos configurados: **não fazer nada** (pode voltar se cruzar o limite de novo), **repostar**, **congelar** (trava a contagem) ou **descartar** (marca como removido permanentemente).

### Ranking e recompensas

1. Cada vez que uma mensagem entra ou sai do destaque, o **autor** acumula estatísticas: **total de estrelas**, **quantas vezes apareceu** no mural e a **melhor pontuação** de uma mensagem. Essas estatísticas existem tanto **por mural** quanto **globais** (somando todos os murais).
2. Com base nesses números, o bot **concede cargos de recompensa** automaticamente quando o membro atinge uma meta, e **remove** quando ele deixa de qualificar (a menos que o mural esteja configurado para "manter cargos antigos"). As metas possíveis são:
   - **Total de estrelas** acumuladas.
   - **Mais estrelada**: maior pontuação de uma única mensagem.
   - **Vezes no mural**: número de mensagens que entraram no destaque.
   - **Vezes no Hall da Fama**.
3. A verificação de recompensas roda continuamente em segundo plano (um reconciliador periódico re-checa os membros cuja pontuação mudou), então os cargos ficam em dia sem ação manual.

### Reset periódico do ranking (opcional)

Se você configurar, o ranking pode ser **zerado de tempos em tempos**, recomeçando a competição. Há dois modos: a cada **N dias** ou em um **dia fixo do mês**. Uma rotina de verificação roda **de hora em hora** e executa os resets que estiverem vencidos, recalculando a próxima data automaticamente.

### Recursos extras

- **Auto-estrela**: em canais escolhidos, o bot pode **reagir automaticamente** nas mensagens (modo "reagir") ou **mandá-las direto para o destaque** sem precisar de votos (modo "auto-postar") — útil para canais de arte, memes ou prints. Há filtros de **mínimo/máximo de caracteres** e **exigir imagem**; mensagens que não passam podem ser **apagadas** automaticamente, se você ligar essa opção.
- **Forçar no destaque**: moderadores podem, pelo menu de clique direito numa mensagem, enviá-la ao destaque mesmo sem atingir o limite de votos (veja Comandos). Se o servidor tem mais de um mural, aparece um seletor para escolher o destino.
- **Hall da Fama**: uma coleção **permanente e curada** das melhores mensagens, adicionada manualmente pela moderação. Diferente do mural automático, o Hall da Fama **não some** quando os votos caem. Se um canal de Hall da Fama estiver configurado, a mensagem também é republicada lá num cartão dourado.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/starboard` | Mostra as estatísticas de estrelas de um membro: total de estrelas, quantas vezes apareceu no destaque e melhor pontuação, com detalhamento por mural. Sem argumento, mostra as suas; com o argumento de usuário, mostra as de outra pessoa. |
| `/hall-of-fame` | Exibe o Hall da Fama do servidor, com navegação por páginas (10 itens por página). |
| **Forçar no Starboard** (menu de clique direito em mensagem) | Envia a mensagem ao destaque ignorando o limite de votos. Com vários murais, mostra um seletor para escolher o destino. Requer permissão **Gerenciar Mensagens**. |
| **Adicionar ao Hall da Fama** (menu de clique direito em mensagem) | Adiciona a mensagem ao Hall da Fama do servidor (e ao canal de Hall da Fama, se configurado). Requer permissão **Gerenciar Mensagens**. |

> Os dois últimos não são comandos de barra: são acessados clicando com o botão direito numa mensagem → **Apps**.

## Configuração

A configuração principal é feita pelo **Dashboard** em [admin.delfus.app](https://admin.delfus.app), na seção **Starboard**. Por lá você cria e edita os murais e tudo que os envolve.

**Por mural (board), você define:**

- **Nome** e **canal de destino** do mural, e se ele está **ativo**.
- **Estrelas para entrar** e **estrelas para sair** (limite de remoção) — por padrão, entrar com 3 e sair abaixo de 2.
- **Emojis de voto**: um ou vários, cada um com seu **peso** e a opção de marcar como **voto negativo** (desconta pontos). Aceita emojis padrão e emojis personalizados do servidor.
- **Permitir auto-voto** (reagir na própria mensagem) ou não.
- **Filtrar bots** (ignorar reações de bots).
- **Remover reações inválidas** automaticamente.
- **Reagir no próprio post** do destaque com o emoji de voto.
- **Sincronizar edições** e **sincronizar exclusões** da mensagem original.
- **Quando o post do destaque for apagado**: não fazer nada / repostar / congelar / descartar.
- **Manter cargos de recompensa antigos** mesmo quando o membro deixa de qualificar.
- **Anti-spam (cooldown)**: máximo de votos por janela e duração da janela (em segundos).
- **Grupo exclusivo** e **prioridade**: garante que uma mesma mensagem apareça em apenas um mural de um grupo (o de maior prioridade vence).
- **Webhook**: postar os cartões via webhook com **nome** e **avatar** personalizados.

**Aparência do cartão:** como mostrar o autor (apelido / nome de exibição / usuário), mencionar o autor, mostrar avatar, mostrar a mensagem respondida, reenviar anexos, estilo do link para a original (botão / rodapé / menção), e limites de tamanho de conteúdo, de mensagem, de embeds e de mídias.

**Níveis de exibição (display tiers):** lista de limiares, cada um com um emoji e uma cor de cartão.

**Filtros de mensagem:** idade mínima, idade máxima e tamanho mínimo de texto.

**Listas de bloqueio/permissão:** por usuário, cargo ou canal; como bloqueio ou permissão; aplicando ao autor, a quem reage ou a ambos.

**Auto-estrela:** canais-alvo, modo (reagir / auto-postar), emojis para reagir, mínimo/máximo de caracteres, exigir imagem e apagar mensagens que não passam nos filtros.

**Cargos de recompensa:** o cargo, o tipo de meta (total de estrelas, mais estrelada, vezes no mural ou vezes no Hall da Fama), o valor exigido e, opcionalmente, a qual mural a meta se aplica.

**Resets de ranking:** modo (a cada N dias ou dia fixo do mês) e o valor, com escopo por mural ou global.

**Hall da Fama:** o canal opcional onde as entradas são republicadas. As entradas em si são adicionadas pela moderação via menu de clique direito.

O Dashboard ainda oferece páginas de **visão geral**, **mensagens** no destaque, **ranking** (por total de estrelas, vezes no mural ou mais estrelada) e **Hall da Fama**.

## Exemplos de uso

- **Mural clássico de estrelas:** crie um mural "Destaques", aponte para o canal `#destaques`, use ⭐ como emoji com peso 1, defina entrar com 5 e sair abaixo de 3, e ligue "remover reações inválidas". Pronto: qualquer mensagem que junte 5 ⭐ vai parar no mural, e some se as estrelas caírem.

- **Canal de arte com auto-estrela:** num canal `#arte`, configure a auto-estrela no modo "reagir" para que o Delfus já reaja com ⭐ em toda mensagem **que contenha imagem**, e ligue "apagar inválidas" para manter o canal só com posts de arte. As reações dos membros decidem o que sobe ao destaque.

- **Competição mensal com recompensa:** ligue um reset de ranking "dia fixo do mês" para zerar a disputa todo mês, e crie um cargo de recompensa "Estrela do Mês" com meta de, por exemplo, 100 estrelas totais — o Delfus dá e tira o cargo automaticamente conforme o ranking muda.

- **Hall da Fama curado:** quando aparecer uma mensagem icônica, um moderador clica com o botão direito → **Apps** → **Adicionar ao Hall da Fama**. Ela fica eternizada (e, se você configurou um canal de Hall da Fama, é republicada lá em dourado), independentemente dos votos.

## Requisitos

- O bot precisa de permissão para **Ver Canal** e **Enviar Mensagens** (e **Incorporar Links**) no canal de destaques e no canal do Hall da Fama, se usar um.
- Para **remover reações inválidas** (auto-votos, votos bloqueados ou acima do limite anti-spam) e para a **auto-estrela com apagamento**, o bot precisa de **Gerenciar Mensagens** nos canais envolvidos.
- Para **reagir automaticamente** (auto-estrela no modo "reagir" e a reação no próprio post), o bot precisa de **Adicionar Reações**.
- Para postar via **webhook**, o bot precisa de **Gerenciar Webhooks** no canal de destaques.
- Para **conceder cargos de recompensa**, o bot precisa de **Gerenciar Cargos**, e o cargo do bot deve estar **acima** dos cargos de recompensa na hierarquia.
- Os comandos **Forçar no Starboard** e **Adicionar ao Hall da Fama** exigem que o moderador tenha **Gerenciar Mensagens**.

## Perguntas frequentes

**Posso ter mais de um mural no mesmo servidor?**
Sim. Você pode criar quantos murais quiser, cada um com seu emoji, canal e limites. Use **grupos exclusivos** se quiser que uma mesma mensagem apareça em apenas um mural do grupo (o de maior prioridade vence).

**Uma mensagem antiga pode ser destacada manualmente?**
Sim. Um moderador pode clicar com o botão direito na mensagem → **Apps** → **Forçar no Starboard** para enviá-la ao destaque mesmo sem os votos necessários.

**O que acontece se as estrelas caírem depois que a mensagem entrou no destaque?**
O cartão é atualizado a cada mudança de pontuação. Se a pontuação cair igual ou abaixo do **limite de remoção**, o destaque é retirado do canal. Defina esse limite abaixo do de entrada para o post não ficar entrando e saindo.

**Por que minha reação não contou?**
Pode ser auto-voto (reagir na própria mensagem) com auto-voto desativado, uma reação de bot com o filtro de bots ligado, um voto acima do limite anti-spam, um usuário/cargo/canal na lista de bloqueio, ou a mensagem não passou nos filtros (muito nova, muito antiga ou texto curto demais). Murais com "remover reações inválidas" tiram a reação nesses casos.

!!! tip "Dica"
    Defina **estrelas para entrar** maiores que **estrelas para sair** (ex.: entra com 5, sai abaixo de 3) para criar uma "zona de segurança" e evitar que o post fique aparecendo e sumindo perto do limite. E combine **emojis de voto negativo** com **níveis de exibição** para que destaques muito votados ganhem um cartão mais chamativo enquanto os negativos derrubam o que não merece ficar.

