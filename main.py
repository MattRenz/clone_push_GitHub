import FUNZIONI.Impostazioni as impostazioni
import FUNZIONI.menu as menu
import FUNZIONI.CloneRepository as clone
import FUNZIONI.PushRepository as push
import sys


impostazioni.ImpostazioneCartellaClonePush()


while(1):

    menu.Menu()
   
    operazione = input("\n ")
        
    if operazione != "1" and operazione != "2" and operazione != "3" and operazione != "4":
        
        impostazioni.alert_errore_operazione(str(operazione))
    
    else:
        
        operazione = int(operazione)
    # INSERISCI NUOVA REPOSITORY
    if operazione == 1:
        
        impostazioni.InserisciNuovaRepository()
        
    # CLONE REPOSITORY
    if operazione == 2:
        
        while(1):
            
            print("\n Scegli repository: (0 = indietro)\n")
            
            count = 1
            for i in clone.RepositoryPresenti():
            
                print(f'{count}) {i}')
                count +=1
                
            SceltaUtente = input("\n Repository: ")
            
            if SceltaUtente.isdigit():
                
                if int(SceltaUtente) == 0:
                   break;
            
            clone_ =  clone.ScetlaRepository_Clone(SceltaUtente)
            print(clone_)
                    
    # PUSH REPOSITORY
    if operazione == 3:
        
        push.allertCartellaNonModificata()

        ldir_push = push.SceltaFilePush()
        
        if len(ldir_push) == 1:
            
            push.PushSingolo(ldir_push[0])
        
        if len(ldir_push) > 1:
            
            print(f'\n Ci sono {len(ldir_push)} cartelle')
            
            oper: int = int(input("\n 1) Pushare tutte le cartelle 2) Scegliere le cartelle da pushare: "))
        
            if oper == 1:
                
                push.PushMultiplo()
        
            if oper == 2:
                
                count: int = 1
                print(" ")
                
                for i in ldir_push:
                    
                    print(f'{count}) {i}')
                    count +=1
                    
                dir_puhs_utente = input("\n Cartella: ")
                
                if dir_puhs_utente.isdigit():
                    
                    push.PushScelta(dir_puhs_utente)
                
                else:
                    
                    match_ok = 0
                    for i2 in ldir_push:
                        
                        if i2.lower() == dir_puhs_utente.lower():
                            
                            push.PushScelta(dir_puhs_utente)
                            match_ok = 1
                            
                    if match_ok == 0: 
                            
                        print(f'\n Cartella {dir_puhs_utente} non trovata')

    # USCITA
    if operazione == 4:
        sys.exit()
        
                
        
        
        
     
        
    



            
        
        
  