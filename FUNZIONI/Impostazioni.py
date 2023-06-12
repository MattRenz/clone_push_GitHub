import os
import sys

percorso_dir_base: str = os.environ.get("PROGRAMDATA") + "/clone_push_BitBucket"

pathDir_File_Link: str = os.environ.get("PROGRAMDATA") + "/clone_push_BitBucket/repository_linkGH.csv"

def alert_errore_operazione(operazione):
    
    testo = f'operazione "{operazione}" non valida'
    codice_colore = "\033[91m"  # Codice ANSI per il colore rosso
    codice_reset = "\033[0m"  # Codice ANSI per ripristinare il colore predefinito

    testo_colorato = codice_colore + testo + codice_reset
    print(testo_colorato)

def CambioPathWindows(path: str):
    
    path = path.replace('"', "")    

    if ("\\"in path):
    
        splitPath = path.split("\\")
        users = splitPath[0]
        newPath = users

        count = 0
        for i in splitPath[1:]:
            count +=1
            newPath += "/" + splitPath[count]
            
        return newPath
    
    elif ("/" in path):
        return path
    
    else:

        print("\n Inserire un path valido")
        sys.exit(0)

def ImpostazioneCartellaClonePush():

    if os.path.exists(percorso_dir_base): 
        pass
    else:
        os.mkdir(percorso_dir_base)
    
    if os.path.exists(pathDir_File_Link): 
        pass
    else:
        with open(pathDir_File_Link, "w") as file:
            sc = "repository,link"
            file.write(sc + "\n")
    
    if os.path.exists(percorso_dir_base + "/DB_dir.txt"):  
        pass    
    else:
        
        print("\n Inserie il path della cartella dove verrà effeetuata la CLONE e la PUSH")
        
        print("\n Quando inserisci il path assicurati di non inesrire come separatore '\\' ma '\\\\'")
        
        path: str = input("\n Path: ")
        
        path = CambioPathWindows(path)
            
        with open(percorso_dir_base + "//DB_dir.txt", "w") as file:
            
            file.write(path)
        
def InserisciNuovaRepository():
       
    nomeRepository: str = input("\n Nome repository: ")
    link: str = input("\n Link: ")
    
    with open(pathDir_File_Link, 'a') as file:
        
       file.write(nomeRepository+","+link + "\n")


    
    
    
