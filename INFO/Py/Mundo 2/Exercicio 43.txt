l=float(input("Qual a sua altura?"))
p=float(input("Qual o seu peso?"))
imc= p/(l**2)
if imc < 18.5:
    print("Seu IMC de {} está Abaixo do Peso ".format(imc))
elif imc <= 25:
    print("Seu IMC de {} está no Peso Ideal".format(imc))
elif imc <= 30:
    print("Seu IMC de {} está com Sobrepeso".format(imc))
elif imc <= 40:
    print("Seu IMC de {} está com Obesidade".format(imc))
elif imc > 40 :
    print("Seu IMC de {} está com Obesidade Mórbida".format(imc))