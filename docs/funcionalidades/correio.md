---
description: "Correio Elegante do Delfus: recados anônimos entre membros do servidor Discord em eventos com data marcada, aprovação da staff e temas visuais."
---

# Correio Elegante

Deixe qualquer membro do seu servidor Discord mandar um recado anônimo para outro durante um evento que você marca na agenda. A staff aprova, o Delfus transforma o recado em post público com visual temático e quem enviou continua em segredo. Serve para Dia dos Namorados, festa junina, aniversário do servidor ou qualquer data comemorativa.

## Como funciona

O Correio Elegante é um evento com hora marcada. Você define início e fim, e o comando `/correio` só responde dentro dessa janela, com o evento ligado no painel. Fora disso, o membro vê a mensagem de "evento inativo" que você escreveu.

O caminho de um recado:

1. **O membro envia** com `/correio`, escolhe o destinatário e escreve o recado (até 500 caracteres). A resposta é sempre privada: ninguém ao lado descobre quem mandou.
2. **A staff avalia** num canal interno. Lá aparece o recado, quem enviou, para quem é, e dois botões: **Aprovar** e **Rejeitar**.
3. **Se aprovado, vira post anônimo** no canal público, com o tema que você escolheu (cor, banner, ícone, moldura). Mostra para quem é, nunca quem enviou.

!!! example "Na prática"
    Ana usa `/correio` e manda um recado fofo pro Bruno. Só a Ana vê a confirmação. O recado cai no canal da moderação, alguém clica em **Aprovar**, e ele aparece no `#correio-publico` marcando o Bruno. O Bruno nunca vai saber que foi a Ana.

O bot cuida de alguns limites sozinho:

- Não dá pra mandar correio para **bots** nem **para si mesmo**. O recado é recusado na hora.
- Há um **intervalo entre envios** (cooldown) por membro, pra ninguém inundar a fila. Tentativas barradas por validação não reiniciam esse cronômetro.
- **Rejeitar** descarta o recado de vez: some da fila e nada é publicado. Sem histórico, sem aviso ao remetente.

!!! note "Detalhes que valem saber"
    O cooldown vive na memória do bot. Se ele reiniciar, os contadores zeram. Cooldown `0` desliga a espera. E só quem tem um dos cargos de aprovação consegue usar os botões; quem mais clicar recebe um aviso privado e nada acontece.

### A moldura de texto

Cada tema pode ter uma moldura: um texto fixo que envolve o recado do membro. Use o marcador `{{mensagem}}` no lugar onde o recado deve entrar.

!!! example "Moldura em ação"
    Com a moldura `"💕 Alguém preparou um recado especial:\n\n{{mensagem}}\n\nCom carinho 💌"`, um recado como "você é incrível" sai decorado, com saudação e assinatura. Sem moldura, o recado aparece sozinho.

Ligue **mencionar destinatário** e ele recebe um ping de verdade na publicação. Ligue um **cargo de recompensa** e todo mundo com correio aprovado ganha esse cargo automaticamente.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/correio usuario:<membro> mensagem:<texto>` | Manda um correio anônimo para outro membro. O recado (até 500 caracteres) vai para a fila da staff e, se aprovado, é publicado sem revelar quem enviou. Só funciona durante o evento ativo. |

!!! note
    Toda a configuração do Correio Elegante é feita pelo painel. Não há comandos de administração.

## Configuração

A configuração fica no Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção **Eventos → Correio Elegante**. Com o evento ligado, preencha:

- **Período do evento**: data/hora de início e fim (o fim tem que ser depois do início).
- **Canal de aprovação**: onde a staff avalia (deixe visível só para ela).
- **Canal público**: onde os correios aprovados aparecem.
- **Cargos de aprovação**: um ou mais cargos que podem aprovar/rejeitar (pelo menos um).
- **Temas**: pelo menos um, com um marcado como **ativo**. Cada tema tem nome, título, cor (`#rrggbb`) e, opcionalmente, banner, ícone, rodapé e moldura.

Ajustes opcionais:

- **Intervalo entre envios**: de `0` a `86400` segundos. O sugerido é 300 (5 minutos).
- **Mencionar destinatário**: liga/desliga o ping na publicação.
- **Cargo de recompensa**: dado automaticamente a quem tem correio aprovado.
- **Mensagem de evento inativo**: o texto que aparece fora do período.

!!! warning "O painel é exigente (de propósito)"
    Com o evento ativado, ele só salva se houver canal de aprovação, canal público, ao menos um cargo de aprovação, ao menos um tema, um tema ativo válido e datas coerentes. Faltou algo, não passa.

Confira também as permissões do bot:

- **Enviar Mensagens** e **Inserir Links/Embeds** nos dois canais, mais acesso para enxergá-los.
- Se usar cargo de recompensa: **Gerenciar Cargos**, com o cargo de recompensa **abaixo** do cargo mais alto do bot. Sem isso, a recompensa falha em silêncio, mas a publicação acontece normalmente.

## Exemplos

!!! example "Dia dos Namorados"
    Crie o tema "Dia dos Namorados" com cor rosa, um banner romântico e a moldura `"💕 Alguém preparou um recado especial:\n\n{{mensagem}}\n\nCom carinho 💌"`. Marque o período de 12 a 14 de junho, aponte `#correio-publico` pra publicação e `#staff-correio` pra aprovação, e dê o cargo de aprovação à moderação. Nesses dias, os recados anônimos pipocam e a staff vai liberando.

!!! example "Recompensar quem participa"
    Crie o cargo "Cupido 2026" como recompensa. Quem tem um correio aprovado ganha o cargo na hora, sem ninguém saber quantos ou quais enviou.

!!! example "Segurar o spam"
    Ponha o cooldown em 600 segundos (10 minutos). Cada membro só manda um novo correio a cada 10 minutos, e a staff aprova com calma.

## Perguntas frequentes

### Dá pra descobrir quem enviou o recado?
No canal público, nunca: só aparece o destinatário. O remetente real só é visível na fila de aprovação, que deve ser restrita à staff. Mantenha esse canal fechado para membros comuns.

### O que acontece se a staff rejeitar?
O recado é descartado na hora: some da fila e nada é publicado. Não há reaproveitamento nem aviso ao remetente. Pra ele, fica só a confirmação de que o correio "foi enviado para aprovação".

### Por que o `/correio` diz que não há evento ativo?
Ou o evento está desligado no painel, ou o momento atual está fora do período (antes do início ou depois do fim). Confira o toggle e as datas.

### Por que o remetente não ganhou o cargo de recompensa?
A recompensa é "melhor esforço". Veja se o cargo está configurado, se o bot tem **Gerenciar Cargos** e se o cargo de recompensa está **abaixo** do cargo mais alto do bot. Se algo falhar, o correio é publicado mesmo assim, só sem o cargo.

!!! tip "Dica"
    Use a moldura de cada tema como uma carta pré-pronta: saudação no começo, `{{mensagem}}` no meio, assinatura no fim. Assim até os recados mais curtos saem com a cara do evento.

