# Cargos por reação

Permite que os membros peguem (e devolvam) cargos sozinhos, clicando em botões de um painel que você publica em um canal. É ideal para cargos de notificação, cores, regiões, pronomes, jogos, interesses e acesso a áreas do servidor — tudo sem precisar de moderador e sem que ninguém saia da conversa para abrir um menu. Para o dono do servidor, isso reduz pedidos manuais de cargo, organiza a comunidade em grupos auto-selecionados e mantém os canais de notificação cheios apenas de quem realmente quer estar neles.

![Cargos por reação no painel do Delfus](../assets/dashboard/reaction-roles.png){ .dx-shot loading=lazy }

*Cargos por reação no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O sistema é baseado em **painéis**. Cada painel é uma mensagem que o bot publica em um canal do seu servidor — com um texto opcional, um embed (título, descrição, cor, imagem) e um ou mais **botões**, onde cada botão está ligado a um cargo. O membro interage clicando nos botões; o bot cuida do resto.

### Montando e publicando o painel

1. Você monta o painel pelo [Dashboard](https://admin.delfus.app): dá um nome (só para você reconhecer na lista), escolhe o canal de destino, escreve o conteúdo (texto e/ou embed) e adiciona a lista de botões, cada um amarrado a um cargo.
2. Ao salvar, o bot publica a mensagem no canal escolhido com todos os botões. Apenas canais de **texto** e de **anúncios** são aceitos como destino.
3. Se você **editar o painel depois** e salvar de novo, o bot **atualiza a mesma mensagem** já publicada (não cria uma nova). Se essa mensagem tiver sido apagada do canal nesse meio-tempo, o bot detecta isso e **publica uma mensagem nova** automaticamente.
4. O Dashboard registra a data e hora do último envio, então você sempre sabe se o painel já foi ao Discord ou se ainda está só salvo como rascunho.

### O clique do membro: o liga/desliga

Cada botão funciona como um interruptor (toggle): o mesmo botão dá e tira o cargo.

1. O membro clica em um botão do painel.
2. O bot verifica na hora se aquele membro já tem o cargo ligado àquele botão:
   - **Não tem** → o cargo é **adicionado**.
   - **Já tem** → o cargo é **removido**.
3. O membro recebe **imediatamente** uma resposta privada e efêmera (só ele vê, e ela some depois) confirmando se recebeu ou perdeu o cargo. Essas mensagens de confirmação são **personalizáveis por painel** (veja a seção "Configuração"). Quando não personalizadas, o bot usa textos padrão: "Você recebeu o cargo **{nome}**!" e "O cargo **{nome}** foi removido."
4. A confirmação ao membro é instantânea, mas a aplicação do cargo em si acontece **logo em seguida, em segundo plano**. O bot enfileira cada clique e processa com **controle de ritmo**, para aguentar muita gente clicando ao mesmo tempo (por exemplo, logo após você publicar um painel novo) sem travar nem ser bloqueado pelo Discord. Na prática, o cargo aparece no membro em geral em poucos instantes.
5. Se um clique falhar por um problema momentâneo (instabilidade da API do Discord, por exemplo), o bot **tenta novamente sozinho** algumas vezes antes de desistir. Falhas definitivas (cargo configurado errado, membro que saiu, etc.) não ficam tentando para sempre.
6. Cliques repetidos no mesmo botão em sequência muito rápida são tratados com segurança: o bot ignora a duplicata para não aplicar e remover o cargo várias vezes seguidas.

### Modo exclusivo (escolha única)

Cada painel tem a opção **"Permitir múltiplos cargos"**:

- **Ativada** (padrão): o membro pode acumular vários cargos daquele painel ao mesmo tempo. Bom para listas onde faz sentido marcar várias opções (notificações, jogos, pronomes).
- **Desativada** (escolha única): ao pegar um cargo daquele painel, o bot **remove automaticamente os outros cargos do mesmo painel** que o membro tivesse. Perfeito para opções mutuamente exclusivas — escolher uma única cor, uma única região, uma única plataforma. O membro não precisa desmarcar a opção anterior; o bot troca sozinho.

Importante: o modo exclusivo só age sobre os cargos **daquele painel específico**. Cargos que o membro tenha de outros painéis ou de outras fontes não são tocados.

### Verificações de segurança a cada clique

Antes de mexer em qualquer cargo, o bot valida tudo, e nada é alterado se algo não bater:

- **Sistema desativado** → se o módulo estiver desligado no Dashboard, o membro vê um aviso de que o sistema está desativado e nenhum cargo muda.
- **Painel ou botão removido** → se o painel ou o botão tiver sido apagado da configuração depois de publicado, o membro recebe um aviso de que aquela opção não está mais disponível.
- **Botão sem cargo** → se um botão ficou sem cargo associado, o membro é avisado de que ele não está configurado.
- **Hierarquia de cargos** → o bot só consegue entregar ou tirar um cargo que esteja **abaixo** do cargo dele na lista de cargos do servidor. Se o cargo do botão estiver igual ou acima do cargo do bot, a ação é ignorada (o Discord não permite). Veja "Requisitos".

## Comandos

Esta feature é configurada apenas pelo painel. Não há comandos de barra: todo o gerenciamento (criar painéis, botões, cargos, mensagens, publicar) acontece no [Dashboard](https://admin.delfus.app).

## Configuração

Toda a configuração é feita pelo Dashboard em [admin.delfus.app](https://admin.delfus.app), na seção **Cargos por Reação**.

### Ativar o sistema

No topo da página há um interruptor geral **Ativado / Desativado**. Ele liga ou desliga todos os painéis de uma vez. Com o sistema desativado, os botões publicados deixam de entregar cargos e os membros veem um aviso ao clicar.

### Criar um painel

Você pode começar de duas formas:

- **Do zero**, clicando em "Novo Painel".
- **A partir de um template** pronto, que já vem com botões e cargos sugeridos. Os templates disponíveis são: **Notificações**, **Cores** (já em modo escolha única), **Jogos** e **Pronomes**. Quando um template usa cargos que ainda não existem no servidor, o bot **cria esses cargos automaticamente** ao salvar (com o nome e a cor sugeridos), e já liga cada botão ao cargo criado.

### Opções de cada painel

Ao editar um painel, você configura:

- **Nome do painel** — rótulo interno para você reconhecer o painel na lista (até 100 caracteres). Não aparece para os membros.
- **Canal** — onde a mensagem será publicada (canal de texto ou de anúncios).
- **Texto acima do embed** (opcional, até 2000 caracteres) — texto simples que aparece antes do embed.
- **Mensagem embed** — título, descrição, cor, imagem, miniatura, rodapé, autor e campos, montados num editor visual com pré-visualização dos botões.
- **Botões & cargos** — a lista de botões. Cada botão tem:
  - **Emoji** (opcional)
  - **Rótulo** (o texto do botão)
  - **Cargo** associado (escolhido entre os cargos do servidor)
  - **Estilo/cor** do botão: azul (primary), cinza (secondary), verde (success) ou vermelho (danger).
- **Permitir múltiplos cargos** — interruptor que define se o painel acumula vários cargos ou funciona como escolha única (ver "Modo exclusivo" acima).
- **Mensagens automáticas** — os textos efêmeros enviados ao membro **ao receber** e **ao perder** um cargo (até 500 caracteres cada). Use o marcador `{cargo}` para inserir o nome do cargo automaticamente. Ex.: `Você agora segue {cargo}!`.

### Ligar/desligar e organizar painéis

Na lista de painéis você pode ativar/desativar cada painel individualmente, **duplicar** um painel (cria uma cópia "(copia)" pronta para ajustar) e **excluir** painéis.

### Publicar

Ao salvar um painel, o bot publica (ou republica) a mensagem no canal escolhido. Edições posteriores atualizam a mesma mensagem; se ela tiver sido apagada, uma nova é enviada.

### Limites

- Cada painel suporta até **25 botões**, organizados em até **5 linhas de 5 botões**.
- Texto acima do embed: até 2000 caracteres. Mensagens de confirmação: até 500 caracteres cada. Nome do painel: até 100 caracteres.

## Exemplos de uso

- **Cargos de notificação (acúmulo livre):** crie um painel "Central de Notificações" com botões "Anúncios", "Eventos", "Transmissões" e "Votações", cada um ligado a um cargo de menção. Deixe **"Permitir múltiplos cargos" ativado**, já que faz sentido o membro seguir vários tipos de aviso ao mesmo tempo. Quem quiser ser marcado em anúncios só clica no botão.

- **Cores do nome (escolha única):** use o template **Cores** ou monte um painel com um botão por cor. **Desative "Permitir múltiplos cargos"** para que escolher uma cor remova a anterior sozinha — assim o membro nunca fica com duas cores brigando. Posicione esses cargos de cor acima dos demais na lista para que a cor apareça no nome.

- **Pronomes ou plataforma:** publique um painel "Pronomes" (Ele/Dele, Ela/Dela, Elu/Delu) com emojis, deixando o acúmulo livre se quiser permitir combinações, ou em escolha única se preferir uma seleção só. Os membros se identificam sozinhos, sem abrir ticket nem pedir a um moderador.

## Requisitos

- O bot precisa da permissão **Gerenciar Cargos**.
- O cargo do bot precisa estar **acima**, na lista de cargos do servidor, de qualquer cargo que ele vá entregar. O bot **nunca** consegue dar ou tirar um cargo que esteja igual ou acima do cargo dele — nesses casos a ação é simplesmente ignorada.
- Para publicar o painel, o bot precisa conseguir **enviar mensagens** no canal escolhido (e o destino deve ser um canal de **texto** ou de **anúncios**).
- Para a criação automática de cargos a partir de templates, o bot também usa a permissão **Gerenciar Cargos**.

## Perguntas frequentes

**O mesmo botão dá e tira o cargo?**
Sim. É um liga/desliga: se o membro não tem o cargo, clicar adiciona; se já tem, clicar remove. A mensagem de confirmação avisa o que aconteceu.

**Por que o cargo demora alguns instantes para aparecer depois do clique?**
A confirmação ao membro é instantânea, mas a aplicação do cargo é feita em segundo plano, com controle de ritmo, para o servidor aguentar muita gente clicando ao mesmo tempo sem travar. Em geral o cargo aparece em poucos segundos.

**Como faço um menu onde só dá para escolher uma opção (uma cor só)?**
Desative o interruptor "Permitir múltiplos cargos" do painel. Aí, ao escolher uma opção, o bot remove sozinho as outras opções daquele painel.

**Editei o painel — preciso apagar a mensagem antiga e publicar de novo?**
Não. Ao salvar, o bot atualiza a mensagem já publicada. Só se ela tiver sido apagada do canal é que ele publica uma nova no lugar.

!!! tip "Dica"
    Quer cargos de cor sem criar nada à mão? Use o template **Cores**: ele já vem em modo escolha única e o bot cria os cargos coloridos automaticamente ao salvar. Depois é só arrastar esses cargos para acima dos demais na lista de cargos do servidor para que a cor apareça no nome dos membros.

