# Encurtador de links

Transforma URLs longas em links curtos (`delfus.app/s/CODIGO`) com estatísticas de cliques detalhadas. Cada link pode ser vinculado ao seu servidor, ter senha, data de expiração, limite de cliques e até uma página de destino personalizada — tudo gerenciado pelo painel.

![Encurtador de links no painel do Delfus](../assets/dashboard/links.png){ .dx-shot loading=lazy }

*Encurtador de links no [Dashboard](https://admin.delfus.app) — exemplo com dados de demonstração.*

## Como funciona

O encurtador é gerenciado inteiramente pelo painel web (não há comando de Discord). O fluxo é:

1. **Criação.** Você cola a URL de destino e, opcionalmente, define um título, descrição, tags, senha, expiração, limite de cliques e parâmetros de campanha (UTM). O sistema gera um código curto automático — ou você escolhe um **código personalizado** (3 a 12 caracteres). O link fica acessível em `delfus.app/s/CODIGO`.
2. **Vínculo com o servidor.** Ao criar pelo painel de um servidor, o link fica associado àquele servidor — assim toda a equipe vê e gerencia os mesmos links na lista. Links criados fora do contexto de um servidor ficam pessoais (só seus).
3. **Acesso (clique).** Quando alguém abre o link curto, o Delfus registra o clique e redireciona para o destino. Antes de redirecionar, ele aplica as regras configuradas:
   - Se o link tem **senha**, o visitante é levado a uma página para digitá-la antes de seguir.
   - Se for um link de **página de destino** (landing page), o visitante vê uma página personalizada (com título, imagem, cores e até efeitos visuais como confete) em vez de ir direto ao destino.
   - Se o link está **inativo**, **expirado** ou já **atingiu o limite de cliques**, o visitante vê uma página informando que o link não está mais disponível.
4. **Coleta de dados do clique.** A cada acesso, o Delfus registra (de forma anônima por visitante) país/cidade aproximados, dispositivo, navegador, sistema operacional, idioma, origem do tráfego (rede social, busca, e-mail, direto) e os parâmetros de campanha. Cliques de robôs e prévias de links (WhatsApp, Discord, etc.) são identificados. Visitantes repetidos são contados separadamente de visitantes únicos.
5. **Estatísticas.** No painel você acompanha o total de cliques, cliques únicos, evolução por dia, distribuição por hora, e os rankings de país, dispositivo, navegador, sistema e origem — incluindo um fluxo de cliques recentes quase em tempo real.

Para evitar abuso, cada link tem um limite de acessos por minuto a partir de um mesmo visitante; ao estourar, o redirecionamento é temporariamente bloqueado.

## Configuração

Toda a gestão é feita pelo Dashboard, em **https://admin.delfus.app** (seção de links). Por lá você cria, edita, ativa/desativa, lista (com busca, filtro por tag e ordenação) e exclui links, além de abrir as estatísticas detalhadas de cada um. Não há comando de barra (`/`) no bot para essa funcionalidade.

Opções disponíveis ao criar/editar um link:

- **URL de destino** (para links de redirecionamento).
- **Código personalizado** (3–12 caracteres; letras e números, mais `_` e `-`).
- **Senha** de acesso.
- **Expiração** por data e/ou **limite de cliques**.
- **Tags** para organização.
- **Parâmetros de campanha (UTM)**, adicionados automaticamente ao destino.
- **Prévia social** personalizada (título, descrição e imagem que aparecem ao compartilhar).
- **Página de destino** (landing page) com modelo, cores, imagem e efeito visual.

## Requisitos

É necessário estar autenticado no painel. Para gerenciar os links de um servidor, você precisa ter acesso ao dashboard daquele servidor. O bot do Discord não precisa de nenhuma permissão especial para essa funcionalidade — ela roda no painel/site, não dentro do servidor.

!!! tip
    Use os parâmetros UTM ao divulgar o link em campanhas diferentes (Twitter, Discord, e-mail): o painel mostra de onde vieram os cliques, ajudando a saber qual divulgação trouxe mais gente.
