maior=mulher_maior=cont_h=0
status="S"
while status!="N":
 print("="*20)
 idade=int(input("Qual a idade da pessoa?: "))
 sexo=str(input("Qual o sexo dela[M/F]: ")).upper().strip()[0] 
 if idade>18:
   maior+=1 
 if sexo == "M":
   cont_h+=1
 if sexo== "F" and idade< 20:
   mulher_maior+=1
 status=str(input("Você deseja cadastrar mais alguém?[S/N]: ")).upper().strip()[0]
 print("="*20)
print(f"Foram cadastradas {cont_h} homens e possuem {maior} pessoas maior de 18, sendo {mulher_maior} mulheres menor de 18 ")