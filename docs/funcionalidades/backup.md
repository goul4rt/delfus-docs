# Backups

Salve uma cópia completa da estrutura do seu servidor — cargos, canais, categorias, permissões e configurações — para poder restaurá-la depois caso algo dê errado (uma reformulação que não deu certo, um ataque que apagou canais, etc.).

## Como funciona

O backup captura uma "foto" da estrutura do servidor em um determinado momento. Cada backup guarda:

- **Cargos**: nomes, cores, permissões, ordem na hierarquia, ícone/emoji.
- **Canais e categorias**: nome, tópico, posição, modo lento, NSFW, bitrate de voz, e as permissões (overwrites) de cada canal.
- **Configurações do servidor**: ícone, banner, nível de verificação, canais de sistema/regras/AFK, idioma, etc.
- **Tópicos (threads)** e, opcionalmente, a **lista de banimentos**.

Um backup **não** salva mensagens, membros nem o conteúdo dos canais — só a estrutura.

**Criando e gerenciando backups**

Tudo acontece num painel interativo aberto pelo comando `/backup` (apenas o dono do servidor pode abri-lo). No painel você consegue **Criar**, **Listar**, **Restaurar** e **Deletar** backups. Ao criar, você pode dar um nome (ex.: "pré-reformulação dos canais"); se não der, recebe um nome padrão. O servidor mantém um número limitado de backups (5 por padrão, configurável); quando esse limite é atingido, o backup mais antigo é apagado automaticamente para dar lugar ao novo.

**Backups automáticos**

Se ativado, o bot cria um backup sozinho em uma frequência definida (diária ou semanal) e em uma hora escolhida do dia. O backup automático respeita o mesmo limite de quantidade dos backups manuais.

**Restaurando um backup**

Pelo painel, ao escolher **Restaurar**, você seleciona o backup e:

1. Escolhe o **modo de restauração**:
   - **Aditivo**: recria cargos, canais e categorias do backup **ao lado** do que já existe, sem apagar nada. É o modo seguro.
   - **Destrutivo**: **apaga** os cargos e canais atuais antes de recriar a estrutura do backup. Recomeça do zero a partir do backup. Exige uma confirmação extra por ser irreversível.
2. Escolhe **o que** restaurar: Cargos e Canais (sempre), e opcionalmente Configurações do Servidor, Cargos/Apelidos dos membros e Banimentos (quando o backup os contém).

A restauração roda em etapas (primeiro os cargos, depois categorias, canais, configurações, etc.), com um ritmo controlado para não esbarrar nos limites do Discord — por isso pode levar alguns minutos em servidores grandes. Só uma restauração pode rodar por vez em cada servidor. Ao final, você recebe um resumo com erros e avisos (por exemplo, cargos que o bot não conseguiu recriar por estarem acima dele na hierarquia).

## Restaurar cargos de um membro específico

Além do backup de estrutura, existe o comando `/restaurar-cargos` (também `/restore-roles`), que devolve a um membro os cargos que ele tinha antes de sair. Isso depende de o servidor estar salvando uma "foto" dos cargos quando alguém sai (recurso de snapshot na saída). Ao usar o comando, escolhendo o membro, o bot mostra um preview paginado dos cargos: quais serão **adicionados**, quais o membro **já tem**, e quais estão **indisponíveis** (cargo deletado, gerenciado por integração, ou acima do bot na hierarquia). Você confirma e os cargos disponíveis são reaplicados. O membro precisa estar no servidor para receber os cargos.

## Configuração

- **Comando**: use `/backup` (somente o dono do servidor) para abrir o painel e fazer tudo — criar, listar, restaurar e deletar.
- **Backups automáticos** (ativar/desativar, frequência, horário, quantidade máxima e se inclui banimentos): configure pelo painel em [admin.delfus.app](https://admin.delfus.app).
- **Restaurar cargos de um membro**: comando `/restaurar-cargos`.

## Requisitos

- O bot precisa das permissões **Gerenciar Cargos** e **Gerenciar Canais** para criar/restaurar a estrutura.
- Para restaurar **configurações do servidor**, o bot também precisa de **Gerenciar Servidor**; para restaurar **banimentos**, precisa de **Banir Membros**.
- Na restauração, o bot só consegue recriar cargos que fiquem **abaixo** do cargo dele na hierarquia. Posicione o cargo do bot bem no topo antes de restaurar.
- Apenas o **dono do servidor** pode abrir o painel `/backup`.

!!! tip
    Antes de qualquer mudança grande (reformular canais, reorganizar cargos), crie um backup manual com um nome descritivo. Se algo der errado, restaure no modo **Aditivo** primeiro — ele não apaga nada e é fácil de reverter. Deixe o **Destrutivo** apenas para casos em que você realmente quer recomeçar do zero.
