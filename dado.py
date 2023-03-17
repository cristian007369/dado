# Programa sobre un dado de 6 caras

import random


print("---------------------------------------------")
print("--------------------Dado---------------------")
print("---------------------------------------------")



#Input

cara_dado=random.randint(1,6)

#Processing y output

if cara_dado==6:
    rta="la cara opuesta es 1"
elif cara_dado==5:
    rta="la cara opuesta es 2"
elif cara_dado==4:
    rta="la cara opuesta es 3"
elif cara_dado==3:
    rta="la cara opuesta es 4"
elif cara_dado==2:
    rta="la cara opuesta es 5"
elif cara_dado==1:
    rta="la cara opuesta es 6"
else:
    rta="Entrada no valida"

cara_dado1=random.randint(1,6)

if cara_dado1==6:
    rta1="la cara opuesta es 1"
elif cara_dado1==5:
    rta1="la cara opuesta es 2"
elif cara_dado1==4:
    rta1="la cara opuesta es 3"
elif cara_dado1==3:
    rta1="la cara opuesta es 4"
elif cara_dado1==2:
    rta1="la cara opuesta es 5"
elif cara_dado1==1:
    rta1="la cara opuesta es 6"
else:
    rta1="Entrada no valida"

if cara_dado1==cara_dado:
    par="Salio par"
else:
    par="No salio par"

print("La cara del dado 1 es "+str(cara_dado)+" y "+rta)
print("La cara del dado 2 es "+str(cara_dado1)+" y "+rta1)
print(par)