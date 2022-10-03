km= int(input("Qual a velocidade do carro?: "))
if km > 80:
  print("Você foi multado! po execesso de velocidade, valor da multa: R${:.2f}".format((km-80)*7))
else:
    print("Você não foi multado!")