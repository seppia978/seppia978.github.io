(function () {
  var lightboxSelector = ".media-lightbox";
  var openSelector = ".current-avatar-link[href^='#'], .current-avatar-badge-link[href^='#']";
  var closeSelector = ".media-lightbox-backdrop, .media-lightbox-close";
  var lastScroll = { x: 0, y: 0 };
  var lastOpener = null;

  function getHashTarget(link) {
    var href = link.getAttribute("href") || "";
    if (href.charAt(0) !== "#" || href.length < 2) return null;

    try {
      return document.getElementById(decodeURIComponent(href.slice(1)));
    } catch (error) {
      return null;
    }
  }

  function activeLightboxFromHash() {
    if (!window.location.hash) return null;
    var id = window.location.hash.slice(1);

    try {
      var target = document.getElementById(decodeURIComponent(id));
      return target && target.matches(lightboxSelector) ? target : null;
    } catch (error) {
      return null;
    }
  }

  function restoreScroll(position) {
    var x = position ? position.x : lastScroll.x;
    var y = position ? position.y : lastScroll.y;
    window.requestAnimationFrame(function () {
      window.scrollTo(x, y);
    });
  }

  function openLightbox(lightbox, opener) {
    lastScroll = { x: window.scrollX, y: window.scrollY };
    lastOpener = opener;

    document.querySelectorAll(lightboxSelector + ".is-open").forEach(function (item) {
      item.classList.remove("is-open");
    });

    lightbox.classList.add("is-open");
    lightbox.setAttribute("aria-hidden", "false");
    restoreScroll();

    var closeButton = lightbox.querySelector(".media-lightbox-close");
    if (closeButton) closeButton.focus({ preventScroll: true });
  }

  function closeLightbox() {
    var lightbox = activeLightboxFromHash() || document.querySelector(lightboxSelector + ".is-open");
    if (!lightbox) return;

    var scrollPosition = lastOpener ? lastScroll : { x: window.scrollX, y: window.scrollY };

    if (window.location.hash && lightbox.id === window.location.hash.slice(1)) {
      window.history.replaceState(null, document.title, window.location.pathname + window.location.search);
    }

    lightbox.classList.remove("is-open");
    lightbox.setAttribute("aria-hidden", "true");
    restoreScroll(scrollPosition);

    if (lastOpener && document.contains(lastOpener)) {
      lastOpener.focus({ preventScroll: true });
    }
  }

  function syncHashLightbox() {
    var hashLightbox = activeLightboxFromHash();

    document.querySelectorAll(lightboxSelector).forEach(function (item) {
      if (item === hashLightbox) {
        item.setAttribute("aria-hidden", "false");
      } else {
        item.classList.remove("is-open");
        item.setAttribute("aria-hidden", "true");
      }
    });
  }

  document.addEventListener("click", function (event) {
    var openLink = event.target.closest(openSelector);
    if (openLink) {
      var target = getHashTarget(openLink);
      if (target && target.matches(lightboxSelector)) {
        event.preventDefault();
        openLightbox(target, openLink);
      }
      return;
    }

    var closeLink = event.target.closest(closeSelector);
    if (closeLink && closeLink.closest(lightboxSelector)) {
      event.preventDefault();
      closeLightbox();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && (activeLightboxFromHash() || document.querySelector(lightboxSelector + ".is-open"))) {
      event.preventDefault();
      closeLightbox();
    }
  });

  window.addEventListener("hashchange", syncHashLightbox);
  syncHashLightbox();
})();
