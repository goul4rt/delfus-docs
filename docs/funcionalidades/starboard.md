# Starboard

O Starboard transforma reações em um mural de destaques: quando uma mensagem recebe estrelas (ou qualquer emoji que você definir) suficientes, o Delfus a republica automaticamente em um canal de destaques do servidor. Inclui ranking de membros, cargos de recompensa e um Hall da Fama curado.

## Como funciona

O Starboard funciona com base em **murais** (boards). Cada mural tem um emoji de voto, um canal de destino e um número mínimo de estrelas para entrar. Você pode ter vários murais ao mesmo tempo (por exemplo, um para "melhores memes" e outro para "mensagens em destaque").

O fluxo, do começo ao fim:

1. **Alguém reage** a uma mensagem com o emoji configurado em um mural. O Delfus identifica qual mural usa aquele emoji e valida a reação.
2. **O voto é validado**. O bot ignora reações de bots, auto-votos (reagir na própria mensagem), usuários ou canais na lista de bloqueio do mural, e respeita um limite anti-spam (quantos votos um membro pode dar em determinado período). Reações inválidas podem ser removidas automaticamente, e quem tenta dar auto-voto recebe um aviso por mensagem direta na primeira vez.
3. **A pontuação é contada**. Cada emoji pode ter um peso diferente, e você pode configurar emojis de "voto negativo" que descontam pontos. A contagem é acumulada de forma eficiente e salva periodicamente.
4. **Ao atingir o mínimo de estrelas**, a mensagem é **republicada no canal de destaques** com um cartão mostrando o autor, o conteúdo, anexos/imagens e um link para a mensagem original. Conforme mais votos chegam, o cartão é **atualizado** com a nova pontuação. Murais com **níveis de exibição** trocam o emoji e a cor do cartão conforme a pontuação sobe (ex.: ⭐ → 🌟 → 💫 → ✨).
5. **Se a pontuação cair** abaixo do limite de remoção (porque pessoas tiraram a reação ou houve votos negativos), o destaque pode ser removido do canal, conforme a configuração do mural.
6. **Ranking e recompensas**. Cada vez que uma mensagem entra em destaque, o autor acumula estatísticas (total de estrelas, quantas vezes apareceu no mural, melhor pontuação). Com base nesses números, o bot pode **conceder cargos de recompensa** automaticamente quando o membro atinge certas metas, e remover quando ele deixa de qualificar (se o mural estiver configurado assim).
7. **Reset periódico do ranking** (opcional). Se você configurar, o ranking pode ser zerado de tempos em tempos (ex.: semanal ou mensal), recomeçando a competição.

Além do fluxo por reação, existem dois recursos extras:

- **Auto-estrela**: em canais escolhidos, o bot pode reagir automaticamente nas mensagens (ou já mandá-las direto para o destaque), com filtros como tamanho mínimo de texto ou exigir imagem — útil para canais de arte, memes ou prints. Mensagens que não passam nos filtros podem ser apagadas, se você quiser.
- **Hall da Fama**: uma coleção permanente e curada das melhores mensagens, adicionada manualmente pela moderação. Diferente do mural automático, o Hall da Fama não some quando os votos caem.

## Configuração

A configuração principal é feita pelo **Dashboard** em [admin.delfus.app](https://admin.delfus.app), na seção **Starboard**. Por lá você cria e edita os murais (emoji de voto, canal de destino, mínimo de estrelas, pesos, votos negativos, níveis de exibição, anti-spam, listas de bloqueio, aparência do cartão), configura a auto-estrela, os cargos de recompensa, os resets de ranking e o Hall da Fama.

Os membros do servidor têm dois comandos disponíveis:

- `/starboard` — mostra as estatísticas de estrelas de um membro (total, quantas vezes apareceu no destaque e melhor pontuação), com detalhamento por mural. Sem argumento, mostra as suas próprias; com o argumento de usuário, mostra as de outra pessoa.
- `/hall-of-fame` — exibe o Hall da Fama do servidor, com navegação por páginas.

## Requisitos

- O bot precisa de permissão para **ver e enviar mensagens** no canal de destaques (e no canal do Hall da Fama, se usar um).
- Para **remover reações inválidas** (auto-votos, votos bloqueados ou acima do limite anti-spam), o bot precisa de **Gerenciar Mensagens**.
- Para **conceder cargos de recompensa**, o bot precisa de **Gerenciar Cargos**, e o cargo do bot deve estar acima dos cargos de recompensa na hierarquia.
- Para a **auto-estrela com apagamento** de mensagens que não passam nos filtros, o bot precisa de **Gerenciar Mensagens** nos canais envolvidos.

!!! tip
    Você pode usar emojis personalizados do servidor como voto e até emojis de voto negativo para "derrubar" mensagens ruins — combine isso com os níveis de exibição para que destaques muito votados ganhem um cartão mais chamativo.
