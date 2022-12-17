casa=float(input("Qual o valor da casa?: "))
sal=float(input("Qual seu salario?: "))
ano=float(input("Em quantos anos você vai pagar?: "))
if (casa/(12*ano)) < ((sal*30)/100):
    print("Seu emprestimo foi aceito! ")
    print("Você pagara a casa de R${:.2f}, em {:.0f} anos, em parcelas de R${:.2f}".format(casa,ano,(casa/(12*ano))))
else:
    print("Seu emprestimo foi NEGADO! ")