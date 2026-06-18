# Anti-raid

O Anti-raid detecta e barra ataques coordenados de divulgação de golpes (scams) por imagem no seu servidor — aqueles posts em massa de "sorteio do MrBeast", "código promocional de crypto", "resgate seu prêmio em USDT" e afins. Quando identifica um ataque, ele apaga a mensagem, pune o autor, limpa o que ele já espalhou e avisa a sua moderação, tudo automaticamente e em segundos. É a sua defesa contra invasões em que dezenas de contas despejam a mesma arte de golpe em vários canais ao mesmo tempo.

![Configuração do anti-raid no painel do Delfus](../assets/dashboard/anti-raid.png){ .dx-shot loading=lazy }

*Configuração do anti-raid no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O módulo entra em ação sempre que alguém envia uma **mensagem com imagem** em um servidor onde o Anti-raid está configurado (com um canal de alertas definido). A cada mensagem assim, o bot roda uma sequência de checagens, da mais barata para a mais cara, e para na primeira que confirmar um ataque.

### 1. Reincidência rápida (golpista já flagrado)

Quando o Anti-raid pune alguém, ele "marca" essa pessoa como golpista por **5 minutos**. Durante esse intervalo, qualquer nova mensagem que ela enviar é **apagada na hora**, sem reanalisar imagem nem ler texto — isso evita que o atacante continue espalhando enquanto a punição é processada e impede gasto desnecessário de análise.

A cada bloqueio preventivo desses, o bot manda um aviso curto ao canal de moderação informando o usuário e o canal. Esse aviso é **limitado a no máximo um a cada 30 segundos por usuário**, para não inundar a moderação de notificações repetidas.

### 2. Velocidade: flood e enxame

Se a checagem de velocidade estiver ativa para o servidor, antes de analisar a imagem o bot mede o **ritmo de envio**. Ele acompanha duas coisas em uma janela de tempo curta (por padrão 10 segundos):

- **Flood de um usuário (alta confiança).** Se a **mesma pessoa** espalha imagens por **vários canais distintos** numa janela curta (por padrão, 3 canais em 10 segundos), isso é tratado como ataque confirmado. O bot aplica o fluxo completo de detecção e **bane** o autor (essa rota é sempre ban, independentemente da ação configurada para o módulo de imagem).

- **Enxame de contas novas (confiança menor).** Se **várias contas recém-chegadas** ao servidor (por padrão, 5 contas que entraram há menos de 24 horas) começam a postar imagens ao mesmo tempo, o bot aplica um **bloqueio brando**: liga o **modo lento (slowmode)** no canal afetado (por padrão 30 segundos) e avisa a moderação. Ele **nunca** bane em massa de forma automática nesse caso — só desacelera o canal e chama a moderação para revisar. O alerta de enxame também é limitado (no máximo um por minuto por servidor) e a análise normal de imagem continua rodando na mensagem que disparou o enxame.

A idade da conta usada aqui é o tempo desde que o membro **entrou no servidor**, não a data de criação no Discord.

### 3. Reconhecimento da imagem do golpe

Esta é a camada principal (o módulo "MrsBeast Hack"). O bot baixa as imagens da mensagem e calcula uma "impressão digital" visual de cada uma (um hash que tolera pequenas diferenças de qualidade, recorte e compressão). Em seguida compara essa impressão com:

- uma **base de artes de golpe de referência** embarcada no bot (golpes conhecidos do tipo MrBeast/crypto), carregada quando o bot inicia; e
- uma **base aprendida** de golpes que o próprio bot já identificou antes (ver passo 4).

Se a imagem ficar visualmente próxima o suficiente de alguma arte conhecida — dentro da **sensibilidade** configurada — a mensagem é considerada um ataque. A sensibilidade vai de 5 (mais rígido, exige imagem quase idêntica) a 30 (mais tolerante), com padrão recomendado entre 10 e 15.

#### Flood de imagens idênticas

Mesmo que a arte não bata com nada conhecido, se a mensagem trouxer **4 ou mais imagens praticamente iguais entre si**, o bot trata isso como flood e bloqueia — é um padrão típico de spam em massa.

### 4. Aprendizado contínuo (leitura de texto em segundo plano)

Quando uma imagem **não** bate com nada conhecido, o bot ainda tenta aprender com ela — mas **sem travar a resposta** ao usuário. Em segundo plano, ele lê o texto da imagem (OCR, em inglês) e procura por **palavras típicas de golpe** organizadas em categorias: crypto (bitcoin, ethereum, USDT...), ação ("claim", "airdrop", "claim your reward"), promoção ("promo code", "code for bonus"), apostas ("rakeback", "VIP club"), pagamento ("withdrawal success", "prize has been credited"), urgência ("post will be deleted", "only the fastest"), QR ("scan QR") e figuras públicas ("MrBeast", "Elon"...).

Para evitar falso-positivo, o bot só considera golpe quando o texto bate em **pelo menos 2 categorias diferentes**. Quando reconhece o padrão, ele **memoriza permanentemente** a impressão digital daquela arte numa base de conhecimento durável (sobrevive a reinícios do bot). Resultado prático: a primeira mensagem com uma arte nova pode passar, mas a partir daí o bot a barra **instantaneamente** pelo reconhecimento de imagem, sem precisar reler o texto.

> Observação: a leitura de texto é só para aprender. Ela **não** pune a mensagem atual — quem pune são as camadas rápidas de reconhecimento de imagem e de velocidade.

### O que acontece quando um ataque é confirmado

Assim que qualquer camada confirma um ataque, o bot, em sequência:

1. **Apaga a mensagem** ofensiva.
2. **Marca o autor como golpista por 5 minutos**, para apagar automaticamente tudo o que ele postar nesse intervalo (passo 1 de "Como funciona").
3. **Aplica a punição configurada** — advertir, silenciar, expulsar ou banir (o padrão do módulo de imagem é **banir**; a rota de flood de velocidade é sempre ban).
4. **Avisa o canal de moderação** que você definiu, dizendo qual módulo disparou, quem foi punido, qual ação foi tomada (e a duração, no caso de silenciar) e o motivo.
5. **Limpa as mensagens recentes do golpista** — varre os canais de texto e apaga o que aquele usuário postou nos **últimos 10 minutos**, removendo o que ele já tinha espalhado antes de ser pego.

### Quando o bot prefere não agir

A segurança é desenhada para **não punir por engano**: se qualquer etapa falhar (download da imagem, leitura, indisponibilidade temporária de cache), o bot **deixa passar** em vez de aplicar uma punição indevida. Além disso, ele só consegue punir membros que estejam **abaixo do cargo dele** na hierarquia — alguém acima do bot não é punido.

## Comandos

Esta feature é configurada apenas pelo painel. O Anti-raid não tem comandos de barra próprios — ele age sozinho, automaticamente, sobre as mensagens dos canais.

## Configuração

A configuração é feita **pelo Dashboard**, em [admin.delfus.app](https://admin.delfus.app), na seção **Anti-Raid**. Selecione o servidor, ajuste as opções e clique em **Salvar**. Para desativar tudo de uma vez, use **Remover Anti-Raid** (desliga todos os módulos).

### Configuração global

- **Canal de Alerta** — canal de texto onde a moderação recebe os avisos de detecção, bloqueios preventivos e alertas de enxame. É **obrigatório**: sem ele, o Anti-raid não funciona. Use um canal só da moderação.

### Módulo "MrsBeast Hack" (reconhecimento de imagem)

Um interruptor **Ativo/Inativo** liga ou desliga o módulo. Com ele ativo, você define:

- **Ação** — o que fazer com o golpista quando um ataque é detectado:
  - **Advertência (Warn)** — registra uma advertência.
  - **Mute (Timeout)** — silencia o membro. Ao escolher esta opção, aparece o campo **Duração do Mute (segundos)**, com mínimo de 60 segundos e máximo de 28 dias (2.419.200 segundos). O padrão é 600 segundos (10 minutos).
  - **Kick** — expulsa o membro.
  - **Ban** — bane o membro (opção padrão).
- **Sensibilidade de detecção** — controle deslizante de **5 a 30** (padrão 12). Valores **menores** deixam o reconhecimento mais sensível (pega variações da arte, mas pode gerar mais falsos positivos); valores **maiores** o tornam mais tolerante (menos falso-positivo, mas pode deixar passar). Recomendado: entre 10 e 15.
- **Mínimo de imagens** — controle deslizante de **1 a 10** (padrão 1). É a quantidade mínima de imagens na mensagem para o bot rodar a análise. Em 1, qualquer mensagem com imagem é analisada; valores maiores ignoram mensagens com poucas imagens.
- **Motivo (opcional)** — texto registrado como motivo da punição e exibido no alerta da moderação. Se ficar vazio, o bot usa um motivo padrão.

> As regras de velocidade (flood cross-canal e enxame de contas novas) fazem parte do comportamento do Anti-raid, mas seus limites finos são ajustados pela equipe Delfus por servidor, não pela tela atual do painel. Os padrões são: 3 canais em 10 segundos para flood de um usuário; 5 contas com menos de 24h para enxame; slowmode de 30 segundos no bloqueio brando.

## Exemplos de uso

- **Proteger um servidor grande contra ataques de scam de crypto:** ative o módulo **MrsBeast Hack**, deixe a ação em **Ban**, sensibilidade em torno de 12 e aponte o **Canal de Alerta** para o canal interno da staff. A partir daí, qualquer post com a arte do "sorteio do MrBeast" é apagado e o autor banido automaticamente, com o registro caindo no canal da moderação.

- **Modo mais cauteloso, sem banir na hora:** se você prefere revisar antes de punições duras, escolha a ação **Mute (Timeout)** com, por exemplo, 600 segundos. O golpe ainda é apagado e o autor é silenciado por 10 minutos, dando tempo de a moderação confirmar pelo alerta e decidir se bane manualmente.

- **Reduzir falsos positivos em um servidor de artes/memes:** se membros legítimos costumam postar imagens parecidas com as artes de golpe, suba a **Sensibilidade** para 15 e considere subir o **Mínimo de imagens**, deixando o bot mais tolerante e focando nos ataques mais óbvios.

## Requisitos

Para o Anti-raid agir, o bot precisa de permissões compatíveis com as ações que ele executa:

- **Gerenciar mensagens** — para apagar a mensagem ofensiva e limpar o histórico recente do golpista em todos os canais.
- **Banir membros** e/ou **Expulsar membros** — conforme a ação escolhida (e a rota de flood, que sempre bane).
- **Moderar membros (timeout)** — se a ação configurada for silenciar.
- **Gerenciar canais** — para ligar o modo lento (slowmode) durante um enxame de contas novas.

Além disso:

- O **cargo do bot precisa estar acima** do cargo dos membros que ele deve punir; do contrário, a punição não é aplicada.
- É preciso ter um **Canal de Alerta** configurado — sem ele o módulo não roda.

## Perguntas frequentes

**O Anti-raid funciona com qualquer imagem ou só com golpes conhecidos?**
Ele já vem com uma base de golpes de referência (estilo MrBeast/crypto) e barra qualquer imagem visualmente parecida com elas. Artes totalmente novas podem passar na primeira vez, mas o bot lê o texto delas em segundo plano e, ao reconhecer o padrão de golpe, memoriza a arte para barrá-la instantaneamente nas próximas vezes.

**O Anti-raid pode banir um membro de boa-fé por engano?**
É raro e o sistema é desenhado para errar para o lado seguro: na dúvida (qualquer falha de análise), ele deixa passar. Ainda assim, todo bloqueio é registrado no Canal de Alerta — acompanhe esse canal para revisar e reverter manualmente se necessário. Se houver muitos falsos positivos, aumente a Sensibilidade.

**O Anti-raid bane todo mundo numa invasão de contas novas?**
Não. Ataques de enxame de contas recém-chegadas geram um **bloqueio brando**: o bot só liga o modo lento no canal e avisa a moderação. Banimentos automáticos acontecem para golpes reconhecidos individualmente e para o flood de um único usuário espalhando imagens por vários canais.

**Por que o golpe sumiu de vários canais, não só do que eu vi?**
Quando o bot pega um golpista, ele também varre os canais e apaga as mensagens daquele usuário dos últimos 10 minutos — assim remove tudo o que ele espalhou antes de ser detectado.

!!! tip "Dica"
    Aponte o **Canal de Alerta** para um canal exclusivo da moderação e mantenha-o sob observação. É por ele que cada bloqueio, alerta preventivo e aviso de enxame chega — o que permite confirmar ataques, revisar rapidamente e reverter manualmente caso um membro legítimo seja afetado.
