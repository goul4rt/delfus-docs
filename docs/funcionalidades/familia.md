# Famílias VIP

As Famílias VIP são grupos exclusivos que membros assinantes podem criar e gerenciar dentro do servidor. Cada família ganha um **cargo do Discord próprio e personalizável** (nome, descrição, cor e ícone), e o dono pode convidar outros membros para fazerem parte dela. É uma recompensa de prestígio amarrada à assinatura VIP — enquanto o VIP estiver ativo, a família existe; quando ele expira, ela é automaticamente "congelada". Para o dono do servidor, é uma forma poderosa de aumentar o valor percebido dos planos VIP, criando subgrupos identitários e cargos coloridos exclusivos sem nenhum trabalho manual de moderação.

## Como funciona

A família é uma das recompensas que vêm com determinados planos VIP. Quem tem uma assinatura ativa com esse benefício pode criar e administrar sua própria família. Todo o uso acontece pelo comando `/familia`, que abre um **painel interativo privado** (visível só para quem usou o comando) onde o membro faz tudo por botões e menus — sem precisar decorar subcomandos.

O painel é montado a partir do estado atual do membro: ele mostra as famílias que a pessoa **possui** (como dono), as famílias das quais ela **participa** (como membro), e quantos **slots de família** ainda estão disponíveis. A sessão do painel fica ativa por cerca de **10 minutos**; depois disso pode ser necessário rodar `/familia` de novo.

### 1. Criar a família

1. Um assinante com slot de família disponível usa `/familia` e clica em **Criar**.
2. O bot revalida na hora se a pessoa tem VIP ativo e se há slot livre. Se o usuário tiver **mais de uma assinatura VIP** ativa ao mesmo tempo, o bot procura automaticamente a primeira combinação de assinatura + recompensa de família ainda não usada — ou seja, ele aproveita capacidade de qualquer um dos VIPs.
3. Abre-se um formulário pedindo o **nome da família** (entre 2 e 80 caracteres).
4. Ao confirmar, o bot cria automaticamente um **cargo do Discord** com esse nome, acrescido de um **prefixo configurável** (por padrão o emoji de casa 🏠 — ex.: "🏠 Minha Família"), e **atribui o cargo ao dono**.
5. A família passa a aparecer no painel já na tela de detalhes, pronta para ser personalizada e receber membros.

**Sobre slots:** cada recompensa de família incluída na assinatura equivale a um slot. O membro só consegue criar enquanto tiver slots livres, e **não pode criar duas famílias com a mesma recompensa**. Se a pessoa tem dois VIPs, cada um com uma recompensa de família, ela pode ter duas famílias simultâneas. Se o nome for recusado pelo filtro de palavras do Discord (termos bloqueados, "everyone", "here", caracteres inválidos), o bot avisa com uma mensagem explicando o motivo.

### 2. Personalizar a família

Ainda pelo painel, na tela de **Editar**, o dono pode ajustar:

- **Nome** — até 80 caracteres. Renomeia também o cargo do Discord (mantendo o prefixo).
- **Descrição** — texto livre de até 255 caracteres, exibido no painel da família.
- **Cor do cargo** — informada em formato hexadecimal (ex.: `#FF5733`). Há três modos:
  - **Cor sólida** — uma única cor.
  - **Gradiente** — uma cor primária + uma secundária (o cargo aparece com um degradê).
  - **Holográfico** — um efeito especial com cores fixas definidas pelo Discord, ativado por um botão de alternância na tela de revisão da cor.

  Antes de aplicar, o bot mostra uma **tela de revisão** com a cor escolhida, para o dono confirmar ou cancelar.
- **Ícone do cargo** — pode ser enviado como **URL pública** de imagem ou como imagem embutida. Formatos aceitos: **PNG, JPEG, GIF ou WEBP**. O Discord limita ícones de cargo a **256 KB**:
  - Imagens PNG/JPEG/WEBP acima do limite são **redimensionadas e comprimidas automaticamente** para caber.
  - **GIFs animados não podem ser comprimidos** (perderiam a animação); se passarem de 256 KB, são recusados com um pedido para reduzir o arquivo antes.
  - Formatos não suportados, URLs inacessíveis ou imagens inválidas são recusados com uma explicação clara.

Só o **dono** pode editar a família, e apenas enquanto ela estiver **ativa** (não congelada).

### 3. Convidar membros

1. Na tela da família, o dono clica em **Convidar** e escolhe um membro do servidor por um menu de seleção.
2. O bot bloqueia escolhas inválidas na hora: não dá para convidar **bots**, nem **a si mesmo**, nem alguém que **já é membro** da família, nem ultrapassar o **limite de membros**.
3. Após confirmar, o convidado recebe uma **mensagem privada (DM)** com um embed mostrando o nome da família, a contagem de membros e quando o convite expira, além de botões **Aceitar** e **Recusar**.
4. O convite tem **prazo de validade** (por padrão **48 horas**) e expira sozinho se não for respondido.
5. **Se a DM do convidado estiver fechada** (ou as configurações de privacidade dele bloquearem mensagens de membros do servidor), o bot não consegue entregar o convite. Nesse caso ele **cancela o convite** e avisa o dono que precisa pedir ao convidado para abrir as DMs e tentar de novo — assim não fica um convite "preso" impedindo novas tentativas.
6. Não é possível ter **dois convites pendentes** para a mesma pessoa na mesma família ao mesmo tempo.

### 4. Entrar na família

1. Ao clicar em **Aceitar** na DM, o membro recebe o **cargo da família na hora**.
2. O bot revalida no momento do aceite: o convite não pode estar **expirado**, **já respondido**, e a família não pode estar **congelada** nem ter **atingido o limite de membros**. Se dois convites forem aceitos ao mesmo tempo e só houver uma vaga, apenas um passa — o outro recebe aviso de que a família está cheia.
3. Ao clicar em **Recusar**, o convite é marcado como recusado e nada acontece.

### 5. Gerenciar e sair

- **Remover membros** — o dono abre **Gerenciar membros**, escolhe alguém no menu e confirma. O cargo é retirado da pessoa. O dono **não pode se remover**.
- **Sair voluntariamente** — qualquer membro comum pode sair da família a qualquer momento pelo painel (botão **Sair**, com confirmação); o cargo é removido na hora. O **dono não pode sair** — para encerrar, precisa excluir a família.
- **Excluir a família** — só o dono, com confirmação. Ao excluir, o **cargo do Discord é apagado** e removido de todos os membros, e a família deixa de existir (membros e convites pendentes também são apagados). Isso libera o slot para criar outra família.

As ações destrutivas (remover, sair, excluir, descongelar) são protegidas contra **cliques duplos**: se a confirmação for clicada duas vezes em sequência, só a primeira é executada.

### 6. Congelamento por expiração do VIP

A família depende da assinatura VIP do dono:

1. **Quando o VIP expira**, o bot **congela automaticamente** todas as famílias daquela assinatura: o cargo é **removido de todos os membros** e a família fica **bloqueada** para edições, convites e gerenciamento.
2. A família **não é apagada** — ela continua existindo com status "congelada", guardando seus membros e personalização.
3. **Quando o VIP é reativado**, o dono volta ao painel e usa o botão **Descongelar**. O bot reativa a família e **re-atribui o cargo** a todos os membros que ainda estão no servidor, mostrando uma barra de progresso enquanto faz isso (já que cargos são re-aplicados um a um, respeitando os limites do Discord).
4. Se a assinatura original não estiver mais ativa mas o dono tiver **outra assinatura VIP ativa com slot livre**, o bot tenta **migrar** a família para essa outra assinatura ao descongelar. Se não houver nenhuma assinatura ativa disponível, o descongelamento é recusado.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/familia` | Abre o painel interativo de Famílias VIP. A partir dele, por botões e menus, o membro pode: criar família, ver detalhes, editar (nome, descrição, cor, ícone), convidar membros, gerenciar/remover membros, sair, excluir a família e descongelar uma família congelada. |

> Esta feature tem um único comando de barra (`/familia`); todas as operações acontecem dentro do painel, não como subcomandos separados.

## Configuração

A feature de Famílias faz parte do sistema **VIP** e é configurada pelo **Dashboard** (https://admin.delfus.app), na seção de configurações de VIP, no painel **Famílias**. Lá o dono do servidor define:

- **Máximo de membros por família** — teto padrão do servidor para o tamanho de cada família (faixa de **1 a 50**; padrão **10**). O limite efetivo de uma família é o **menor** entre esse teto do servidor e o `maxMembers` definido na recompensa de família do plano VIP.
- **Prefixo do cargo** — texto colocado na frente do nome de cada cargo de família (padrão 🏠). Deixe vazio para não usar prefixo. Exemplo: "🏠 Minha Família".
- **Expiração de convites (horas)** — prazo de validade dos convites enviados por DM, em horas (faixa de **1 a 720**; padrão **48**).
- **Cargo de referência (âncora)** — cargo opcional usado para **posicionar** os cargos de família na lista de cargos do servidor. Os cargos de família são criados próximos a essa âncora, o que ajuda a manter a hierarquia organizada. Selecione "nenhum" para deixar o Discord posicionar automaticamente.

Para que membros possam **efetivamente criar famílias**, é preciso também ter ao menos um **tier/plano VIP que inclua a recompensa de família** (configurado na mesma área de VIP do painel). A configuração da recompensa de família define o `maxMembers` daquele plano e se ela permite **cor secundária (gradiente)** e **cor holográfica**.

## Exemplos de uso

- **Oferecer "clãs" coloridos como benefício VIP premium.** No Dashboard, crie um tier VIP com uma recompensa de família (`maxMembers` 10, gradiente liberado). Defina o prefixo do cargo como o emoji do seu servidor. Agora cada assinante desse tier pode criar sua própria família, dar um cargo colorido exclusivo a si e a até 9 amigos, e exibir esse status no servidor.

- **Casais/duplas de criadores.** Um assinante usa `/familia`, cria a família "Os Invencíveis", personaliza com uma cor holográfica e um ícone, e convida o parceiro. O parceiro aceita pela DM e os dois passam a ostentar o mesmo cargo personalizado.

- **Manter cargos organizados na hierarquia.** Defina um **cargo-âncora** (por exemplo, um cargo separador chamado "── Famílias ──") nas configurações. Todos os cargos de família serão criados perto dele, mantendo a lista de cargos do servidor arrumada em vez de espalhar cargos de família por toda parte.

## Requisitos

- O bot precisa da permissão **Gerenciar Cargos**, já que cria, edita e remove os cargos de cada família.
- O cargo do bot deve estar **acima** dos cargos das famílias na hierarquia de cargos, para conseguir gerenciá-los (criar, colorir, atribuir e remover).
- O servidor **não pode** ter atingido o **limite de 250 cargos** do Discord — sem espaço para novos cargos, a criação de famílias falha.
- Para usar a feature, o membro precisa de uma **assinatura VIP ativa** que inclua a **recompensa de família** com slot disponível.

## Perguntas frequentes

**Por que o convite que enviei não chegou ao membro?**
Provavelmente as DMs dele estão fechadas para membros do servidor. O bot só consegue entregar convites de família por mensagem privada; quando a DM está bloqueada, o convite é cancelado automaticamente e você recebe um aviso. Peça à pessoa para abrir as DMs do servidor e tente convidar de novo.

**O que acontece com a minha família se meu VIP expirar?**
Ela é **congelada**, não apagada: o cargo é removido de todos os membros e a família fica bloqueada para edições e convites, mas tudo (membros, nome, cor, ícone) é preservado. Quando você renovar o VIP, é só abrir `/familia` e clicar em **Descongelar** para reativar a família e devolver o cargo a todos.

**Posso ter mais de uma família?**
Sim, desde que você tenha mais de um slot de família — seja porque seu plano inclui várias recompensas de família, seja porque você mantém mais de uma assinatura VIP ativa, cada uma com sua recompensa. Cada slot livre permite uma família, e você não pode reutilizar a mesma recompensa em duas famílias.

**Por que meu GIF foi recusado como ícone do cargo?**
O Discord limita ícones de cargo a 256 KB. Imagens estáticas (PNG/JPEG/WEBP) acima disso são comprimidas automaticamente, mas **GIFs animados não podem ser comprimidos** sem perder a animação. Reduza o tamanho do GIF antes de enviá-lo, ou use uma imagem estática.

!!! tip "Dica"
    Peça aos seus assinantes que mantenham as **DMs do servidor abertas** — os convites de família chegam por mensagem privada, e com a DM fechada o convite simplesmente não é entregue. Vale também reservar um **cargo-âncora** nas configurações para que todos os cargos de família nasçam no mesmo ponto da hierarquia, deixando a lista de cargos organizada.

