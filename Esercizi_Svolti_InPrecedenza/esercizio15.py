#ASSEGNAZIONE DIN UN TUTOR


#Algoritmo che assegna i 10 tutor disponibili agli studenti che necessitano di recupero in un istituto scolastico.
#Per ogni studente dato in input il sistema deve controllare la disponibilita dei tutore e nel caso di disponibilita assegnarlo allo studente.
#Se il numero di tutor scende a zero occorre aumentare il numero dei studenti in lista d'attesa.Occore confermare sia l'assegnazione del tutor con 
#successo che l'inserimento nella lista d'attesa allo studente. L'algoritmo termina solo quando il numero di tutor e pari a 0 e la lista d'attesa
#conta 50 studenti.

tutor = 10
attesa = 0

while True:

    studenti = str(input("Inserisci nome studente:"))

    if tutor > 0:

        tutor -= 1
        print("Tutor asseganto con successo:")

    
    else:
        attesa += 1
        print("Studente aggiunto in lista d'attesa")

    if tutor == 0 and attesa > 50:
        break
    



