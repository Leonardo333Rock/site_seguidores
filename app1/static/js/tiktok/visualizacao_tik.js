let corpo = document.getElementById('corpo')

const valores = ['5,90','8,90','14,90','25,90','44,90','62,90']
const quantidades = ['500','1.000','2.000','5.000','10.000','15.000']

for(let x=0; x<6; x++){
    let card = document.createElement('div')
    let card_header = document.createElement('div')
    let p1 = document.createElement('p')
    let p2 = document.createElement('p')
    let class_corpo = document.createElement('div')
    let p_preco = document.createElement('p')
    let spam_preco = document.createElement('span')
    let class_footer = document.createElement('div')
    let ul = document.createElement('ul')
    let li1 = document.createElement('li')
    let li2 = document.createElement('li')
    let li3 = document.createElement('li')
    let li4 = document.createElement('li')
    let li5 = document.createElement('li')
    let li6 = document.createElement('li')
    let button = document.createElement('button')


    corpo.appendChild(card)
    card.setAttribute('class','card')

    card_header.setAttribute('class','card_header')
    card.appendChild(card_header)

    p1.setAttribute('class','p1')
    p1.innerHTML=`${quantidades[x]} VISUALIZAÇOES`
    p2.setAttribute('class','p2')
    p2.innerHTML = "SEGUIDORES BRASILEIROS E REAIS🚀"

    card_header.appendChild(p1)
    card_header.appendChild(p2)

    class_corpo.setAttribute('class','class_corpo flex')
    card.appendChild(class_corpo)

    class_corpo.appendChild(p_preco)
    p_preco.setAttribute('class','p_preco')
    p_preco.innerHTML=`<span class="spam_preco">R$</span> ${valores[x]}`

    class_footer.setAttribute('class','class_footer flex')

    card.appendChild(class_footer)
    class_footer.appendChild(ul)

    li1.innerHTML="Entrega Imediata"
    li2.innerHTML="Seguidores Reais"
    li3.innerHTML="Seguidores Brasileiros"
    li4.innerHTML="Suporte Via WhatsApp"
    li5.innerHTML="Garantia total - 100%"
    li6.innerHTML="Não pedimos a sua senha"

    ul.appendChild(li1)
    ul.appendChild(li2)
    ul.appendChild(li3)
    ul.appendChild(li4)
    ul.appendChild(li5)
    ul.appendChild(li6)

    button.setAttribute('class','btn btn-success')
    button.setAttribute('id','btn_comprar')
    button.innerHTML='Comprar'
    class_footer.appendChild(button)

}
let btn_comprar = [...document.querySelectorAll('#btn_comprar')]

var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
var numeroTelefone = '5599984634296'
var mensagem = ""


btn_comprar.map((e) => {
    e.addEventListener('click', (e) => {
        mensagem = ""
        mensagem = 'Olá quero comprar '+ e.target.parentNode.parentNode.children[0].children[0].innerHTML + " no Tiktok"
        if (isMobile) {
            var url = 'whatsapp://send?phone=' + numeroTelefone + '&text=' + encodeURIComponent(mensagem);
            window.location.href = url;
        } else {
            var webUrl = 'https://web.whatsapp.com/send?phone=' + numeroTelefone + '&text=' + encodeURIComponent(mensagem);
            window.open(webUrl);
        }

    })
})