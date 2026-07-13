// Busca ao vivo da home (search-first). Filtra um corpus curado e leva
// direto ao guia. document$ do Material re-executa a cada instant-nav.
document$.subscribe(function () {
  var box = document.getElementById("dxh-search");
  if (!box) return; // só na home

  var input = document.getElementById("dxh-q");
  var results = document.getElementById("dxh-results");
  var list = document.getElementById("dxh-results-list");
  var label = document.getElementById("dxh-results-label");

  // title, categoria, url (relativa à raiz do site)
  var corpus = [
    ["Configurar o anti-raid por imagem", "Segurança", "funcionalidades/anti-raid/"],
    ["Bloquear convites (anti-invite)", "Segurança", "funcionalidades/anti-invite/"],
    ["Honeypot e canais-armadilha", "Segurança", "funcionalidades/honeypot/"],
    ["Moderação, punições e gatilhos", "Segurança", "funcionalidades/moderacao/"],
    ["Backups automáticos do servidor", "Segurança", "funcionalidades/backup/"],
    ["Oráculo anti-scam", "Segurança", "funcionalidades/oraculo/"],
    ["Cartão de boas-vindas e despedida", "Recepção", "funcionalidades/recepcao/"],
    ["Cargos automáticos", "Recepção", "funcionalidades/auto-roles/"],
    ["Cargos por reação", "Recepção", "funcionalidades/reaction-roles/"],
    ["Programa VIP, níveis e recompensas", "Monetização", "funcionalidades/vip/"],
    ["Recompensas de boost", "Monetização", "funcionalidades/boost/"],
    ["Starboard e Hall da Fama", "Engajamento", "funcionalidades/starboard/"],
    ["Mensagens e embeds", "Engajamento", "funcionalidades/mensagens/"],
    ["Emojis personalizados", "Engajamento", "funcionalidades/emojis/"],
    ["Aniversários", "Engajamento", "funcionalidades/aniversarios/"],
    ["Famílias", "Engajamento", "funcionalidades/familia/"],
    ["Correio anônimo", "Engajamento", "funcionalidades/correio/"],
    ["Automações de canal", "Engajamento", "funcionalidades/automacoes/"],
    ["Gestão de equipe", "Operação", "funcionalidades/equipe/"],
    ["Métricas, Health Score e insights", "Análise", "funcionalidades/analise/"],
    ["Encurtador de links", "Utilidades", "funcionalidades/links/"],
    ["Download de vídeos", "Utilidades", "funcionalidades/video/"],
    ["Adicionar o bot", "Primeiros passos", "comecar/adicionar/"],
    ["Configuração inicial", "Primeiros passos", "comecar/configuracao/"],
    ["Definir o idioma do bot", "Primeiros passos", "comecar/idioma/"]
  ];

  var ICON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 6h11"/><path d="M8 12h11"/><path d="M8 18h11"/><path d="M4 6h.01"/><path d="M4 12h.01"/><path d="M4 18h.01"/></svg>';

  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function render() {
    var q = input.value.trim().toLowerCase();
    var items = (q
      ? corpus.filter(function (a) { return (a[0] + " " + a[1]).toLowerCase().indexOf(q) !== -1; })
      : corpus).slice(0, 6);
    label.textContent = q ? "Resultados" : "Sugestões";

    if (q && items.length === 0) {
      list.innerHTML = '<div class="dxh-results__empty">Nada encontrado. Tente outra palavra ou <a href="suporte/">fale com o suporte</a>.</div>';
      return;
    }
    list.innerHTML = items.map(function (a) {
      return '<a class="dxh-result" href="' + a[2] + '">'
        + '<span class="dxh-result__ic">' + ICON + '</span>'
        + '<span class="dxh-result__t">' + esc(a[0]) + '</span>'
        + '<span class="dxh-result__c">' + esc(a[1]) + '</span>'
        + '<span class="dxh-result__kbd">↵</span></a>';
    }).join("");
  }

  input.addEventListener("input", render);
  input.addEventListener("focus", function () { render(); results.hidden = false; });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      var first = list.querySelector("a.dxh-result");
      if (first) window.location.href = first.getAttribute("href");
    } else if (e.key === "Escape") {
      input.blur();
      results.hidden = true;
    }
  });
  document.addEventListener("click", function (e) {
    if (!box.contains(e.target)) results.hidden = true;
  });

  // atalho "/" foca a busca da home (sem abrir a busca do Material).
  // Registrado uma vez; em outras páginas #dxh-q não existe → deixa o Material tratar.
  if (!window.__dxhSlash) {
    window.__dxhSlash = true;
    document.addEventListener("keydown", function (e) {
      if (e.key !== "/") return;
      var t = document.activeElement;
      if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.isContentEditable)) return;
      var el = document.getElementById("dxh-q");
      if (!el) return;
      e.preventDefault();
      e.stopImmediatePropagation();
      el.focus();
    }, true); // captura: roda antes do handler de "/" do Material
  }
});
