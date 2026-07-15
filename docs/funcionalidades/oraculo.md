---
description: "Oráculo do Delfus: monitore canais do Discord e registre mensagens para alimentar insights, scoring de membros e análise de conteúdo no painel."
---

# Oráculo

Saiba quem movimenta cada canal e em que horários ele bomba. O Oráculo do Delfus grava as mensagens dos canais do Discord que você escolher, e esse registro alimenta os painéis do Dashboard: atividade, scoring de membros e análise de conteúdo.

## Como funciona

Você aponta os canais que quer acompanhar. A partir daí, cada mensagem nova é registrada automaticamente.

O Oráculo só grava o que acontece depois que você liga o canal. Ele não puxa o histórico antigo. Quanto antes você ativar, mais cedo os painéis ganham dados.

A cada mensagem, ele guarda: quem postou (nome, apelido, foto), o texto, anexos, embeds, figurinhas, menções, se é resposta, se está numa thread e o horário (UTC e Brasília). Mensagens só com figurinha, anexo ou emoji também contam.

Ele ignora de propósito as mensagens de sistema (entrou no servidor, fixou mensagem) e as do próprio Delfus. Essas nunca são registradas.

!!! example "Exemplo"
    Você liga o `#geral` às 14h. A mensagem do João às 14h05 é registrada na hora, com o texto, a foto dele e o horário. A conversa da manhã, antes de você ligar, não entra.

!!! note "E os outros bots?"
    Mensagens de outros bots são registradas e marcadas como "de bot". Só as do próprio Delfus e as de sistema ficam de fora.

## Comandos

| Comando | O que faz |
| --- | --- |
| `/oraculo canal:<#canal>` | Liga ou desliga o monitoramento do canal. Funciona como interruptor: liga se estava desligado, desliga se estava ligado. O campo `canal` tem autocompletar. Só administradores. |

## Configuração

Dá pra ligar e desligar de dois jeitos. Os dois escrevem na mesma configuração e ficam sempre em sincronia. Use o que for mais prático.

### Pelo Dashboard (recomendado)

Em [admin.delfus.app](https://admin.delfus.app), abra a **Configuração do Oráculo**:

1. Clique no seletor e escolha um ou mais canais para acompanhar.
2. Os canais aparecem na lista "Canais monitorados". Para tirar um, clique no "X".
3. Clique em **Salvar**. Enquanto houver mudanças não salvas, o painel avisa e oferece um botão **Desfazer**.
4. A mudança vale na hora, sem reiniciar nada.

O Dashboard é uma seleção múltipla: você gerencia a lista inteira de uma vez, em vez de ir canal por canal.

### Pelo comando

Rode `/oraculo` e escolha o canal. Liga se estava desligado, desliga se estava ligado. O bot confirma o que fez ("Monitoramento Iniciado" ou "Monitoramento Parado").

## Exemplos

!!! example "Acompanhar o canal mais movimentado"
    Adicione o `#geral` pelo Dashboard e salve. Os painéis de Insights e Análise de conteúdo passam a mostrar quem mais participa e em que horários o canal fica mais agitado.

!!! example "Medir engajamento em vários canais de uma vez"
    No painel, selecione `#geral`, `#anúncios` e `#suporte` juntos e salve. O scoring de membros passa a considerar a participação nos três canais.

!!! example "Ligar e desligar rápido para uma campanha"
    Vai rodar um evento? Rode `/oraculo canal:#eventos` para começar a registrar. Quando acabar, rode o mesmo comando de novo para parar.

## Onde os dados aparecem

Todo o registro alimenta os painéis do Dashboard:

- **Insights:** análise automática da atividade do servidor.
- **Scoring de membros:** pontuação baseada na participação.
- **Análise de conteúdo:** métricas e tendências por canal.
- **Status do Oráculo:** quantos e quais canais estão sendo monitorados.

## Requisitos

- No canal monitorado, o Delfus precisa de permissão para **Ver canal** e **Ler histórico de mensagens**.
- Para usar o comando `/oraculo`, você precisa ser **Administrador** do servidor.
- Para configurar pelo Dashboard, você precisa ter acesso àquele servidor no painel.

## Perguntas frequentes

### O Oráculo registra mensagens antigas?
Não. Só as novas, enviadas depois que você ligou o canal. O histórico anterior não é importado.

### Configurei pelo painel e usei o comando, qual vale?
Os dois escrevem na mesma lista e ficam sincronizados. Vale a última ação.

### Preciso reiniciar o bot depois de mudar a configuração?
Não. A mudança vale na hora, tanto pelo Dashboard quanto pelo comando.

!!! tip "Dica"
    Monitore só os canais que você vai analisar. Cada canal ligado gera registro contínuo de tudo que é postado. Focar nos mais relevantes (geral, anúncios, suporte) deixa os painéis mais precisos e enxutos.

