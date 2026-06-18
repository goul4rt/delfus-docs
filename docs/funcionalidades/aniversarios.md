# Aniversários

A funcionalidade de Aniversários deixa cada membro registrar a própria data de nascimento e faz o bot parabenizá-los automaticamente no dia certo, em um canal à sua escolha, com uma mensagem personalizada e, se você quiser, um cargo temporário de aniversariante. É uma forma simples de aumentar o engajamento e fazer a comunidade se sentir lembrada, sem que ninguém da moderação precise acompanhar calendário manualmente.

![Configuração de aniversários no painel do Delfus](../assets/dashboard/aniversarios.png){ .dx-shot loading=lazy }

*Configuração de aniversários no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

A funcionalidade combina o **registro feito pelos próprios membros** com uma **verificação automática a cada hora** que dispara os parabéns no horário e fuso que você definir.

### 1. Registro pelo membro

Cada pessoa usa `/aniversario registrar` informando o **dia** (1–31) e o **mês** (1–12), e, conforme a política do servidor, o **ano** de nascimento (entre 1900 e 2025).

- O bot **valida a data**: rejeita meses fora de 1–12 e dias que não existem no mês (por exemplo, 31 de fevereiro). 29 de fevereiro é aceito.
- A data fica salva **por servidor**. O mesmo usuário pode ter aniversários diferentes registrados em servidores diferentes.
- **Quem já registrou não consegue alterar sozinho.** Se a pessoa rodar `/aniversario registrar` de novo, o bot recusa e orienta a pedir a um administrador para corrigir via `/aniversario-admin definir-usuario`. Isso evita que alguém troque a data toda hora para "ganhar" o anúncio em outro dia.

### 2. Política do ano de nascimento

O comportamento do campo "ano" depende da configuração do painel:

- **Opcional** (padrão): a pessoa pode informar o ano ou deixar em branco. Com ano, a idade aparece nos parabéns e na consulta; sem ano, só a data.
- **Obrigatório**: o registro é recusado se a pessoa não informar o ano.
- **Desativado**: mesmo que a pessoa tente informar um ano, ele é ignorado e descartado — só dia e mês são guardados.

### 3. Verificação automática a cada hora

De hora em hora (sempre na hora cheia), o bot percorre todos os servidores que têm a funcionalidade ativada. Para cada um:

1. Lê a configuração de fuso horário (padrão: `America/Sao_Paulo`, horário de Brasília) e o horário de parabéns (padrão: **9h**).
2. Calcula a **hora local** naquele fuso. Se a hora local não for exatamente o horário de parabéns configurado, o servidor é pulado nessa rodada — os parabéns só saem quando a hora bate.
3. Quando a hora bate, busca quem faz aniversário **naquele dia e mês**.

Como a verificação roda de hora em hora mas só age quando a hora local é a configurada, os anúncios saem **uma vez por dia**, no horário que você escolheu, respeitando o fuso do seu público.

### 4. Anúncio no canal

Para cada aniversariante do dia, o bot envia uma mensagem de parabéns no canal configurado. A mensagem pode ser:

- **Uma embed personalizada** que você monta no painel, com estes marcadores preenchidos automaticamente:
  - `{@user}` — menção (clica e leva ao perfil) do aniversariante
  - `{user}` — nome do aniversariante
  - `{user.tag}` — tag completa do usuário
  - `{age}` — idade que a pessoa está completando (só aparece se o ano foi registrado)
  - `{guild}` — nome do servidor
- **Ou um modelo padrão festivo** ("🎂 Feliz Aniversário!"), usado quando nenhuma embed foi configurada. Se houver ano registrado, ele inclui a idade automaticamente.

### 5. Cargo de aniversariante (opcional)

Se você definir um cargo:

- Ele é **atribuído** a cada aniversariante do dia, logo após o anúncio.
- Os aniversariantes **do dia anterior** têm esse mesmo cargo **removido** automaticamente na mesma rodada.

O efeito prático: a pessoa fica destacada com o cargo **apenas durante o seu dia**, e o cargo "circula" sozinho de um aniversariante para o próximo sem intervenção manual.

### 6. Sem mensagens duplicadas

O bot **marca o dia como já processado** por servidor. Mesmo que a verificação de hora em hora rode várias vezes, os parabéns daquele dia saem uma única vez. Essa marca vale por 24 horas e é registrada até nos dias sem nenhum aniversariante, para não reprocessar à toa.

### Consultas a qualquer momento

Independente do anúncio automático, qualquer membro pode consultar:

- **`/aniversario ver`** — mostra a data de aniversário (e a idade, quando o ano foi informado) de si mesmo ou de outro membro. A idade é calculada com precisão, considerando se a pessoa já fez aniversário neste ano ou não.
- **`/aniversario proximos`** — lista os **10 próximos** aniversários do servidor, ordenados de quem está mais perto para quem está mais longe. A contagem "dá a volta no ano": em dezembro, aniversários de janeiro aparecem corretamente como próximos. Quem faz aniversário hoje aparece marcado como **"Hoje! 🎉"**.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/aniversario registrar` | Membro registra o próprio aniversário (dia, mês e, conforme a política, ano). Só pode registrar uma vez. |
| `/aniversario ver` | Mostra o aniversário (e idade, se houver ano) de si mesmo ou de outro membro informado em `usuario`. |
| `/aniversario proximos` | Lista os 10 próximos aniversários do servidor, em ordem de proximidade. |
| `/aniversario-admin definir-usuario` | **(Admin)** Define ou corrige o aniversário de um membro, informando dia, mês e ano opcional. Funciona mesmo se a pessoa já tinha registrado. |
| `/aniversario-admin remover-usuario` | **(Admin)** Remove o aniversário registrado de um membro. |

Os comandos `/aniversario-admin` exigem permissão de **Administrador** no servidor.

## Configuração

A configuração é feita pelo **[Dashboard](https://admin.delfus.app)**, em **Eventos → Aniversários**.

Passo a passo:

1. **Ative a funcionalidade** no botão de liga/desliga (vem desativada por padrão). Enquanto estiver desativada, nenhum anúncio é enviado.
2. **Canal de Anúncios** — selecione o canal de texto onde os parabéns serão postados. Sem canal definido, o anúncio não acontece.
3. **Fuso Horário** — escolha o fuso do seu público (padrão `America/Sao_Paulo`). É ele que define quando "é o dia" do aniversário e quando dispara o horário de envio.
4. **Horário de Envio** — escolha a hora cheia (de 00:00 a 23:00) em que os parabéns saem. Padrão: **09:00**.
5. **Cargo de Aniversariante (opcional)** — escolha um cargo que será atribuído no dia e removido no dia seguinte. Deixe em "Nenhum" para não usar cargo. Cargos gerenciados por integrações não aparecem na lista.
6. **Ano de Nascimento** — defina a política: **Opcional**, **Obrigatório** ou **Desativado**.
7. **Embed de Anúncio** — na aba "Anúncio de Aniversário", monte a mensagem de parabéns no editor visual. Marcadores disponíveis: `{@user}`, `{user}`, `{user.tag}`, `{age}`, `{guild}`.
8. **Embed de Próximos Aniversários** — na aba "Próximos Aniversários", personalize o template do comando `/aniversario proximos`. Marcadores: `{list}`, `{guild}`, `{count}`.
9. Clique em **Salvar**.

Você pode editar a data de um membro específico tanto pelo painel quanto pelo comando `/aniversario-admin definir-usuario` dentro do Discord.

## Exemplos de uso

- **Comunidade que quer celebrar todo mundo, sem expor idade.** Defina "Ano de Nascimento" como **Desativado**, escolha um canal de avisos e um horário às 09:00. Os membros registram só dia e mês, e os parabéns saem sem mencionar idade.

- **Servidor com público internacional.** Ajuste o **Fuso Horário** para o do seu público principal (por exemplo, `Europe/Lisbon`) e o horário para uma hora em que a maioria está online, como 18:00. Assim os parabéns aparecem no momento certo para quem está no servidor.

- **Destacar visualmente o aniversariante do dia.** Crie um cargo chamado "🎉 Aniversariante", coloque-o acima na lista de cargos para ele ganhar cor/destaque, e selecione-o em "Cargo de Aniversariante". No dia, o bot dá o cargo automaticamente e o remove no dia seguinte — sem trabalho manual.

## Requisitos

- A funcionalidade precisa estar **ativada** e ter um **canal definido** no painel — sem isso, nenhum anúncio é enviado.
- O bot precisa de permissão para **enviar mensagens** e **inserir links/embeds** no canal de anúncios.
- Para usar o cargo de aniversariante, o bot precisa da permissão **Gerenciar Cargos**, e o **cargo do bot deve estar acima** do cargo de aniversariante na hierarquia de cargos — caso contrário, ele não consegue atribuir nem remover o cargo.

## Perguntas frequentes

**Por que os parabéns não saíram?**
Verifique se a funcionalidade está ativada, se há um canal definido e se o bot consegue enviar mensagens nele. Lembre que o anúncio respeita o **fuso horário** e o **horário** configurados — ele só dispara quando a hora local bate com o horário escolhido.

**Registrei a data errada, como corrigir?**
Membros não conseguem alterar o próprio registro depois de gravado. Peça a um administrador para usar `/aniversario-admin definir-usuario` (corrige) ou `/aniversario-admin remover-usuario` (apaga, permitindo registrar de novo).

**A idade vai aparecer nos parabéns?**
Só se o ano de nascimento estiver registrado. Se a política for "Desativado", o ano nunca é guardado e a idade nunca aparece. Se for "Opcional", aparece apenas para quem informou o ano.

**Posso ter aniversários diferentes em servidores diferentes?**
Sim. O registro é por servidor, então cada comunidade mantém sua própria lista de aniversários de forma independente.

!!! tip "Dica"
    Use a política **Opcional** ou **Obrigatório** para o ano de nascimento e inclua o marcador `{age}` na embed de anúncio: assim os parabéns mostram automaticamente quantos anos a pessoa está completando, deixando a mensagem muito mais pessoal.

