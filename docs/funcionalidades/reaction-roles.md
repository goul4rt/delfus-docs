# Cargos por reação

Deixe seus membros pegarem (e largarem) cargos sozinhos, num clique. Você publica um painel com botões num canal, e cada um se serve do que quiser: cargos de notificação, cores, pronomes, jogos, regiões, acesso a áreas do servidor. Zero pedido manual de cargo, zero moderador envolvido — e seus canais de aviso ficam cheios só de quem realmente quer estar lá.

![Cargos por reação no painel do Delfus](../assets/dashboard/reaction-roles.png){ .dx-shot loading=lazy }

*Cargos por reação no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

A ideia é simples: você cria um **painel**, que nada mais é do que uma mensagem que o bot publica num canal. Essa mensagem pode ter um texto, um embed bonitinho (título, descrição, cor, imagem) e, o mais importante, os **botões** — cada botão amarrado a um cargo.

O membro clica, o bot resolve o resto. E cada botão funciona como um interruptor: o mesmo botão **dá e tira** o cargo. Se você ainda não tem aquele cargo, clicar adiciona. Se já tem, clicar remove. Pronto.

Na hora do clique, o membro recebe uma confirmação privada (só ele vê, e ela some sozinha) dizendo o que rolou. A confirmação é instantânea; o cargo em si entra logo em seguida, em segundo plano — em geral, em poucos segundos.

!!! example "Exemplo"
    Imagine que você abre um painel novo de notificações e 200 pessoas clicam ao mesmo tempo. Cada uma vê na hora a mensagem "Você recebeu o cargo **Eventos**!", e o bot vai aplicando os cargos com calma, em fila, sem travar nem apanhar do Discord. Ninguém fica esperando uma tela de carregamento.

!!! note "Por baixo dos panos"
    O bot processa os cliques com controle de ritmo e tenta de novo sozinho se der uma instabilidade momentânea. Cliques duplicados em sequência rápida são ignorados, pra não ficar dando e tirando o cargo várias vezes seguidas. Você não precisa fazer nada disso — é automático.

### Escolha única (modo exclusivo)

Todo painel tem o botão **"Permitir múltiplos cargos"**:

- **Ligado** (padrão) — o membro pode acumular vários cargos do painel ao mesmo tempo. Ótimo pra listas onde faz sentido marcar várias opções (notificações, jogos, pronomes).
- **Desligado** — vira escolha única. Ao pegar um cargo daquele painel, o bot **tira sozinho os outros** do mesmo painel. Perfeito pra cor do nome, região, plataforma — coisas em que só pode existir uma.

!!! note
    O modo exclusivo só mexe nos cargos **daquele painel**. Cargos de outros painéis (ou que o membro ganhou de outras formas) ficam intocados.

## Comandos

Essa feature não tem comando de barra. Tudo — criar painéis, botões, cargos, mensagens e publicar — acontece no [Dashboard](https://admin.delfus.app), na seção **Cargos por Reação**.

## Configuração

Toda a montagem é pelo [Dashboard](https://admin.delfus.app). O caminho é rápido:

1. **Ligue o sistema** no interruptor geral no topo da página. Ele liga/desliga todos os painéis de uma vez. (Com tudo desligado, os botões param de entregar cargos e o membro vê um aviso ao clicar.)
2. **Crie um painel** — do zero, em "Novo Painel", ou a partir de um **template** pronto: **Notificações**, **Cores** (já em escolha única), **Jogos** ou **Pronomes**. Se o template usar cargos que ainda não existem, o bot **cria eles pra você** ao salvar, já com nome e cor sugeridos.
3. **Configure o painel**: dê um nome (só pra você achar na lista), escolha o canal de destino (texto ou anúncios), escreva o conteúdo e monte a lista de botões.
4. **Salve** — e o bot publica a mensagem no canal. Editou depois? Ele **atualiza a mesma mensagem**, não cria outra. (Se alguém apagou a mensagem do canal nesse meio-tempo, ele percebe e publica uma nova.)

Cada botão tem **emoji** (opcional), **rótulo**, **cargo** e **cor** (azul, cinza, verde ou vermelho).

E dá pra personalizar as **mensagens de confirmação** que o membro recebe ao ganhar e ao perder um cargo. Use `{cargo}` pra inserir o nome automaticamente:

!!! example "Exemplo"
    Em vez do texto padrão "Você recebeu o cargo **Lives**!", você escreve `Pronto! Agora você é avisado toda vez que rolar uma {cargo}. 🎉`

!!! tip "Organizar painéis"
    Na lista você ativa/desativa cada painel individualmente, **duplica** um (sai uma cópia "(copia)" pronta pra ajustar) e **exclui** o que não usa mais.

!!! note "Limites"
    Até **25 botões** por painel (5 linhas de 5). Texto acima do embed: 2000 caracteres. Mensagens de confirmação: 500 cada. Nome do painel: 100.

## Exemplos

!!! example "Central de notificações (acúmulo livre)"
    Crie um painel "Central de Notificações" com os botões **Anúncios**, **Eventos**, **Transmissões** e **Votações**, cada um num cargo de menção. Deixe **"Permitir múltiplos cargos" ligado** — afinal, dá pra querer ser avisado de várias coisas ao mesmo tempo. Quem quer ser marcado em anúncios, clica e pronto.

!!! example "Cor do nome (escolha única)"
    Use o template **Cores** ou monte um painel com um botão por cor, e **desligue "Permitir múltiplos cargos"**. Aí escolher uma cor nova remove a anterior sozinha — ninguém fica com duas cores brigando. Só lembre de arrastar esses cargos de cor pra cima dos demais na lista de cargos, pra cor aparecer no nome.

!!! example "Pronomes, sem pedir a ninguém"
    Publique um painel "Pronomes" (Ele/Dele, Ela/Dela, Elu/Delu) com emojis. Deixe acúmulo livre se quiser permitir combinações, ou escolha única se preferir uma seleção só. Cada um se identifica sozinho — sem abrir ticket, sem chamar moderador.

## Perguntas frequentes

**O mesmo botão dá e tira o cargo?**
Sim, é um liga/desliga. Não tem o cargo, clicar adiciona; já tem, clicar remove. A confirmação avisa o que aconteceu.

**Por que o cargo demora alguns instantes pra aparecer?**
A confirmação é na hora, mas o cargo é aplicado em segundo plano, em fila, pro servidor aguentar muita gente clicando junto sem travar. Costuma entrar em poucos segundos.

**Como faço um menu de uma opção só (uma cor só)?**
Desligue o "Permitir múltiplos cargos" do painel. Escolher uma opção passa a remover as outras automaticamente.

**Editei o painel — preciso apagar a mensagem antiga e publicar de novo?**
Não. Ao salvar, o bot atualiza a mensagem que já está lá. Só publica uma nova se a antiga tiver sido apagada do canal.

**O bot não está entregando um cargo. Por quê?**
Quase sempre é hierarquia: o bot só mexe em cargos que estão **abaixo** dele na lista de cargos do servidor. Se o cargo do botão estiver igual ou acima do cargo do bot, o Discord não deixa e a ação é ignorada. Confira também se o bot tem a permissão **Gerenciar Cargos** e consegue **enviar mensagens** no canal do painel.

!!! tip "Dica"
    Quer cargos de cor sem criar nada na mão? Use o template **Cores**: ele já vem em modo escolha única e o bot cria os cargos coloridos sozinho ao salvar. Depois é só arrastar esses cargos pra cima dos demais na lista, e a cor aparece no nome dos membros.
