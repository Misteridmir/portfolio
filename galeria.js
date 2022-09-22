window.alert("No atual momento o site não está adaptado á ser visualizado em celulares!")
function igualar(num){
  const limite= 276

     if(num<=0){
      
        for(a=0;a>-5;a--){
          if(a==num){num=limite+a}      
        console.log(num, a)}
    }else
    if(num>=277){
     
       for(a=277;a<=282;a++){
         if(a==num){num=a-limite}      
       console.log(num, a)}}

    /*switch(num) {
   
        case -5: num = 271; break;
        case -4: num = 272; break;
        case -3: num = 273; break;  
        case -2: num = 274; break;
        case -1: num = 275; break;
        case 0: num = 276; break; 


        case 277: num = 1; break;
        case 278: num = 2; break;
        case 279: num = 3; break;  
        case 280: num = 4; break;
        case 281: num = 5; break;
        case 282: num = 6; break; 
} */return num }        
    
var foto = 1

function muda_preview(){
  for(i=-2;i<=2;i++){
    var preview = foto-i
    preview = igualar(preview)   
    document.getElementById("p"+i).src = "IFPA/foto ("+preview+").jpg"
 
  }}

window.onload= function atualizar(){
foto=igualar(foto)
document.getElementById("foto").src = "IFPA/foto ("+foto+").jpg" 
muda_preview()
}
function rodar(){
foto=igualar(foto)
document.getElementById("foto").src = "IFPA/foto ("+foto+").jpg" 
muda_preview()
}
function voltar_foto(){
foto--
rodar()
}
function passar_foto(){
foto++
rodar()
}


