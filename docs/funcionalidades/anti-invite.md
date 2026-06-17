# Anti-invite

O Anti-invite remove automaticamente mensagens com convites de outros servidores do Discord (links `discord.gg` / `discord.com/invite`) e pode punir quem os envia, mantendo a divulgação de outras comunidades fora do seu servidor.

## Como funciona

O módulo analisa cada mensagem enviada por membros (mensagens de bots são ignoradas) nos servidores em que está ativado. O fluxo é:

1. **Verificação inicial.** A cada mensagem, o bot confere se o Anti-invite está ligado no servidor. Se o canal estiver na lista de exceções, ou se o autor tiver um cargo liberado, a mensagem é ignorada.
2. **Detecção de convites.** O bot procura na mensagem qualquer link de convite do Discord. Se não houver nenhum, nada acontece.
3. **Convite interno x externo.** O bot mantém uma lista atualizada dos convites do próprio servidor (incluindo a URL personalizada/vanity). Convites que pertencem ao seu servidor são tratados como **internos**; todos os outros, como **externos**.
4. **Decisão.** Convites externos sempre contam como violação. Convites do próprio servidor só viram violação se você tiver desligado a opção de permitir convites próprios.
5. **Ação.** Quando há violação, o bot:
   - **apaga a mensagem** com o convite;
   - opcionalmente **avisa no canal** marcando o autor (esse aviso é removido sozinho após alguns segundos);
   - **registra um log** num canal de sua escolha, com usuário, canal, ação aplicada e os códigos detectados;
   - aplica a **punição configurada** ao membro: nenhuma, advertência, silenciamento (mute) por um tempo definido, expulsão (kick) ou banimento (ban).

Tudo isso acontece em tempo real, no momento em que a mensagem é enviada — não há fila nem espera.

## Configuração

A configuração é feita pelo painel em [admin.delfus.app](https://admin.delfus.app), na seção **Anti-invite**. Lá você pode:

- **Ativar/desativar** o módulo;
- **permitir ou bloquear convites do próprio servidor**;
- definir **canais** e **cargos liberados** (exceções que nunca são moderadas);
- escolher a **ação** aplicada na violação: nenhuma, advertência, silenciamento, expulsão ou banimento;
- definir a **duração do silenciamento** (obrigatória quando a ação é mute);
- personalizar o **motivo**, ligar/desligar o **aviso no canal** e o **texto desse aviso**;
- escolher o **canal de logs** das remoções.

Não há comando de barra para esse módulo — toda a configuração é feita pelo painel.

## Requisitos

Para o módulo funcionar por completo, o bot precisa de permissões compatíveis com as ações escolhidas:

- **Gerenciar Mensagens** para apagar os convites;
- **Enviar Mensagens** no canal de aviso e no canal de logs;
- conforme a punição: **Moderar Membros** (silenciamento), **Expulsar Membros** (kick) ou **Banir Membros** (ban).

O cargo do bot também precisa estar **acima** do cargo dos membros que ele vai moderar.

!!! tip
    Use a lista de **cargos liberados** para a equipe de moderação e parceiros oficiais, e os **canais liberados** para áreas como divulgação ou parcerias, evitando remoções indesejadas.
