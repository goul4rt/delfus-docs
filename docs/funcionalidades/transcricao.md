---
description: "Transcrição de áudio do Delfus no Discord: mensagens de voz viram texto no canal, com quem falou, duração e páginas para áudios longos."
---

# Transcrição de áudio

Alguém manda uma mensagem de voz e o Delfus responde ali mesmo com o que foi dito. Quem está no ônibus, sem fone, ou simplesmente não pode ouvir, lê. Você escolhe em quais canais e para quais cargos isso vale.

## Como funciona

O Delfus só olha para **mensagens de voz gravadas no Discord** (aquelas do botão de microfone). Áudio anexado como arquivo não conta, nem vídeo, nem link.

Quando uma chega num canal onde o recurso está ligado, ele mostra o "digitando…", transcreve e responde à mensagem original com um cartão contendo:

- **Quem falou e quanto durou**, no topo: "Áudio de Lua · 48s", com o avatar da pessoa.
- **O texto transcrito**.
- Um rodapé lembrando que é transcrição automática e pode conter erros.

A resposta não dá ping em ninguém.

!!! example "Exemplo"
    No `#combinados`, alguém manda 48 segundos de áudio explicando o evento de sábado. Logo abaixo aparece o cartão com o texto inteiro, e quem está no trabalho lê sem precisar dar play.

### Áudios longos viram páginas

Transcrição comprida não vira um paredão de texto. O Delfus quebra em páginas de mais ou menos 3.500 caracteres, cortando no fim de uma frase, e coloca os botões **Anterior** e **Próxima** embaixo do cartão. O rodapé mostra em qual página você está.

Qualquer pessoa do canal pode virar as páginas, como qualquer outra leitura pública. O texto completo fica guardado por 24 horas; depois disso os botões somem e a página que estava aberta continua visível.

## Configuração

Tudo pelo painel, em [Transcrição de áudio](https://admin.delfus.app/dashboard/transcricao). Não há comando no Discord.

1. Ligue a chave **Transcrição automática**.
2. Escolha **em quais canais** vale:
    - *Só nestes canais*: apenas os que você marcar transcrevem. Lista vazia significa nenhum canal, e o painel avisa.
    - *Em todos, exceto*: transcreve no servidor inteiro, menos os marcados.
3. Escolha **para quais cargos** vale, com a mesma lógica. Deixe em "para todos, exceto" com a lista vazia para liberar todo mundo.
4. Opcional: escolha um **canal de log**.

!!! note "Quem pode configurar"
    Quem tem acesso ao painel do servidor. O bot precisa conseguir ver o canal e enviar mensagens ali; sem isso, a transcrição não aparece.

### Log de áudios transcritos

Se você escolher um canal de log, cada transcrição também é publicada lá, com um botão **Ir para a mensagem** que leva à conversa original. Serve para moderação acompanhar o que foi dito em áudio sem precisar entrar em cada canal.

É o mesmo campo que aparece em [Logs de Ação](https://admin.delfus.app/dashboard/action-log/config): mudou num lugar, muda no outro. As páginas funcionam na cópia igual funcionam na resposta original.

## Limites

| Limite | Valor |
| --- | --- |
| Duração máxima do áudio | 3 minutos |
| Tamanho máximo do arquivo | 8 MB |
| Cota diária no plano grátis | 5 minutos de áudio por servidor |
| Cota diária no premium | 60 minutos de áudio por servidor |

A cota conta a duração dos áudios transcritos e zera à meia-noite UTC (21h em Brasília). O painel mostra quanto do dia já foi usado e quantos áudios foram transcritos.

!!! warning "Quando o bot reage em vez de responder"
    O Delfus nunca enche o canal com mensagem de erro. Em vez disso, ele reage à mensagem de voz:

    - ⏳ significa que o áudio passou de 3 minutos, de 8 MB, ou que a cota do dia acabou.
    - ⚠️ significa que a transcrição falhou (problema na conversão ou no serviço de fala).

    Nos dois casos o áudio continua lá, intacto, e nada é apagado.

## Privacidade

O áudio é enviado a um serviço de reconhecimento de fala só para virar texto, e não fica guardado depois disso. O que persiste é o texto da transcrição na mensagem publicada no canal (e no canal de log, se houver) — visível para quem já podia ler aquele canal.

Se o servidor não quer isso em determinados espaços, use a lista de canais para deixá-los de fora, ou restrinja por cargo.

## Perguntas frequentes

### O bot transcreve qualquer áudio postado?
Não. Só mensagens de voz gravadas pelo próprio Discord. Um `.mp3` anexado, um vídeo ou um link não são transcritos.

### Mandei um áudio e o bot não respondeu. O que houve?
Confira se o canal (e o seu cargo) estão nas listas certas e se a transcrição está ligada. Se aparecer ⏳ na mensagem, o áudio passou dos limites ou a cota diária acabou; se aparecer ⚠️, a transcrição falhou.

### A transcrição é sempre correta?
Não. É automática e erra, principalmente com ruído de fundo, várias pessoas falando ao mesmo tempo, gírias e nomes próprios. Por isso o rodapé avisa. Trate como apoio, não como registro literal.

### Dá para transcrever só num canal?
Dá. Escolha "só nestes canais" e marque apenas ele. É a configuração mais comum: um canal de recados por voz onde todo áudio vira texto, e o resto do servidor fica de fora.

### E se o áudio for muito longo?
Até 3 minutos ele transcreve normalmente; se o texto ficar grande, vira páginas. Acima disso, ele reage com ⏳ e não transcreve.

!!! tip "Dica"
    Combine com o canal de log: os membros leem a transcrição no canal onde o áudio foi mandado, e a equipe acompanha tudo num canal só, com link para cada conversa.

Veja também: [Automações de canal](automacoes.md), [Mensagens e embeds](mensagens.md), [Moderação](moderacao.md).
