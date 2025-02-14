#Algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, 
#conoscendo quelle dell’ipotenusa a e dell’altro cateto b.

import math                       #Importo la library *math

a = int(input("Leggi (a):"))      #Inserimento di un valore attribuibile alla variabile (a)
b = int(input("Leggi (b):"))      #Inserimento di un valore attribuibile alla variabile (b)


if a > b:                         #Controllo se la condizione di (a) è maggiore di (b)
    c = math.sqrt(a**2 - b**2)    #Dichiarazione di una nuovo variabile (c), calcolo misura di un cateto (c)
    print(c)                      #Print variabile (c)

else:                             #Se la condizione (a)>(b) è falsa
    print("Errore")               #Print "Errore"

