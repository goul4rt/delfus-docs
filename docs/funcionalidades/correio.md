# Correio Elegante

O Correio Elegante transforma seu servidor em uma "agência de cartas" temática: durante um evento com data marcada, qualquer membro pode mandar um recado **anônimo** para outro membro. Cada recado passa pela aprovação da equipe antes de aparecer num canal público com um visual personalizado (cor, banner, moldura), mantendo o remetente sempre em segredo. É ideal para datas como Dia dos Namorados, festas juninas, aniversário do servidor ou qualquer ocasião em que você queira incentivar interação carinhosa entre a comunidade.

## Como funciona

O Correio Elegante é um **evento com janela de tempo**: você define uma data/hora de início e uma de fim. O comando `/correio` só funciona enquanto o relógio do bot estiver **dentro** dessa janela e o evento estiver marcado como ativado no painel. Fora disso, o membro recebe a mensagem de "evento inativo" que você configurou.

Todo recado segue este fluxo, do envio até a publicação:

1. **Envio pelo membro** — O membro usa `/correio`, escolhe o destinatário (`usuario`) e escreve o recado (`mensagem`, até **500 caracteres**). A resposta do comando é sempre **privada** (só o próprio remetente vê), então ninguém ao redor descobre quem enviou.
2. **Verificação de evento ativo** — O bot confere se o evento está habilitado **e** se o momento atual está entre o início e o fim configurados. Se não estiver, mostra a mensagem de evento inativo e encerra ali.
3. **Validações automáticas do destinatário** — O recado é recusado na hora se:
   - O destinatário for um **bot** ("Você não pode enviar um correio para um bot.").
   - O destinatário for o **próprio remetente** ("Você não pode enviar um correio para si mesmo.").
4. **Intervalo mínimo entre envios (cooldown)** — Há um tempo de espera configurável entre um envio e o próximo, contado por membro. Se o membro tentar enviar rápido demais, recebe um aviso do tipo "Calma! Espere Ns antes de enviar outro correio." O cooldown só "trava" depois que o correio é **efetivamente enfileirado** — tentativas barradas por validação não consomem nem reiniciam o cronômetro.

   !!! note "Detalhe do cooldown"
       O cronômetro do cooldown é mantido na memória do bot. Se o bot reiniciar, os cooldowns em andamento são zerados. Definir o cooldown como `0` desliga essa espera.

5. **Fila de aprovação (canal interno)** — Se tudo passou, o recado é postado no **canal de aprovação** (visível só para a equipe) como um embed que mostra: o conteúdo cru do recado, **quem enviou** (Remetente), **para quem é** (Destinatário) e dois botões — **Aprovar** (verde) e **Rejeitar** (vermelho). O membro recebe a confirmação privada "Seu correio foi enviado para aprovação!".
6. **Decisão da equipe** — Apenas membros que possuem um dos **cargos de aprovação** configurados podem usar os botões. Quem não tem o cargo e clica recebe "Você não tem permissão para aprovar correios." (resposta privada, nada acontece com o recado).
   - **Rejeitar** → o recado é descartado: a mensagem some do canal de aprovação e nada é publicado. Não há reciclagem nem histórico.
   - **Aprovar** → o recado é publicado no canal público (próximo passo).
7. **Publicação anônima** — Ao aprovar, o recado é postado no **canal público** com o visual do **tema ativo**: cor, título, banner (imagem grande), ícone (miniatura), rodapé e a **moldura de texto**. A publicação mostra para quem é o recado, mas **nunca revela o remetente**. Depois de publicado, a mensagem da fila de aprovação é apagada para manter o canal interno limpo.

   ### Moldura de texto (frameText)
   Cada tema pode ter uma moldura: um texto fixo com o marcador `{{mensagem}}`, que é substituído pelo recado do membro. Por exemplo, uma moldura `"💕 Alguém preparou um recado especial:\n\n{{mensagem}}\n\nCom carinho 💌"` envolve o recado com a decoração definida por você. Se o tema não tiver moldura, o recado aparece sozinho. O embch público começa com "Para @destinatário" antes do corpo.

8. **Notificação do destinatário (opcional)** — Se a opção "mencionar destinatário" estiver ligada, o destinatário recebe uma menção real (ping) na publicação. Se estiver desligada, o nome dele ainda aparece escrito, mas sem notificação.
9. **Recompensa opcional ao remetente** — Se você configurou um **cargo de recompensa**, o membro que enviou o correio **aprovado** ganha esse cargo automaticamente. É aplicado em "melhor esforço": se o bot não tiver permissão ou hierarquia para dar o cargo, a publicação acontece mesmo assim, só a recompensa falha silenciosamente.

### Sobre o tema ativo

O servidor pode cadastrar **vários temas** e escolher qual fica ativo durante o evento. O bot usa o tema marcado como ativo; se por algum motivo o tema ativo não for encontrado, ele cai para o **primeiro tema** da lista. Se não houver nenhum tema cadastrado ou o canal de aprovação não estiver definido, o comando avisa o membro que "o Correio Elegante não está configurado corretamente".

## Comandos

| Comando | O que faz |
| --- | --- |
| `/correio usuario:<membro> mensagem:<texto>` | Envia um correio elegante anônimo para outro membro. O recado (até 500 caracteres) vai para a fila de aprovação da equipe; após aprovado, é publicado no canal público sem revelar quem enviou. Só funciona durante o evento ativo. |

Toda a **configuração** do Correio Elegante é feita pelo painel — não há comandos de barra de administração para esta feature.

## Configuração

A configuração é feita pelo Dashboard em [https://admin.delfus.app](https://admin.delfus.app), na seção de **Eventos → Correio Elegante**. Os campos disponíveis são:

1. **Ativar o evento** — Um toggle liga/desliga o Correio Elegante. Quando ligado, os campos de canais, cargos e temas passam a ser obrigatórios.
2. **Período do evento** — Data/hora de **início** e **fim**. O comando `/correio` só responde dentro dessa janela. O fim precisa ser depois do início.
3. **Canais**:
   - **Canal de aprovação** — onde a equipe avalia os recados (deve ficar visível só para a staff).
   - **Canal público** — onde os correios aprovados são publicados.
4. **Cargos de aprovação** — um ou mais cargos cujos membros podem aprovar/rejeitar. É obrigatório definir **ao menos um** quando o evento está ativo.
5. **Temas** — você cria um ou mais temas (é obrigatório **ao menos um**) e escolhe qual fica **ativo**. Cada tema tem:
   - **Nome do tema** (até 80 caracteres) — uso interno/identificação (ex.: "Dia dos Namorados").
   - **Título do embed** (até 256 caracteres) — o título mostrado na publicação pública.
   - **Cor** — em formato hexadecimal `#rrggbb`.
   - **Banner** (URL de imagem, opcional) — imagem grande no embed.
   - **Ícone** (URL de imagem, opcional) — miniatura no canto do embed.
   - **Rodapé** (até 2048 caracteres, opcional).
   - **Texto-moldura** (até 2000 caracteres, opcional) — texto decorativo com o marcador `{{mensagem}}`, que é substituído pelo recado do membro.
6. **Intervalo entre envios (cooldown)** — em segundos, de `0` (sem espera) até `86400` (24 horas). O padrão sugerido é 300 segundos (5 minutos).
7. **Mencionar destinatário** — toggle que define se o destinatário recebe uma menção (ping) na publicação.
8. **Cargo de recompensa** (opcional) — cargo dado automaticamente ao remetente quando o correio é aprovado.
9. **Mensagem de evento inativo** — texto mostrado quando alguém usa `/correio` fora do período do evento.

!!! note "Validações do painel"
    Com o evento ativado, o painel exige: canal de aprovação, canal público, ao menos um cargo de aprovação, ao menos um tema, um tema ativo válido e datas de início/fim coerentes. Sem isso, o painel não salva.

## Exemplos de uso

- **Evento de Dia dos Namorados** — Você cria um tema "Dia dos Namorados" com cor rosa, um banner romântico e a moldura `"💕 Alguém preparou um recado especial:\n\n{{mensagem}}\n\nCom carinho 💌"`. Define o período de 12 a 14 de junho, escolhe o canal `#correio-publico` para publicação e `#staff-correio` para aprovação, e dá o cargo de aprovação para a moderação. Durante esses dias, os membros mandam recados anônimos e a equipe vai liberando.

- **Recompensar quem participa** — Você configura um **cargo de recompensa** ("Cupido 2026"). Cada membro que tem um correio aprovado ganha o cargo automaticamente, criando um incentivo divertido para participar — sem que ninguém saiba quantos ou quais recados a pessoa mandou.

- **Controlar spam** — Para evitar que uma pessoa inunde a fila, você define o **cooldown** em 600 segundos (10 minutos). Assim cada membro só consegue enviar um novo correio a cada 10 minutos, dando tempo para a equipe aprovar com calma.

## Requisitos

- O bot precisa das permissões de **Enviar Mensagens** e **Inserir Links/Embeds** nos canais de aprovação e público (o comando `/correio` exige `SendMessages` e `EmbedLinks`).
- O bot precisa **enxergar e acessar** o canal de aprovação e o canal público (se não conseguir buscar o canal, avisa o membro que não encontrou o canal).
- Se você usar o **cargo de recompensa**, o bot precisa da permissão **Gerenciar Cargos** e o cargo de recompensa deve estar **abaixo** do cargo mais alto do bot na hierarquia — caso contrário a recompensa não é aplicada (mas a publicação acontece normalmente).
- O comando só funciona **dentro de um servidor** (não funciona em DM).

## Perguntas frequentes

**O destinatário ou outras pessoas conseguem descobrir quem enviou o recado?**
Não. No canal público o envio é sempre anônimo — só aparece o destinatário. O remetente real só é visível na **fila de aprovação**, que deve ser restrita à equipe. Por isso, mantenha o canal de aprovação fechado para membros comuns.

**O que acontece se a equipe rejeitar um correio?**
O recado é descartado de imediato: a mensagem some do canal de aprovação e nada é publicado. Não há reaproveitamento nem aviso ao remetente — para ele, fica apenas a confirmação de que o correio foi "enviado para aprovação".

**Por que o comando `/correio` diz que não há evento ativo?**
Isso acontece quando o evento está desligado no painel ou quando a data/hora atual está fora do período configurado (antes do início ou depois do fim). Verifique no painel se o toggle está ativado e se as datas de início e fim cobrem o momento atual.

**Por que o remetente não ganhou o cargo de recompensa?**
A recompensa é aplicada em "melhor esforço". Confira se o cargo de recompensa está configurado, se o bot tem a permissão **Gerenciar Cargos** e se o cargo de recompensa está **abaixo** do cargo mais alto do bot na hierarquia. Se algum desses pontos falhar, o correio é publicado mesmo assim, mas o cargo não é dado.

!!! tip "Dica"
    Use o **texto-moldura** de cada tema para criar uma "carta" pré-formatada — coloque uma saudação, o marcador `{{mensagem}}` no meio e uma assinatura no fim. Assim, mesmo recados curtos dos membros saem com um visual caprichado e coerente com o tema do evento.
