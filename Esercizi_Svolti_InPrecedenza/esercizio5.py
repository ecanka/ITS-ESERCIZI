#Verifica se un numero è primo

#Algoritmo per determinare se un numero intero positivo inserito 
#dall'utente è un numero primo.

primo = True
n = int(input("Scrivi un numero:"))
if n < 2:
    print("Il numero non è primo")

else:    
    div: int = 2
    while div < n:
        
        if n % div == 0:
            print("Il numero non è primo")
            primo = False
            break
        div += 1
if primo:
    print("Il numero è primo")
