print("="*20)
print("COMPRA TUDO BARATÃO! ")
print("="*20)
mais_barato=cont=valor=mais_mil=0
status=False
nome_mais_barato=""
while status != "N":
 nome=str(input("Qual o nome do produto?: ")).strip().title()
 preço=int(input("Qual o preço do produto?:"))
 valor+=preço
 if preço>1000:
  mais_mil+=1 
 if cont==1:
  mais_barato=preço
  nome_mais_barato=nome
 if preço<mais_barato:
    mais_barato=preço
    nome_mais_barato=nome      
 status=str(input("Você quer continuar?[S/N]: ")).strip().upper()[0]  
print(f"O total gasto da compra é R${valor}") 
print(f"O produto mais barato é {nome_mais_barato}, custa {mais_barato}")
print(f"você comprou {mais_mil} produtos que custam mais de mil reais")
