print("Aluguel de carros")
dias_aluguel=int(input("Por quantos dias o carro foi alugado?: "))
km_rodado= float(input("Por quantos km o carro rodou?: "))
print("O carro foi alugado por {} dias e rodou {:.2f}km, o valor do aluguel é R${:.2f}".format(dias_aluguel,km_rodado,(dias_aluguel*60)+(km_rodado*0.15)))