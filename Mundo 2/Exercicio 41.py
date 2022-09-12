from datetime import date
ano_atual=date.today().year
ano=int(input("Qual o seu ano de nascimento?: "))
idade=ano_atual-ano
if idade <= 9 :
    print("Você tem {} anos, participara da categoria MIRIN!".format(idade))
elif idade <= 14:
    print("Você tem {} anos, participara da categoria INFANTIL!".format(idade))
elif idade <= 19:
    print("Você tem {} anos, participara da categoria JÚNIOR!".format(idade))
elif idade <= 25:
    print("Você tem {} anos, participara da categoria SÊNIOR!".format(idade))        
elif idade < 25:
    print("Você tem {} anos, participara da categoria MASTER!".format(idade))