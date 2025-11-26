=========================
Python: Simulazione esame 1
=========================

Proviamo a simulare insieme una prova d'esame! in particolare stiamo simulando l'esame del 24 7 2020


TESTO
-----
Scrivere un programma che  
  

#. prenda in ingresso:
    #. un file con annotazioni di score di artefatti in ecografie polmonari, fatte da più medici diversi. 
    #. due indici di medici di cui confrontare le annotazioni

#. per ogni coppia di score s i , s j stampi il numero di volte in cui il primo medico ha annotato un’ecografica come s i ed il secondo come s j (anche quando s i = s j )
#. stampi il numero totale di volte in cui i due medici sono stati d’accordo, ed il numero di volte in cui sono stati in disaccordo


**ESMPIO File in input**

video_scores.csv::

    Video	Score M1	Score M2	Score M3	Score M4	Score M5	Score M6
    1	2	1	2	3	3	2	
    2	1	2	1	1	1	2	
    3	3	3	3	3	3	1	
    4	3	3	3	3	3	3


**ESMPIO DI OUTPUT**

python agreement.py::

    Inserire nome file: video_scores.csv
    Indice primo medico: 0
    Indice secondo medico: 4
    M0  M4  Count
    2   3   8
    1   1   5
    3   3   5
    0   0   11
    0   1   6
    Totale accordo: 28
    Totale disaccordo: 32


**SUGGERIMENTI**

Si possono implementare 5 funzioni separate:


#. una che legga il file dati e restituisca una lista di liste di score (una per ogni video)
#. una che data la lista di liste ed un indice, restituisca la lista di score associati al medico con quell’indice
#. una che data la lista di liste e due indici, restituisca un dizionario che per ogni coppia di score (s i , s j ) contiene il numero di volte in cui il primo medico ha annotato con s i e il secondo con s j
#. una che dato il dizonario (e gli indici dei medici per l’intestazione) stampi i conteggi delle varie coppie di score e calcoli e stampi i totali di accordo e disaccordo
#. una (o un main) che realizzi il programma richiesto usando le funzioni di cui sopra


Soluzione
---------

**LEGGETE E RI LEGGETE la consegna per capire se è chiara**

iniziamo seguendo i suggerimenti:

suggerimento 1
    #. una che legga il file dati e restituisca una **lista di liste** di score (una per ogni video)

**SEMPLICE**
lo abbiamo sempre fatto::

    def load_file(filename):   #definisco la funzione

        file = open(filename,"r") #apro il file in modalità read
        righe = file.readlines()  #leggo le tighe
        res = []                  #creo una variabile contenente il risultato
        
        for i in righe[1:]:       # itero sulle righe saltando la prima 
                                  # perche è un intestazione 
            res.append(i.split()[1:])   # splitto la riga, e prendo tutti gli elementi
                                        # eccetto il primo, perche è il numero del video
        return(res)

**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_file(filename)
    print(prova)


si, funziona!

suggerimento 2
    #. una che data la lista di liste ed un indice, restituisca la lista di score associati al medico con quell’indice

mmmm, che cosa ci sta chiedendo?  
ci chiede di creare una funzione che prenda in input la lista di liste (il file che abbiamo appena caricato con load_file), 
e un indice (riferito ad un medico), ci restituisca una **lista** contenente gli score che ha dato il medico.
Quindi, se come indice abbiamo inserito 1, allora il la nostra funzione deve restituire la lista [2,1,3,3,...]

**SEMPLICE**::

    def get_score(table,index):
        scores = []
        for row in table:               #itero sulla ogni riga della tabella
            scores.append(row[index])   #mi salvo solo i valori in posizione index
        return(scores)


**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_file(filename)
    scores = get_score(prova,index)
    print(scores)


si, funziona!

suggerimento 3
    #. una che data la lista di liste e due indici, restituisca un dizionario che per ogni coppia di score (s i , s j ) contiene il numero di volte in cui il primo medico ha annotato con s i e il secondo con s j

mmmm, che cosa ci sta chiedendo? 
ci chiede di creare una funzione che prenda in input la lista di liste (il file che abbiamo appena caricato con load_file), 
e *due* indici (riferiti a due medici), ci restituisca un **dizionario**. Il dizionario deve aver come chiave la coppia degli score data dai medici, e come valore il totale delle volte in cui si è verificata questa situazione.
Esempio, supponiamo che le liste degli scores dei medici m1 e m2 siano le seguenti::

    Score M1 = [2,1,3,3]
    Score M2 = [1,2,3,3]

allora il dizionario in output è il seguente::

    diz = { 
        (2,1): 1,
        (1,2): 1,
        (3,3): 3,
        }

Ora che abbiamo capito la consegna, scrivere il codice è easy :) ::

    def get_agreement(table,m1,m2):
        score_m1 = get_score(table,m1)  #uso la funzione che ho fatto prima per prendere gli score del medico m1
        score_m2 = get_score(table,m2)  #uso la funzione che ho fatto prima per prendere gli score del medico m2

        diz = dict()
        for i in range(len(score_m1)):       #itero sul range della lungheza degli score i.e il numero di video

            key = (score_m1[i],score_m2[i])  # creo la chiave, che è una coppia di score (score di m1, score di m2)
            if key in diz:                   # se la chiave è già presente nel dizionario, allora incremento il suo valore
                diz[key] = diz[key] + 1
            else:                            # altrimenti (se non è presente)
                diz[key] = 1                 # aggiungo la chiave al dizionario con valore 1

        return(diz)



**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_file(filename)
    dizionario = get_agreement(prova,m1,m2)
    print(dizionario)


si, funziona!



suggerimento 4

#. una che dato il dizonario (e gli indici dei medici per l’intestazione) stampi i conteggi delle varie coppie di score e calcoli e stampi i totali di accordo e disaccordo

In sostanza qui ci sta chiedendo di stampare l'output in un formato piu leggibile (come quelle del esempio del output), 
e ci sta anche chiedendo di calcolare il numero di volte in cui i medici sono in accordo e quelle in cui sono in disaccordo.

semplice::

    def print_agreemnt(diz,m1,m2):
        tot_agree = 0                       #inizializzo gli agree
        tot_disagree = 0                    #inizializzo i  disagree
        print("M%d\tM%d\tCount" %(m1,m2))   #stampo un intestazione 
        for i,j in diz.keys():              #itero sulle chiavi del dizionario
            print(i,"\t",j,"\t",diz[(i,j)]) #stampo score di m1, score di m2, e valore
            if i == j:                      # se sono in accordo
                tot_agree = tot_agree + diz[(i,j)]  # incremento il tot_agree
            else:                                         # se non sono in accordo
                tot_disagree = tot_disagree + diz[(i,j)]  # incremento il tot_disagree
                
        print("Totale accordo: ",tot_agree)
        print("Totale disaccordo: ",tot_disagree)



suggerimento 5

#. una (o un main) che realizzi il programma richiesto usando le funzioni di cui sopra

semplice ci chiede di mettere tutto insieme::

    def load_file(filename):

        file = open(filename,"r")
        righe = file.readlines()
        res = []
        for i in righe[1:]:
            res.append(i.split()[1:])

        return(res)

    def get_score(table,index):
        scores = []
        for row in table:
            scores.append(row[index])

        return(scores)

    def get_agreement(table,m1,m2):
        score_m1 = get_score(table,m1)
        score_m2 = get_score(table,m2)

        diz = dict()
        for i in range(len(score_m1)):
            key = (score_m1[i],score_m2[i])

            if key in diz:
                diz[key] = diz[key] + 1
            else:
                diz[key] = 1

        return(diz)



    def print_agreemnt(diz,m1,m2):
        tot_agree = 0
        tot_disagree = 0
        print("M%d\tM%d\tCount" %(m1,m2))
        for i,j in diz.keys():
            print(i,"\t",j,"\t",diz[(i,j)])
            
            if i == j:
                tot_agree = tot_agree + diz[(i,j)]
            else:
                tot_disagree = tot_disagree + diz[(i,j)]
                
        print("Totale accordo: ",tot_agree)
        print("Totale disaccordo: ",tot_disagree)




    filename = input("Inserire nome file")
    m1 = int(input("indice medico 1: "))
    m2 = int(input("indice medico 2: "))


    res = load_file(filename)
    agreement = get_agreement(res,m1,m2)
    print_agreemnt(agreement,m1,m2)


