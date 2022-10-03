from sys import flags


flags = True 
while flags == True :
  valor= str(input("Digite o seu sexo [M/F]")).upper()
  if valor == "M" or valor == "F":
      flags= False