# Anti-raid

O Anti-raid detecta e barra ataques coordenados de divulgação de golpes (scams) por imagem no seu servidor — aqueles posts em massa de "sorteio do MrBeast", "código promocional de crypto" e afins. Quando identifica um ataque, ele apaga a mensagem, pune o autor e avisa a sua moderação, tudo automaticamente.

## Como funciona

O módulo entra em ação sempre que alguém envia uma **mensagem com imagem** em um servidor onde o Anti-raid está configurado. A partir daí ele combina várias camadas de checagem:

1. **Reincidência rápida.** Se o autor já foi flagrado como golpista nos últimos 5 minutos, a nova mensagem é apagada na hora — sem reanalisar nada — e um alerta preventivo é enviado ao canal de moderação (no máximo um a cada 30 segundos por usuário).

2. **Velocidade (flood e enxame).** Se a checagem de velocidade estiver ligada, o bot acompanha o ritmo de envio de imagens:
   - **Flood de um usuário:** se a mesma pessoa espalha imagens por vários canais distintos em uma janela curta (por padrão, 3 canais em 10 segundos), isso é tratado como ataque de alta confiança e o autor é **banido**.
   - **Enxame de contas novas:** se várias contas recém-entradas (por padrão, 5 contas com menos de 24h no servidor) começam a postar imagens ao mesmo tempo, o bot aplica um **bloqueio brando**: ativa o modo lento (slowmode, por padrão 30s) no canal afetado e avisa a moderação. Ele **nunca** bane em massa de forma automática nesse caso.

3. **Reconhecimento da imagem do golpe.** O bot compara cada imagem com uma base de artes de golpe conhecidas (referências internas + golpes que ele já aprendeu). Também detecta **floods de imagens idênticas** (4 ou mais imagens praticamente iguais na mesma mensagem). Se bater, a mensagem é considerada um ataque.

4. **Aprendizado contínuo.** Quando uma imagem nova não bate com nada conhecido, o bot lê o texto dela em segundo plano (sem travar a resposta) procurando por palavras típicas de golpe — promoções de crypto, "resgate seu prêmio", códigos de bônus, urgência ("será apagado em 1 hora"), nomes de celebridades, etc. Se reconhece o padrão, ele **memoriza** aquela arte para barrá-la instantaneamente na próxima vez.

Quando qualquer uma dessas camadas confirma um ataque, o bot:

1. **Apaga a mensagem** ofensiva.
2. **Marca o autor como golpista por 5 minutos**, para apagar tudo que ele postar nesse intervalo sem reanalisar.
3. **Aplica a punição configurada** — avisar, silenciar, expulsar ou banir (o padrão é **banir**).
4. **Avisa o canal de moderação** que você definiu, dizendo qual módulo disparou, quem foi punido, qual ação foi tomada e o motivo.
5. **Limpa as mensagens recentes** daquele usuário (dos últimos 10 minutos) em todos os canais, para remover o que ele já tinha espalhado.

Se qualquer etapa falhar (download da imagem, análise, etc.), o bot escolhe **não punir por engano** — ou seja, na dúvida ele deixa passar em vez de aplicar uma punição indevida.

## Configuração

A configuração é feita **pelo Dashboard**, em [admin.delfus.app](https://admin.delfus.app), na seção **Anti-raid**. Lá você define:

- O **canal de alertas** onde a moderação recebe os avisos (obrigatório para o módulo funcionar).
- A **ação de punição** aplicada quando um golpe é detectado (avisar, silenciar, expulsar ou banir) e, no caso de silenciar, a duração.
- A **checagem de velocidade**: se está ligada e os limites de flood (canais por usuário e janela de tempo), de enxame (quantidade de contas novas e idade máxima para contar como "conta nova") e o slowmode aplicado no bloqueio brando.

Não há comando de barra para esta funcionalidade — toda a configuração passa pelo painel.

## Requisitos

Para o Anti-raid agir, o bot precisa de permissões compatíveis com as ações que ele executa:

- **Gerenciar mensagens** — para apagar mensagens e limpar o histórico recente do golpista.
- **Expulsar** e/ou **Banir membros** — conforme a punição escolhida.
- **Silenciar membros (timeout)** — se a ação configurada for silenciar.
- **Gerenciar canais** — para ativar o modo lento (slowmode) durante um enxame.

Além disso, o cargo do bot precisa estar **acima** do cargo dos membros que ele deve punir; caso contrário a punição não pode ser aplicada.

!!! tip
    Defina o canal de alertas em um canal só da moderação. É por ele que você acompanha cada bloqueio, o que permite revisar rapidamente e reverter manualmente caso algum membro legítimo seja afetado.
