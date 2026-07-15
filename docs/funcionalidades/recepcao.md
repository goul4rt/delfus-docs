---
description: "Boas-vindas e despedida do Delfus no Discord: mensagens automáticas em texto, embed ou cartão de imagem com avatar, no canal ou na DM do membro."
---

# Boas-vindas e despedida

Receba cada novo membro do seu servidor Discord pelo nome e avise quando alguém sai, no automático. Você configura uma vez e o Delfus cuida do resto.

As mensagens podem ser texto simples, um cartão do Discord (embed) ou uma imagem gerada na hora com o avatar da pessoa. Dá pra mandar boas-vindas no canal, no privado (DM), ou nos dois.

![Configuração de boas-vindas no painel do Delfus](../assets/dashboard/recepcao.webp){ .dx-shot width="1200" height="934" fetchpriority=high }

*Configuração de boas-vindas no [Dashboard](https://admin.delfus.app) (exemplo com dados de demonstração).*

## Como funciona

São três tipos de mensagem, cada um liga e desliga separado:

- **Boas-vindas no canal**: aparece num canal que você escolhe quando alguém entra.
- **DM de boas-vindas**: chega no privado do novo membro assim que ele entra.
- **Despedida no canal**: aparece num canal quando alguém sai.

Use um, dois, os três ou nenhum. São independentes.

Quando alguém entra, o Delfus atualiza a contagem de membros e dispara as boas-vindas ativas (canal e DM). Quando alguém sai, ele atualiza a contagem e posta a despedida, se estiver ligada.

!!! example "Exemplo"
    A Ana entra no servidor. Em segundos, aparece no canal de boas-vindas: *"Bem-vinda, Ana! Você é o membro nº 1.240 do nosso servidor."*, com o avatar dela num cartão. E no privado dela chega uma mensagem com os primeiros passos.

### Os três formatos

Cada tipo de mensagem aceita formatos diferentes:

| Tipo | Texto | Embed | Cartão de imagem |
| --- | :---: | :---: | :---: |
| Boas-vindas no canal | sim | sim | sim |
| DM de boas-vindas | sim | sim | não |
| Despedida no canal | sim | sim | não |

- **Texto**: uma mensagem simples, de uma ou várias linhas.
- **Embed**: o cartão organizado do Discord, com título, cor, imagem e rodapé.
- **Cartão de imagem**: uma imagem gerada na hora com o avatar do membro. Exclusivo das boas-vindas no canal.

!!! note "Por que a despedida não tem DM nem cartão?"
    A pessoa já saiu, então não dá pra mandar DM. Despedida é só texto ou embed.

### Atalhos que se preenchem sozinhos

Escreva a mensagem com atalhos e o Delfus troca pelos dados reais na hora de enviar:

- `{{@user}}`: menciona a pessoa (com notificação). No cartão de imagem, vira só o nome.
- `{{user}}`: o nome da pessoa (apelido ou usuário).
- `{{server}}`: o nome do servidor.
- `{{memberCount}}`: quantos membros o servidor tem naquele momento.

### O cartão de imagem

O cartão é uma imagem de 960×540 px com o avatar do membro num círculo. Escolha um de três layouts:

- **Centralizado**: avatar no meio, título e subtítulo embaixo.
- **À esquerda**: avatar à esquerda, textos ao lado.
- **Minimalista**: sem avatar, só o título grande, uma linha colorida e o subtítulo.

Você ajusta título, subtítulo, cores, fonte (Inter, Roboto, Poppins, Montserrat, Open Sans ou Lato), imagem de fundo por URL, sombra no texto e a cor de destaque do avatar. Para as cores, há predefinições prontas (Blurple, Oceano, Pôr do Sol, Floresta, Escuro, Rosa Neon, Ouro, Ártico, Lavanda, Vermelho) que você aplica com um clique.

!!! tip "Texto difícil de ler sobre a imagem de fundo?"
    Aumente a opacidade do overlay (a camada de cor por cima do fundo) ou ligue a sombra do texto.

### Botões de link

Nas boas-vindas do canal você adiciona até 3 botões com link, tipo "Leia as regras" ou "Site oficial". Cada botão tem um nome e uma URL. Só existe nas boas-vindas do canal, não na DM nem na despedida.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/welcome teste tipo:<Welcome \| Farewell \| DM>` | Mostra uma prévia de uma das três mensagens, usando você como exemplo, sem esperar ninguém entrar ou sair. Só você vê. |

A prévia respeita o que você configurou: gera o cartão de imagem de verdade, monta o embed real e troca os atalhos pelos seus dados. Se o tipo escolhido ainda não estiver configurado, o bot pede pra configurar pelo painel primeiro.

## Configuração

Tudo é feito no Dashboard em [admin.delfus.app](https://admin.delfus.app), na seção de boas-vindas e despedida. Cada tipo se configura separado.

**Boas-vindas no canal:**

1. Ative o toggle.
2. Escolha o canal.
3. Escolha o formato (texto, embed ou cartão).
4. Escreva o conteúdo ou monte o cartão. Use os atalhos à vontade.
5. (Opcional) Adicione até 3 botões de link.
6. Decida se quer ignorar bots.

**DM de boas-vindas:**

1. Ative o toggle.
2. Escolha o formato (texto ou embed).
3. Escreva o conteúdo. (Aqui não tem botões nem a opção de ignorar bots.)

**Despedida no canal:**

1. Ative o toggle.
2. Escolha o canal.
3. Escolha o formato (texto ou embed).
4. Escreva o conteúdo.
5. Decida se quer ignorar bots.

!!! warning "Antes de soltar pra geral"
    Rode `/welcome teste` dentro do servidor pra conferir o resultado. A prévia já mostra como vai ficar, com o seu avatar.

## Exemplos

!!! example "Receber com um cartão visual"
    Ative as boas-vindas no canal, escolha o formato **cartão**, defina o título `Bem-vindo, {{user}}!` e o subtítulo `Você é o membro nº {{memberCount}} do {{server}}`. Use o layout centralizado, aplique uma predefinição de cores e adicione um botão "Leia as regras" apontando pro canal de regras. Rode `/welcome teste tipo:Welcome` e veja o cartão pronto.

!!! example "Mandar um guia no privado"
    Para orientar quem chega sem poluir os canais, ative a **DM de boas-vindas** em formato embed, com uma descrição tipo `Olá {{user}}, seja bem-vindo ao {{server}}!` e os primeiros passos do servidor. Cada novo membro recebe isso direto no privado.

!!! example "Anunciar saídas só pra staff"
    Para registrar quem sai sem alarde, ative a **despedida** em texto simples, num canal de logs da staff, com `{{user}} deixou o servidor. Agora somos {{memberCount}} membros.` Ligue **ignorar bots** pra não anunciar entrada e saída de robôs.

## Veja na prática

O estilo **Cartão de Imagem** monta uma arte de boas-vindas na hora, com o avatar do membro e presets de cor prontos:

![Cartão de boas-vindas no painel do Delfus](../assets/dashboard/recepcao-cartao.webp){ .dx-shot width="1200" height="1227" loading=lazy }

*Estilo "Cartão de Imagem" com preview ao vivo e presets de cor (dados de demonstração).*

## Perguntas frequentes

### Posso ter cartão de imagem na despedida ou na DM?
Não. O cartão é exclusivo das boas-vindas no canal. Despedida e DM aceitam só texto ou embed.

### Por que alguns membros não recebem a DM?
Porque bloqueiam mensagens privadas de gente do servidor. O bot tenta enviar e, se não der, ignora sem erro.

### A opção "ignorar bots" vale pra DM também?
Não. Vale pras boas-vindas do canal e pra despedida. A DM não tem essa opção (mas, na prática, bots quase nunca aceitam DM).

### Quantos botões de link posso colocar?
Até 3, e só nas boas-vindas do canal.

### E se o canal escolhido for apagado?
O Delfus pula a mensagem em silêncio, sem erro visível. Ele precisa ter permissão pra enviar mensagens (e imagens/embeds) no canal. Pro comando `/welcome teste`, quem roda precisa ser Administrador e o bot precisa da permissão Gerenciar Servidor.

!!! tip "Dica"
    Monte o cartão e rode `/welcome teste tipo:Welcome` antes de ativar pra todos. A prévia gera o cartão real com o seu avatar, então você vê como vai ficar, inclusive se o texto está legível sobre a imagem de fundo.
