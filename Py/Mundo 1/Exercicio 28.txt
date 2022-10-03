import random
num=random.randint(0,5)
usu=int(input("Escolha um numero entre 0 a 5: "))
print("O computador escolheu {}".format(num))
if num == usu:
  print("Parabéns, você acertou! ")
else:
  print("Que pena, você errou! ")  