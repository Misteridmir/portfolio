print("="*20)
print("CAIXA ELETRONICO!")
print("="*20)
valor=int(input("Qual o valor deseja sacar?: "))
cont_50=cont_20=cont_10=cont_1=0
while valor !=0:
 
 while valor >=50:
  valor-=50
  cont_50+=1
 print(f"Total de {cont_50} cedulas de R50")   
 while valor >=20:
  valor-=20
  cont_20+=1
 print(f"Total de {cont_20} cedulas de R$20") 
 while valor >=10:
  valor-=10
  cont_10+=1
 print(f"Total de {cont_10} cedulas de R$10") 
 while valor >=1:
  valor-=1
  cont_1+=1
 print(f"Total de {cont_1} cedulas de R$1")
 
  
print("="*20) 