# Automações de canal

Trave cada canal numa regra ("aqui só entra imagem", "aqui é só comando") e o Delfus aplica em tempo real, sem moderador online. Ele também abre um tópico de discussão por post e publica seus anúncios sozinho. Tudo fica registrado pra você acompanhar pelo painel.

## Como funciona

Cada canal pode ter uma ou mais automações. A cada mensagem, o Delfus confere as regras e age na hora. Canal sem automação não muda nada: as regras só valem onde você liga.

Algumas coisas o bot sempre ignora, não importa a configuração: mensagens de sistema do Discord, mensagens de webhooks e as próprias mensagens (assim ele nunca se autoapaga).

Você também escolhe quem passa livre:

- **Ignorar bots**: outros bots não são afetados pela regra (ligado por padrão).
- **Cargos liberados**: quem tiver um dos cargos da lista passa batido. Bom pra equipe postar à vontade.

!!! example "Exemplo"
    Você cria a regra "só imagens" no canal de memes. Alguém manda um textão sem foto. O Delfus apaga na hora, deixa um aviso rápido e já reage com 👍 e 👎 no próximo print pra abrir a votação.

### Quando o canal tem várias regras

Empilhou mais de uma automação no mesmo canal? O Delfus roda por ordem de prioridade, número menor primeiro. Assim que uma regra apaga a mensagem, as seguintes nem rodam (a mensagem já não existe). Regras que não apagam (reagir, criar tópico, publicar) não interrompem a fila. Com uma regra só, deixa a prioridade em 0.

### Os avisos temporários

Ao apagar uma mensagem, o bot manda um aviso curto com o motivo e some com ele sozinho uns 8 segundos depois, pra não poluir o canal. Dois cuidados:

- Os avisos nunca dão ping em @everyone, @here, cargos ou pessoas. Mesmo que o texto tenha menções, elas são neutralizadas.
- Se o mesmo membro manda mensagem atrás de mensagem, os avisos ficam limitados a um a cada 10 segundos por pessoa (pro bot não virar spam). A remoção acontece em todas as vezes; só o aviso é segurado.

!!! note "E a privacidade?"
    Cada ação do bot fica registrada (apagou, avisou, criou tópico, publicou), mas o registro guarda só identificadores e o motivo, nunca o conteúdo da mensagem. É isso que alimenta as estatísticas do painel.

### Os cinco tipos de automação

São cinco "modos" de canal:

- **Somente mídia**: aceita só imagens, GIFs, vídeos e/ou figurinhas (você escolhe quais). Pode exigir tamanho mínimo de imagem pra barrar emoji salvo, bloquear legendas e reagir automaticamente com emojis. O resto é apagado.
- **Somente comandos**: passa só comando de barra (slash) ou mensagem que começa com os prefixos que você definir (`/`, `!`, `?`...). Conversa solta é removida, com um aviso que pode linkar o canal de bate-papo certo.
- **Somente arquivos**: só entram anexos válidos, com extensão permitida (ex.: `.pdf`, `.zip`) e tamanho dentro do intervalo que você definir. Sem arquivo válido, é apagado.
- **Tópico automático**: a cada post novo, o bot abre um tópico atrelado a ele. O nome sai de um modelo seu, com as etiquetas `{author}` (quem postou) e `{date}` (data de hoje). Você escolhe quando ele arquiva sozinho.
- **Publicação automática**: em canais de anúncio, o bot publica suas mensagens pra todo mundo que segue o canal, sem ninguém clicar em "Publicar". Antes, passa pelos filtros que você definir (cargo, conteúdo rico, tamanho mínimo de texto).

!!! warning "A publicação automática só vale em canais de anúncio"
    Em canal de texto normal, esse tipo é ignorado. Pra usá-lo, o canal precisa ser do tipo anúncio.

## Comandos

Esta funcionalidade é configurada só pelo painel. Não tem comando no Discord.

## Configuração

Tudo acontece no Dashboard, em [admin.delfus.app](https://admin.delfus.app), na seção **Automações de canal**. Cada automação tem campos comuns e campos do tipo escolhido.

Em toda automação você define:

- **Canal**: onde a regra vale.
- **Tipo**: mídia, comandos, arquivos, tópico ou publicação.
- **Ativado**: liga e desliga sem precisar apagar.
- **Ignorar bots**: não aplica a regra a bots (padrão: ligado).
- **Cargos que ignoram a regra**: até 50 cargos livres da automação.
- **Prioridade**: de 0 a 100, menor roda primeiro. Só importa com mais de uma regra no mesmo canal.

E os campos de cada tipo:

| Tipo | Você ajusta |
| --- | --- |
| **Somente mídia** | Quais mídias entram, permitir legenda, tamanho mínimo de imagem (0–4096px), mensagem de aviso (até 500 caracteres) e até 10 emojis de reação (inclui os personalizados). |
| **Somente comandos** | Prefixos (1 a 10, padrão `/`), mensagem de redirecionamento e um canal de conversa opcional pra virar link no aviso. |
| **Somente arquivos** | Extensões permitidas (até 50; vazio = todas), tamanho mínimo e máximo em KB (máximo 0 = sem limite) e mensagem de aviso. |
| **Tópico automático** | Modelo do nome com `{author}` e `{date}` (padrão `{author} — {date}`) e quando arquivar: 1 hora, 1 dia, 3 dias ou 1 semana. |
| **Publicação automática** | Atraso antes de publicar (0–1440 min; 0 = na hora), filtro de cargos, exigir imagem/conteúdo rico e tamanho mínimo de texto. |

!!! note "Permissões"
    Pro Delfus agir, ele precisa das permissões certas no canal: **Gerenciar mensagens** pra apagar, **Enviar mensagens** pros avisos, **Adicionar reações** pras reações automáticas, **Criar tópicos públicos** pro tópico automático e **publicar em canal de anúncio** pra publicação. Pra reagir com emojis personalizados, o bot também precisa ter acesso a eles.

A página tem ainda uma aba de **estatísticas**, com os totais de mensagens apagadas, tópicos criados, publicações e avisos do servidor.

## Exemplos

!!! example "Canal de memes só com imagem e votação automática"
    Crie uma automação **Somente mídia**, deixe ligados Imagens, GIFs e Vídeos, ponha um tamanho mínimo (uns 100px) pra cortar miniatura e adicione as reações 👍 e 👎. Cada print já abre a votação sozinho, e textão solto some na hora.

!!! example "Canal de comandos do bot, sem bate-papo"
    Configure **Somente comandos** com o prefixo `/`, aponte o `#bate-papo` como redirecionamento e escreva um aviso simpático. Quem mandar conversa ali é mandado pro canal certo. Quer a staff escrevendo livre? Adicione o cargo dela às exceções.

!!! example "Canal de sugestões onde cada post vira discussão"
    Use **Tópico automático** com o modelo `{author} — {date}` e arquivamento de 3 dias. Toda sugestão ganha o próprio tópico, e a comunidade discute sem bagunçar o canal principal.

!!! example "Canal de anúncios que se espalha sozinho"
    Num canal de anúncio seguido por outros servidores, ligue **Publicação automática** exigindo conteúdo rico e limitando aos cargos da equipe. Cada anúncio oficial vai automaticamente pra todos os seguidores.

## Perguntas frequentes

**A regra apaga as mensagens da minha equipe também?**
Não, se você adicionar os cargos dela à lista de "cargos que ignoram a regra". Quem tiver um desses cargos passa livre. Bots já são ignorados por padrão.

**Posso ter mais de uma automação no mesmo canal?**
Pode. Elas rodam por prioridade (menor primeiro). Lembre: quando uma regra apaga a mensagem, as seguintes não rodam. Ajuste a ordem das regras de remoção com cuidado.

**Por que meu aviso não menciona o cargo que coloquei nele?**
Por segurança. Os avisos automáticos nunca dão ping em @everyone, cargos ou pessoas, mesmo com a menção escrita no texto. Assim ninguém leva ping a cada mensagem removida.

**A publicação automática não funciona no meu canal. Por quê?**
Ela só vale em canais de anúncio. Confira também se a mensagem passou nos filtros (cargo, conteúdo rico, tamanho mínimo de texto) e se o bot tem permissão pra publicar ali.

!!! tip "Dica"
    Em canal de mídia movimentado, ligue o **tamanho mínimo de imagem** (uns 64–100px) no "Somente mídia". Isso barra emoji salvo e miniatura minúscula, que tecnicamente são "imagens", e deixa o canal só com print e foto de verdade.

