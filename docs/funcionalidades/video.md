# Download de vídeos

Cola um link de TikTok, Reels ou YouTube no chat e o Delfus baixa o vídeo, reenviando o `.mp4` direto no canal. Funciona com YouTube, TikTok, Instagram, Twitter/X, Reddit e Twitch. Vídeo grande, ele comprime.

## Como funciona

Você ativa o recurso num canal e o Delfus passa a observar as mensagens dali. Quando alguém posta um link de vídeo, ele baixa nos bastidores e responde com o arquivo anexado, sem dar ping. O link continua na conversa, agora com o vídeo logo abaixo.

Detalhes que valem saber:

- Se a mensagem tem vários links, o Delfus baixa só o primeiro, pra não lotar o canal de anexos.
- Enquanto trabalha, ele mostra o "digitando…".
- O arquivo é apagado logo após o envio. Nada fica guardado.

!!! example "Exemplo"
    Alguém cola um Reel no `#memes`. Em segundos, o Delfus responde àquela mensagem com o vídeo em `.mp4` anexado, e a galera assiste sem abrir o Instagram.

Plataformas suportadas: YouTube (vídeos, Shorts e `youtu.be`), TikTok, Instagram (posts e Reels), Twitter/X, Reddit e clipes da Twitch. Links que não são vídeo direto (playlist, página de canal, live inteira) são ignorados.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/video-download canal:<#canal>` | Liga ou desliga o download automático no canal. Rodar de novo no mesmo canal inverte o estado. |

!!! tip "Atalho"
    O campo `canal` tem autocompletar: comece a digitar e o Discord sugere os canais do servidor.

## Configuração

Tudo é feito por comando, dentro do Discord. Não há ajuste no painel web.

1. Rode `/video-download` em qualquer canal onde você possa usar comandos.
2. No campo `canal`, escolha onde quer ativar.
3. Envie:
    - Canal inativo: o bot confirma com "📹 Download de Vídeos Ativado".
    - Canal já ativo: o mesmo comando desativa e responde "⏹️ Download de Vídeos Desativado".

Pra ativar em vários canais, repita o comando em cada um. A configuração vale por servidor e continua valendo mesmo se o bot reiniciar. Você não precisa reativar nada.

!!! note "Quem pode configurar"
    Só administradores usam `/video-download`. O bot precisa de permissão pra ver o canal, enviar mensagens e anexar arquivos. Sem "Anexar arquivos", ele não posta o `.mp4`. O comando só funciona dentro de um servidor, não em DM.

## Exemplos

!!! example "Um canal só pra colar links"
    Crie um `#links-virais` e rode `/video-download canal:#links-virais`. Daí em diante, todo TikTok, Reel ou Short colado ali vira vídeo assistível na hora, e os outros canais ficam livres de anexos.

!!! example "Canal de clipes e memes"
    Ative no `#clipes`. Os clipes da Twitch e vídeos do Reddit que a comunidade postar aparecem já reproduzíveis, sem prévia quebrada nem link pra abrir no navegador.

!!! example "Desligar quando virar bagunça"
    Canal lotado de download indesejado? Rode `/video-download` de novo apontando pro mesmo canal. O recurso desliga ali na hora, sem mexer nos outros.

## Vídeos grandes e quando o bot fica quieto

O Discord limita o tamanho dos anexos, então o Delfus trabalha com teto de 8 MB (margem segura, funciona até sem Nitro). Se o vídeo passa disso, ele comprime: reduz a resolução pra no máximo 720p, mira um arquivo de uns 7,5 MB e mantém a proporção original. Vídeos grandes ou longos podem perder um pouco de qualidade nesse processo.

!!! warning "Quando o Delfus não responde"
    O recurso nunca polui o canal com mensagens de erro. Se algo dá errado, o bot fica quieto e o link original continua na conversa. Isso acontece quando o vídeo é privado, removido, exige login, tem restrição de idade ou bloqueio de direitos autorais; quando é longo demais pra caber mesmo após comprimir; ou quando o download demora demais. Há também um limite anti-spam: cada pessoa só dispara um download a cada 10 segundos.

## Perguntas frequentes

**O bot baixa qualquer vídeo da internet?**
Não. Só YouTube, TikTok, Instagram, Twitter/X, Reddit e clipes da Twitch, nos formatos de vídeo direto de cada plataforma. O resto ele ignora.

**Postei um link e o bot não respondeu. O que houve?**
Provavelmente o vídeo é privado, foi removido, exige login, tem restrição de idade, está bloqueado por direitos autorais, é longo demais pra caber no limite, ou você postou outro link nos últimos 10 segundos. Em todos esses casos ele ignora em silêncio, sem mensagem de erro.

**A qualidade é a original?**
Se o vídeo já cabe em 8 MB, vai como veio. Se é maior, o Delfus comprime pra caber (até 720p), então pode haver alguma perda em vídeos grandes ou longos.

**Posso ativar em mais de um canal?**
Pode. Rode `/video-download` uma vez pra cada canal. Cada um funciona de forma independente e a configuração sobrevive a reinícios do bot.

!!! tip "Dica"
    Dedique um canal só pra colar links de vídeo e ative o recurso apenas nele. Assim os membros sabem onde os links viram vídeos, e os outros canais não enchem de anexos. Se um deles sair de controle, rode `/video-download` de novo no mesmo canal pra desligar na hora.

