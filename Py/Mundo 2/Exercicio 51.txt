print("="*20)
print("PA")
print("="*20)
ter=int(input("Digite o primeiro termo da PA: "))
raz=int(input("Digite a razão da PA: "))
for a in range(ter, ter+(raz*10) , raz ):
  print(a,end=" => ") 
print("ACABOU!")   