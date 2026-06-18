# Backups

Recrie cargos, canais, categorias, permissões e configurações do servidor com poucos cliques, mesmo depois de um ataque ou de uma reforma que deu errado. O Delfus tira uma "foto" da estrutura do servidor e guarda pra você restaurar quando precisar.

![Backups do servidor no painel do Delfus](../assets/dashboard/backup.png){ .dx-shot loading=lazy }

*Backups do servidor no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O Delfus salva uma foto da estrutura do servidor: cargos, canais, categorias, permissões e configurações. Mensagens e a lista de membros não entram. Só o esqueleto.

Essa foto é compactada pra ocupar pouco espaço. Você gerencia tudo pelo painel que abre com `/backup`.

São três peças que trabalham juntas:

- **Backup de estrutura**: a foto principal, criada e restaurada pelo painel `/backup`.
- **Backups automáticos**: o bot tira a foto sozinho, na frequência e horário que você definir.
- **Snapshot de cargos por membro**: quando alguém sai, o Delfus guarda os cargos da pessoa pra você devolver depois com `/restaurar-cargos`.

!!! example "Exemplo"
    Você vai reorganizar todos os canais. Antes de mexer, roda `/backup`, clica em **Criar** e dá o nome "antes da reforma". Se a bagunça piorar, restaura essa foto e volta tudo ao lugar, sem reconfigurar nada na mão.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/backup` | Abre o painel de backups (só o dono do servidor). Por ali você cria, lista, restaura e deleta backups. |
| `/restaurar-cargos` (`/restore-roles`) | Devolve a um membro os cargos guardados no snapshot mais recente. |

## Configuração

O dia a dia (criar, restaurar e deletar) acontece no painel `/backup`, dentro do Discord. Só o dono do servidor consegue abrir. A automação e os limites ficam no [Dashboard](https://admin.delfus.app).

No painel `/backup` você tem quatro botões:

- **Criar**: abre uma janela pedindo um nome (opcional). Em segundos o bot tira a foto e mostra um resumo: quantos cargos, canais e categorias foram salvos.
- **Listar**: mostra todos os backups, com nome, data e contagens.
- **Restaurar**: recria a estrutura a partir de um backup (mais sobre isso abaixo).
- **Deletar**: remove um backup, com confirmação antes.

!!! note "Limite de backups"
    Cada servidor guarda um número máximo de backups (5 por padrão, de 1 a 10 no Dashboard). Quando você cria um novo acima do limite, o mais antigo some pra abrir espaço.

No Dashboard, na página "Backups do Servidor", você liga o **Auto-Backup** e escolhe:

- **Frequência**: *Diário* ou *Semanal (domingos)*.
- **Horário**: a hora do dia em que ele roda. O horário é em UTC, então some 3 horas do horário de Brasília (06:00 UTC = 03:00 no Brasil).
- **Backup de bans**: incluir ou não a lista de banimentos (vem ligado).
- **Máximo de backups**: de 1 a 10.

Na página "Backup de Usuários" você controla os snapshots de cargos por membro: liga a captura automática quando alguém sai e define quantas fotos guardar por pessoa (2 por padrão).

### Restaurando um backup

No botão **Restaurar**, escolha a foto e o modo:

- **Aditivo** (seguro): recria cargos e canais ao lado do que já existe, sem apagar nada. Roda na hora.
- **Destrutivo**: apaga os cargos e canais atuais antes de recriar tudo do zero a partir da foto. Como é irreversível, pede uma confirmação extra. O `@everyone`, cargos de bots/boosters e canais obrigatórios de Comunidade nunca são apagados.

Em backups completos, você ainda escolhe o que recriar: cargos e canais (sempre), configurações do servidor, cargos e apelidos dos membros, e bans.

A restauração roda em fases, num ritmo controlado pra não esbarrar nos limites do Discord. Em servidores grandes, pode levar alguns minutos. Você acompanha por uma barra de progresso e, no fim, recebe um resumo com o que deu certo e o que foi pulado.

!!! warning "Suba o cargo do bot antes de restaurar"
    O Delfus só recria cargos que estejam abaixo do cargo dele. Deixe o cargo do bot bem no topo da hierarquia antes de restaurar. Senão os cargos acima dele são pulados e aparecem como "hierarquia" no resumo.

### Devolvendo cargos a quem saiu

Com o snapshot automático ligado, o Delfus guarda os cargos de cada membro no momento em que ele sai. Depois, use `/restaurar-cargos` apontando a pessoa.

O bot mostra um preview do que vai acontecer: quais cargos serão adicionados, quais a pessoa já tem e quais não dá pra aplicar (porque foram deletados, são de integrações ou estão acima do bot). Você confere e confirma.

!!! note
    O membro precisa estar de volta no servidor pra receber os cargos. Se ainda não voltou, o preview avisa que nada será aplicado.

## Exemplos

!!! example "Reforma que deu errado"
    Você reorganizou os canais e o servidor virou uma confusão. Abra `/backup`, clique em **Restaurar**, escolha o backup "antes da reforma" no modo **Aditivo** e a estrutura antiga volta, lado a lado com o que já existe, sem apagar nada.

!!! example "Servidor atacado"
    Alguém invadiu e apagou vários canais. Abra `/backup`, **Restaurar**, pegue o backup mais recente. Use **Aditivo** pra trazer de volta o que foi perdido, ou **Destrutivo** se quiser zerar tudo e recriar exatamente como estava na foto.

!!! example "Proteção no piloto automático"
    No Dashboard, ligue o **Auto-backup**, escolha *Diário* às 06:00 UTC e deixe o máximo em 7. O Delfus passa a guardar uma semana inteira de fotos diárias, sem você fazer nada.

!!! example "Membro antigo voltou"
    Aquele moderador veterano saiu e agora voltou. Com o snapshot ligado, rode `/restaurar-cargos`, escolha ele, confira o preview e confirme. Todos os cargos que ele tinha voltam de uma vez.

## Perguntas frequentes

**O backup salva as mensagens dos canais?**
Não. Ele guarda só a estrutura: cargos, canais, categorias, permissões e configurações. Nunca o conteúdo das mensagens nem a lista de membros.

**Posso restaurar sem apagar o que já existe?**
Sim, é o modo **Aditivo**: ele recria os itens ao lado dos atuais, sem deletar nada. O modo **Destrutivo** (que apaga antes) só roda depois de uma confirmação extra.

**Por que alguns cargos não foram restaurados?**
Cargos acima do cargo do bot, cargos já deletados ou cargos de integrações não podem ser recriados. Eles aparecem no resumo como ignorados. Suba o cargo do bot ao topo e tente de novo.

**Quantos backups o servidor guarda?**
De 1 a 10 (padrão 5), definido no Dashboard. Ao passar do limite, o mais antigo é apagado. Os snapshots de cargos por membro têm o próprio limite (padrão 2 por pessoa).

**Preciso de alguma permissão pro bot?**
Sim. Ele precisa de **Gerenciar Cargos** e **Gerenciar Canais** pra criar e restaurar a estrutura. Pra restaurar configurações do servidor, também precisa de **Gerenciar Servidor**; pra restaurar bans, de **Banir Membros**.

!!! tip "Dica"
    Antes de qualquer mudança grande, crie um backup manual com um nome descritivo. Se algo der errado, restaure primeiro no modo **Aditivo**, que não apaga nada e é fácil de desfazer. Deixe o **Destrutivo** só pra quando você realmente quer recomeçar do zero.

