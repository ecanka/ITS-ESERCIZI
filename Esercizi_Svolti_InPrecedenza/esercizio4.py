#Controllo della parità di un numero
#Algoritmo utile a determinare se un numero inserito 
#dall'utente è pari o dispari.

n = int(input("Scrivi un numero:"))


if n % 2 == 0:
    print("Il numero è pari.")
else:
    print("Il numero è dispari.")
