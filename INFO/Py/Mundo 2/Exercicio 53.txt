print("="*20)
print("PALINDROMO")
print("="*20)
frase_seca=str(input("Digite a frase à verificar!")).strip().upper()
frase=''.join(frase_seca)
tamanho=len(frase)
loop=tamanho-1
for a in range(0,tamanho-1,1) :  
 if frase[a] == frase[loop]:
   status=True
   loop=loop-1
 else:
   status=False;break    
if status== True:
    print("A frase {} é um palindromo".format(frase))
else: 
     print("A frase {} NÃO é um palindromo".format(frase_seca))