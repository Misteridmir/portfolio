from ast import Num
from distutils.log import fatal
from itertools import count
from tracemalloc import start



num=int(input("Digite um numero para calcular o fatorial!"))
fat=num
print(num,end="! = ")
while num!=1:
  fat*=num-1
  print(num,end=" ")
  print(" X " if num > 2 else " =", end=" ")
  num-=1
print(fat)  