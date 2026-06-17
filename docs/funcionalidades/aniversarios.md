# Aniversários

Permite que os membros registrem a data de aniversário e o bot os parabenize automaticamente no canal escolhido, no dia certo, opcionalmente entregando um cargo temporário de aniversariante.

## Como funciona

A funcionalidade combina o registro feito pelos próprios membros com um anúncio automático diário.

1. **Registro pelo membro.** Cada pessoa usa `/aniversario registrar` informando dia, mês e (conforme a política do servidor) o ano. A data fica salva por servidor — quem já registrou não consegue alterar sozinho; só um administrador pode corrigir.
2. **Verificação automática a cada hora.** De hora em hora o bot percorre os servidores com a funcionalidade ativada. Quando a hora local (no fuso configurado) bate com o horário de parabéns escolhido, ele busca quem faz aniversário naquele dia.
3. **Anúncio no canal.** Para cada aniversariante do dia, o bot envia uma mensagem de parabéns no canal configurado. A mensagem pode ser uma embed personalizada (com campos como menção ao usuário, nome, idade e nome do servidor preenchidos automaticamente) ou um modelo padrão festivo.
4. **Cargo de aniversariante (opcional).** Se um cargo estiver configurado, ele é atribuído aos aniversariantes do dia e removido automaticamente dos aniversariantes do dia anterior — então a pessoa fica "destacada" só durante o seu dia.
5. **Sem duplicatas.** O bot marca o dia como já processado por servidor, então os parabéns saem uma única vez por dia mesmo que a verificação rode várias vezes.

Além do anúncio automático, os membros podem consultar a qualquer momento:

- `/aniversario ver` — mostra o aniversário (e a idade, se o ano foi informado) de si mesmo ou de outro membro.
- `/aniversario proximos` — lista os próximos aniversários do servidor, em ordem de quão perto estão.

## Configuração

A configuração principal é feita pelo **Dashboard** (https://admin.delfus.app), na seção de Eventos > Aniversários. Lá você define:

- Ativar/desativar a funcionalidade.
- O **canal** onde os parabéns são enviados.
- O **horário** e o **fuso horário** em que os anúncios saem (padrão: 9h, horário de Brasília).
- O **cargo** opcional de aniversariante.
- A **mensagem de anúncio** (embed personalizada).
- A **política do ano de nascimento**: obrigatório, opcional ou desativado.

Comandos disponíveis no Discord:

- `/aniversario registrar` — membro registra o próprio aniversário (dia, mês e ano conforme a política).
- `/aniversario ver` — consulta o aniversário de um membro.
- `/aniversario proximos` — lista os próximos aniversários do servidor.
- `/aniversario-admin definir-usuario` — administrador define ou corrige o aniversário de um membro.
- `/aniversario-admin remover-usuario` — administrador remove o aniversário de um membro.

## Requisitos

- A funcionalidade precisa estar **ativada** e ter um **canal definido** — sem isso, nenhum anúncio é enviado.
- O bot precisa conseguir **enviar mensagens** no canal configurado.
- Para usar o cargo de aniversariante, o bot precisa de permissão para **gerenciar cargos**, e o cargo do bot deve estar **acima** do cargo de aniversariante na hierarquia.

!!! tip
    Peça aos membros que informem o ano de nascimento (ou torne-o obrigatório no painel) para que a idade apareça automaticamente nos parabéns e na consulta `/aniversario ver`.
