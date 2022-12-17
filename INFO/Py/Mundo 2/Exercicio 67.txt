while True:
 print("="*20)
 cont=0
 num=int(input("Digite um valor para tabuada: "))
 while cont <=10:
  print(f"{cont} X {num} = {cont*num}")   
  cont+=1   
 print("="*20)
 if num < 0:
     break
print("Acabou!")    