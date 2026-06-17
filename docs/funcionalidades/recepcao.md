# Boas-vindas e despedida

O Delfus pode dar boas-vindas automáticas a quem entra no servidor e anunciar quando alguém sai, com mensagens personalizadas em texto, embed ou cartão de imagem. Também envia uma mensagem privada (DM) de boas-vindas, se você quiser.

## Como funciona

Tudo acontece automaticamente, com base no que você configurar. São três tipos de mensagem, cada um ativado de forma independente:

1. **Quando um novo membro entra**, o bot verifica se as boas-vindas estão ativas. Se estiverem, ele envia a mensagem no canal que você escolheu. Em paralelo, se a mensagem privada (DM) estiver ativa, o bot também manda uma mensagem no privado do novo membro.
2. **Quando alguém sai do servidor**, o bot envia (se ativada) a mensagem de despedida no canal configurado.

Cada mensagem pode usar um destes formatos:

- **Texto** — uma mensagem simples.
- **Embed** — um cartão estruturado do Discord, com título, descrição, cor, imagem, rodapé e campos.
- **Cartão (imagem)** — disponível só nas boas-vindas: uma imagem gerada na hora com o avatar do membro, papel de parede de fundo, título e subtítulo. Você pode escolher entre três estilos de layout (centralizado, alinhado à esquerda ou minimalista) e ajustar cores, fonte e borda do avatar.

Em qualquer formato, o texto aceita atalhos que o bot substitui automaticamente na hora do envio:

- `{{@user}}` — menciona o membro (no cartão de imagem, vira só o nome).
- `{{user}}` — nome de exibição do membro.
- `{{server}}` — nome do servidor.
- `{{memberCount}}` — total de membros do servidor.

Você também pode adicionar **botões de link** à mensagem de boas-vindas do canal (por exemplo, um botão que leva às regras ou a outro site).

Há ainda uma opção para **ignorar bots**: quando ativada, entradas e saídas de bots não disparam as mensagens.

## Configuração

A configuração é feita pelo **Dashboard** (https://admin.delfus.app): lá você ativa cada tipo de mensagem (boas-vindas, despedida e DM), escolhe o canal, o formato (texto, embed ou cartão), o conteúdo e os botões.

Para conferir o resultado sem precisar esperar alguém entrar ou sair, use o comando de teste dentro do servidor:

- `/welcome teste` — gera uma prévia de um dos tipos (boas-vindas, despedida ou DM), usando você mesmo como exemplo. A prévia só é visível para você.

Se você tentar testar um tipo que não está configurado ou não está habilitado, o bot avisa para configurá-lo primeiro pelo painel.

## Requisitos

- O bot precisa ter acesso ao canal escolhido e permissão para enviar mensagens nele.
- O comando `/welcome teste` exige a permissão de **Administrador** (ou **Gerenciar Servidor**) de quem usa.
- A DM de boas-vindas só chega se o membro permitir mensagens privadas de membros do servidor; caso contrário, o bot simplesmente ignora sem erro visível.

!!! tip
    Configure o cartão de imagem e use `/welcome teste` para ver exatamente como ele vai aparecer antes de ativar para todos os novos membros.
