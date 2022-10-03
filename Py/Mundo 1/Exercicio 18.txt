import math
angle= float(input("Qual o valor do angulo?: "))
print("O seno de {}° é {:.2f}".format(angle,(math.sin(math.radians(angle)))))
print("O cosseno de {}° é {:.2f}".format(angle,(math.cos(math.radians(angle)))))
print("O tangente de {}° é {:.2f}".format(angle,(math.tan(math.radians(angle)))))