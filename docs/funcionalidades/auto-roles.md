# Cargos automáticos

Atribui cargos automaticamente a novos membros e bots assim que eles entram no servidor, sem precisar de nenhuma ação manual da equipe.

![Cargos automáticos no painel do Delfus](../assets/dashboard/auto-roles.png){ .dx-shot loading=lazy }

*Cargos automáticos no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

Sempre que alguém (ou um bot) entra no servidor, o Delfus cuida da atribuição de cargos sozinho:

1. **Entrada detectada** — assim que um novo membro entra, o bot verifica se os Cargos automáticos estão ativados para o servidor.
2. **Escolha dos cargos certos** — o bot diferencia contas humanas de bots e separa os cargos de cada tipo: membros recebem a lista de "cargos para membros" e bots recebem a lista de "cargos para bots". Se a lista correspondente estiver vazia, nada é feito.
3. **Atribuição em fila** — a entrega dos cargos passa por uma fila interna com um pequeno atraso (cerca de 1,5 segundo), o que evita conflitos quando muitas pessoas entram ao mesmo tempo e respeita os limites do Discord. Membros humanos têm prioridade sobre bots na fila.
4. **Aplicação dos cargos** — o bot adiciona cada cargo configurado ao novo membro. Cargos que ele já tenha são ignorados, e cargos acima do bot na hierarquia ou para os quais ele não tem permissão são pulados automaticamente.
5. **Resultado** — em poucos segundos o novo membro já aparece com todos os cargos previstos, com acesso aos canais e permissões correspondentes.

Se algo der errado temporariamente (por exemplo, um limite momentâneo do Discord), o bot tenta novamente várias vezes de forma automática, lembrando quais cargos já foram entregues para não duplicar o trabalho. Caso uma entrega falhe definitivamente após todas as tentativas, ela é registrada para acompanhamento, sem travar as demais.

## Configuração

A configuração é feita pelo Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção **Cargos automáticos**:

1. Ative a funcionalidade pelo botão de ativar/desativar.
2. Selecione os cargos que serão atribuídos a novos **membros** (humanos).
3. Selecione os cargos que serão atribuídos a novos **bots**.
4. Clique em **Salvar** para aplicar.

Você pode deixar uma das listas vazia — por exemplo, configurar cargos só para membros e nenhum para bots.

## Requisitos

- O Delfus precisa da permissão **Gerenciar cargos**.
- O cargo do bot deve estar **acima**, na lista de cargos do servidor, de qualquer cargo que ele precise atribuir. Cargos posicionados acima do bot são silenciosamente ignorados.

!!! tip
    Use a separação entre membros e bots a seu favor: dê aos novos bots um cargo restrito de "bots" e reserve os cargos de acesso e cor apenas para os membros humanos.
