sal= float(input("Qual o salario do funcionario?:"))
if sal>1250:
  print("Com o aumento de 10%, seu novo salario é R${:.2f}".format(((sal*10)/100)+sal))  
elif sal <=1250: 
    print("Com o aumento de 15%, seu novo salario é R${:.2f}".format(((sal*15)/100)+sal))  