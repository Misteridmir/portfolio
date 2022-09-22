window.alert("No atual momento o site não está adaptado á ser visualizado em celulares!")
function foco(){scroll(0, 1000)}
window.onload = foco()

function abrirAgro(){document.getElementById("agri").style.display = "flex"
        
}
function abrirInf(){document.getElementById("inf").style.display = "flex"
}
function fecharAgro(){document.getElementById("agri").style.display = "none"

}
function fecharInf(){document.getElementById("inf").style.display = "none"

}
function teste1() {
    window.open('Agro.html', '_blank');
}