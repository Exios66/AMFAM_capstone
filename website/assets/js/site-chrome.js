// ---------------------------------------------------------------------------
// Site chrome — reading progress bar + misc page polish.
// Respects prefers-reduced-motion (CSS also disables the transition).
// ---------------------------------------------------------------------------
(function () {
  "use strict";

  function addProgressBar() {
    var bar = document.createElement("div");
    bar.id = "reading-progress";
    bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);

    var ticking = false;
    function update() {
      var doc = document.documentElement;
      var scrollTop = window.scrollY || doc.scrollTop || 0;
      var height = Math.max(doc.scrollHeight, document.body.scrollHeight) - window.innerHeight;
      var pct = height > 0 ? (scrollTop / height) * 100 : 0;
      bar.style.width = pct + "%";
      ticking = false;
    }
    function requestTick() {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }
    window.addEventListener("scroll", requestTick, { passive: true });
    window.addEventListener("resize", requestTick);
    update();
  }

  function init() {
    addProgressBar();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
