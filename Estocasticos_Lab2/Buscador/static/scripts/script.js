document.querySelector("#buscador").addEventListener("input", e => {
  const searchTerm = e.target.value.toLowerCase();
  const articulos = document.querySelectorAll(".articulo");
  const articuloMayor = document.querySelectorAll(".articulo_mayor");

  articuloMayor.forEach(articulo2 => {
    if (searchTerm === "") {
      articulo2.style.display = "flex";
      articulo2.style.justifyContent = "center";
      articulo2.style.alignItems = "center";
      articulo2.style.marginTop = "20px";
      articulo2.style.hover = "red";
    } else {
      articulo2.style.display = "none";
    }
  });

  articulos.forEach(articulo => {
    const contenido = articulo.textContent.toLowerCase();
    if (contenido.includes(searchTerm)) {
      articulo.classList.add("filtro");
    } else {
      articulo.classList.remove("filtro");
    }
  });
  if (searchTerm === "") {
    articulos.forEach(articulo => {
      articulo.classList.remove("filtro");
  });
  }
});

const articulos = document.querySelectorAll(".articulo");
const buscadorInput = document.querySelector("#buscador");
articulos.forEach(articulo => {
  articulo.addEventListener("click", e => {
    const valor = e.target.textContent.trim();
    buscadorInput.value = valor;
  });
});

const articulos2 = document.querySelectorAll(".articulo_mayor");
const buscadorInput2 = document.querySelector("#buscador");
articulos2.forEach(articulo2 => {
  articulo2.addEventListener("click", e => {
    const valor = e.target.textContent.trim();
    buscadorInput2.value = valor;
  });
});

