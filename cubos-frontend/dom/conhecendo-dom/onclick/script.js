const colecaoDeLi = document.querySelectorAll('li');

for (let li of colecaoDeLi) {
    li.onclick = (event) => {
        const elementoClicada = event.target;
        console.log(elementoClicada.style.backgroundColor);

        if (elementoClicada.style.backgroundColor === "rgb(204, 204, 204)") {
            elementoClicada.style.backgroundColor = "#d19feb";
            elementoClicada.style.textDecoration = "none";
        } else {
            elementoClicada.style.backgroundColor = "rgb(204, 204, 204)";
            elementoClicada.style.textDecoration = "line-through";
        }
    }
}

