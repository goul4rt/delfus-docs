# Correio Elegante

Quer dar um toque especial ao seu servidor numa data comemorativa? O Correio Elegante deixa qualquer membro mandar um recado **anônimo** para outro membro durante um evento que você marca na agenda. A equipe dá um ok rápido, o recado aparece num canal público com um visual caprichado e quem enviou continua em segredo.

Perfeito para Dia dos Namorados, festa junina, aniversário do servidor ou qualquer ocasião em que você queira espalhar carinho na comunidade.

## Como funciona

O Correio Elegante é um **evento com hora marcada**. Você define quando começa e quando termina, e o comando `/correio` só responde dentro dessa janela (e com o evento ligado no painel). Fora disso, o membro vê a mensagem de "evento inativo" que você escreveu.

Quando um recado é enviado, o caminho é simples:

1. **O membro envia** com `/correio`, escolhendo o destinatário e escrevendo o recado (até 500 caracteres). A resposta é sempre privada — ninguém ao lado descobre quem mandou.
2. **A equipe avalia** num canal interno, só para a staff. Lá aparece o recado, quem enviou, para quem é, e dois botões: **Aprovar** e **Rejeitar**.
3. **Se aprovado, vira post anônimo** no canal público, com a cara do tema que você escolheu (cor, banner, ícone, moldura). Mostra para quem é — mas nunca quem enviou.

!!! example "Na prática"
    Ana usa `/correio` e manda um recado fofo pro Bruno. Só a Ana vê a confirmação. O recado cai no canal da moderação, alguém clica em **Aprovar**, e ele aparece bonito no `#correio-publico` marcando o Bruno. O Bruno fica todo feliz — e nunca vai saber que foi a Ana.

Alguns cuidados que o bot toma sozinho:

- Não dá pra mandar correio para **bots** nem **para si mesmo** — o recado é recusado na hora.
- Existe um **intervalo entre envios** (cooldown) por membro, pra ninguém inundar a fila. Tentativas barradas por validação não reiniciam esse cronômetro.
- **Rejeitar** descarta o recado de vez: some da fila e nada é publicado. Sem histórico, sem aviso ao remetente.

!!! note "Detalhes que valem saber"
    O cooldown vive na memória do bot — se ele reiniciar, os contadores zeram. Definir o cooldown como `0` desliga a espera. E só quem tem um dos cargos de aprovação consegue usar os botões; qualquer outra pessoa que clicar recebe um aviso privado e nada acontece.

### A moldura de texto

Cada tema pode ter uma **moldura**: um texto fixo que envolve o recado do membro. Você usa o marcador `{{mensagem}}` no lugar onde o recado deve entrar.

!!! example "Moldura em ação"
    Se a moldura for `"💕 Alguém preparou um recado especial:\n\n{{mensagem}}\n\nCom carinho 💌"`, um recado simples como "você é incrível" sai assim, todo decorado, com saudação e assinatura. Sem moldura, o recado aparece sozinho.

E se você ligar a opção **mencionar destinatário**, ele recebe um ping de verdade na publicação. Se ligar um **cargo de recompensa**, todo mundo que tem um correio aprovado ganha esse cargo automaticamente — um mimo pra quem participa.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/correio usuario:<membro> mensagem:<texto>` | Manda um correio anônimo para outro membro. O recado (até 500 caracteres) vai para a fila da equipe e, se aprovado, é publicado sem revelar quem enviou. Só funciona durante o evento ativo. |

!!! note
    Toda a configuração do Correio Elegante é feita pelo painel — não há comandos de administração para essa função.

## Configuração

A configuração fica no Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção **Eventos → Correio Elegante**. Com o evento ligado, você precisa preencher:

- **Período do evento** — data/hora de início e fim (o fim tem que ser depois do início).
- **Canal de aprovação** — onde a equipe avalia (deixe visível só para a staff).
- **Canal público** — onde os correios aprovados aparecem.
- **Cargos de aprovação** — um ou mais cargos que podem aprovar/rejeitar (pelo menos um).
- **Temas** — pelo menos um, com um marcado como **ativo**. Cada tema tem nome, título, cor (`#rrggbb`) e, opcionalmente, banner, ícone, rodapé e a moldura de texto.

E os ajustes opcionais:

- **Intervalo entre envios** — de `0` a `86400` segundos. O sugerido é 300 (5 minutos).
- **Mencionar destinatário** — liga/desliga o ping na publicação.
- **Cargo de recompensa** — dado automaticamente a quem tem correio aprovado.
- **Mensagem de evento inativo** — o texto que aparece fora do período.

!!! warning "O painel é exigente (de propósito)"
    Com o evento ativado, ele só salva se houver canal de aprovação, canal público, ao menos um cargo de aprovação, ao menos um tema, um tema ativo válido e datas coerentes. Faltou algo, não passa.

Vale também conferir as permissões do bot:

- **Enviar Mensagens** e **Inserir Links/Embeds** nos dois canais, e acesso para enxergar esses canais.
- Se usar cargo de recompensa: **Gerenciar Cargos**, com o cargo de recompensa **abaixo** do cargo mais alto do bot. Se não, a recompensa falha em silêncio — mas a publicação acontece normalmente.

## Exemplos

!!! example "Dia dos Namorados"
    Você cria o tema "Dia dos Namorados" com cor rosa, um banner romântico e a moldura `"💕 Alguém preparou um recado especial:\n\n{{mensagem}}\n\nCom carinho 💌"`. Marca o período de 12 a 14 de junho, aponta `#correio-publico` pra publicação e `#staff-correio` pra aprovação, e dá o cargo de aprovação à moderação. Nesses dias, os recados anônimos pipocam e a equipe vai liberando.

!!! example "Recompensar quem participa"
    Você cria o cargo "Cupido 2026" como recompensa. Quem tem um correio aprovado ganha o cargo na hora — um incentivo divertido pra mandar recados, sem ninguém saber quantos ou quais a pessoa enviou.

!!! example "Segurar o spam"
    Pra evitar que alguém entupa a fila, você põe o cooldown em 600 segundos (10 minutos). Cada membro só manda um novo correio a cada 10 minutos, e a equipe aprova com calma.

## Perguntas frequentes

**Dá pra descobrir quem enviou o recado?**
No canal público, nunca — só aparece o destinatário. O remetente real só é visível na fila de aprovação, que deve ser restrita à equipe. Por isso, mantenha esse canal fechado para membros comuns.

**O que acontece se a equipe rejeitar?**
O recado é descartado na hora: some da fila e nada é publicado. Não há reaproveitamento nem aviso ao remetente — pra ele, fica só a confirmação de que o correio "foi enviado para aprovação".

**Por que o `/correio` diz que não há evento ativo?**
Ou o evento está desligado no painel, ou o momento atual está fora do período (antes do início ou depois do fim). Confira o toggle e as datas no painel.

**Por que o remetente não ganhou o cargo de recompensa?**
A recompensa é "melhor esforço". Veja se o cargo está configurado, se o bot tem **Gerenciar Cargos** e se o cargo de recompensa está **abaixo** do cargo mais alto do bot. Se algo falhar, o correio é publicado mesmo assim, só sem o cargo.

!!! tip "Dica"
    Use a moldura de cada tema como uma "carta" pré-pronta: uma saudação no começo, o `{{mensagem}}` no meio e uma assinatura no fim. Assim, até os recados mais curtos saem caprichados e com a cara do evento.

