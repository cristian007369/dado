# Programa sobre un dado de 6 caras

print("---------------------------------------------")
print("--------------------Dado---------------------")
print("---------------------------------------------")

#Input

cara_dado=int(input("Ingrese el número de una de las caras del dado: "))

#Processing y output

if cara_dado==6:
    print("---------------------------------------------")
    print("La cara opuesta es 1")
    print("---------------------------------------------")
elif cara_dado==5:
    print("---------------------------------------------")
    print("La cara opuesta es 2")
    print("---------------------------------------------")
elif cara_dado==4:
    print("---------------------------------------------")
    print("La cara opuesta es 3")
    print("---------------------------------------------")
elif cara_dado==3:
    print("---------------------------------------------")
    print("La cara opuesta es 4")
    print("---------------------------------------------")
elif cara_dado==2:
    print("---------------------------------------------")
    print("La cara opuesta es 5")
    print("---------------------------------------------")
elif cara_dado==1:
    print("---------------------------------------------")
    print("La cara opuesta es 6")
    print("---------------------------------------------")
else:
    print("---------------------------------------------")
    print("Entrada no valida")
    print("---------------------------------------------")