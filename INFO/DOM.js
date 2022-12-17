//document.body.onload = adicionar_Elemento_baixo;
/*function adicionar_Elemento_baixo(conteudo,irmao) {
    if(typeof conteudo != "object"){
        
    // cria um novo elemento div
    // e dá à ele conteúdo
    var divNova = document.createElement("div");
    var conteudoNovo = document.createTextNode(conteudo);
    divNova.appendChild(conteudoNovo); //adiciona o nó de texto à nova div criada

    // adiciona o novo elemento criado e seu conteúdo ao DOM
    var divAtual = document.getElementById(irmao);
    document.body.insertBefore(divNova, divAtual);
    
  //}console.log(conteudo, typeof conteudo)}*/



function guardar_no_json(){ 

}


function buscar(){
    a=document.getElementsByTagName("body")[0].children[2]
    //for(d in a){
     //   if (d == "children"){
     //       n=a[d][0][d].length
     //       
      //      console.log(n)}
   //}

    for ( b in a){
        if (b == "tagName"){
            tag=a[b]
            console.log(tag, typeof tag)
           //adicionar_Elemento_baixo(tag,"modelo_agro")
        
        }
        if (b == "children"){
        a=a[b]; console.log(a, typeof a); break}
        }

}

buscar()
