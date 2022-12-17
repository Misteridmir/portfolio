cont=0
num=0
for a in range(1,500,2):
    if a%3==0:
      num=num+1  
      cont=cont+a  
print("Todos os {}, somados possuem o resultado {}".format(num,cont))
