#Calcolo del fattoriale di un numero

#Algoritmo per calcolare il fattoriale di un 
#numero intero positivo fornito dall'utente.

n = int(input("Scrivi un numero:"))

while n < 0:
    print("Il numero inserito deve essere positivo ")
    n = int(input("Scrivi un numero:"))


fattoriale = 1
i = 1    
while i <= n:
    fattoriale = fattoriale * i
    i += 1
print(fattoriale)

