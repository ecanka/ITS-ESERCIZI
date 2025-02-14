#Sistema di gestione per un parcheggio

#Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio con un numero massimo di posti dato in input. 
# L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:
# se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
# se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
# se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
# se l'utente inserisce "esci", termina l'algoritmo.
# Torna all'inserimento di una opzione finché l'utente non seleziona "esci".


n = int(input("Inserisci il nr massimo di parcheggi:"))
posti_liberi = n
posti_occupati = 0

while True:
    opzione = str(input("Inserisci una opzione (ingresso, uscita, stato, esci:)"))
    
    

    if opzione =="ingresso":

        if posti_liberi > 0:

            n -= 1
            posti_occupati += 1

            print("Posti liberi:",n)
            print("Posti occupati:",posti_occupati)

        else: print("Il parcheggio e pieno.")

    elif opzione == "uscita":

        if posti_occupati >= 0:

            n += 1
            posti_occupati -= 1

            print("Posti liberi:", n)
            print("Posto liberato:", posti_occupati)

        else: print("Parcheggio vuoto")

    elif opzione == "stato":

        print("Posti liberi:", n)
        print("Posti occupati:", posti_occupati)

    elif opzione == "esci":
        break
    else: print("Inserisci un opzione valida.")



        


    



