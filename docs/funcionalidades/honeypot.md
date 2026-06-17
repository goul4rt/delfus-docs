# Honeypot (Canal Isca)

O Honeypot cria um "canal armadilha": qualquer membro que enviar mensagem nele é automaticamente punido e a equipe recebe um alerta. É uma forma simples de capturar spammers e contas maliciosas, que costumam disparar mensagens em todos os canais ao entrar no servidor.

![Configuração do honeypot no painel do Delfus](../assets/dashboard/honeypot.png){ .dx-shot loading=lazy }

*Configuração do honeypot no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

A ideia é deixar um canal visível mas onde ninguém legítimo deveria escrever (por exemplo, um canal chamado "nao-escreva-aqui" no topo da lista). Bots de spam normalmente escrevem em tudo, então caem na armadilha.

Quando o Honeypot está ativo e alguém envia uma mensagem no canal observado:

1. A mensagem é apagada na hora.
2. O autor recebe a punição configurada (advertência, silenciar, expulsão ou banimento). Por padrão, é **silenciar por 10 minutos**.
3. Um alerta é enviado para o canal de alertas que você definiu, informando quem foi punido, qual ação foi aplicada e em qual canal a pessoa caiu.
4. O bot interrompe qualquer outro processamento daquela mensagem (ela não passa por triggers, filtros ou comandos).

Bots e a própria conta do bot Delfus são ignorados. A punição só é aplicada se o bot tiver permissão para moderar aquele membro (cargos acima dele, etc.); caso contrário, a mensagem ainda é apagada, mas a punição pode falhar.

O texto do alerta pode ser personalizado. Você pode trocar a mensagem padrão por um texto ou por um embed próprio, usando os marcadores `{user}` (menciona quem caiu) e `{channel}` (menciona o canal isca), que são substituídos automaticamente no envio.

## Configuração

Você pode configurar o Honeypot de duas formas:

**Pelo painel** (https://admin.delfus.app): há uma página dedicada ao Honeypot no Dashboard onde você define o canal observado, o canal de alertas, a ação e a mensagem.

**Por comando**, com o slash command `/honeypot` e seus subcomandos:

- `/honeypot ativar` — define o canal observado (a isca) e o canal de alertas. Ao ativar, a ação padrão já fica como silenciar por 10 minutos. Rodar `ativar` de novo com os mesmos dois canais **desativa** o Honeypot.
- `/honeypot acao` — escolhe o que acontece com quem cai na armadilha: advertência, silenciar, expulsão ou banimento. Para silenciar, você também define a duração (em segundos).
- `/honeypot mensagem` — personaliza o alerta enviado ao canal de alertas: como texto simples ou como embed (com título, descrição e cor).

Os subcomandos `acao` e `mensagem` só funcionam depois que o Honeypot estiver ativado.

## Requisitos

- Apenas administradores do servidor podem configurar o Honeypot.
- O bot precisa das permissões: **Ver canais**, **Ver histórico de mensagens**, **Gerenciar mensagens** (para apagar) e **Moderar membros / Colocar em time-out** (para silenciar). Para expulsar ou banir, o bot também precisa das permissões correspondentes de **Expulsar membros** / **Banir membros**.
- O cargo do bot precisa estar acima dos membros que você quer punir, senão a punição não é aplicada.

!!! tip
    Coloque o canal isca bem no topo da lista de canais e com um nome claro de "não escreva aqui". Spammers escrevem nos primeiros canais que veem; membros reais leem o aviso e passam direto.
