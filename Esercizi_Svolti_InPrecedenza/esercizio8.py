#Trovare i numeri maggiori di un valore soglia
#Algoritmo che dati 7 numeri, trova e comunica i numeri 
#maggiori di un valore soglia fornito dall'utente.


soglia = int(input("Scrivi un valore soglia:"))
cont = 1
while cont <= 7:
     
     n = int(input("Scrivi il numero:"))
     
     if n > soglia:
        cont += 1
        print(n)
     else:
        cont += 1

        
