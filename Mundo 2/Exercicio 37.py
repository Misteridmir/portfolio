num=int(input("Digite um valor inteiro: "))
print("Escolha a base de conversão:")
print("1- Binário")
print("2- Octadecimal")
print("3- Hexadecimal")
a=int(input())
if a == 1:
    print("O Binario de {} é {} ".format(num,bin(num)[2:]))
elif a == 2:
    print("O Octadecimal de {} é {} ".format(num,oct(num)[2:]))
elif a == 3:
    print("O Hexadecimal de {} é {} ".format(num,hex(num)[2:]))