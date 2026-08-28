(() => {
  const art = [
    "                                                 ",
    "               ,----..                           ",
    "  ,----..     /   /   \\      ,---,        ,---,. ",
    " /   /   \\   /   .     :   .'  .' `\\    ,'  .' | ",
    "|   :     : .   /   ;.  \\,---.'     \\ ,---.'   | ",
    ".   |  ;. /.   ;   /  ` ;|   |  .`\\  ||   |   .' ",
    ".   ; /--` ;   |  ; \\ ; |:   : |  '  |:   :  |-, ",
    ";   | ;    |   :  | ; | '|   ' '  ;  ::   |  ;/| ",
    "|   : |    .   |  ' ' ' :'   | ;  .  ||   :   .' ",
    ".   | '___ '   ;  \\; /  ||   | :  |  '|   |  |-, ",
    "'   ; : .'| \\   \\  ',  / '   : | /  ; '   :  ;/| ",
    "'   | '/  :  ;   :    /  |   | '` ,/  |   |    \\ ",
    "|   :    /    \\   \\ .'   ;   :  .'    |   :   .' ",
    " \\   \\ .'      `---`     |   ,.'      |   | ,'   ",
    "  `---`                  '---'        `----'     ",
    "                                                 "
  ].join("\n");

  document.querySelectorAll('.ascii-portal pre').forEach((pre) => {
    pre.textContent = art;
    pre.classList.add('aleph-wordmark');
  });

  /*
    Profundidad visual para portada y routers.
    La capa 3D queda detrás, pero los paneles dejan de ser muros opacos.
    Controles y bloques de lectura conservan fondos sólidos para legibilidad.
  */
  if (!document.getElementById('aleph-depth-ui')) {
    const style = document.createElement('style');
    style.id = 'aleph-depth-ui';
    style.textContent = `
      header {
        background: rgba(0,0,0,.66) !important;
      }

      .ascii-portal {
        background: rgba(0,0,0,.48) !important;
      }

      .ascii-portal pre {
        text-shadow: 0 1px 2px #000, 0 0 5px rgba(0,0,0,.85);
      }

      .node-map > a {
        background: rgba(0,0,0,.58) !important;
      }

      .node-map > a:hover,
      .node-map > a:focus-visible {
        background: var(--acid) !important;
        color: #000 !important;
      }

      .card {
        background: rgba(0,0,0,.54) !important;
      }

      .ringcard {
        background: rgba(0,0,0,.60) !important;
      }

      .ringcard:nth-child(even) {
        background: rgba(7,7,7,.60) !important;
      }

      .card .lead,
      .ringcard span,
      .tiny,
      details,
      footer {
        text-shadow: 0 1px 2px #000, 0 0 4px rgba(0,0,0,.9);
      }

      /* Los elementos interactivos siguen siendo superficies sólidas. */
      button,
      .btn,
      input,
      .terminal,
      .external,
      .jodi-note,
      details[open] {
        background-color: rgba(0,0,0,.92);
      }

      /* En pantallas pequeñas priorizamos un poco más la lectura. */
      @media (max-width: 700px) {
        header { background: rgba(0,0,0,.78) !important; }
        .ascii-portal { background: rgba(0,0,0,.62) !important; }
        .card { background: rgba(0,0,0,.68) !important; }
        .ringcard { background: rgba(0,0,0,.72) !important; }
        .ringcard:nth-child(even) { background: rgba(7,7,7,.72) !important; }
      }
    `;
    document.head.appendChild(style);
  }
})();
