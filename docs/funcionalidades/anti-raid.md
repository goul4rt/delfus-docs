# Anti-raid

Sabe aqueles ataques em que dezenas de contas despejam a mesma arte de golpe — "sorteio do MrBeast", "código promocional de crypto", "resgate seu prêmio em USDT" — em vários canais ao mesmo tempo? O Anti-raid é a sua defesa contra isso. Ele identifica o ataque, apaga a mensagem, pune o autor, limpa o rastro e avisa a sua moderação. Tudo automático, em segundos.

![Configuração do anti-raid no painel do Delfus](../assets/dashboard/anti-raid.png){ .dx-shot loading=lazy }

*Configuração do anti-raid no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

Sempre que alguém posta uma **mensagem com imagem** (num servidor onde o Anti-raid está ligado), o bot dá uma olhada rápida nela. Ele roda algumas checagens em ordem — das mais leves para as mais pesadas — e para na primeira que confirmar um golpe.

Em resumo, ele olha três coisas:

- **Já é reincidente?** Quando o bot pune alguém, marca essa pessoa como golpista por **5 minutos**. Nesse tempo, qualquer coisa que ela postar é apagada na hora, sem nem reanalisar — pra ela não continuar espalhando enquanto a punição rola.
- **Está postando rápido demais?** Se a mesma pessoa joga imagens em vários canais em poucos segundos, ou se um monte de contas novas começa a postar junto, o bot trata como ataque (mais sobre isso abaixo).
- **A imagem é um golpe conhecido?** Essa é a camada principal. O bot calcula uma "impressão digital" visual da imagem e compara com uma base de golpes que ele já conhece. Se bater, é ataque.

!!! example "Exemplo"
    Alguém entra no servidor e posta um print de "sorteio oficial do MrBeast — resgate seus 5 BTC". O Delfus reconhece a arte do golpe, apaga a mensagem na hora e bane o autor — antes que mais alguém clique no link.

### Velocidade: flood e enxame

Quando a checagem de velocidade está ligada, o bot mede o **ritmo de envio** numa janela curta (por padrão, 10 segundos) e reage a dois cenários:

- **Uma pessoa floodando vários canais.** Se a mesma conta espalha imagens por vários canais distintos de uma vez (padrão: 3 canais em 10 segundos), é ataque confirmado — e aqui a punição é **sempre ban**, não importa o que você configurou.
- **Enxame de contas novas.** Se várias contas recém-chegadas (padrão: 5 contas que entraram há menos de 24h) começam a postar imagens ao mesmo tempo, o bot pisa no freio com cuidado: liga o **modo lento** no canal (slowmode de 30s) e chama a moderação. Ele **nunca** bane todo mundo em massa nesse caso — só desacelera e pede pra vocês revisarem.

!!! note "Detalhe"
    A "idade da conta" no caso do enxame conta a partir de quando o membro **entrou no servidor**, não da data de criação no Discord.

### Aprendizado contínuo

E se aparecer uma arte de golpe totalmente nova, que o bot ainda não conhece? Ele tenta aprender com ela — sem travar a resposta ao usuário.

Em segundo plano, o bot lê o texto da imagem (OCR) e procura por palavras típicas de golpe: crypto, "claim", "airdrop", "promo code", "withdrawal success", "MrBeast", "Elon" e por aí vai. Pra não errar, ele só considera golpe quando o texto bate em **pelo menos 2 categorias diferentes**.

Quando reconhece o padrão, ele **memoriza a arte pra sempre**. Resultado: a primeira mensagem com uma arte nova pode escapar, mas da próxima vez o bot barra instantaneamente.

!!! note "Importante"
    Essa leitura de texto é só pra **aprender** — ela não pune a mensagem atual. Quem pune são as camadas rápidas de reconhecimento de imagem e de velocidade.

### O que acontece quando um ataque é confirmado

Assim que qualquer camada confirma o golpe, o bot, em sequência:

1. **Apaga** a mensagem.
2. **Marca o autor como golpista por 5 minutos** (pra apagar tudo que ele postar nesse intervalo).
3. **Aplica a punição** que você configurou — advertir, silenciar, expulsar ou banir.
4. **Avisa o canal de moderação**: qual módulo disparou, quem foi punido, qual ação foi tomada e o motivo.
5. **Limpa o rastro** — varre os canais e apaga tudo que aquele usuário postou nos **últimos 10 minutos**.

!!! tip "Erra pro lado seguro"
    Se qualquer etapa falhar (download da imagem, leitura, cache indisponível), o bot prefere **deixar passar** a punir por engano. E ele só consegue punir quem está **abaixo do cargo dele** na hierarquia — alguém acima do bot não é tocado.

## Comandos

O Anti-raid não tem comandos de barra. Ele age sozinho, automaticamente, sobre as mensagens dos canais. Toda a configuração é feita pelo painel.

## Configuração

Tudo pelo **Dashboard**, em [admin.delfus.app](https://admin.delfus.app), na seção **Anti-Raid**. Selecione o servidor, ajuste as opções e clique em **Salvar**. Pra desligar tudo de uma vez, use **Remover Anti-Raid**.

**Configuração global**

- **Canal de Alerta** — onde a moderação recebe os avisos. É **obrigatório**: sem ele, o Anti-raid não funciona. Use um canal só da staff.

**Módulo "MrsBeast Hack" (reconhecimento de imagem)**

Um interruptor liga ou desliga o módulo. Com ele ativo, você define:

- **Ação** — o que fazer com o golpista: **Advertência**, **Mute** (com duração entre 60s e 28 dias; padrão 10 min), **Kick** ou **Ban** (padrão).
- **Sensibilidade** — de 5 a 30 (padrão 12). Quanto **menor**, mais sensível (pega variações, mas pode dar falso-positivo); quanto **maior**, mais tolerante. O recomendado fica entre 10 e 15.
- **Mínimo de imagens** — de 1 a 10 (padrão 1). Quantas imagens a mensagem precisa ter pro bot analisar. Em 1, qualquer imagem é checada.
- **Motivo (opcional)** — texto que aparece na punição e no alerta. Vazio, o bot usa um padrão.

!!! note "Limites finos"
    As regras de velocidade (flood e enxame) fazem parte do Anti-raid, mas seus números exatos são ajustados pela equipe Delfus por servidor. Os padrões: 3 canais em 10s para flood de um usuário; 5 contas com menos de 24h para enxame; slowmode de 30s no bloqueio brando.

## Exemplos

!!! example "Servidor grande, proteção firme"
    Ative o **MrsBeast Hack**, deixe a ação em **Ban**, sensibilidade em torno de 12 e aponte o **Canal de Alerta** pra staff. Pronto: todo print do "sorteio do MrBeast" é apagado e o autor banido na hora, com o registro caindo no canal da moderação.

!!! example "Modo cauteloso, sem banir na hora"
    Prefere revisar antes? Escolha a ação **Mute** com 600 segundos. O golpe ainda é apagado e o autor fica calado por 10 minutos — tempo de a moderação conferir o alerta e decidir se bane manualmente.

!!! example "Servidor de artes/memes"
    Se membros legítimos postam imagens parecidas com golpes, suba a **Sensibilidade** para 15 e considere aumentar o **Mínimo de imagens**. Assim o bot fica mais tolerante e foca só nos ataques óbvios.

## Requisitos

Pra agir, o bot precisa das permissões certas:

- **Gerenciar mensagens** — pra apagar o golpe e limpar o rastro.
- **Banir** e/ou **Expulsar membros** — conforme a ação escolhida (o flood sempre bane).
- **Moderar membros (timeout)** — se a ação for silenciar.
- **Gerenciar canais** — pra ligar o slowmode num enxame.

E mais duas coisas: o **cargo do bot precisa estar acima** dos membros que ele vai punir, e o **Canal de Alerta** precisa estar configurado — sem ele, o módulo nem roda.

## Perguntas frequentes

**Funciona com qualquer imagem ou só com golpes conhecidos?**
Ele já vem com uma base de golpes de referência e barra qualquer imagem parecida com elas. Artes totalmente novas podem passar na primeira vez, mas o bot lê o texto delas em segundo plano e, ao reconhecer o padrão, memoriza a arte pra barrar instantaneamente depois.

**O bot pode banir um membro de boa-fé por engano?**
É raro — na dúvida, ele deixa passar. Mesmo assim, todo bloqueio fica registrado no Canal de Alerta, então dá pra revisar e reverter manualmente. Se aparecerem muitos falsos positivos, aumente a Sensibilidade.

**Ele bane todo mundo numa invasão de contas novas?**
Não. Enxame de contas novas gera só um **bloqueio brando**: modo lento no canal e aviso à moderação. Banimento automático rola pra golpes reconhecidos individualmente e pro flood de um único usuário em vários canais.

**Por que o golpe sumiu de vários canais, não só do que eu vi?**
Porque, ao pegar o golpista, o bot também varre os canais e apaga tudo que ele postou nos últimos 10 minutos — removendo o que ele já tinha espalhado antes de ser pego.

!!! tip "Dica"
    Aponte o **Canal de Alerta** para um canal exclusivo da moderação e fique de olho nele. É por ali que cada bloqueio e alerta chega — o que te deixa confirmar ataques, revisar rápido e reverter na mão caso um membro legítimo seja afetado.

