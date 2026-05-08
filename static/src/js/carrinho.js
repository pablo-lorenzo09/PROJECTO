const cartBadge = document.querySelector('#cartBadge')

async function mostrar_carrinho(){
    const resposta = await fetch("http://10.110.134.39:8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")
        carrinho.innerHTML = ""

        for (let dado of dados){
            let linha = `    
        <div class="cart-item" >    
            <img src="${dado.foto}" alt="Hambúrguer" class="cart-item__image">
        <div class="cart-item__info">
            <div class="cart-item__title">${dado.produto}</div>
            <div class="cart-item__price">${dado.preco}.00</div>
            <div class="cart-item__description">Pão, hambúrguer 180g, queijo, bacon, alface, tomate e molho especial.</div>
        </div>
            <a href="/home/delete/${dado.produto} class="cart-item__delete">
                <svg class="delete-icon" viewBox="0 0 24 24" width="20" height="20">
                <path fill="currentColor" d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
                </svg>
            </a>
        </div>

        `
        carrinho.innerHTML += linha;
        // cartBadge.innerText += 1
        precototal = 0
        precototal += dado.preco
        };
        subtotal = document.getElementById("cartSubtotal")
        subtotal.innerHTML = `R$ ${precototal},00`
    };
};

mostrar_carrinho();

async function inserirItemCarrinho(cod_produto, quantidade=1) {
    const resposta = await fetch("/api/post/item_carrinho",
                                    {
                                        method:"POST",
                                        headers:{
                                                    "Content-Type": "application/json"
                                                },
                                        body: JSON.stringify(
                                                                {
                                                                    "cod_produto":cod_produto,
                                                                    "quantidade":quantidade
                                                                },
                                        )
                                    }
    )

    if (!resposta.ok)
    {
        alert("Erro ao inserir item!")
    }

    mostrar_carrinho();
}