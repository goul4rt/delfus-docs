# Download de vídeos

Sabe aquele link de TikTok ou Reels que cai no chat e ninguém clica? O Delfus resolve isso: ele baixa o vídeo sozinho e reenvia o arquivo `.mp4` direto no canal, prontinho pra assistir sem sair do Discord. Funciona com YouTube, TikTok, Instagram, Twitter/X, Reddit e Twitch — e ainda comprime o vídeo quando ele é grande demais.

## Como funciona

Você ativa o recurso em um canal e pronto: o Delfus passa a ficar de olho nas mensagens dali. Quando alguém posta um link de vídeo, ele baixa nos bastidores e responde com o arquivo anexado, sem dar ping em ninguém. O link continua na conversa, agora com o vídeo logo abaixo.

Alguns detalhes que valem saber:

- Se a mensagem tiver vários links, o Delfus baixa **só o primeiro** — pra não inundar o canal de anexos.
- Enquanto trabalha, ele mostra o "digitando…" pra você saber que algo está vindo.
- O arquivo é **apagado logo após o envio**. Nada fica guardado.

!!! example "Exemplo"
    Alguém cola um Reel engraçado no `#memes`. Em segundos, o Delfus responde àquela mensagem com o vídeo em `.mp4` anexado — e a galera assiste sem precisar abrir o Instagram.

**Plataformas suportadas:** YouTube (vídeos, Shorts e `youtu.be`), TikTok, Instagram (posts e Reels), Twitter/X, Reddit e clipes da Twitch. Links que não sejam vídeo direto — como uma playlist, a página de um canal ou uma live inteira — são ignorados.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/video-download canal:<#canal>` | Liga ou desliga o download automático no canal escolhido. Rodar de novo no mesmo canal inverte o estado (liga/desliga). |

!!! tip "Atalho"
    O campo `canal` tem autocompletar: comece a digitar e o Discord sugere os canais do servidor.

## Configuração

Tudo é feito por comando, dentro do próprio Discord (não tem ajuste no painel web):

1. Rode `/video-download` em qualquer canal onde você possa usar comandos.
2. No campo **`canal`**, escolha onde quer ativar o download.
3. Envie:
    - Canal ainda inativo → o bot confirma com **"📹 Download de Vídeos Ativado"**.
    - Canal já ativo → o mesmo comando **desativa** e responde **"⏹️ Download de Vídeos Desativado"**.

Quer ativar em vários canais? É só repetir o comando pra cada um. A configuração vale por servidor e **continua valendo mesmo se o bot reiniciar** — você não precisa reativar nada.

!!! note "Quem pode configurar"
    Só **administradores** usam `/video-download`, e o bot precisa de permissão pra **ver o canal, enviar mensagens e anexar arquivos**. Sem "Anexar arquivos", ele não consegue postar o `.mp4`. O comando também só funciona dentro de um servidor, não em DM.

## Exemplos

!!! example "Um canal só pra colar links"
    Crie um `#links-virais` e rode `/video-download canal:#links-virais`. Daí em diante, todo TikTok, Reel ou Short colado ali vira vídeo assistível na hora — e os outros canais ficam livres de anexos.

!!! example "Canal de clipes e memes"
    Ative no `#clipes` e os clipes da Twitch e vídeos do Reddit que a comunidade postar aparecem já reproduzíveis, sem prévia quebrada nem link pra abrir no navegador.

!!! example "Desligar quando virar bagunça"
    Canal lotado de download indesejado? Rode `/video-download` de novo apontando pro mesmo canal. O recurso desliga ali na hora, sem mexer nos outros.

## Vídeos grandes e quando o bot fica quieto

O Discord limita o tamanho dos anexos, então o Delfus trabalha com um teto de **8 MB** (margem segura, funciona até sem Nitro). Se o vídeo passa disso, ele **comprime automaticamente**: reduz a resolução pra no máximo 720p, mira um arquivo de uns 7,5 MB e mantém a proporção original. Vídeos grandes ou longos podem perder um pouco de qualidade nesse processo.

!!! warning "Quando o Delfus simplesmente não responde"
    Essa feature foi feita pra **nunca poluir o canal com mensagens de erro**. Se algo dá errado, o bot só fica quieto — e o link original continua na conversa. Isso acontece quando o vídeo é privado, removido, exige login, tem restrição de idade ou bloqueio de direitos autorais; quando é longo demais pra caber mesmo após comprimir; ou quando o download demora demais. Também há um limite anti-spam: cada pessoa só dispara **um download a cada 10 segundos**.

## Perguntas frequentes

**O bot baixa qualquer vídeo da internet?**
Não. Só YouTube, TikTok, Instagram, Twitter/X, Reddit e clipes da Twitch, nos formatos de vídeo direto de cada plataforma. O resto ele ignora.

**Postei um link e o bot não respondeu. O que houve?**
Provavelmente o vídeo é privado, foi removido, exige login, tem restrição de idade, está bloqueado por direitos autorais, é longo demais pra caber no limite — ou você postou outro link nos últimos 10 segundos. Em todos esses casos ele ignora em silêncio, sem mensagem de erro.

**A qualidade é a original?**
Se o vídeo já cabe em 8 MB, vai como veio. Se é maior, o Delfus comprime pra caber (até 720p), então pode haver alguma perda em vídeos grandes ou longos.

**Posso ativar em mais de um canal?**
Pode. Rode `/video-download` uma vez pra cada canal. Cada um funciona de forma independente e a configuração sobrevive a reinícios do bot.

!!! tip "Dica"
    Dedique um canal só pra "colar links de vídeo" e ative o recurso apenas nele. Assim os membros sabem exatamente onde os links viram vídeos, e os outros canais não enchem de anexos. Se um deles sair de controle, é só rodar `/video-download` de novo no mesmo canal pra desligar na hora.
