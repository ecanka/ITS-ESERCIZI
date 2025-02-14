#Conta i numeri pari e dispari

#Algoritmo che dati 10 numeri forniti dall'utente, 
#conta quanti sono pari e quanti dispari.


pari = 0
dispari = 0
cont = 1

while cont <= 10:
    n = int(input("Scrivi un numero:"))
    if n % 2 == 0:
        pari += 1
    elif n % 2 != 0:
        dispari += 1
    cont += 1
print(f"Hai digitato: {pari} pari")
print(f"Hai digitato: {dispari} dispari")