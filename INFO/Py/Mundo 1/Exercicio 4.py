a=input("digite algo: ")
print("O que foi digitado é do tipo primitivo: {}".format(type(a)))
print("Só tem espaços?: {}".format(a.isspace()))
print("É um número?: {}".format(a.isnumeric()))
print("É alfabetico?: {}".format(a.isalpha()))
print("è alfanumerico?: {}".format(a.isalnum()))
print("É maiúscula?: {}".format(a.isupper()))
print("É minúscula?: {}".format(a.islower()))
print("É capitalizada?: {}".format(a.istitle()))