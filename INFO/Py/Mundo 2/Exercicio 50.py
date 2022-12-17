total=0
pares=0
num=["0"]
for a in range(1,7,1):
 num.append(float(input("Digite o valor {}: ".format(a))))
 if num[a]%2== False:
     total=total+num[a]
     pares=pares+1
print("Valor total dos {} pares = {}".format(pares,total))