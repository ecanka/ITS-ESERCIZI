
#SISTEMA DI REGISTRAZIONE DEGLI STUDENTI A CORSI
#Algoritmo che gestisce l'iscrizione degli studenti a corsi disponibili in una universita. per ogni corso ci sono un massimo di 100 posti liberi
#Richiesto il nome del corso, mostra un meni con le seguenti opzioni"iscrivi", "annulla", "visualizza", "elimina," "esci".
#-Se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili per il corso, quindi incrementa il numero di posti occupati;
#-Se l'utente inserisce "annulla", decrementa il numero dei posti occupati;
#-Se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati nel corso;
#-Se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
#-Se l'utente inserisce "esci", termina l'algoritmo.



while True:
    
    corso = str(input("Inserisci nome corso:"))

    max_posti = 10
    posti_occupati = 0

    while True:

        nuovo_corso = corso
        
        opzione = str(input("Scegli una delle opzioni: (iscrivi), (annulla), (visualizza), (elimina), (esci):"))
     
        if opzione == "iscrivi":
          
            if max_posti > 0:
                    max_posti -= 1
                    posti_occupati += 1
            else: print("Non ci sono posti disponibili")

        elif opzione == "annulla":
          
            if posti_occupati > 0:
               max_posti += 1
               posti_occupati -= 1

            else: print("Tutti i posti sono disponibili")

        elif opzione == "visualizza":
          
            print("Posti ancora disponibili:",max_posti)
            print("Totale posti occupati:",posti_occupati)

        elif opzione == "elimina":

            print("Corso eliminato, inserisci un nuovo corso")
            break
              
          
          
        elif opzione == "esci":
            break
         
