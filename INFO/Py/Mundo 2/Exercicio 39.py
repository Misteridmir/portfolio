from datetime import date
ano_atual=date.today().year
ano=int(input("Digite o ano do seu nascimento: "))
if (ano_atual-ano) == 18:
    print("Esse ano é o ano do seu alistamento ")
if (ano_atual-ano) < 18:
    print("Ainda não é o ano do seu alistamento, o ano do seu alistamento é {}".format(ano+18))
if (ano_atual-ano) > 18:
    print("O seu alistamento ja passou, o ano do seu alistamento foi em {}".format(ano+18))        