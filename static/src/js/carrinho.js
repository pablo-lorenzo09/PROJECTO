async function mostrar_carrinho(){
    const resposta = await fetch("http://10.110.134.31:8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")

        for (let dado of dados){
            let linha = `    
        <div class="cart-item" >    
            <img src="${dado.foto}" alt="Hambúrguer" class="cart-item__image">
        <div class="cart-item__info">
            <div class="cart-item__title">${dado.produto}</div>
            <div class="cart-item__price">${dado.preco}</div>
            <div class="cart-item__description">Pão, hambúrguer 180g, queijo, bacon, alface, tomate e molho especial.</div>
        </div>
        </div>
        `
        carrinho.innerHTML += linha;
        };
    
    };
};

mostrar_carrinho();