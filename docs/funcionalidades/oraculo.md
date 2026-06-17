# Oráculo

O Oráculo monitora um ou mais canais do servidor e registra todas as mensagens enviadas neles, alimentando os painéis de análise (insights e análise de conteúdo) do Dashboard. Serve para entender o que e quem mais movimenta um canal.

## Como funciona

O Oráculo funciona como um "gravador" de canais. Você escolhe quais canais quer acompanhar e, a partir daí, tudo o que for postado neles passa a ser registrado automaticamente.

1. Você marca um canal para ser monitorado (pelo painel ou pelo comando). A escolha fica salva nas configurações do servidor, então continua valendo mesmo depois de o bot reiniciar.
2. Cada nova mensagem postada em um canal monitorado é capturada na hora. Se a mensagem chegar "vazia" (caso comum de mensagens que demoram a carregar), o bot busca o conteúdo completo antes de registrar.
3. Para cada mensagem, o Oráculo guarda os detalhes: quem enviou (nome, apelido, foto), o texto, anexos, embeds, figurinhas, menções, se é uma resposta, horário, e mais. Mensagens sem texto (só emoji, anexo ou figurinha) também são identificadas e marcadas.
4. Esses dados ficam disponíveis para os painéis de análise do Dashboard — como visão geral de atividade, análise de conteúdo e o status do próprio Oráculo —, onde você consegue ver tendências de participação e o que mais acontece nos canais acompanhados.
5. Repetir a ação sobre um canal já monitorado desliga o monitoramento daquele canal. A partir daí, novas mensagens dele deixam de ser registradas.

O monitoramento vale só para mensagens novas, enviadas enquanto o canal está ativo — ele não puxa o histórico anterior do canal.

## Configuração

Há duas formas de ligar/desligar:

- **Pelo Dashboard** ([admin.delfus.app](https://admin.delfus.app)): defina a lista de canais que o Oráculo deve monitorar nas configurações do servidor. A mudança passa a valer automaticamente, sem precisar reiniciar nada.
- **Pelo comando** `/oraculo`: informe o canal a monitorar. Se o canal ainda não estiver sendo acompanhado, o monitoramento começa; se já estiver, o comando desliga. O comando avisa qual ação foi feita.

O comando `/oraculo` é restrito a administradores do servidor.

## Requisitos

- O bot precisa das permissões **Ver canal** e **Ler histórico de mensagens** no canal que você quer monitorar.
- Quem usa o comando `/oraculo` precisa ser **Administrador** do servidor.

!!! tip
    Monitore só os canais que você realmente quer analisar. Cada canal ativo gera registro contínuo de tudo que é postado — focar nos canais mais relevantes deixa os painéis mais úteis e enxutos.
