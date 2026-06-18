# Cargos automáticos

Sabe aquele trabalho chato de dar cargo na mão pra cada pessoa que entra no servidor? O Delfus faz isso por você. Toda conta nova já chega com os cargos certos — acesso, cor, identidade visual — sem ninguém da equipe precisar levantar um dedo. E os bots ganham um conjunto separado, só deles.

![Cargos automáticos no painel do Delfus](../assets/dashboard/auto-roles.png){ .dx-shot loading=lazy }

*Cargos automáticos no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

A regra é simples: **alguém entra, o Delfus entrega os cargos.** Tudo acontece no momento da entrada, automaticamente.

Por baixo dos panos, ele dá uma conferida rápida em cada conta:

- **É pessoa ou é bot?** Humanos recebem a lista de cargos de membros; bots recebem a lista de bots. Cada um na sua.
- **Espera 1,5 segundo.** Um respiro proposital pra deixar o Discord "assentar" a entrada e segurar a onda quando muita gente entra de uma vez. Nessa fila, pessoas têm prioridade sobre bots.
- **Entrega os cargos.** Um por um, registrando "Auto-role" no log de auditoria do servidor.

Alguns cargos são pulados de propósito, sem drama: os que o membro já tem, os que foram apagados, e os que estão acima do Delfus na hierarquia (o Discord não deixa ele entregar cargo mais alto que o dele).

!!! example "Exemplo"
    Uma pessoa entra no seu servidor. Em poucos segundos ela já aparece com o cargo de "Membro", a cor da comunidade e acesso aos canais de bate-papo — tudo sem você fazer nada. Logo depois entra um bot novo: esse ganha só o cargo "Bots", separadinho, sem pegar as cores e acessos pensados pra gente de verdade.

!!! note "E se o Discord der uma engasgada?"
    Acontece. Se rolar uma instabilidade no meio da entrega, o Delfus lembra quais cargos já deu e tenta de novo de onde parou — até 5 vezes, sem nunca duplicar nada. Se o membro entrou e saiu correndo, ele percebe e para de tentar à toa.

## Comandos

Essa função não tem comando de barra. É tudo no painel — você configura uma vez e o Delfus cuida do resto sozinho, a cada entrada.

## Configuração

Tudo pelo Dashboard em [admin.delfus.app](https://admin.delfus.app), na seção **Cargos automáticos**:

1. **Ligue a função** no botão no topo do cartão.
2. **Escolha os cargos para Membros** (as pessoas). Pode colocar vários.
3. **Escolha os cargos para Bots.** Também pode colocar vários.
4. **Clique em Salvar.** Pronto — já vale pra próxima pessoa que entrar.

!!! tip "Pode deixar uma lista vazia"
    Quer cargo só pra membros e nada pra bots? Tranquilo. Quando uma das listas está vazia, o Delfus simplesmente não faz nada pra aquele tipo de conta.

Os seletores só mostram cargos que o Delfus consegue dar de verdade. Cargos gerenciados por integração (o cargo de outros bots, boosters do Nitro, etc.) não aparecem, porque o próprio Discord não deixa ninguém atribuir eles na mão.

!!! warning "Hierarquia importa"
    O Delfus precisa da permissão **Gerenciar cargos**, e o **cargo dele tem que estar acima** de tudo que ele vai entregar na lista de cargos do servidor. Esse é, de longe, o motivo número 1 de "tô configurando e o cargo não vem".

## Exemplos

!!! example "Cargo de Membro automático"
    Crie um cargo "Membro" com acesso aos canais públicos e jogue ele na lista de Membros. A partir daí, toda pessoa que entrar já enxerga e participa do servidor — sem fila, sem pegar cargo na mão.

!!! example "Bots agrupados e isolados"
    Crie um cargo "Bots" com cor própria, posicionado abaixo dos cargos humanos, e use só na lista de Bots. Todo bot que entrar fica visualmente separado num cantinho, sem ganhar as cores e acessos que são da galera.

!!! example "Boas-vindas com cor"
    Coloque um cargo de cor + um cargo "Comunidade" na lista de Membros. Os novatos já chegam com a cara do servidor e acesso ao bate-papo — e você deixa os canais avançados pra cargos que se conquistam depois.

## Perguntas frequentes

**Um dos cargos não foi dado. Por quê?**
Quase sempre é hierarquia: o cargo está acima do Delfus na lista. Mova o cargo do Delfus pra cima dele. Também pode ser cargo apagado, falta da permissão "Gerenciar cargos", ou o membro já ter aquele cargo.

**Demora pra aplicar?**
Tem um atraso de propósito (cerca de 1,5 segundo), além do tempo normal do Discord. Na prática, o membro recebe tudo em poucos segundos.

**Mudei a config — preciso reiniciar o bot?**
Não. O Delfus lê a configuração na hora, a cada entrada. O que você salvar já vale pra próxima pessoa.

**E se o membro entrar e sair num piscar de olhos?**
O Delfus tenta de novo automaticamente e lembra o que já entregou, sem duplicar. Se o membro saiu antes de receber, ele encerra a tentativa e não fica insistindo.

!!! tip "Dica"
    Use a separação entre membros e bots a seu favor: deixe o cargo "Bots" **abaixo** dos cargos humanos e com permissões restritas. Os bots entram agrupados e isolados, e as cores e acessos ficam reservados pras pessoas. E nunca esqueça: o cargo do Delfus precisa ficar **acima** de tudo que ele vai entregar.
