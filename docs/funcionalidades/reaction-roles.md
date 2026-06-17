# Cargos por reação

Permite que os membros peguem (e devolvam) cargos sozinhos, clicando em botões de um painel que você publica em um canal. Ideal para cargos de notificação, cores, regiões, interesses e acesso a áreas do servidor — sem precisar de moderador.

## Como funciona

O sistema é baseado em **painéis**: cada painel é uma mensagem que o bot publica em um canal do seu servidor, com um texto/embed e um ou mais **botões**, em que cada botão está ligado a um cargo.

1. Você monta o painel pelo painel de controle (texto, embed e a lista de botões com seus cargos) e manda publicar em um canal.
2. O bot envia a mensagem nesse canal com os botões. Se você editar o painel depois, o bot atualiza a mesma mensagem (e, se ela tiver sido apagada, publica uma nova).
3. Quando um membro clica em um botão, o bot verifica se ele já tem aquele cargo:
   - **Não tem** → o cargo é adicionado.
   - **Já tem** → o cargo é removido.
   (É um liga/desliga: o mesmo botão dá e tira o cargo.)
4. O membro recebe na hora uma resposta privada (só ele vê), confirmando que recebeu ou perdeu o cargo. Você pode personalizar essas mensagens de confirmação por painel.
5. A aplicação do cargo é feita logo em seguida, em segundo plano. O bot processa os cliques de forma organizada e com controle de ritmo, para aguentar muita gente clicando ao mesmo tempo sem travar nem ser bloqueado pelo Discord. Se algo falhar momentaneamente, ele tenta de novo automaticamente.

**Modo exclusivo (escolha única):** cada painel pode permitir múltiplos cargos ao mesmo tempo ou trabalhar como "escolha única". No modo de escolha única, ao pegar um cargo daquele painel o bot remove automaticamente os outros cargos do mesmo painel — perfeito para opções mutuamente exclusivas (por exemplo, escolher uma única cor ou uma única região).

Se o sistema estiver desativado, ou se o painel/botão tiver sido removido da configuração, o membro recebe um aviso de que aquela opção não está mais disponível e nenhum cargo é alterado.

## Configuração

A configuração é feita **pelo painel** em [admin.delfus.app](https://admin.delfus.app). Lá você:

- Cria e edita painéis (conteúdo, embed e botões).
- Associa cada botão a um cargo, define o rótulo, o emoji e o estilo/cor do botão.
- Define se o painel permite vários cargos ou é de escolha única.
- Personaliza as mensagens de confirmação ao receber e ao perder um cargo.
- Escolhe o canal e publica (ou republica) o painel.

Não há comando de barra para esta funcionalidade — todo o gerenciamento acontece no painel de controle.

## Requisitos

- O bot precisa da permissão **Gerenciar cargos**.
- O cargo do bot precisa estar **acima**, na lista de cargos do servidor, de qualquer cargo que ele vá entregar. O bot nunca consegue dar ou tirar um cargo que esteja igual ou acima do cargo dele — nesses casos a ação é ignorada.
- Cada painel suporta até 25 botões (em até 5 linhas de 5 botões).

!!! tip
    Para menus de "escolha única" (cor, região, plataforma), ative o modo exclusivo do painel: ao escolher uma opção, a anterior é removida sozinha, sem o membro precisar desmarcá-la antes.
