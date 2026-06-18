# Honeypot (Canal Isca)

O Honeypot cria um "canal armadilha": qualquer membro que enviar mensagem nele é automaticamente punido, a mensagem é apagada e a sua equipe recebe um alerta. É uma forma simples e eficaz de capturar spammers e contas maliciosas, que ao entrar no servidor costumam disparar mensagens em todos os canais que veem pela frente — incluindo o canal isca, onde nenhum membro legítimo deveria escrever.

![Configuração do honeypot no painel do Delfus](../assets/dashboard/honeypot.png){ .dx-shot loading=lazy }

*Configuração do honeypot no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

A ideia central é deixar um canal **visível, mas onde ninguém legítimo deveria escrever** (por exemplo, um canal chamado "nao-escreva-aqui" no topo da lista). Bots de spam e contas-laranja normalmente escrevem em todos os canais ao chegar, então caem na armadilha; membros reais leem o aviso e passam direto.

Quando o Honeypot está ativo e o bot detecta uma **mensagem nova** no canal observado, a sequência abaixo acontece, nessa ordem:

1. **A mensagem é apagada na hora.** O bot remove a mensagem assim que ela aparece no canal isca (desde que tenha permissão para isso). A exclusão é tentada logo no início e reforçada de novo após a punição, garantindo que o conteúdo do spammer não fique visível.
2. **O autor recebe a punição configurada.** As opções são: advertência, silenciar (timeout), expulsão ou banimento. Por padrão, ao ativar, a ação fica como **silenciar por 10 minutos** (600 segundos).
3. **Um alerta é enviado ao canal de alertas** que você definiu, informando quem caiu, qual ação foi aplicada e em qual canal isca a pessoa escreveu.
4. **O bot interrompe qualquer outro processamento daquela mensagem.** Ela não passa por triggers, filtros, contadores de mensagens nem comandos — o Honeypot é a primeira verificação do fluxo de mensagens e tem prioridade.

### Quem é ignorado

- **Bots** (incluindo o próprio Delfus) e **mensagens de sistema** são sempre ignorados — só contas de usuários reais são punidas.
- A punição só é aplicada se o bot **conseguir moderar aquele membro** (ou seja, o cargo do bot precisa estar acima do membro na hierarquia). Se o bot não tiver hierarquia suficiente, a **mensagem ainda é apagada e o alerta ainda é enviado**, mas a punição em si pode não ser aplicada.

### A punição em detalhe

A ação é executada pelo mesmo sistema de moderação usado pelos comandos de punição do bot, então ela respeita as mesmas regras (registro de advertências, aplicação de timeout, etc.):

- **Advertência (`warn`)** — registra uma advertência para o usuário, como se um moderador tivesse advertido.
- **Silenciar (`mute`)** — aplica um timeout do Discord pela duração configurada. A duração padrão é de **600 segundos (10 minutos)**, mas pode ir de **1 minuto a 28 dias** (limite máximo de timeout do próprio Discord).
- **Expulsar (`kick`)** — remove o membro do servidor (ele pode entrar novamente com um novo convite).
- **Banir (`ban`)** — bane o membro permanentemente.

O motivo registrado na punição é, por padrão: *"Honeypot: enviou mensagem no canal isca destinado a capturar spammers/usuários maliciosos"*.

### O alerta enviado à equipe

Por padrão, o alerta é uma mensagem de texto simples no formato:

> 🚨 Honeypot: @usuário foi silenciado (10 min) por enviar mensagem no canal #nome-do-canal-isca.

O verbo muda conforme a ação aplicada (advertido / silenciado / expulso / banido), e a duração só aparece quando a ação é silenciar.

Você pode **personalizar esse alerta**, trocando-o por um texto próprio ou por um **embed** (com título, descrição e cor). Em qualquer um dos formatos, dois marcadores são substituídos automaticamente no momento do envio:

- `{user}` — menciona quem caiu na armadilha.
- `{channel}` — menciona o canal isca onde a pessoa escreveu.

Se você configurar um embed sem nenhum conteúdo visível (sem título, descrição, campos, imagem, etc.), o bot detecta isso e cai de volta na mensagem de texto padrão, para que o alerta nunca deixe de ser entregue.

### Configuração que sobrevive a reinícios

A configuração do Honeypot é salva no banco de dados do servidor e recarregada automaticamente quando o bot reinicia ou quando você altera as configurações pelo painel. Na prática, isso significa que, depois de ativado, o Honeypot continua funcionando indefinidamente, sem precisar reconfigurar — e edições feitas no Dashboard passam a valer assim que salvas.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/honeypot ativar` | Ativa o Honeypot definindo o **canal observado** (a isca) e o **canal de alertas**. Ao ativar, a ação já fica como silenciar por 10 minutos. Rodar o comando de novo com **exatamente os mesmos dois canais desativa** o Honeypot. |
| `/honeypot acao` | Escolhe o que acontece com quem cai na armadilha: **advertir**, **silenciar**, **expulsar** ou **banir**. Para silenciar, há uma opção de duração em segundos (mínimo 60, máximo 2.419.200 — 28 dias). |
| `/honeypot mensagem` | Personaliza o alerta enviado ao canal de alertas: como **texto** simples ou como **embed** (com título e cor opcionais). |

Observações sobre os comandos:

- Os subcomandos `acao` e `mensagem` **só funcionam depois que o Honeypot estiver ativado** com `ativar`. Se não estiver ativo, o bot avisa que não há Honeypot configurado.
- Nos campos de canal de `ativar`, o bot oferece **autocompletar** com os canais de texto do servidor, para facilitar a escolha.
- O comando exige **permissão de Administrador** para ser usado.

## Configuração

Você pode configurar o Honeypot de duas formas: pelo **Dashboard** ou por **comando**. As duas escrevem na mesma configuração, então você pode misturar (ativar por comando e ajustar pelo painel, por exemplo).

### Pelo Dashboard (recomendado)

Acesse [https://admin.delfus.app](https://admin.delfus.app), selecione o seu servidor e abra a página **Honeypot**. Lá você define, em diálogos separados:

1. **Canais** — o **canal observado** (a isca) e o **canal de alertas** para onde os avisos serão enviados.
2. **Punição** — a **ação** (advertência, mute/timeout, kick ou ban), a **duração** em segundos (usada quando a ação é mute; padrão 600 = 10 minutos) e um **motivo** opcional para o registro da punição.
3. **Mensagem de alerta** — escolha entre o alerta **padrão**, um **texto** personalizado ou um **embed** próprio (com título, descrição, cor, rodapé, etc.). Use `{user}` e `{channel}` no texto para inserir automaticamente a menção de quem caiu e do canal isca.

Para desligar o Honeypot pelo painel, basta remover a configuração na própria página.

### Por comando

1. Rode `/honeypot ativar`, informando o canal isca e o canal de alertas. Pronto: já fica ativo silenciando por 10 minutos.
2. (Opcional) Ajuste a punição com `/honeypot acao`, escolhendo a ação e, no caso de silenciar, a duração em segundos.
3. (Opcional) Personalize o alerta com `/honeypot mensagem`, escolhendo texto ou embed e escrevendo o conteúdo.

Para **desativar** por comando, rode `/honeypot ativar` de novo com **os mesmos dois canais** que você usou para ativar — isso alterna o Honeypot para desligado.

## Exemplos de uso

- **Pegar spammers que entram disparando em todos os canais:** crie um canal "🚫-nao-escreva-aqui" no topo da lista, rode `/honeypot ativar` apontando esse canal como isca e um canal interno de staff como alertas. Qualquer conta que escrever na isca é silenciada por 10 minutos e a equipe recebe o aviso instantaneamente.

- **Banir contas maliciosas automaticamente:** depois de ativar, rode `/honeypot acao` e escolha **Banir**. A partir daí, quem cair na armadilha é banido na hora, sem precisar de moderador online.

- **Alerta personalizado para a equipe:** rode `/honeypot mensagem` com tipo **embed**, título "⚠️ Honeypot acionado" e descrição "O usuário {user} caiu na isca {channel} e foi punido." — o alerta chega formatado e já com as menções corretas.

## Requisitos

- Apenas **administradores do servidor** podem configurar o Honeypot (tanto pelo comando quanto pelo Dashboard).
- O bot precisa das permissões: **Ver canais**, **Ver histórico de mensagens**, **Gerenciar mensagens** (para apagar) e **Moderar membros / Colocar em time-out** (para silenciar). Para **expulsar** ou **banir**, o bot também precisa das permissões correspondentes de **Expulsar membros** / **Banir membros**.
- O **cargo do bot precisa estar acima** dos membros que você quer punir na hierarquia de cargos; caso contrário, a mensagem é apagada e o alerta é enviado, mas a punição pode falhar.

## Perguntas frequentes

**O Honeypot pune bots ou o próprio Delfus?**
Não. Bots (inclusive o próprio Delfus) e mensagens de sistema são sempre ignorados — só contas de usuários reais caem na armadilha.

**Preciso reconfigurar depois que o bot reinicia?**
Não. A configuração fica salva e é recarregada automaticamente. Uma vez ativado, o Honeypot continua valendo até você desativá-lo.

**Como desativo o Honeypot?**
Pelo Dashboard, remova a configuração na página do Honeypot. Por comando, rode `/honeypot ativar` novamente com exatamente os mesmos dois canais (isca e alertas) que usou para ativar.

**O membro punido fica sabendo que caiu numa armadilha?**
A mensagem dele é apagada e a punição é aplicada como qualquer outra moderação (timeout, kick ou ban). O alerta detalhado vai apenas para o canal de alertas da equipe, não para o usuário.

!!! tip "Dica"
    Coloque o canal isca bem no topo da lista de canais, com um nome claro de "não escreva aqui". Spammers escrevem nos primeiros canais que veem; membros reais leem o aviso e passam direto. Combine com a ação **Banir** para que contas maliciosas sejam removidas automaticamente, sem depender de um moderador online.

