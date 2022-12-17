a=str(input("Qual seu nome completo?: ")).strip()
print("Seu primeiro nome é {}.".format(a[0:(a.find(" "))]))
print("Seu ultimo nome é {}.".format(a[(a.rfind(" ")+1):]))