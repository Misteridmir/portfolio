print("="*20)
print("PA")
print("="*20)
primeiro_termo=int(input("Digite o primeiro termo da PA: "))
raz=int(input("Digite a razão da PA: "))
print(primeiro_termo,end=" => ")
valor=primeiro_termo+ raz  
while valor!=(raz*10)+primeiro_termo:
  print(valor,end=" => ") 
  valor+=raz
  
print("ACABOU!")   