# Automações de canal

Sabe aquele canal que vive saindo dos trilhos? Onde era pra ter só prints, mas todo mundo fica de bate-papo? As automações de canal resolvem isso pra você.

Você define a regra uma vez — "aqui só entra imagem", "aqui é só comando" — e o Delfus cuida do resto, em tempo real, sem precisar de moderador online. Ele também sabe abrir um tópico de discussão pra cada post ou publicar seus anúncios automaticamente. E tudo fica registrado pra você acompanhar pelo painel.

## Como funciona

Cada canal pode ter uma ou mais automações. Toda vez que alguém manda uma mensagem ali, o Delfus confere as regras e age na hora. Canal sem automação? Nada muda — as regras só valem onde você liga.

Algumas coisas o bot **sempre ignora**, não importa a configuração: mensagens de sistema do Discord, mensagens de webhooks e as próprias mensagens dele (assim ele nunca se autoapaga).

E você ainda escolhe quem passa livre:

- **Ignorar bots** — outros bots não são afetados pela regra (vem ligado por padrão).
- **Cargos liberados** — quem tiver um dos cargos da lista passa batido. Perfeito pra sua equipe postar à vontade.

!!! example "Exemplo"
    Você cria a regra "só imagens" no canal de memes. Alguém manda um textão sem nenhuma foto — o Delfus apaga na hora, deixa um avisinho rápido e ainda já reage com 👍 e 👎 no próximo print pra abrir a votação.

### Quando o canal tem várias regras

Se você empilhar mais de uma automação no mesmo canal, o Delfus roda por **ordem de prioridade** — número menor primeiro. E assim que uma regra **apaga** a mensagem, as seguintes nem chegam a rodar (afinal, a mensagem já não existe). Regras que não apagam — reagir, criar tópico, publicar — não interrompem a fila. Com uma regra só, esquece a prioridade: deixa em 0.

### Os avisinhos temporários

Quando o bot apaga uma mensagem, ele manda um aviso curto explicando o porquê e **some com ele sozinho uns 8 segundos depois**, pra não poluir o canal. Dois cuidados importantes:

- Esses avisos **nunca dão ping** em @everyone, @here, cargos ou pessoas — mesmo que seu texto tenha menções, elas são neutralizadas.
- Se o mesmo membro manda mensagem atrás de mensagem, os avisos são limitados a um a cada 10 segundos por pessoa (pro bot não virar spam). Mas calma: **a remoção acontece em todas as vezes** — só o textinho de aviso é segurado.

!!! note "E a privacidade?"
    Cada ação do bot fica registrada (apagou, avisou, criou tópico, publicou) — mas o registro guarda só identificadores e o motivo, **nunca o conteúdo da mensagem**. É isso que alimenta as estatísticas do painel.

### Os cinco tipos de automação

Pensa neles como cinco "modos" de canal:

- **Somente mídia** — o canal aceita só imagens, GIFs, vídeos e/ou figurinhas (você escolhe quais). Pode exigir um tamanho mínimo de imagem pra barrar emojizinho salvo, bloquear legendas e ainda reagir automaticamente com emojis. O resto é apagado.
- **Somente comandos** — passa só comando de barra (slash) ou mensagem que começa com os prefixos que você definir (`/`, `!`, `?`...). Conversa solta é removida, com um aviso que pode até linkar o canal de bate-papo certo.
- **Somente arquivos** — só entram anexos válidos: extensão permitida (ex.: `.pdf`, `.zip`) e tamanho dentro do intervalo que você definir. Sem arquivo válido, é apagado.
- **Tópico automático** — pra cada post novo, o bot abre um tópico atrelado a ele. O nome sai de um modelo seu, com as etiquetas `{author}` (quem postou) e `{date}` (data de hoje). Você escolhe quando ele arquiva sozinho.
- **Publicação automática** — em canais de anúncio, o bot publica suas mensagens automaticamente pra todo mundo que segue o canal, sem ninguém clicar em "Publicar". Antes, passa pelos filtros que você definir (cargo, conteúdo rico, tamanho mínimo de texto).

!!! warning "A publicação automática só vale em canais de anúncio"
    Em canal de texto normal, esse tipo é simplesmente ignorado. Se quiser usá-lo, o canal precisa ser do tipo anúncio.

## Comandos

Esta funcionalidade é configurada só pelo painel — não tem comando no Discord.

## Configuração

Tudo acontece no Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção **Automações de canal**. Cada automação tem campos comuns e campos do tipo escolhido.

**Em toda automação você define:**

- **Canal** — onde a regra vale.
- **Tipo** — mídia, comandos, arquivos, tópico ou publicação.
- **Ativado** — liga e desliga sem precisar apagar.
- **Ignorar bots** — não aplica a regra a bots (padrão: ligado).
- **Cargos que ignoram a regra** — até 50 cargos livres da automação.
- **Prioridade** — de 0 a 100; menor roda primeiro. Só importa com mais de uma regra no mesmo canal.

**E os campos de cada tipo:**

| Tipo | Você ajusta |
| --- | --- |
| **Somente mídia** | Quais mídias entram, permitir legenda, tamanho mínimo de imagem (0–4096px), mensagem de aviso (até 500 caracteres) e até 10 emojis de reação (inclui os personalizados). |
| **Somente comandos** | Prefixos (1 a 10, padrão `/`), mensagem de redirecionamento e um canal de conversa opcional pra virar link no aviso. |
| **Somente arquivos** | Extensões permitidas (até 50; vazio = todas), tamanho mínimo e máximo em KB (máximo 0 = sem limite) e mensagem de aviso. |
| **Tópico automático** | Modelo do nome com `{author}` e `{date}` (padrão `{author} — {date}`) e quando arquivar: 1 hora, 1 dia, 3 dias ou 1 semana. |
| **Publicação automática** | Atraso antes de publicar (0–1440 min; 0 = na hora), filtro de cargos, exigir imagem/conteúdo rico e tamanho mínimo de texto. |

!!! note "Permissões"
    Pro Delfus agir, ele precisa das permissões certas no canal: **Gerenciar mensagens** pra apagar, **Enviar mensagens** pros avisos, **Adicionar reações** pras reações automáticas, **Criar tópicos públicos** pro tópico automático e **publicar em canal de anúncio** pra publicação. Pra reagir com emojis personalizados, o bot também precisa ter acesso a eles.

A página ainda tem uma aba de **estatísticas**, com os totais de mensagens apagadas, tópicos criados, publicações e avisos do servidor.

## Exemplos

!!! example "Canal de memes só com imagem e votação automática"
    Crie uma automação **Somente mídia**, deixe ligados Imagens, GIFs e Vídeos, ponha um tamanho mínimo (uns 100px) pra cortar miniatura e adicione as reações 👍 e 👎. Cada print já abre a votação sozinho — e textão solto some na hora.

!!! example "Canal de comandos do bot, sem bate-papo"
    Configure **Somente comandos** com o prefixo `/`, aponte o `#bate-papo` como redirecionamento e escreva um aviso simpático. Quem mandar conversa ali é gentilmente mandado pro canal certo. Quer que a staff escreva livre? Adicione o cargo dela às exceções.

!!! example "Canal de sugestões onde cada post vira discussão"
    Use **Tópico automático** com o modelo `{author} — {date}` e arquivamento de 3 dias. Toda sugestão ganha o próprio tópico, e a comunidade discute sem bagunçar o canal principal.

!!! example "Canal de anúncios que se espalha sozinho"
    Num canal de anúncio seguido por outros servidores, ligue **Publicação automática** exigindo conteúdo rico e limitando aos cargos da equipe. Cada anúncio oficial vai automaticamente pra todos os seguidores.

## Perguntas frequentes

**A regra apaga as mensagens da minha equipe também?**
Não, se você adicionar os cargos dela à lista de "cargos que ignoram a regra". Quem tiver um desses cargos passa livre. Bots já são ignorados por padrão.

**Posso ter mais de uma automação no mesmo canal?**
Pode. Elas rodam por prioridade (menor primeiro). Só lembre: quando uma regra apaga a mensagem, as seguintes não rodam. Então ajuste a ordem das regras de remoção com carinho.

**Por que meu aviso não menciona o cargo que coloquei nele?**
Por segurança. Os avisos automáticos nunca dão ping em @everyone, cargos ou pessoas, mesmo com a menção escrita no texto. Assim ninguém leva ping a cada mensagem removida.

**A publicação automática não funciona no meu canal. Por quê?**
Ela só vale em **canais de anúncio**. Confira também se a mensagem passou nos filtros (cargo, conteúdo rico, tamanho mínimo de texto) e se o bot tem permissão pra publicar ali.

!!! tip "Dica"
    Em canal de mídia bem movimentado, ligue o **tamanho mínimo de imagem** (uns 64–100px) no "Somente mídia". Isso barra emoji salvo e miniatura minúscula — que tecnicamente são "imagens" — e deixa o canal só com print e foto de verdade.
