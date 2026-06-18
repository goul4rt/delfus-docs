# Oráculo

Quer saber quem mais movimenta cada canal do seu servidor e quando ele bomba? O Oráculo é o "gravador" do Delfus: você escolhe os canais que quer acompanhar e, daí em diante, ele registra tudo que é postado. Esse registro vira a matéria-prima dos painéis do Dashboard — atividade, scoring de membros e análise de conteúdo.

## Como funciona

Você aponta os canais que quer acompanhar. A partir desse momento, cada mensagem nova enviada neles é registrada automaticamente — sem você fazer mais nada.

Um detalhe importante: o Oráculo só grava o que acontece **depois** que você liga o canal. Ele não puxa o histórico antigo. Então, quanto antes você ativar, mais cedo os painéis começam a ter dados.

A cada mensagem nova, ele guarda bastante coisa: quem postou (nome, apelido, foto), o texto, anexos, embeds, figurinhas, menções, se é resposta, se está numa thread e o horário (em UTC e em horário de Brasília). Mensagens que só têm figurinha, anexo ou emoji também contam — mesmo sem texto.

Algumas coisas ele ignora de propósito: mensagens de sistema (entrou no servidor, fixou mensagem) e as mensagens do próprio Delfus nunca são registradas.

!!! example "Exemplo"
    Você liga o `#geral` no Oráculo às 14h. A mensagem do João às 14h05 é registrada na hora — com o texto, a foto dele e o horário. Já a conversa que rolou de manhã, antes de você ligar, não entra: o Oráculo só grava daqui pra frente.

!!! note "E os outros bots?"
    Mensagens de outros bots são registradas e marcadas como "de bot". Só as mensagens do próprio Delfus e as de sistema é que ficam de fora.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/oraculo canal:<#canal>` | Liga ou desliga o monitoramento daquele canal. Se ainda não estava ligado, começa a registrar; se já estava, para. O campo `canal` tem autocompletar. Só administradores podem usar. |

## Configuração

Tem dois jeitos de ligar e desligar o Oráculo. Os dois escrevem na mesma configuração, então estão sempre em sincronia — use o que for mais prático no momento.

### Pelo Dashboard (recomendado)

Em [admin.delfus.app](https://admin.delfus.app), abra a **Configuração do Oráculo**:

1. Clique no seletor e escolha um ou mais canais que o Oráculo deve acompanhar.
2. Os canais escolhidos aparecem numa lista "Canais monitorados". Para tirar algum, é só clicar no "X".
3. Clique em **Salvar**. Enquanto houver mudanças não salvas, o painel avisa e oferece um botão **Desfazer**.
4. Pronto — a mudança vale na hora, sem reiniciar nada.

O Dashboard é uma seleção múltipla: você gerencia a lista inteira de uma vez, em vez de ir canal por canal.

### Pelo comando

Rode `/oraculo` e escolha o canal. O comando funciona como um interruptor: liga se estava desligado, desliga se estava ligado. O bot responde confirmando o que fez ("Monitoramento Iniciado" ou "Monitoramento Parado").

## Exemplos

!!! example "Acompanhar o canal mais movimentado"
    Adicione o `#geral` pelo Dashboard e salve. Daí em diante, os painéis de Insights e Análise de conteúdo passam a mostrar quem mais participa e em que horários o canal fica mais agitado.

!!! example "Medir engajamento em vários canais de uma vez"
    No painel, selecione `#geral`, `#anúncios` e `#suporte` juntos e clique em Salvar. O scoring de membros passa a considerar a participação nesses três canais ao mesmo tempo.

!!! example "Ligar e desligar rápido para uma campanha"
    Vai rodar um evento? Rode `/oraculo canal:#eventos` para começar a registrar. Quando a campanha acabar, rode `/oraculo canal:#eventos` de novo para parar.

## Onde os dados aparecem

Todo esse registro alimenta os painéis do Dashboard:

- **Insights** — análise automática da atividade do servidor.
- **Scoring de membros** — pontuação baseada na participação.
- **Análise de conteúdo** — métricas e tendências por canal.
- **Status do Oráculo** — quantos e quais canais estão sendo monitorados.

## Requisitos

- **No canal monitorado**, o Delfus precisa de permissão para **Ver canal** e **Ler histórico de mensagens**.
- Para usar o comando `/oraculo`, você precisa ser **Administrador** do servidor.
- Para configurar pelo Dashboard, você precisa ter acesso àquele servidor no painel.

## Perguntas frequentes

**O Oráculo registra mensagens antigas?**
Não. Só as novas, enviadas depois que você ligou o canal. O histórico anterior não é importado.

**Configurei pelo painel e usei o comando — qual vale?**
Os dois escrevem na mesma lista, então ficam sincronizados. Vale a última ação que você fez.

**Preciso reiniciar o bot depois de mudar a configuração?**
Não. A mudança passa a valer na hora, tanto pelo Dashboard quanto pelo comando.

!!! tip "Dica"
    Monitore só os canais que você realmente vai analisar. Cada canal ligado gera registro contínuo de tudo que é postado — focar nos mais relevantes (geral, anúncios, suporte) deixa os painéis mais precisos e enxutos.

