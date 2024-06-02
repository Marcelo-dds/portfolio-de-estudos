const inputCadastrar = document.querySelector('input');

const botaoCadastrar = document.querySelector('button');

const elementoUl = document.querySelector('ul');


const limparImputCadatrar = () => {
    inputCadastrar.value = "";
}

const injetarElementoNoHtml = (elementoPai, novoElemento) => {
    elementoPai.appendChild(novoElemento);
}

const criarElemento = (tagName, texto) => {
    const elemento = document.createElement(tagName);
    if (texto) {
        elemento.textContent = texto;
    }
    return elemento;
}


botaoCadastrar.onclick = () => {

    //vereficando o valor do input
    if (inputCadastrar.value.length <= 0) {
        inputCadastrar.classList.add('borda-vermelha');
        return
    }

    //criar uma li
    const novaLi = criarElemento("li");

    //exclui botao
    const botaoExcluir = criarElemento('button', "Excluir");


    botaoExcluir.onclick = () => {
        novaLi.remove()
    }

    const elementoSpan = criarElemento('span', inputCadastrar.value)


    //injetar na novali elemento span e botao li
    injetarElementoNoHtml(novaLi, elementoSpan);
    injetarElementoNoHtml(novaLi, botaoExcluir);


    // criando evento de click para li
    novaLi.onclick = (event) => {
        const elemento = event.target
        if (elemento.nodeName == "LI") {
            elemento.classList.toggle("comprado")
        } else {
            elemento.parentElement.classList.toggle("comprado")
        }
    }

    // injetando li na ul
    injetarElementoNoHtml(elementoUl, novaLi);

    //limpando input cadastrar
    limparImputCadatrar();
};