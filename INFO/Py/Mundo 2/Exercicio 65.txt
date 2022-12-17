flag=False
valor=maior=cont=0
menor=9999999999999
while flag==False:
 num=int(input("Digite um numero: "))
 valor+=num
 cont+=1
 a=str(input("Quer continuar a digitar?[S/N] : ")).upper().strip()[0]
 if a == "S":
     flag=False
 elif a == "N":
     flag=True    
 if num < menor:
     menor=num
 if num > maior:
     maior=num
print("A media dos valores é {:.2f}, o maior valor é {}, e o menor valor é {}".format(valor/cont,maior,menor))            