cont=valor=0
while True:
 num=int(input("Digite um valor[999 para parar]: "))
 if num == 999:
     break
 cont+=1
 valor+=num
print(f"você digitou {cont}, e a soma entre eles é {valor/cont}")