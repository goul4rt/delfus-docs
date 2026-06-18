# Boas-vindas e despedida

O Delfus dá boas-vindas automáticas a quem entra no servidor e anuncia quando alguém sai, com mensagens personalizadas em **texto**, **embed** (cartão estruturado do Discord) ou **cartão de imagem** gerado na hora com o avatar do membro. Também pode enviar uma **mensagem privada (DM)** de boas-vindas. É a forma mais simples de fazer cada novo membro se sentir recebido — e de manter um registro visível de quem chega e quem sai — sem que você precise digitar nada manualmente.

![Configuração de boas-vindas no painel do Delfus](../assets/dashboard/recepcao.png){ .dx-shot loading=lazy }

*Configuração de boas-vindas no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

Tudo acontece de forma automática, disparado por eventos do Discord, com base no que você configurar pelo painel. São **três tipos de mensagem independentes**, cada um ligado/desligado por conta própria:

- **Boas-vindas no canal** — postada em um canal à sua escolha quando alguém entra.
- **DM de boas-vindas** — enviada no privado do novo membro quando ele entra.
- **Despedida no canal** — postada em um canal à sua escolha quando alguém sai.

### Quando um novo membro entra

1. O bot detecta a entrada e, antes de tudo, registra o evento de entrada e atualiza a contagem de membros do servidor (isso alimenta o `{{memberCount}}` e as estatísticas).
2. Em seguida, verifica se as **boas-vindas de canal** estão ativas. Se estiverem:
   - Se a opção **ignorar bots** estiver ligada e quem entrou for um bot, nada é enviado.
   - O bot busca o canal configurado. Se o canal não existir mais ou não for um canal de texto, ele apenas registra um aviso e não envia nada (não dá erro visível).
   - Caso contrário, monta a mensagem no formato escolhido (texto, embed ou cartão), substitui os atalhos de texto pelos valores reais do membro/servidor, anexa os botões de link (se houver) e publica no canal.
3. Em paralelo, se a **DM de boas-vindas** estiver ativa, o bot envia a mensagem no privado do novo membro (texto ou embed). A opção "ignorar bots" **não** se aplica à DM.

As boas-vindas de canal e a DM são independentes: você pode ter só uma, as duas, ou nenhuma.

### Quando alguém sai do servidor

1. O bot detecta a saída, registra o evento e atualiza a contagem de membros. (Se você usar o recurso de snapshot de cargos na saída, ele também é enfileirado aqui — isso é uma funcionalidade à parte.)
2. Verifica se a **despedida** está ativa. Se estiver:
   - Se "ignorar bots" estiver ligada e quem saiu for um bot, nada é enviado.
   - O bot busca o canal configurado; se ele não existir ou não for de texto, registra um aviso e para.
   - Caso contrário, publica a despedida no formato escolhido (texto ou embed).

A despedida **não** tem DM (faz sentido: a pessoa já saiu) nem cartão de imagem — apenas texto ou embed.

### Formatos de mensagem

Cada tipo aceita formatos diferentes:

| Tipo | Texto | Embed | Cartão de imagem |
| --- | :---: | :---: | :---: |
| Boas-vindas no canal | sim | sim | sim |
| DM de boas-vindas | sim | sim | não |
| Despedida no canal | sim | sim | não |

- **Texto** — uma mensagem simples de uma linha ou várias.
- **Embed** — um cartão estruturado do Discord, com título, descrição, cor, imagem, miniatura, autor, rodapé (com ícone), data/hora e campos (que podem ficar lado a lado). Os atalhos de texto funcionam em todos esses campos.
- **Cartão (imagem)** — exclusivo das boas-vindas de canal: uma imagem 960×540 gerada na hora, descrita em detalhe abaixo.

### Atalhos de texto (placeholders)

Em qualquer formato e em qualquer campo de texto, o bot substitui automaticamente os atalhos abaixo no momento do envio:

- `{{@user}}` — **menciona** o membro (ex.: @Fulano, com notificação). No **cartão de imagem**, vira apenas o nome de exibição (imagem não menciona ninguém).
- `{{user}}` — nome de exibição do membro (apelido no servidor, ou nome de usuário).
- `{{server}}` — nome do servidor.
- `{{memberCount}}` — total de membros do servidor **no momento do envio** (já contando quem acabou de entrar ou descontando quem saiu).

### O cartão de imagem em detalhe

O cartão é uma imagem PNG de 960×540 pixels com o avatar circular do membro (128 px). Você escolhe um entre **três estilos de layout**:

- **Centralizado** (`centered`) — avatar no centro, título e subtítulo logo abaixo, centralizados. Tem uma barra de destaque colorida na base.
- **Alinhado à esquerda** (`left`) — avatar à esquerda, título e subtítulo alinhados à direita dele. Também tem a barra de destaque na base.
- **Minimalista** (`minimalist`) — **sem avatar**, só o título grande, uma linha divisória colorida e o subtítulo, tudo centralizado. Não tem a barra de destaque na base.

O que você pode ajustar no cartão:

- **Título** e **subtítulo** (ambos aceitam os atalhos de texto).
- **Cor de fundo** e **cor do texto**.
- **Papel de parede (wallpaper)** — uma imagem de fundo por URL. Por cima dela é aplicada uma camada da cor de fundo com **opacidade do overlay** ajustável (deixa o texto legível). Se a URL falhar, o bot usa só a cor de fundo.
- **Fonte** — uma entre: Inter, Roboto, Poppins, Montserrat, Open Sans, Lato. Se a fonte escolhida não estiver disponível, o bot usa Inter como padrão.
- **Sombra do texto** (liga/desliga) — melhora a leitura sobre fundos claros.
- **Cor da borda do avatar** e **cor de destaque (accent)** — a cor de destaque colore o brilho ao redor do avatar, a barra da base e a linha divisória do minimalista.

O painel ainda traz **predefinições de cores** prontas (Blurple, Oceano, Pôr do Sol, Floresta, Escuro, Rosa Neon, Ouro, Ártico, Lavanda, Vermelho) para você aplicar um esquema de cores com um clique e ajustar depois.

### Botões de link

Você pode adicionar **até 3 botões de link** à mensagem de **boas-vindas do canal** (apenas a ela — não à DM nem à despedida). Cada botão tem um rótulo e uma URL e abre o link ao ser clicado (por exemplo, um botão "Regras" ou "Site oficial"). Botões sem rótulo ou sem URL são ignorados.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/welcome teste tipo:<Welcome \| Farewell \| DM>` | Gera uma **prévia** de um dos três tipos de mensagem, usando você mesmo como exemplo, sem esperar alguém entrar ou sair. A prévia só é visível para você e vem com um rodapé avisando que é um preview. |

Detalhes do comando:

- A opção **tipo** é obrigatória e tem três escolhas: **Welcome (entrada)**, **Farewell (saída)** e **DM (mensagem privada)**.
- A prévia respeita exatamente o formato configurado: gera o cartão de imagem real se o tipo "welcome" estiver no formato cartão, monta o embed real, etc., trocando os atalhos pelos seus dados.
- Se o sistema de boas-vindas ainda não foi configurado, ou se o tipo escolhido não está habilitado, o bot avisa para configurá-lo primeiro pelo painel.

## Configuração

A configuração é feita pelo **Dashboard** em [admin.delfus.app](https://admin.delfus.app), na seção de boas-vindas/despedida. Cada um dos três tipos é configurado separadamente.

Para **boas-vindas no canal**:

1. Ative o tipo (toggle **ativado/desativado**).
2. Escolha o **canal** onde a mensagem será postada.
3. Escolha o **formato**: texto, embed ou cartão.
4. Preencha o **conteúdo** (texto/embed) ou configure o **cartão** (layout, título, subtítulo, cores, fonte, papel de parede, opacidade do overlay, sombra do texto, cor da borda do avatar e cor de destaque). Use os atalhos `{{@user}}`, `{{user}}`, `{{server}}` e `{{memberCount}}` à vontade.
5. Opcionalmente, adicione **até 3 botões de link** (rótulo + URL).
6. Ligue ou não a opção **ignorar bots**.

Para a **DM de boas-vindas**:

1. Ative o tipo.
2. Escolha o **formato**: texto ou embed (sem cartão).
3. Preencha o **conteúdo**. (A DM não tem botões nem a opção "ignorar bots".)

Para a **despedida no canal**:

1. Ative o tipo.
2. Escolha o **canal**.
3. Escolha o **formato**: texto ou embed (sem cartão).
4. Preencha o **conteúdo**.
5. Ligue ou não a opção **ignorar bots**.

Limites e padrões reais do código:

- **Máximo de 3 botões de link** na mensagem de boas-vindas.
- **6 fontes** para o cartão (Inter, Roboto, Poppins, Montserrat, Open Sans, Lato) — padrão Inter.
- Tamanho do cartão fixo em **960×540 px**, avatar **128 px**.
- **3 layouts** de cartão: centralizado, alinhado à esquerda, minimalista.

Depois de configurar, use `/welcome teste` dentro do servidor para conferir o resultado antes de deixar tudo no ar.

## Exemplos de uso

- **Receber novos membros com cartão visual**: ative as boas-vindas de canal, escolha o formato **cartão**, defina o título `Bem-vindo, {{user}}!` e o subtítulo `Você é o membro nº {{memberCount}} do {{server}}`, escolha o layout centralizado e uma predefinição de cores, e adicione um botão "Leia as regras" apontando para o canal de regras. Rode `/welcome teste tipo:Welcome` para ver o cartão.

- **Mandar um guia no privado**: ative a **DM de boas-vindas** no formato embed, com um título de boas-vindas e uma descrição explicando os primeiros passos no servidor (`Olá {{user}}, seja bem-vindo ao {{server}}!`). Quem entrar recebe isso direto no privado, sem poluir os canais.

- **Anunciar saídas discretamente**: ative a **despedida** no formato texto simples, em um canal de logs só para staff, com `{{user}} deixou o servidor. Agora somos {{memberCount}} membros.` e a opção **ignorar bots** ligada para não anunciar entrada/saída de bots.

## Requisitos

- O bot precisa ter acesso ao canal escolhido e **permissão para enviar mensagens** nele (e para enviar imagens/embeds, no caso de cartão e embed). Se o canal for apagado ou ficar inacessível, a mensagem é silenciosamente pulada.
- O comando `/welcome teste` exige a permissão de **Administrador** de quem o executa, e o bot precisa da permissão **Gerenciar Servidor** (Manage Guild) para o comando funcionar.
- A **DM** só chega se o membro permitir mensagens privadas de pessoas do servidor. Se ele bloquear DMs, o bot apenas registra um aviso interno e segue sem erro visível.
- O papel de parede do cartão precisa estar acessível por **URL pública**; se a imagem não carregar, o cartão usa só a cor de fundo.

## Perguntas frequentes

**Posso ter um cartão de imagem na despedida ou na DM?**
Não. O cartão de imagem é exclusivo das boas-vindas de canal. Despedida e DM aceitam apenas texto ou embed.

**Por que alguns membros não recebem a DM de boas-vindas?**
Porque eles bloqueiam mensagens privadas de membros do servidor. O bot tenta enviar e, se não conseguir, ignora silenciosamente — ninguém recebe erro.

**A opção "ignorar bots" vale para a DM também?**
Não. "Ignorar bots" se aplica às boas-vindas de canal e à despedida. A DM não tem essa opção (mas, na prática, bots não costumam aceitar DMs).

**Quantos botões de link posso colocar nas boas-vindas?**
Até 3. Botões só existem na mensagem de boas-vindas do canal — não na DM nem na despedida.

!!! tip "Dica"
    Monte o cartão de imagem e rode `/welcome teste tipo:Welcome` antes de ativar para todos: a prévia gera o cartão real com o seu avatar, então você vê exatamente como vai aparecer — incluindo se o texto está legível sobre o papel de parede (ajuste a opacidade do overlay ou ligue a sombra do texto se ficar difícil de ler).

