print("Forma triangulo?")
r1=int(input("Valor da primeira reta: "))
r2=int(input("Valor da segunda reta: "))
r3=int(input("Valor da terceira reta: "))
if r1+r2 > r3 and r1+r3 > r2 and r3+r2 > r1:
 print("Essas 3 retas formam um triangulo!")
else: 
 print("Essas 3 retas NÃO formam um triangulo!")    