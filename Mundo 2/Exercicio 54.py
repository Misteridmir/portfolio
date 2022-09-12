from datetime import date
pessoas=[0]
maior=0
menor=0
ano_atual= date.today().year
for a in range(1,8,1):
    pessoas.append(int(input("Qual o ano de nascimento da pessoa {} :".format(a)))) 
    if (ano_atual-pessoas[a])>=21:
        maior = maior +1
    elif (ano_atual-pessoas[a]) < 21:
        menor= menor +1    

print("{} pessoas são maior de idade e {} NÃO são de maior".format(maior,menor))        