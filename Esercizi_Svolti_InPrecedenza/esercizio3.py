#Calcolo della somma di numeri positivi
#Algoritmo che calcola la somma dei soli 
#numeri positivi tra 5 valori inseriti dall'utente.

somma = 0
contattore = 1

while contattore <= 5:
    n = int(input("Inserisci un valore:"))
    if n >0:
        somma += n
    contattore += 1
else: 
    print( somma ) 