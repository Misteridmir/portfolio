km=float(input("Qual a distancia da viagem?: "))
if km <= 200:
    print("A viagem de {} KM, custará R${:.2f} ".format(km, km*0.50))
else:
    print("A viagem de {} KM, custará R${:.2f} ".format(km, km*0.45))