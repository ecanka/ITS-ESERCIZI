#Trova il massimo tra 4 numeri
#Algoritmo per trova il massimo fra quattro numeri inseriti dall'utente.

massimo = 0
contattore = 1

while contattore <= 4:
    n = int(input("Scrivi un numero:"))
    if (n > massimo):
        massimo = n
    contattore += 1
else:
    print(massimo)