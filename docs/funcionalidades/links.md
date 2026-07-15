---
description: "Encurtador de links do Delfus: crie links curtos com estatísticas de cliques, senha, expiração e UTMs para divulgar no Discord e redes sociais."
---

# Encurtador de links

Transforme uma URL longa num link curto do Delfus tipo `link.delfus.app/s/CODIGO` e veja quem clicou: país, dispositivo e de onde veio (Twitter, Discord e outros). Bom pra divulgar votações, campanhas e anúncios e medir o que funcionou.

![Encurtador de links no painel do Delfus](../assets/dashboard/links.webp){ .dx-shot width="1200" height="1227" fetchpriority=high }

*Encurtador de links no [Dashboard](https://admin.delfus.app) (exemplo com dados de demonstração).*

## Como funciona

Você cria o link pelo painel e escolhe o destino. A cada clique, o Delfus registra de onde veio. Não precisa de comando no Discord.

Na criação, escolha entre dois tipos:

- **Redirecionamento**: o visitante clica e vai direto pra URL que você definiu.
- **Landing Page**: em vez de mandar pra fora, o Delfus mostra uma página personalizada (título, imagem, cores e até confetes). Boa pra confirmação de voto, anúncios e páginas de "obrigado".

!!! example "Exemplo"
    Você vai abrir uma votação. Cria um link curto que aponta pro formulário, divulga nos canais e, no dia seguinte, abre o painel: 340 cliques, 210 pessoas diferentes, a maioria do Brasil, pelo celular. Em segundos você sabe o alcance real.

Os números aparecem rápido. Cada clique entra na hora e o Delfus consolida as estatísticas ao longo do dia.

## Comandos

Essa funcionalidade vive 100% no painel web. **Não há comando de barra (`/`) no Discord** pro encurtador.

## Configuração

Tudo acontece no Dashboard, em **[https://admin.delfus.app](https://admin.delfus.app)**, na seção de links. Lá você cria, lista (com busca por título/código/URL, filtro por tag e ordenação), edita, ativa/desativa, exclui e abre as estatísticas de cada link.

**O básico pra criar um link:**

- **Tipo**: redirecionamento ou landing page.
- **URL de destino** (obrigatória no redirecionamento).
- **Título** pra você se organizar (o visitante não vê).
- **Tags** separadas por vírgula, pra filtrar a lista depois.
- **Código personalizado**: escolha o final do link ou deixe o Delfus gerar um automaticamente.

!!! note "Sobre o código curto"
    Em branco, o sistema cria um código fácil de ler (sem caracteres confusos como `0`, `O`, `I` ou `l`). Pra escolher o seu, use de 3 a 12 caracteres: letras, números, `_` e `-`. Não vale repetir um código que já existe.

**Opções avançadas:**

- **Proteção**: senha de acesso, data de expiração e limite máximo de cliques.
- **Prévia em redes sociais** (só redirecionamento): personalize o card que aparece quando o link é colado no Discord ou no Twitter (título, descrição e imagem).
- **Parâmetros UTM** (só redirecionamento): rótulos que o Delfus gruda na URL de destino pra rastrear de qual campanha veio cada clique.

**Se escolher Landing Page**, você monta a página: um **template** (Confirmação de Voto, Anúncio, Agradecimento ou Personalizado), título e descrição, imagem, cores (fundo, texto e destaque) e um **efeito visual** (confetti, fogos ou brilhos). Dá pra mostrar ou esconder o botão de compartilhar e a marca do Delfus.

!!! note "Vínculo com o servidor"
    Links criados a partir do painel de um servidor ficam **daquele servidor**: toda a equipe com acesso vê e gerencia os mesmos links. Os criados fora desse contexto ficam **pessoais**, só você enxerga.

## Exemplos

!!! example "Descobrir qual divulgação trouxe mais gente"
    Você anuncia um evento no Twitter e no Discord. Cria o link com UTMs diferentes pra cada canal. No fim do dia, o painel mostra: o Discord trouxe 80% dos cliques e o Twitter quase nada. Da próxima vez, você sabe onde investir.

!!! example "Link com senha pra conteúdo de membros"
    Você tem um link só pra apoiadores. Adiciona uma senha na criação. Quem clicar cai numa página pedindo a senha antes de continuar. A senha fica guardada cifrada, nem o Delfus enxerga o texto puro.

!!! example "Campanha com prazo"
    Um sorteio que fecha sexta. Você cria o link com data de expiração na sexta à noite. Passou da hora? Quem clicar vê uma página avisando que o link não está mais disponível. Sem gente entrando atrasada.

## Perguntas frequentes

### Posso escolher o final do link?
Pode. Use um código de 3 a 12 caracteres (letras, números, `_` e `-`, sem os confusos `0`, `O`, `I`, `l`). Se já estiver em uso, escolha outro. Em branco, o Delfus gera um automaticamente.

### A senha do link é segura?
É. Ela nunca é guardada em texto puro, só um "hash" dela. O visitante precisa digitar a senha certa numa página de desbloqueio antes de chegar ao destino.

### O que acontece quando o link expira ou bate o limite de cliques?
Ele para de redirecionar e o visitante passa a ver uma página de "link indisponível". Vale o mesmo pra links desativados na mão. Você pode reativar ou ajustar o prazo/limite quando quiser pelo painel.

### Como sei de onde veio cada clique?
Pelas estatísticas. O Delfus classifica a origem sozinho: rede social, busca, e-mail ou direto. Pra separar campanhas específicas (post no Twitter vs. mensagem no Discord), use os UTMs.

### O bot precisa de alguma permissão pra isso?
Não. O encurtador roda no painel/site, não dentro do servidor. Nada pra configurar no Discord, só estar logado no painel (e, pra gerenciar os links de um servidor, ter acesso ao dashboard dele).

!!! tip "Dica"
    Use UTMs sempre que divulgar o mesmo link em canais diferentes: o painel mostra qual divulgação trouxe mais gente. Lembre que "cliques únicos" contam cada pessoa uma vez a cada 24 horas (bom pra medir alcance real), enquanto o "total de cliques" mede engajamento.
