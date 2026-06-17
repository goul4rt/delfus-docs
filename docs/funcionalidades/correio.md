# Correio Elegante

O Correio Elegante permite que membros enviem recados anônimos uns para os outros durante um evento temático no servidor. Cada recado passa por aprovação da equipe antes de ser publicado em um canal público, mantendo o remetente em segredo.

## Como funciona

O Correio Elegante funciona como um evento com data de início e fim. Enquanto o evento está ativo, qualquer membro pode mandar um recado para outro membro usando o comando `/correio`. O fluxo completo é:

1. **Envio** — O membro usa `/correio`, escolhe o destinatário e escreve o recado (até 500 caracteres). O comando só funciona enquanto o evento estiver dentro do período configurado; fora disso, o membro recebe uma mensagem avisando que não há evento ativo.
2. **Validações automáticas** — O recado é recusado se o destinatário for um bot ou o próprio remetente. Há também um intervalo mínimo entre envios (cooldown configurável): se o membro tentar mandar correios em sequência rápido demais, ele é avisado para esperar alguns segundos.
3. **Fila de aprovação** — O recado vai para um canal interno visível só para a equipe. Ali, a staff vê o conteúdo do recado, quem enviou e para quem é, junto de dois botões: **Aprovar** e **Rejeitar**.
4. **Decisão da equipe** — Apenas membros com os cargos de aprovação configurados podem usar os botões. Se a equipe **rejeitar**, o recado é descartado e some da fila. Se **aprovar**, o recado é publicado.
5. **Publicação anônima** — Ao aprovar, o recado é postado no canal público com a aparência do tema ativo (cor, título, banner, moldura). A publicação mostra para quem é o recado, mas **nunca revela quem o enviou**. Opcionalmente, o destinatário pode receber uma notificação (menção).
6. **Recompensa opcional** — Se um cargo de recompensa estiver configurado, o membro que enviou o correio aprovado ganha esse cargo automaticamente.

O visual de cada correio é definido por um **tema** (cor, título, banner, ícone, rodapé e uma moldura de texto). O servidor pode ter vários temas cadastrados e escolher qual fica ativo durante o evento.

## Configuração

A configuração é feita pelo painel em [https://admin.delfus.app](https://admin.delfus.app), onde o dono do servidor define:

- O período do evento (datas de início e fim) e se ele está ativado.
- O **canal de aprovação** (onde a equipe avalia) e o **canal público** (onde os correios aprovados aparecem).
- Os **cargos de aprovação**, que dão permissão de aprovar/rejeitar correios.
- Os **temas** visuais e qual deles fica ativo.
- O **intervalo entre envios** (cooldown), se o destinatário deve ser mencionado ao publicar, o cargo de recompensa (opcional) e a mensagem exibida quando não há evento ativo.

O envio em si é feito pelos membros com o comando `/correio` (parâmetros: `usuario` e `mensagem`).

## Requisitos

- O bot precisa poder **enviar mensagens** e **inserir embeds (links)** nos canais de aprovação e público.
- Se o cargo de recompensa for usado, o bot precisa da permissão de **gerenciar cargos**, e o cargo de recompensa deve estar **abaixo** do cargo mais alto do bot na hierarquia — caso contrário a recompensa não é aplicada.

!!! tip
    Mantenha o canal de aprovação visível apenas para a equipe. É lá que o remetente real de cada recado aparece — no canal público o envio é sempre anônimo.
