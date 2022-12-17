from random import randint
flag= True
cont=0
print("="*20)
print("Adivinha!")
print("="*20)
while flag==True:
 pc=randint(0,10)
 num=int(input(("Tente adivinhar, o numero entre 0 e 10: ")))
 cont+=1
 if num == pc:
     flag= False
 else:
  print("Você errou, tente denovo!")       
print("Você acertou!, em {} tentativas".format(cont))