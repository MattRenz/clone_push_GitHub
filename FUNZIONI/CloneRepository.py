import pandas
import os
import subprocess

pathDir_File_Link: str = os.environ.get("PROGRAMDATA") + "/clone_push_BitBucket/repository_linkGH.csv"
pathDir_File = os.environ.get("PROGRAMDATA") + "/clone_push_BitBucket/DB_dir.txt"


def RepositoryPresenti(): 

    file = pandas.read_csv(pathDir_File_Link, sep=",", header=0)

    lrepository: list = file['repository'].values
    
    return lrepository


def ScetlaRepository_Clone(SceltaUtente): # restituisce il link della repository scelta / clona da terminale
    
    with open(pathDir_File, "r") as file:
        
        os.chdir(file.readline())
        
    file = pandas.read_csv(pathDir_File_Link, sep=",", header=0)
     
    if SceltaUtente.isdigit():
        
        SceltaUtente = int(SceltaUtente)
        
        file = pandas.read_csv(pathDir_File_Link, sep=",", header=0) 
    
        x = file['repository'].values
        
        SceltaUtente = x[SceltaUtente -1]
        
        corrispondenza: str = file.loc[file['repository'] == SceltaUtente, 'link']
        corrispondenza_split = corrispondenza.values[0].split()
        
        comando = "git clone " + corrispondenza.values[0]
        output = subprocess.check_output(comando, shell=True)
                
        try:
            return (output.decode("utf-8"))
        except UnicodeDecodeError:
            return(output.decode("utf-8", errors="ignore"))
        
        
    else: # Caso str
            
        for i in RepositoryPresenti():
            
            match_ok = 0
            if SceltaUtente.lower() == i.lower():
                match_ok +=1
                    
                corrispondenza: str = file.loc[file['repository'] == SceltaUtente, 'link']
                corrispondenza_split = corrispondenza.values[0].split()
                
                if corrispondenza_split[0] != 'git':
                    
                    return f'\n Link: {corrispondenza.values[0]} non valido'
                
                else:
                    comando = "git push " + corrispondenza.values[0]
                    output = subprocess.check_output(comando, shell=True)
                
                    try:
                        return (output.decode("utf-8"))
                    except UnicodeDecodeError:
                        return(output.decode("utf-8", errors="ignore"))
        
        if match_ok == 0: 
            s = f'\n Repository {SceltaUtente} non trovata'
            return s
        

   

    
        


    


