let link_zap = document.getElementById('link_zap')
let hora = new Date().getHours()

var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
var numeroTelefone = '5599984634296'
var mensagem = ""



const abriZap = () => {
  if (hora > 12 && hora < 18) {
    mensagem = "Olá Boa Tarde, gostaria algumas informações!"
  } else if (hora < 12 && hora > 5) {
    mensagem = "Olá Bom dia, gostaria algumas informações!"
  } else {
    mensagem = "Olá Boa noite, gostaria algumas informações!"
  }
  
  if (isMobile) {
    var url = 'whatsapp://send?phone=' + numeroTelefone + '&text=' + encodeURIComponent(mensagem);
    window.location.href = url;
  } else {
    var webUrl = 'https://web.whatsapp.com/send?phone=' + numeroTelefone + '&text=' + encodeURIComponent(mensagem);
    window.open(webUrl);
  }

}

link_zap.addEventListener('click', abriZap)