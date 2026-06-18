# Download de vídeos

O Delfus baixa automaticamente os vídeos de links postados em canais que você escolher e reenvia o arquivo direto no chat como anexo `.mp4`, sem que ninguém precise sair do Discord para abrir o link. Funciona com YouTube, TikTok, Instagram, Twitter/X, Reddit e Twitch, e ainda comprime o vídeo sozinho quando ele é grande demais para o limite do Discord. Para o dono do servidor, é uma forma de manter a conversa fluida: o conteúdo aparece pronto para assistir, sem cliques externos e sem prévias quebradas.

## Como funciona

Depois que você ativa o recurso em um canal específico (veja [Configuração](#configuracao)), o bot passa a observar todas as mensagens postadas **naquele canal**. O fluxo real, do link até o vídeo no chat, é este:

1. **Um membro posta uma mensagem com um link de vídeo** de uma plataforma suportada no canal monitorado.
2. **O bot detecta o link automaticamente.** Ele lê o conteúdo da mensagem e procura por endereços de vídeo conhecidos. Mensagens de **outros bots são ignoradas**. Se a mensagem chegar "vazia" para o bot (acontece com mensagens muito recentes ou editadas), ele busca o conteúdo completo antes de prosseguir.
3. **Apenas o primeiro link é processado.** Se houver vários links de vídeo na mesma mensagem, o bot baixa só o primeiro, para evitar floodar o canal com vários anexos de uma vez. Links repetidos são contados uma única vez.
4. **O bot mostra o indicador de "digitando…"** no canal enquanto trabalha, sinalizando que algo está sendo preparado.
5. **O vídeo é baixado nos bastidores.** O bot tenta pegar a melhor versão que caiba no limite do Discord, dando preferência a arquivos menores e a uma resolução de até 720p quando possível.
6. **Se o arquivo for grande demais, o bot comprime automaticamente** (detalhes em [Compressão automática](#compressao-automatica)) até caber no limite de envio.
7. **O vídeo é enviado como _resposta_ (reply) à mensagem original**, em formato `.mp4`, anexado direto no canal. A resposta **não menciona** (não dá ping) em quem postou o link.
8. **O arquivo temporário é apagado** do servidor logo depois de ser enviado. Nada fica armazenado.

### Plataformas e tipos de link suportados

O bot reconhece links destes serviços:

| Plataforma | Tipos de link reconhecidos |
| --- | --- |
| **YouTube** | Vídeos (`youtube.com/watch`), Shorts (`youtube.com/shorts`) e links curtos `youtu.be` |
| **TikTok** | Vídeos de perfil (`tiktok.com/@usuario/video/...`) e links curtos `vm.tiktok.com` |
| **Instagram** | Posts, Reels (`instagram.com/p/`, `/reel/`, `/reels/`) |
| **Twitter/X** | Tweets com vídeo (`twitter.com/.../status/...` e `x.com/.../status/...`) |
| **Reddit** | Posts de vídeo (`reddit.com/r/.../comments/...`) e links curtos `redd.it` |
| **Twitch** | **Clipes** (`twitch.tv/.../clip/...` e `clips.twitch.tv/...`) |

Links que não baterem com esses formatos (por exemplo, a página de um canal, uma playlist ou uma transmissão ao vivo inteira do Twitch) são simplesmente ignorados.

### Controle de spam (limite por usuário)

Para evitar abuso e fila de downloads, cada membro só pode disparar **um novo download a cada 10 segundos** no canal. Se alguém postar vários links em sequência rápida, os posts dentro dessa janela são ignorados **em silêncio** — o bot não responde nem avisa. Além disso, o próprio comando de configuração tem um pequeno intervalo entre usos.

### Compressão automática

O Discord limita o tamanho dos anexos. O bot trata esse limite como **8 MB** (margem de segurança que funciona até em servidores sem Nitro). Quando o vídeo baixado passa desse tamanho:

1. O bot recomprime o vídeo nos bastidores, mostrando de novo o "digitando…".
2. A resolução é reduzida para **no máximo 720p**, mantendo a proporção original.
3. O bitrate é ajustado de acordo com a duração do vídeo, mirando um arquivo final de cerca de **7,5 MB**, com um piso de qualidade para o vídeo não ficar irreconhecível.
4. Se, mesmo após a compressão, o arquivo **ainda não couber** no limite (vídeos muito longos), o bot desiste e **não envia nada**.

### Quando o bot não responde (falhas silenciosas)

Esta feature foi feita para **nunca poluir o canal com mensagens de erro**. Se algo der errado, o bot simplesmente não responde. Isso acontece quando:

- O vídeo é **privado, indisponível ou foi removido**.
- O link **exige login** para ser assistido.
- O vídeo tem **restrição de idade**.
- O conteúdo está **bloqueado por direitos autorais**.
- O YouTube aplicou um **limite temporário de requisições** (acontece em rajadas de downloads).
- O vídeo é **longo demais** para comprimir e caber no limite.
- O download **demora demais** (há um tempo-limite de cerca de 2 minutos para baixar e de até 5 minutos para comprimir).

Nesses casos, a mensagem original com o link continua no canal normalmente; apenas o anexo não é gerado.

### O que acontece após reiniciar o bot

A lista de canais com download ativo fica **salva na configuração do servidor**. Quando o bot reinicia ou recarrega as configurações, ele recarrega essa lista automaticamente — você **não precisa** reativar nada.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/video-download canal:<#canal>` | Liga ou desliga (toggle) o download automático de vídeos no canal informado. Se o canal já estiver ativo, rodar o comando **desativa**; se estiver inativo, **ativa**. |

O parâmetro `canal` tem **autocompletar**: ao começar a digitar, o Discord sugere os canais de texto do servidor.

## Configuração

Este recurso é configurado **dentro do próprio Discord, por comando** — não há ajuste para ele no painel web.

1. Em qualquer canal onde você tenha permissão de usar comandos, execute `/video-download`.
2. No parâmetro **`canal`**, escolha (ou comece a digitar para autocompletar) o canal de texto onde quer ativar o download automático.
3. Envie o comando:
   - Se o canal **ainda não estava ativo**, o bot confirma com **"📹 Download de Vídeos Ativado"** e passa a monitorar aquele canal.
   - Se o canal **já estava ativo**, o mesmo comando **desativa** o recurso ali e o bot confirma com **"⏹️ Download de Vídeos Desativado"**.
4. Se o canal informado não existir ou o bot não tiver acesso a ele, você recebe um aviso de **"❌ Canal Inválido"** e nada é alterado.

Você pode ativar o recurso em **vários canais ao mesmo tempo** — basta rodar o comando uma vez para cada canal. A configuração é por servidor e persiste entre reinícios do bot.

Não há outros campos, toggles ou opções de qualidade para esta feature: o comportamento (plataformas suportadas, limite de 8 MB, compressão até 720p, cooldown de 10s por usuário) é fixo.

## Exemplos de uso

- **Canal dedicado a "colar links":** crie um canal chamado, por exemplo, `#links-virais` e rode `/video-download canal:#links-virais`. A partir daí, qualquer link de TikTok, Reels ou Shorts colado lá vira um vídeo assistível direto no chat, sem ninguém precisar sair do Discord.
- **Canal de memes/clipes:** ative o recurso em `#clipes` para que clipes do Twitch e vídeos do Reddit postados pela comunidade apareçam já reproduzíveis, evitando prévias quebradas ou links que exigem abrir o navegador.
- **Desativar quando virar bagunça:** se um canal ficar cheio de downloads indesejados, rode `/video-download` de novo apontando para o mesmo canal — isso desliga o recurso ali na hora, sem afetar os outros canais ativos.

## Requisitos

- **Quem pode configurar:** apenas membros com permissão de **Administrador** podem usar `/video-download`.
- **Permissões do bot no canal monitorado:** o bot precisa de **Ver canal**, **Enviar mensagens** e **Anexar arquivos** para conseguir responder com o vídeo. Sem **Anexar arquivos**, ele não consegue postar o `.mp4`.
- **Contexto de servidor:** o comando só funciona dentro de um servidor (não em mensagens diretas).

## Perguntas frequentes

**O bot baixa qualquer vídeo da internet?**
Não. Ele só reconhece links de YouTube, TikTok, Instagram, Twitter/X, Reddit e Twitch, e nos formatos específicos de cada plataforma (clipes no caso do Twitch). Outros links são ignorados.

**Postei um link e o bot não respondeu. O que houve?**
Provavelmente o vídeo é privado, foi removido, exige login, tem restrição de idade, está bloqueado por direitos autorais, é longo demais para caber no limite, ou você acabou de postar outro link nos últimos 10 segundos. Nesses casos o bot ignora em silêncio, sem mensagem de erro.

**A qualidade do vídeo é a original?**
Quando o vídeo já cabe no limite do Discord (até 8 MB), ele é enviado como veio. Quando é maior, o bot comprime para caber, reduzindo a resolução para no máximo 720p — então pode haver perda de qualidade em vídeos grandes ou longos.

**Posso ativar em mais de um canal?**
Sim. Rode `/video-download` uma vez para cada canal desejado. Cada um funciona de forma independente, e a configuração continua valendo após o bot reiniciar.

!!! tip "Dica"
    Dedique um canal específico para "colar links de vídeo" e ative o recurso só nele. Assim os membros sabem exatamente onde os links viram vídeos automaticamente, e a conversa nos outros canais não fica cheia de anexos. Se um canal sair de controle, é só rodar `/video-download` de novo no mesmo canal para desligar na hora.
