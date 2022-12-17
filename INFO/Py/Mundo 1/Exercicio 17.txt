import math
print("Triangulo")
cat_op=float(input("Digite o valor do cateto oposto: "))
cat_ad=float(input("Digite o valor do cateto adjacente: "))
print("O valor da hipotenusa é {:.2f}".format(math.sqrt((cat_op**2)+(cat_ad**2))))
