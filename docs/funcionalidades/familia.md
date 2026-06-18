# Famílias VIP

Quer transformar suas assinaturas VIP em algo que as pessoas realmente vão querer exibir? As Famílias VIP deixam cada assinante criar seu próprio grupinho exclusivo dentro do servidor — com um cargo colorido e personalizado só dele e dos amigos que convidar.

É um benefício de prestígio amarrado ao VIP: enquanto a assinatura está ativa, a família existe. Quando o VIP expira, ela é congelada sozinha — sem você precisar mexer um dedo na moderação.

## Como funciona

A família é uma das recompensas que vêm com certos planos VIP. Quem tem uma assinatura ativa com esse benefício pode criar e administrar a sua.

Tudo acontece por um único comando: `/familia`. Ele abre um **painel privado** (só você enxerga) onde dá pra fazer tudo no clique — criar, editar, convidar, gerenciar. Nada de decorar subcomandos.

O painel mostra na hora as famílias que você **possui**, as que você **participa** e quantos **slots** ainda tem livres. A sessão fica de pé por uns **10 minutos**; depois disso, é só rodar `/familia` de novo.

!!! example "Exemplo"
    Um assinante usa `/familia`, clica em **Criar**, escolhe o nome "Os Invencíveis" e pronto: o Delfus já gera um cargo do Discord exclusivo e atribui pra ele. Em segundos a família está no ar, pronta pra ganhar cor, ícone e novos membros.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/familia` | Abre o painel de Famílias VIP. Por ali você cria família, edita (nome, descrição, cor, ícone), convida e gerencia membros, sai, exclui e descongela — tudo por botões. |

!!! note "Um comando só"
    A feature tem **um único** comando de barra. Todas as ações vivem dentro do painel, não como subcomandos separados.

## Configuração

A família faz parte do sistema **VIP** e é configurada pelo [Dashboard](https://admin.delfus.app), na seção de VIP, no painel **Famílias**. Lá você ajusta:

- **Máximo de membros por família** — de 1 a 50 (padrão 10). Vale sempre o menor número entre esse teto e o limite definido na recompensa do plano.
- **Prefixo do cargo** — texto na frente do nome de cada cargo (padrão 🏠). Deixe vazio para não usar.
- **Expiração de convites** — em horas, de 1 a 720 (padrão 48).
- **Cargo de referência (âncora)** — opcional, serve pra posicionar os cargos de família num ponto fixo da hierarquia e manter a lista organizada.

!!! warning "Antes de tudo"
    Para os membros conseguirem criar famílias, você precisa de pelo menos um **plano VIP que inclua a recompensa de família**. É lá que se define o limite de membros do plano e se ele libera **gradiente** e **cor holográfica**.

    O bot também precisa da permissão **Gerenciar Cargos**, e o cargo dele tem que estar **acima** dos cargos de família. E lembre: o Discord limita o servidor a 250 cargos — sem espaço, a criação falha.

## O que dá pra fazer

Depois de criada, é o dono que comanda — sempre pelo painel:

- **Personalizar** — nome (até 80 caracteres), descrição (até 255) e a cor do cargo, que pode ser **sólida**, **gradiente** (duas cores em degradê) ou **holográfica** (efeito especial do Discord). Antes de aplicar a cor, o bot mostra uma prévia pra confirmar.
- **Ícone do cargo** — por URL ou imagem enviada, em PNG, JPEG, GIF ou WEBP. O Discord limita a 256 KB; imagens estáticas grandes são comprimidas sozinhas, mas GIFs animados acima disso precisam ser reduzidos antes.
- **Convidar e gerenciar** — convide membros do servidor, remova quem quiser, e qualquer membro comum pode sair quando bem entender. O dono não sai (precisa excluir a família) nem se remove.

Só o dono edita, e só enquanto a família está ativa.

## Exemplos

!!! example "Clãs coloridos como benefício premium"
    No Dashboard, você cria um tier VIP com recompensa de família (10 membros, gradiente liberado) e define o prefixo do cargo com o emoji do servidor. Pronto: cada assinante desse tier monta sua própria família, ganha um cargo colorido exclusivo e leva até 9 amigos junto. Status na veia.

!!! example "Convite que chega na DM"
    O dono clica em **Convidar** e escolhe alguém. A pessoa recebe uma mensagem privada com o nome da família, a contagem de membros e botões de **Aceitar** ou **Recusar**. Aceitou? Ganha o cargo na hora. O convite vale por 48 horas (padrão) e some sozinho se ninguém responder.

!!! example "VIP expirou, e agora?"
    Imagine que a assinatura do dono vence. O Delfus **congela** a família automaticamente: tira o cargo de todo mundo e tranca edições e convites — mas não apaga nada. Quando o VIP volta, é só clicar em **Descongelar** e o bot devolve o cargo a todos os membros, com barra de progresso e tudo.

## Perguntas frequentes

**O convite que enviei não chegou. Por quê?**
Quase sempre é DM fechada. Os convites só saem por mensagem privada — se a pessoa bloqueia DMs do servidor, o bot cancela o convite e te avisa. Peça pra ela abrir as DMs e convide de novo.

**O que acontece com a família se meu VIP expirar?**
Ela é congelada, não apagada. O cargo sai de todo mundo e a família fica trancada, mas nome, cor, ícone e membros ficam guardados. Renovou o VIP? Abra `/familia`, clique em **Descongelar** e está tudo de volta.

**Posso ter mais de uma família?**
Pode, desde que tenha mais de um slot livre — seja porque seu plano inclui várias recompensas de família, seja porque você mantém mais de uma assinatura VIP ativa. Cada slot dá direito a uma família, e você não pode usar a mesma recompensa em duas.

**Por que meu GIF foi recusado como ícone?**
Por causa do limite de 256 KB do Discord. Imagens estáticas grandes são comprimidas automaticamente, mas GIFs animados não dá — perderiam a animação. Reduza o tamanho do GIF ou use uma imagem estática.

!!! tip "Dica"
    Peça aos seus assinantes que mantenham as **DMs do servidor abertas** — sem isso o convite simplesmente não chega. E reserve um **cargo-âncora** nas configurações pra que todos os cargos de família nasçam no mesmo ponto da hierarquia, deixando sua lista de cargos arrumadinha.
