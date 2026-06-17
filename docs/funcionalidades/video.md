# Download de vídeos

O Delfus baixa automaticamente vídeos de links postados em canais que você escolher e reenvia o vídeo direto no chat como anexo, sem que ninguém precise abrir o link. Funciona com YouTube, TikTok, Instagram, Twitter/X, Reddit e Twitch.

## Como funciona

Depois que você ativa o recurso em um canal, o bot fica de olho nas mensagens daquele canal:

1. Um membro posta uma mensagem com um link de vídeo de uma plataforma suportada.
2. O bot detecta o link automaticamente (ignora mensagens de outros bots). Se houver mais de um link na mesma mensagem, apenas o primeiro é processado, para evitar excesso.
3. O bot mostra o indicador de "digitando" e baixa o vídeo nos bastidores.
4. Se o vídeo for grande demais para o Discord, o bot o comprime automaticamente (reduzindo para no máximo 720p) até caber no limite de envio.
5. O vídeo é enviado como **resposta** à mensagem original, em formato `.mp4`, anexado direto no canal.

Detalhes do comportamento:

- **Limite por usuário:** cada membro só pode disparar um novo download a cada 10 segundos no canal. Postagens em sequência rápida são ignoradas em silêncio.
- **Falhas são silenciosas:** se o vídeo for privado, indisponível, exigir login, tiver restrição de idade, estiver bloqueado por direitos autorais, for longo demais para comprimir, ou demorar demais, o bot simplesmente não responde — ele não polui o canal com mensagens de erro.
- **Arquivos temporários:** o vídeo baixado é apagado do servidor logo após ser enviado.

## Configuração

A configuração é feita **por comando**, dentro do próprio Discord (não há ajuste no painel web para este recurso):

- Use `/video-download` e informe o canal onde quer ativar o download automático.
- O comando funciona como liga/desliga (toggle): rodá-lo num canal já ativo **desativa** o recurso ali; rodá-lo num canal inativo **ativa**.
- A escolha fica salva na configuração do servidor e continua valendo mesmo após o bot reiniciar.

## Requisitos

- Apenas membros com permissão de **Administrador** podem usar `/video-download`.
- No canal monitorado, o bot precisa das permissões **Ver canal**, **Enviar mensagens** e **Anexar arquivos** para conseguir responder com o vídeo.

!!! tip
    Dedique um canal específico para "colar links de vídeo" e ative o recurso só nele — assim os membros sabem onde os links viram vídeos automaticamente, sem afetar a conversa nos outros canais.
