pesos=[0]
maior=0
menor=100000
for a in range(1,6,1):
   pesos.append(float(input("Qual o peso da pessoa {} ".format(a))))
   if pesos[a]> maior:
       maior = pesos[a]
   if pesos[a]< menor:
        menor = pesos[a]    
print("O peso maior é {:.2f}Kg, e o peso menor é {:.2f}Kg.".format(maior,menor))