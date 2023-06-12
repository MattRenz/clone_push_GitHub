import os
import subprocess
import datetime
import sys
import time

pathDir_File = os.environ.get("PROGRAMDATA") + "/clone_push_BitBucket/DB_dir.txt"
today = datetime.date.today()

def allert():
    
    testo = "\n Una volta eseguita la push ricorda di svuotare la cartella principale \n per evitare che si accumolano più cartelle quando fai la clone"
    codice_colore = "\033[91m"  # Codice ANSI per il colore rosso
    codice_reset = "\033[0m"  # Codice ANSI per ripristinare il colore predefinito

    testo_colorato = codice_colore + testo + codice_reset
    print(testo_colorato)

def allertCartellaNonModificata():
    
    testo = "\n Per evitare errori non eseguire la push su repository che NON sono stati modificati"
    codice_colore = "\033[32m"
    reset_colore = "\033[0m"
    testo_formattato = f"{codice_colore}{testo}{reset_colore}"
    print(testo_formattato)
    
def SceltaFilePush():
    
    with open(pathDir_File, "r") as file:
    
        lFile = os.listdir(file.readline())
        
    return lFile
 
def push():
    

    comando_stato = "git status"
    comando_aggiungi = "git add ."
    comando_commit = f'git commit -m "aggiunto il {today.day}/{today.month}/{today.year}"'
    comando_push = "git push"

    output_stato = subprocess.check_output(comando_stato, shell=True)
    output_agggiungi1 =  subprocess.check_output(comando_aggiungi, shell=True)
    output_agggiungi2 = subprocess.check_output(comando_aggiungi, shell=True)
    output_commit =  subprocess.check_output(comando_commit, shell=True)
    output_push = subprocess.check_output(comando_push, shell=True)
    
    
    try:
        print (output_stato.decode("utf-8"))
    except UnicodeDecodeError:
        print (output_stato.decode("utf-8", errors="ignore"))
        
        
    try:
        print (output_push.decode("utf-8"))
    except:
        print (output_push.decode("utf-8", errors="ignore"))

    allert()
        
        
def PushSingolo(dir_push: str):
        
    with open(pathDir_File, "r") as file:
        
        filePush = file.readline() + "/" + dir_push
        
        os.chdir(filePush)
    

    push()
    
                   
def PushScelta(dir_push_utente: str):
    
    if dir_push_utente.isdigit(): # int
        
        dir_push_utente = int(dir_push_utente)
        
        with open(pathDir_File, "r") as file:
            
            f = file.readline()
            push_scelta_utente = os.listdir(f)
            
            path_push_int = f + "/" + push_scelta_utente[dir_push_utente - 1]
            
            os.chdir(path_push_int)

        push()

        
    else:  # str
        
        with open(pathDir_File, "r") as file:
            
            path_puh_str = file.readline() + "/" + dir_push_utente
            
            os.chdir(path_puh_str)
        
        push()
       
                             
def PushMultiplo():
    
    ldir_push = SceltaFilePush()
    
    for dir_push in ldir_push:
        
        with open(pathDir_File, "r") as file:
            
            path_push_multiplo = file.readline() + "/" + dir_push
            
            os.chdir(path_push_multiplo)
            
        push()
 
            
    

  

