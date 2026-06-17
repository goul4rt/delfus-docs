# Famílias VIP

As Famílias VIP são grupos exclusivos que membros assinantes podem criar e gerenciar dentro do servidor. Cada família ganha um cargo próprio personalizável (nome, cor e ícone), e o dono pode convidar outros membros para fazerem parte dele — uma recompensa de prestígio amarrada à assinatura VIP.

## Como funciona

A família é uma das recompensas que vêm com determinados planos VIP. Quem tem uma assinatura ativa com esse benefício pode criar e administrar sua própria família. Todo o uso acontece pelo comando `/familia`, que abre um painel interativo privado onde o membro faz tudo por botões — sem precisar decorar subcomandos.

1. **Criar a família.** Um assinante com slot de família disponível usa `/familia`, abre o painel e cria a família dando um nome a ela. O bot cria automaticamente um **cargo do Discord** com esse nome (acrescido de um prefixo configurável, por padrão um emoji de casa) e atribui o cargo ao dono. Cada recompensa de família da assinatura equivale a um slot — o membro só consegue criar enquanto tiver slots livres.
2. **Personalizar.** Ainda pelo painel, o dono pode editar o nome, a descrição, a cor do cargo (sólida, em gradiente ou holográfica) e o ícone do cargo. Imagens grandes são ajustadas automaticamente para caber no limite do Discord; ícones em formato ou tamanho inválido são recusados com uma explicação.
3. **Convidar membros.** O dono escolhe um membro para convidar. O convidado recebe uma **mensagem privada (DM)** com botões de Aceitar e Recusar. Esse convite tem prazo de validade (por padrão 48 horas) e expira sozinho se não for respondido. Se a DM do convidado estiver fechada, o bot avisa o dono que não conseguiu entregar e o convite é cancelado para permitir nova tentativa.
4. **Entrar na família.** Ao aceitar o convite pela DM, o membro recebe o cargo da família na hora. Existe um limite de membros por família — definido pela recompensa e por um teto do servidor —, e convites que ultrapassariam esse limite são bloqueados.
5. **Gerenciar.** O dono pode remover membros ou excluir a família inteira; ao excluir, o cargo é apagado e removido de todos. Membros comuns podem sair voluntariamente a qualquer momento. O dono não pode sair nem se remover — para encerrar, precisa excluir a família.
6. **Congelamento por expiração do VIP.** A família depende da assinatura VIP do dono. **Quando o VIP expira**, o bot **congela** automaticamente todas as famílias daquela assinatura: o cargo é removido de todos os membros e a família fica bloqueada para edições e convites. Quando o VIP é reativado, o dono usa o painel para **descongelar** a família e os cargos são re-atribuídos a todos os membros que ainda estão no servidor.

## Configuração

A feature de Famílias faz parte do sistema **VIP** e é configurada pelo **Dashboard** (https://admin.delfus.app), na seção de configurações de VIP. Lá o dono do servidor define:

- O **prefixo** que vai na frente do nome de cada cargo de família.
- O **limite máximo de membros** por família (teto do servidor).
- O **prazo de validade dos convites** (em horas).
- Um **cargo-âncora** opcional, que determina a posição em que os cargos de família são criados na lista de cargos do servidor.

Para que membros possam efetivamente criar famílias, é preciso também ter um plano VIP que inclua a recompensa de família (configurado na mesma área de VIP do painel).

Para os membros, todo o uso é feito pelo comando:

- `/familia` — abre o painel para criar, listar, convidar, editar, remover, sair, excluir e descongelar.

## Requisitos

- O bot precisa da permissão **Gerenciar Cargos**, já que cria, edita e remove os cargos de cada família.
- O cargo do bot deve estar **acima** dos cargos das famílias na hierarquia, para conseguir gerenciá-los.
- O servidor não pode ter atingido o limite de 250 cargos do Discord.
- Para usar a feature, o membro precisa de uma **assinatura VIP ativa** que inclua a recompensa de família.

!!! tip
    Peça aos membros que mantenham as DMs do servidor abertas — os convites de família chegam por mensagem privada, e com a DM fechada o convite não é entregue.
