a=str(input("Digite uma frase: ")).strip()
print("'A' aparece {} vez na frase.".format(a.count("a")))
print("'A' aparece pela primeira vez na posição {}.".format(a.find("a")))
print("'A' aparece pela ultima vez na posição {}.".format(a.rfind("a")))
