
term=int(input("Digite o numero de termos que deseja : "))
b=0
c=1
cont=0
print(b,end=" => ")
while cont != term-1:
 a= b+c
 b=c
 print(b,end=" => ")
 c=a
 cont+=1
print("Acabou!",end="")