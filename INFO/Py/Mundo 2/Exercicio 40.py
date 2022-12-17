print("="*20)
print("Situaçãodo Aluno!")
print("="*20)
n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
media= (n1+n2)/2
if media < 5.0 :
    print("Media {}, a nota abaixo de 5.0, aluno está REPROVADO!".format(media))
elif media >= 5.0 and media < 7.0 :
    print("Media {}, nota entre 5.0 e 6.9, aluno está de RECUPERAÇÃO!".format(media))
elif media >= 7.0 :
    print("Media {}, a nota acima de 7.0, aluno está APROVADO!".format(media))