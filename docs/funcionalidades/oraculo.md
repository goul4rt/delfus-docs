# Oráculo

O Oráculo é o "gravador" de canais do Delfus: você escolhe quais canais quer acompanhar e, a partir daí, tudo que for postado neles passa a ser registrado automaticamente. Esse registro é a matéria-prima dos painéis de análise do Dashboard — insights de atividade, scoring de membros e análise de conteúdo — e responde, na prática, à pergunta "o que e quem mais movimenta este canal?".

## Como funciona

O Oráculo monitora canais específicos do servidor e captura cada mensagem nova enviada neles. Ele não puxa o histórico anterior — só registra o que acontece **a partir do momento** em que o canal entra na lista de monitoramento.

### Ativando o monitoramento

1. Você marca um ou mais canais para monitorar, pelo Dashboard ou pelo comando `/oraculo`. A escolha é salva nas configurações do servidor (campo `oraculoChannels`), então continua valendo mesmo depois de o bot reiniciar.
2. O bot mantém em memória uma lista dos canais monitorados de todos os servidores. Quando você altera a configuração pelo painel, essa lista em memória é atualizada de forma incremental — o monitoramento começa (ou para) quase imediatamente, sem reinício.
3. Pelo comando `/oraculo`, a ação é um **liga/desliga**: se o canal informado ainda não está sendo acompanhado, o monitoramento começa; se já está, o comando desliga. O bot responde com um aviso confirmando qual ação foi realizada ("Monitoramento Iniciado" ou "Monitoramento Parado").

### O que acontece a cada mensagem

Sempre que alguém posta em um canal monitorado, o Oráculo executa esta sequência:

1. **Filtro inicial.** Mensagens de sistema (entradas no servidor, fixar mensagem, etc.) e mensagens enviadas pelo próprio bot são ignoradas e nunca registradas.
2. **Recuperação de conteúdo "vazio".** É comum o Discord entregar uma mensagem ainda sem o texto carregado (especialmente as que demoram a renderizar). Se isso acontecer com uma mensagem de um usuário real (não bot, não sistema), o Oráculo busca a versão completa da mensagem antes de registrar, para não perder o conteúdo.
3. **Coleta dos detalhes.** Para cada mensagem o Oráculo guarda um conjunto rico de informações:
   - **Autor:** ID, nome de usuário, apelido de exibição, discriminador (quando houver), se é bot, e a URL da foto de perfil.
   - **Conteúdo:** o texto e o tamanho dele (número de caracteres).
   - **Anexos:** quantidade, e para cada um o nome, tamanho, URL e tipo do arquivo.
   - **Embeds:** quantidade, e para cada um título, descrição, URL e cor.
   - **Figurinhas (stickers):** quantidade, nome, ID e formato.
   - **Menções:** quantas pessoas e quantos cargos foram mencionados, e se a mensagem usou @everyone/@here.
   - **Contexto:** se é uma resposta (e a qual mensagem), se está numa thread, o tipo da mensagem e o horário de edição (se foi editada).
   - **Horário:** registrado em formato padrão (UTC) e também em horário de Brasília.
4. **Identificação de mensagens sem texto.** Mensagens que só têm figurinha, anexo, embed ou que chegam totalmente vazias (geralmente só um emoji/reação) são identificadas e marcadas como tal — elas contam para a análise mesmo sem texto.
5. **Gravação.** Os dados vão para o banco de dados compartilhado com o Dashboard. Em paralelo, o bot também escreve um arquivo de log por canal (um legível por humanos e um em formato estruturado) na máquina onde roda.
6. **Atualização do perfil do membro.** Se a mensagem for de um usuário real (não bot), o nome, apelido e foto de perfil atuais dele são enviados para o agregador de perfis — o que mantém os painéis de membros com a identidade visual sempre atualizada.

### Onde os dados aparecem

Todo esse registro alimenta os painéis de análise do Dashboard:

- **Insights:** análise automática da atividade do servidor.
- **Scoring de membros:** pontuação baseada em participação.
- **Análise de conteúdo:** métricas e tendências por canal.
- **Status do Oráculo:** quantos e quais canais estão sendo monitorados.

> Importante: o Oráculo registra **apenas mensagens novas**, enviadas enquanto o canal está ativo. Ele não importa o histórico anterior do canal. Quanto antes você ativar um canal, mais cedo os painéis começam a ter dados dele.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/oraculo canal:<#canal>` | Liga/desliga o monitoramento do canal informado. Se ainda não estava monitorado, começa a registrar; se já estava, para. O campo `canal` tem autocompletar com os canais de texto do servidor. Restrito a administradores. |

## Configuração

Há duas formas de ligar e desligar o Oráculo. As duas escrevem na mesma configuração do servidor, então ficam sempre em sincronia.

### Pelo Dashboard (recomendado)

No painel em [admin.delfus.app](https://admin.delfus.app), abra a **Configuração do Oráculo**:

1. Clique no seletor de canais e escolha um ou mais canais que o Oráculo deve monitorar (gerais, anúncios, suporte — os que fizerem sentido para suas métricas).
2. Os canais selecionados aparecem numa lista "Canais monitorados", com a contagem total. Você pode remover qualquer um pelo botão de "X".
3. Clique em **Salvar** para aplicar. Enquanto houver mudanças não salvas, o painel avisa e oferece o botão **Desfazer** para voltar ao estado salvo.
4. Assim que salva, a alteração passa a valer automaticamente — não é preciso reiniciar nada.

O painel é uma **seleção múltipla**: você gerencia a lista inteira de canais de uma vez (adiciona, remove, salva), em vez do liga/desliga por canal do comando.

### Pelo comando

Use `/oraculo` e informe o canal no campo `canal`. O comando alterna o estado daquele canal: liga se estava desligado, desliga se estava ligado. Ele responde confirmando a ação.

Não há limite documentado de canais — mas vale focar nos mais relevantes (veja a dica abaixo).

## Exemplos de uso

- **Acompanhar o canal mais movimentado:** adicione o canal #geral pelo Dashboard e salve. A partir daí, os painéis de Insights e Análise de conteúdo passam a mostrar quem mais participa e quando o canal fica mais ativo.
- **Medir engajamento em vários canais ao mesmo tempo:** no painel, selecione #geral, #anúncios e #suporte de uma vez e clique em Salvar. O scoring de membros passa a considerar a participação nesses três canais.
- **Ligar/desligar rápido por um canal só:** rode `/oraculo canal:#eventos` para começar a monitorar o canal de eventos durante uma campanha; ao terminar, rode `/oraculo canal:#eventos` de novo para parar de registrar.

## Requisitos

- **Permissões do bot no canal monitorado:** **Ver canal** e **Ler histórico de mensagens** — necessárias para enxergar as mensagens e recuperar o conteúdo completo das que chegam "vazias".
- **Quem usa o comando `/oraculo`:** precisa ser **Administrador** do servidor.
- **Quem configura pelo Dashboard:** precisa ter acesso àquele servidor no painel.

## Perguntas frequentes

**O Oráculo registra mensagens antigas do canal?**
Não. Ele captura apenas mensagens novas, enviadas a partir do momento em que o canal entra na lista de monitoramento. O histórico anterior não é importado.

**O bot guarda mensagens de outros bots?**
As mensagens do próprio Delfus e as mensagens de sistema são ignoradas. Mensagens de outros bots são registradas e marcadas como sendo de bot, mas elas não passam pelo recálculo de conteúdo "vazio" nem alimentam o perfil de membro.

**Configurei pelo painel e usei o comando — qual vale?**
Ambos escrevem na mesma lista de canais do servidor, então ficam sincronizados. A última ação (no painel ou pelo comando) é a que define o estado atual de cada canal.

**Preciso reiniciar o bot depois de mudar a configuração?**
Não. A mudança feita pelo Dashboard ou pelo comando passa a valer automaticamente, sem reinício.

!!! tip "Dica"
    Monitore só os canais que você realmente vai analisar. Cada canal ativo gera registro contínuo de tudo que é postado — concentrar nos canais mais relevantes (geral, anúncios, suporte) deixa os painéis de Insights e Scoring mais precisos e enxutos.

