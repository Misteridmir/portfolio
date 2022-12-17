///////////////////////////////variaveis gloais///////////////////////
let border_radiuson = "25px"
let border_radiusoff = "0px"
let border_righton = "1px solid rgba(160, 160, 160, 0.555)"
let border_rightoff = ""
////////faz a mudança do dsplay de aordo com o ID q vai no paramentro/////////////////

function carta(lugar, flex){document.getElementById(lugar).style.display = flex}

///////////////////////////////////////////////////////////////////////////////////


//////////muda o display do mundo de flex para none e vice-versa/////////////////
var giro1= false;
var giro2= false;
function mundar_mundo(lugar){
    function muda_style(){
        function mudar_picture(valor,valor1){
        tag_mundo1=document.getElementById("picture_mundo1").style
        tag_mundo1.borderTopRightRadius = valor
        tag_mundo1.borderBottomRightRadius = valor
        tag_mundo1.borderRight = valor1
        tag_mundo2=document.getElementById("picture_mundo2").style
        tag_mundo2.borderTopLeftRadius = valor
        tag_mundo2.borderBottomLeftRadius = valor 
        tag_mundo2.borderLeft = valor1
    }
        
        if(giro1==false && giro2==false){mudar_picture(border_radiuson,border_righton)}else{mudar_picture(border_radiusoff, border_rightoff)}
    }
    
    
    
    function girar(giro){
        if(giro==true){flex="flex";muda_style()}else if(giro==false){flex="none";muda_style()};
        return flex
    }

    switch(lugar){
        case 1 :giro1= !giro1;
            flex=girar(giro1);break
        case 2: giro2= !giro2;
            flex=girar(giro2);break
    }
    carta("mundo_"+lugar,flex)
}

/////////////////////////////////////////////////////////////////////




//////////atualiza o code do iframe ao clickar na atividade ou nas setas////////////////

var exercicio_anterior = 1
function atualizar(mundo,exercicio){
    document.getElementById('frame').src= "INFO/Py/Mundo "+mundo+"/Exercicio "+exercicio+".html"
    
    
    var a=document.getElementById("tela_py_body")
    var b=a.getElementsByTagName("li")
    for (index in b){ 
    var c=b[index].outerText
    if(c==exercicio_anterior){
        b[index].style.backgroundColor="transparent"
        exercicio_anterior= exercicio
    }
    if(c==exercicio){
        switch(mundo){
        case 1:b[index].style.backgroundColor= "#ffcf3f";break
        case 2:b[index].style.backgroundColor= "#3771a1";break
    }
      
        
    }
    }
   
}
//////////ativado pelas setas do painel, para passar ou voltar o code //////////
function mudar(passo){
   
    
    local= document.getElementById('frame').src //pega o local do iframe que recebe as paginas; local=str

    //valores em str
    mundo_atual=local[38]                         
    exercicio_atual1=local[52]
    exercicio_atual2=local[53]

    if(exercicio_atual2!="."){exercicio_atual= exercicio_atual1+exercicio_atual2}
    else{ exercicio_atual= exercicio_atual1}
     
        exercicio_int= parseInt (exercicio_atual)
        mundo_int= parseInt(mundo_atual)

        mundo= mundo_int
        exercicio= exercicio_int+passo 
        switch(exercicio){
        case 0: exercicio=71; mundo=2;break;
        case 35: mundo=1;break;
        case 36: mundo=2;break;        
        case 72: exercicio=1; mundo=1;break;}
        
        //console.log( "mundo_atual:", mundo_atual,"mundo:", mundo,"exercicio_atual1", exercicio_atual1,"exercicio_atual2",exercicio_atual2,"exercicio:", exercicio)
        //console.log(local)
        atualizar(mundo,exercicio)
}
////////////////////////////////////////////////////////////////////////////////