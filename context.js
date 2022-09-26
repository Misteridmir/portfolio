window.alert("No atual momento o site não está adaptado á ser visualizado em celulares!")
//function foco(){scroll(0, 1000)}
window.onload = foco()

function carta(lugar, flex){document.getElementById(lugar).style.display = flex}

function enviar(link) {
    window.open(link, '_self');
}
function focar(foco){document.getElementById(foco).focus({preventScroll:true});}