const config = window.SHOP_CONFIG || {};

const products = [
  {
    name: "Atlas 45A",
    type: "Maintenance-free",
    use: "Small petrol cars",
    ah: "45Ah",
    cca: "400CCA",
    dimensions: "238 x 129 x 227 mm",
    terminals: "Right positive",
    warranty: "12-month warranty",
    price: "GH₵850",
    availability: "In stock",
    image: ""
  }
];

function getPhoneDigits() {
  return (config.phone || "").replace(/\D/g, "");
}

function setContactLinks() {
  const digits = getPhoneDigits();
  document.querySelectorAll("[data-phone-link]").forEach((link) => {
    link.href = digits ? `tel:+${digits}` : "#";
    if (!digits) link.addEventListener("click", (event) => event.preventDefault());
  });

  document.querySelectorAll("[data-whatsapp-link]").forEach((link) => {
    if (digits) {
      link.href = `https://wa.me/${digits}?text=${encodeURIComponent(config.whatsappMessage || "")}`;
      link.target = "_blank";
      link.rel = "noopener";
    } else {
      link.href = "#";
      link.addEventListener("click", (event) => event.preventDefault());
    }
  });

  document.querySelectorAll("[data-directions-link]").forEach((link) => {
    if (config.directionsUrl) {
      link.href = config.directionsUrl;
      link.target = "_blank";
      link.rel = "noopener";
    } else {
      link.href = "#";
      link.addEventListener("click", (event) => event.preventDefault());
    }
  });
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (character) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;"
  }[character]));
}

function renderProducts() {
  const list = document.getElementById("battery-list");
  if (!list) return;
  list.innerHTML = products.map((product) => `
    <article class="battery-card">
      <div class="battery-image">
        ${product.image
          ? `<img src="${escapeHtml(product.image)}" alt="${escapeHtml(product.name)} battery">`
          : `<span>Product photo<br><strong>Replacement placeholder</strong></span>`}
      </div>
      <div class="battery-body">
        <span class="battery-type">${escapeHtml(product.type)}</span>
        <h3>${escapeHtml(product.name)}</h3>
        <p>${escapeHtml(product.use)}</p>
        <dl>
          <div><dt>Capacity</dt><dd>${escapeHtml(product.ah)}</dd></div>
          <div><dt>CCA</dt><dd>${escapeHtml(product.cca)}</dd></div>
          <div><dt>Dimensions</dt><dd>${escapeHtml(product.dimensions)}</dd></div>
          <div><dt>Terminals</dt><dd>${escapeHtml(product.terminals)}</dd></div>
        </dl>
        <p><span class="battery-price">${escapeHtml(product.price)}</span><span class="battery-status">${escapeHtml(product.availability)}</span></p>
        <p class="battery-disclaimer">Warranty: ${escapeHtml(product.warranty)}. Fit depends on exact model, year, engine, size, terminals and vehicle requirements.</p>
      </div>
    </article>
  `).join("");
}

const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");
if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });
  navLinks.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      navLinks.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

renderProducts();
setContactLinks();
