#CALCOLO DELLA SOMMA DEI QUADRATI FINO A UN NUMERO INTERO POSITIVO n

#Algoritmo che dato un numero intero positivo n definito dall'utente, calcola la somma: 1(2) + 2(2) + 3(2)+ n(2),
#mostrando in output il risultato. Se n e negativo, l'algoritmo mostra un messaggio di errore e termina.



while True:
    n = int(input("Inserisci un numero intero positivo:"))

    if n / 2 == 0 and n > 0:

        while True:

            somma = 0
            i = 1


        
            if i > n:

                somma = somma + (i * i)
                i += 1

            print("La somma e:", somma)
            break

        
            

    else: print("Errore, n deve essere positivo.")

    

    
