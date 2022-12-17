print("="*20)
print("PA")
print("="*20)
primeiro_termo=int(input("Digite o primeiro primeiro_termo da PA: "))
raz=int(input("Digite a razão da PA: "))
valor= primeiro_termo
term = 10
resultado=(term*raz)+primeiro_termo
while term != 0:
    while valor!= resultado :
       print(valor,end=" => ") 
       valor+=raz
    print("ACABOU!")   
    term=int(input("Quantos primeiro_termo mais vc quer? : "))
    resultado=(term*raz)+resultado   