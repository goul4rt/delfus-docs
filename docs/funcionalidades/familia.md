# Famílias VIP

Cada assinante VIP cria seu próprio grupo no servidor, com um cargo colorido e personalizado para ele e os amigos que convidar. Enquanto o VIP está ativo, a família existe. Quando expira, ela é congelada sozinha, sem trabalho de moderação.

## Como funciona

A família é uma recompensa de certos planos VIP. Quem tem assinatura ativa com esse benefício pode criar e administrar a sua.

Tudo passa por um comando: `/familia`. Ele abre um painel privado (só você vê) onde dá pra criar, editar, convidar e gerenciar no clique. Sem decorar subcomandos.

O painel mostra na hora as famílias que você possui, as que participa e quantos slots ainda tem livres. A sessão dura uns 10 minutos. Depois, é só rodar `/familia` de novo.

!!! example "Exemplo"
    Um assinante usa `/familia`, clica em **Criar** e escolhe o nome "Os Invencíveis". O Delfus gera um cargo exclusivo do Discord e atribui a ele. Em segundos a família está no ar, pronta pra ganhar cor, ícone e membros.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/familia` | Abre o painel de Famílias VIP. Cria família, edita (nome, descrição, cor, ícone), convida e gerencia membros, sai, exclui e descongela. Tudo por botões. |

!!! note "Um comando só"
    A feature tem **um único** comando de barra. Todas as ações ficam no painel, não em subcomandos separados.

## Configuração

A família faz parte do sistema **VIP** e é configurada no [Dashboard](https://admin.delfus.app), na seção de VIP, no painel **Famílias**. Lá você ajusta:

- **Máximo de membros por família** — de 1 a 50 (padrão 10). Vale o menor número entre esse teto e o limite da recompensa do plano.
- **Prefixo do cargo** — texto na frente do nome de cada cargo (padrão 🏠). Deixe vazio para não usar.
- **Expiração de convites** — em horas, de 1 a 720 (padrão 48).
- **Cargo de referência (âncora)** — opcional. Posiciona os cargos de família num ponto fixo da hierarquia e mantém a lista organizada.

!!! warning "Antes de tudo"
    Para os membros criarem famílias, você precisa de pelo menos um **plano VIP com a recompensa de família**. É nele que se define o limite de membros e se ele libera **gradiente** e **cor holográfica**.

    O bot também precisa da permissão **Gerenciar Cargos**, e o cargo dele tem que estar **acima** dos cargos de família. Lembre que o Discord limita o servidor a 250 cargos: sem espaço, a criação falha.

## O que dá pra fazer

Depois de criada, o dono comanda tudo pelo painel:

- **Personalizar** — nome (até 80 caracteres), descrição (até 255) e a cor do cargo: **sólida**, **gradiente** (duas cores em degradê) ou **holográfica** (efeito especial do Discord). Antes de aplicar a cor, o bot mostra uma prévia pra confirmar.
- **Ícone do cargo** — por URL ou imagem enviada, em PNG, JPEG, GIF ou WEBP. O Discord limita a 256 KB. Imagens estáticas grandes são comprimidas sozinhas, mas GIFs animados acima disso precisam ser reduzidos antes.
- **Convidar e gerenciar** — convide membros do servidor, remova quem quiser. Qualquer membro comum pode sair quando quiser. O dono não sai (precisa excluir a família) nem se remove.

Só o dono edita, e só enquanto a família está ativa.

## Exemplos

!!! example "Clãs coloridos como benefício premium"
    No Dashboard, você cria um tier VIP com recompensa de família (10 membros, gradiente liberado) e define o prefixo do cargo com o emoji do servidor. Cada assinante desse tier monta sua família, ganha um cargo colorido exclusivo e leva até 9 amigos junto.

!!! example "Convite que chega na DM"
    O dono clica em **Convidar** e escolhe alguém. A pessoa recebe uma mensagem privada com o nome da família, a contagem de membros e botões de **Aceitar** ou **Recusar**. Ao aceitar, ganha o cargo na hora. O convite vale por 48 horas (padrão) e some sozinho se ninguém responder.

!!! example "Quando o VIP expira"
    A assinatura do dono vence e o Delfus **congela** a família automaticamente: tira o cargo de todo mundo e tranca edições e convites, mas não apaga nada. Quando o VIP volta, basta clicar em **Descongelar** e o bot devolve o cargo a todos os membros, com barra de progresso.

## Perguntas frequentes

**O convite que enviei não chegou. Por quê?**
Quase sempre é DM fechada. Os convites só saem por mensagem privada. Se a pessoa bloqueia DMs do servidor, o bot cancela o convite e te avisa. Peça pra ela abrir as DMs e convide de novo.

**O que acontece com a família se meu VIP expirar?**
Ela é congelada, não apagada. O cargo sai de todo mundo e a família fica trancada, mas nome, cor, ícone e membros ficam guardados. Ao renovar o VIP, abra `/familia`, clique em **Descongelar** e está tudo de volta.

**Posso ter mais de uma família?**
Pode, desde que tenha mais de um slot livre, seja porque seu plano inclui várias recompensas de família, seja porque você mantém mais de uma assinatura VIP ativa. Cada slot dá direito a uma família, e você não pode usar a mesma recompensa em duas.

**Por que meu GIF foi recusado como ícone?**
Por causa do limite de 256 KB do Discord. Imagens estáticas grandes são comprimidas automaticamente, mas GIFs animados não, pois perderiam a animação. Reduza o tamanho do GIF ou use uma imagem estática.

!!! tip "Dica"
    Peça aos seus assinantes que mantenham as **DMs do servidor abertas**, senão o convite não chega. E reserve um **cargo-âncora** nas configurações para que todos os cargos de família nasçam no mesmo ponto da hierarquia, deixando a lista de cargos arrumada.

