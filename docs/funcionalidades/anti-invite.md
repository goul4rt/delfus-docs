# Anti-invite

Bloqueia quem entra no servidor só pra postar `discord.gg` e roubar seus membros. O Anti-invite apaga a mensagem na hora e pune o autor, sem você precisar vigiar o chat.

Ele distingue os seus convites dos de fora. Links criados dentro do seu servidor e sua URL personalizada passam normalmente. Qualquer link apontando pra outro lugar é barrado.

![Configuração do anti-invite no painel do Delfus](../assets/dashboard/anti-invite.png){ .dx-shot loading=lazy }

*Configuração do anti-invite no [Dashboard](https://admin.delfus.app) (exemplo com dados de demonstração).*

## Como funciona

O bot monitora as mensagens dos membros (ignora as de outros bots). A cada envio, faz uma checagem rápida: tem link de convite? É do seu servidor ou de fora?

- Convite **do seu servidor**: passa (comportamento padrão).
- Convite **de fora**: a mensagem some e a punição configurada entra em ação.

Tudo em tempo real, no instante do envio. Sem fila nem espera.

Você não precisa dizer ao bot quais convites são seus. Ele monta a lista sozinho na inicialização e atualiza sempre que um convite é criado ou expira. Um link recém-feito por um membro legítimo já vale como interno na hora.

!!! example "Exemplo"
    Um usuário entra e posta no chat geral: "vem pro meu server, melhor que esse aqui: discord.gg/outroserver".

    O Delfus apaga a mensagem na hora, manda um aviso marcando o autor (que some em ~8 segundos pra não poluir o canal), registra no seu canal de logs e aplica a punição configurada, digamos 10 minutos de silêncio.

Na violação, o bot faz quatro coisas independentes. Se uma falhar, as outras seguem:

1. **Apaga a mensagem** com o convite.
2. **Avisa no canal** (opcional, ligado por padrão) marcando o autor. O aviso some sozinho em ~8 segundos.
3. **Registra um log** no canal que você escolher, com embed detalhado: quem foi, em qual canal, a ação aplicada e os códigos detectados.
4. **Pune o membro** conforme você configurou: nada, advertência, silêncio temporário, expulsão ou banimento.

## Comandos

Não há comando de barra. O Anti-invite roda 100% automático e todos os ajustes ficam no painel.

## Configuração

Configure pelo painel em [admin.delfus.app](https://admin.delfus.app), na seção **Anti-invite**. As opções principais:

- **Ativar/desativar:** liga ou desliga o módulo. Vem desligado por padrão.
- **Permitir convites do próprio servidor:** ligado por padrão, libera seus links e a URL personalizada. Desligue pra bloquear **qualquer** convite, inclusive os seus.
- **Canais liberados:** canais onde o módulo nunca atua. Útil pra áreas de divulgação ou parcerias.
- **Cargos liberados:** membros com qualquer um desses cargos ficam isentos. Bom pra equipe e parceiros oficiais.
- **Ação na violação:** o que fazer com quem manda convite proibido: `none` (só apaga), `warn`, `mute`, `kick` ou `ban`.
- **Duração do silêncio:** em segundos, quando a ação é `mute`. De 1 segundo até 28 dias (limite do Discord). Sem definir, o padrão é 10 minutos.
- **Motivo:** texto livre (até 500 caracteres) usado na punição e no aviso.
- **Avisar no canal:** liga/desliga o aviso público ao autor. Ligado por padrão.
- **Texto do aviso:** mensagem personalizada (até 2.000 caracteres). Em branco, usa um texto padrão.
- **Canal de logs:** onde cada remoção fica registrada. Opcional.

!!! note "Aplica na hora"
    Depois de salvar, a configuração vai pro bot automaticamente. Não precisa reiniciar nada.

!!! warning "Permissões"
    O bot precisa de **Gerenciar Mensagens** (apagar), **Gerenciar Servidor** (reconhecer os convites internos), **Enviar Mensagens** (avisos e logs) e a permissão da punição escolhida (**Moderar Membros**, **Expulsar** ou **Banir**).

    O cargo do bot precisa estar **acima** do cargo de quem ele vai punir. Senão o Discord recusa o mute/kick/ban.

## Exemplos

!!! example "Bloquear concorrentes, mas liberar seus próprios links"
    Ative o módulo, mantenha "permitir convites do próprio servidor" **ligado** e escolha `mute` com 600 segundos.

    Resultado: seus membros compartilham links do seu servidor à vontade, mas qualquer `discord.gg` de fora é apagado e o autor fica 10 minutos de castigo.

!!! example "Tolerância zero, exceto num canal"
    Ative o módulo, **desligue** "permitir convites do próprio servidor" e adicione o canal de parcerias aos canais liberados.

    Agora nenhum convite passa em lugar nenhum, só naquele canal onde a equipe divulga.

!!! example "Moderação suave, só pra acompanhar"
    Use a ação `none`, mantenha o aviso ligado com um texto educado e configure um canal de logs.

    O bot apaga os convites externos, avisa o autor de forma amigável e guarda o histórico pra equipe, sem punir ninguém.

## Perguntas frequentes

**Os convites do meu próprio servidor são apagados?**
Não, desde que "permitir convites do próprio servidor" esteja ligado (o padrão). O bot reconhece seus links e sua URL personalizada como internos. Se desligar, tudo é removido, inclusive os seus.

**A equipe de moderação também é afetada?**
Não, se você colocar os cargos da equipe nos **cargos liberados**. Quem tem um cargo liberado é ignorado pelo Anti-invite. O mesmo vale pra canais inteiros, via **canais liberados**.

**Por que o aviso no canal some sozinho?**
É de propósito. O aviso marcando o autor some em ~8 segundos pra não acumular mensagens de moderação no chat. Pra registro permanente, use um **canal de logs**.

**O bot pega convites com `https://`, `www` ou em maiúsculas?**
Pega tudo. Reconhece `discord.gg`, `discord.com/invite` e `discordapp.com/invite`, com ou sem `https://` e `www.`, sem ligar pra maiúsculas ou minúsculas.

!!! tip "Dica"
    Combine as duas listas: **cargos liberados** pra equipe e parceiros oficiais, **canais liberados** pra áreas de divulgação. Você bloqueia convites externos no servidor inteiro sem atrapalhar quem precisa compartilhar links.
