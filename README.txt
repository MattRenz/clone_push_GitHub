PROGETTAZIONE PROGRAMMA CLONE-PUSH GitHub

Programma che permetta di fare la clone e la push (anche multipla di più file) su GitHub.

Questo progetto nasce per velocizare la push e la clone su GitHub.
Dato che i comandi da terminale sono sempre gli stessi, questo programma esegue i comandi da linea di comando 
velocizzando il lavoro dell'utente. Permette di clonare singole repository che abbiamo salvate sul nostro profilo GitHub, 
dopo che abbiamo modificato queste repository Permette di effetuare la push o di cartelle singole, o di tutte le cartelle che 
abbiamo modificato, velocizzando così il lavoro di push. 

Il programma andrà a creare delle cartelle e i file contenenti i link alle nostre repository dentro: 

    C:\ProgramData\clone_push_BitBucket



Funzionalità del Sistema (Push):

	1 Push Singolo

		1 Impostazione cartella di lavoro: pathFile + dir_da_pushare
		1.1 pushare la cartella
			
	2 Push Scelta / Multiplo

		1 Scegliere se 1) pushare multiplo 2) pushare a Scelta
			1.1 Pushare repository a scelta
				1.2.1 Controllare se l'utente ha scelto il NUMERO della cartella o il NOME della cartella
					1.2.1.1 NUMERO
						1.2.1.1.1 Modificare l'ambiente di lavoro, prendendosi dal numero il nome della cartella
						1.2.1.1.2 pushare la cartella
					
					1.2.1.2 NOME: 
						1.2.1.2.2 Controllare se la cartella scelta dall'utente esista nei file da pushare
						1.2.1.2.2 Modificare l'ambiente di lavoro, mettendo la cartella scelta dall'utente nel paht della cartella di lavoro
						1.2.1.2.3 pushare la cartella
						
			1.2 Pushare tutte le repository

				

ERRORI PROGRAMMA:

    Il Programma in qustione ha degli errori legati alla gestione di GitHub, questi errori fanno morire il Programma.

    Tali errori o motivi di non funzionamento del Programma sono:

        1) Il sistema operativo non è Windows
        2) Il Programma non ha le autorizzazioni necessarie per crere le cartelle all'interno del file
        3) Non si possiede l'autorizzazione per effetuare la push su GitHub, questo programma infatti deve essere eseguito 
        solamente dopo aver impostato GitHub

    Possibili errori legati alla clone o alla push:

        1) Il programma NON gestisce i link delle repository, una volta inseriti i link delle repository per farre la clone
        saranno quelli per sempre. Ciò significa che se andiamo a cambiare (su GitHub) nome ad una repository, automaticamente 
        cambierà anche il nome del link, e quindi il link di clone salvato non è più valido

        2) Cercare di  pushare una cartella/repository non modificata solleva un eccezioneche che manderà in errore il programma

        3) Clonare una cartella che è già stata clonata manderà in errore il programma



Il programma nonostante ha dei problemi (che però non sono inerenti all'esecuzione del programma) funziona bene

In un ipotetica versione successiva verrà implementato: 

    0) Guida di impostazione Software
    1) Possibilità di eliminare il link di una repository
    2) Allert in caso di tentativo di clone una cartella già clonata
    3) Allert in caso di tetnativo di pushare una cartella che non è stata modificata
    4) Versione Linux e altri servizi 



In caso di domande generiche o sul funzionamento del Programma o se si vuole visionare il codice: 
    
    email: mattrenzwork9@gmail.com








