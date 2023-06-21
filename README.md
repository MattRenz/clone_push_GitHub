# Titolo del Progetto

clone push GitHub. Programma che permetta di fare la clone e la push (anche multipla di più file) su GitHub.

## Descrizione

    Questo progetto nasce per velocizare la push e la clone su GitHub.
    Dato che i comandi da terminale sono sempre gli stessi, questo programma 
    esegue i comandi da linea di comando velocizzando il lavoro dell'utente. 
    Permette di clonare singole repository che abbiamo salvate sul nostro profilo GitHub, 
    dopo che abbiamo modificato queste repository Permette di effetuare la push o di 
    cartelle singole, o di tutte le cartelle che abbiamo modificato, velocizzando così il lavoro di push. 

## Funzionalità

    0. Impostazione programma

        0.1 Impoostare la cartella dove verrà effetuata la CLONE delle repository
        // (tale cartella può essere stare sul desktop o in qualsiasi altro percorso che vogliamo, 
        //   l'importante sta nel passare il path completo al programma)

    1. Inserisci Repository
        1.2 Nome repository
        1.3 Link di clone GitHub: 
            (`https://github.com/tuo-username/nome-repository.git`)

    2. Clona Repository

        2.1 Scegli repository da clonare (elenco numerato) 
        // Si può scegliere la repository o dal nome o dal numero
        2.2 Clone repository scelta 

    3. Push

        3.1 Push Singolo (in caso è presente solo 1 cartella modificata)
            3.1.2 Push con esito risposta

        3.2 Push multiplo (in caso sono presenti più cartelle modificate)
            3.2.1 Scegli se pushare TUTTE le cartelle 
                3.2.1.1 Push con esito risposta
            3.2.2 Scegli se pushare le singole cartelle 
                3.2.2.1 Push con esito risposta

## Installazione

1. Clona il repository: `git clone https://github.com/MattRenz/clone_push_BitBucket.git`
2. Il programma andrà a creare delle cartelle e i file contenenti i link alle nostre repository dentro:
    `C:\ProgramData\clone_push_BitBucket`

## Utilizzo

1. Dentro la directory di progetto precedentemente clonata entrare dentro:
    `\clone_push_BitBucket\build_clone_push_BitBucket\exe.win-amd64-3.11`
2. Da terminale esegui l'applicazione: `main.exe start`
3. Se non da terminale si può eseguire direttamente l'applicazione `main.exe` (che si trova sempre dentro la repository clonata)
4. Aperto il programma
    1 Inserire una nuova repository
    2 Clonare repository inserita
    3 Modificarla
    4 Eseguire la push

## Bug

- Bug, errori e morte programma:

    Il Programma in qustione ha degli errori legati alla gestione di GitHub,
    questi errori fanno morire il Programma.

- Tali errori o motivi di non funzionamento del Programma sono:

        1) Il sistema operativo non è Windows
        2) Il Programma non ha le autorizzazioni necessarie per crere le cartelle all'interno del file
        3) Non si possiede l'autorizzazione per effetuare la push su GitHub, 
        questo programma infatti deve essere eseguito solamente dopo aver impostato GitHub 

- Possibili errori legati alla clone o alla push:

        1) Il programma NON gestisce i link delle repository, una volta inseriti i link delle repository per farre la clone
        saranno quelli per sempre. Ciò significa che se andiamo a cambiare il nome ad una repository (su GitHub), automaticamente 
        cambierà anche il nome del link, e quindi il link di clone salvato non è più valido.

            Esempio link clone: `git clone https://github.com/tuo-username/nome-repository.git`

            Il link è formato dal nome della repository, se dovessimo andare a cambaire nome ad una repositroy che abbiamo salvato        
            automaticamente il link che abbiamo diventa obsoleto

        2) Cercare di pushare una cartella/repository non modificata solleva un eccezioneche che manderà in errore il programma

        3) Clonare una cartella che è già stata clonata manderà in errore il programma

- Nuove funzionalità ipotetica versione successiva:
        0) Guida di impostazione Software
        1) Possibilità di eliminare il link di una repository
        2) Allert in caso di tentativo di clone una cartella già clonata
        3) Allert in caso di tetnativo di pushare una cartella che non è stata modificata
        4) Possibilità di impostare il messaggio di commit -m ""
        5) Versione Linux e altri servizi

## Consigli

    - Controllare che la cartella dove si effetua la clone sia sempre vuota
    - Non pushare cartelle non modificate
    - Non clonare cartelle non modificate
    - In caso di voler cambiare nome ad una repository eliminare il link nel file csv salvato dentro: (v. Installazione 2. )

## Contatti

- In caso di domande generiche sul funzionamento del Programma, se si vuole visionare il codice
  o per suggerimenti:
  
    email: <mattrenzwork9@gmail.com>
