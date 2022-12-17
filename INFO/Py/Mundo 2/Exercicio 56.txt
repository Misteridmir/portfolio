total_idade=0
mais_velho=0
nome_mais_velho=""
menos_de_vinte=0
for a in range(1,5,1):
    nome=str(input("Qual nome da pessoa {}: ".format(a))).strip()
    idade=int(input("Qual a idade da pessoa {}: ".format(a)))
    sexo_nome=str(input("Qual o sexo da pessoa {} [M/F]: ".format(a))).strip().upper()  #true= masculino e false = feminino
    if sexo_nome == "M":
      sexo=True
    elif sexo_nome=="F":
      sexo=False      
    total_idade= total_idade+ idade
    if sexo==True and idade> mais_velho:
        mais_velho= idade
        nome_mais_velho=nome
    if sexo==False and idade<20:
        menos_de_vinte= menos_de_vinte+1   
media=total_idade/4    
print("A media de idade do grupo é {}".format(media))
print("O homem mais velho do grupo é {} que tem {} anos".format(nome_mais_velho,mais_velho))
print("{} mulheres tem menos de 20 anos".format(menos_de_vinte))