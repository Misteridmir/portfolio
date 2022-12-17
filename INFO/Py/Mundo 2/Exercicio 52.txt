from ast import Break
from pickle import TRUE


print("="*20)
print("NUMERO PRIMO!")
print("="*20)
num=int(input("Digite o valor à verificar: "))
for a in range (2,num, 1):
  if num%a == 0:
      primo=TRUE
  else: primo=False; break    
if primo== True  : 
    print("Esse numero não é PRIMO!")

else:
  print("Esse numero é PRIMO!") 
  