---
description: "Recompensas de boost no Delfus: mensagem de agradecimento e VIP automático para quem impulsiona seu servidor Discord, com renovação enquanto o boost durar."
---

# Recompensas de boost

Quando alguém impulsiona o seu servidor Discord, o Delfus agradece sozinho e ainda pode dar um VIP de presente pra quem apoiou. Sem a moderação precisar mexer um dedo.

![Recompensas de boost no painel do Delfus](../assets/dashboard/boost.webp){ .dx-shot width="1200" height="1227" fetchpriority=high }

*Recompensas de boost no [Dashboard](https://admin.delfus.app) (exemplo com dados de demonstração).*

## Como funciona

O Delfus acompanha os boosts em tempo real. Assim que o Discord avisa que alguém começou ou deixou de impulsionar, o bot reage na hora.

Quando alguém dá boost, você escolhe o que acontece:

- **Mensagem de agradecimento:** o bot publica, no canal que você definir, a mensagem que você montou. Pode ser texto simples ou um embed com imagem e até 3 botões de link.
- **VIP automático:** a pessoa ganha na hora o plano VIP que você escolher, válido pelos dias que você definir (padrão de 30 dias).

As duas opções são independentes. Ative só a mensagem, só o VIP, ou os dois.

Enquanto o boost continuar ativo, o Delfus renova o VIP sozinho. A pessoa nunca fica sem o benefício no meio do caminho.

!!! example "Exemplo"
    A Maria impulsiona o servidor. Em segundos aparece no canal de avisos: *"Maria acabou de dar boost! Agora temos 12 boosts"*. Ao mesmo tempo, ela recebe o cargo VIP de booster. O bot cuidou de tudo.

### Variáveis para as mensagens

Use estas variáveis em qualquer campo de texto. O bot troca pelo valor real no envio.

| Variável | Vira |
| --- | --- |
| `{{@user}}` | Menção da pessoa que deu boost (notifica ela) |
| `{{user}}` | Nome de exibição da pessoa (sem notificar) |
| `{{server}}` | Nome do servidor |
| `{{memberCount}}` | Total de membros |
| `{{boostCount}}` | Total de boosts ativos |
| `{{boostTier}}` | Nível de boost do servidor (0 a 3) |
| `{{boostTierName}}` | Nome do nível (`Nenhum`, `Tier 1`, `Tier 2`, `Tier 3`) |

!!! note "E quando alguém para de impulsionar?"
    O Delfus também percebe quando alguém remove o boost e pode mandar uma mensagem de despedida, com as mesmas opções de personalização. Por enquanto essa parte é configurada nos bastidores do bot. O painel ainda não traz essa opção na interface.

## Comandos

Essa funcionalidade não tem comandos de barra. Toda a configuração é feita pelo [Dashboard](https://admin.delfus.app).

## Configuração

A configuração fica no Dashboard, na seção **Boost do Servidor**, separada por servidor. A tela tem duas abas: **Boost** e **VIP**.

!!! warning "Antes de tudo, ative no Discord"
    Vá em **Configurações do Servidor → Visão geral / Sistema** e ligue a opção **"Enviar uma mensagem quando alguém impulsionar este servidor"**, escolhendo um canal. Sem isso, o aviso de boost pode não chegar de forma confiável.

### Aba Boost (a mensagem de agradecimento)

1. Ligue o interruptor **Ativo** no topo do cartão.
2. **Canal:** onde a mensagem vai aparecer.
3. **Estilo:** escolha **Texto Simples** ou **Rich Embed** (cartão com título, cor, imagem etc.).
4. **Imagem (opcional):** cole a URL de uma imagem.
5. **Botões de link (até 3):** cada um com um texto e uma URL.

Use as variáveis da tabela acima em qualquer campo de texto. O painel também mostra todas elas à mão.

### Aba VIP (a recompensa automática)

1. Ligue o interruptor **Ativo** no cartão **VIP por Boost**.
2. **Tier VIP:** qual plano a pessoa ganha. Você precisa já ter pelo menos um plano VIP criado no servidor.
3. **Duração (dias):** quanto tempo o VIP dura a cada concessão. De 1 a 365 dias, padrão de 30.

Ao terminar, clique em **Salvar**. O botão **Deletar** remove a configuração inteira (mensagens e VIP) de uma vez.

## Exemplos

!!! example "Agradecer cada novo boost na frente de todo mundo"
    Ative a aba Boost, escolha o canal de avisos e use algo como:
    `{{@user}} acabou de dar boost! Agora temos {{boostCount}} boosts e estamos no {{boostTierName}}`
    Toda vez que alguém impulsionar, o servidor vê o agradecimento e a pessoa é marcada.

!!! example "Premiar boosters com VIP no piloto automático"
    Crie um plano VIP só pra boosters, vá na aba VIP, selecione esse plano e deixe a duração em 30 dias. Quem impulsiona ganha o VIP na hora, e o bot renova sozinho enquanto o boost continuar. A moderação não precisa acompanhar quem ainda está impulsionando.

!!! example "Uma mensagem caprichada com botões"
    Monte a mensagem como embed, com a cor da marca do servidor e uma imagem comemorativa. Adicione botões de link como "Saiba mais sobre boost" ou "Entrar no canal VIP", apontando pra uma página ou canal de regras.

## Perguntas frequentes

### O membro perde o VIP assim que ele vence, mesmo continuando a impulsionar?
Não. A cada 6 horas o bot revisa quem ainda está com boost ativo e renova o VIP de quem continua impulsionando, mesmo que a concessão anterior já tenha vencido. O benefício só acaba quando o VIP vence e o boost some.

### Posso usar texto e embed ao mesmo tempo?
Você escolhe um estilo por mensagem. No estilo embed, se você também preencher o campo de texto, o bot manda o texto junto com o embed. No estilo texto, vai só o texto (com a imagem como anexo, se houver).

### Recebi uma reclamação de que a pessoa foi notificada sem querer. Por quê?
A variável `{{@user}}` cria uma menção de verdade e notifica a pessoa. Para mostrar só o nome sem incomodar ninguém, use `{{user}}`.

### Existe comando de barra pra configurar isso?
Não. Mensagens e VIP são configurados só pelo Dashboard.

!!! tip "Dica"
    Deixe o VIP ativo com duração perto de 30 dias. Como o bot renova a cada 6 horas enquanto o boost estiver de pé, a pessoa só perde o benefício quando para de impulsionar de verdade. O VIP vira um incentivo contínuo pra manter o boost.

