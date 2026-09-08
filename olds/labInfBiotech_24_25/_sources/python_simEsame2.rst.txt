=========================
Lezione 11.2 - Python: Simulazione esame 2 (19/6/2020)
=========================

Testo e soluzioni a cura di Andrea Passerini ed Antonio Longa, riviste da Luca Marchetti.

**NOTA 1:** questi esercizi sono relativi alla seconda parte dell'esame, la parte che si svolgera'
al computer. Prima di questa ci sara' una breve parte su foglio protocollo in cui vi sara' chiesto 
di correggere un programma python dato o di scrivere cosa stampa un programma Python fornito
nel testo dell'esercizio.

**NOTA 2:** Per domande sulle soluzioni o sui testi, per favore riferitevi al tutore del corso:

**Domenico Stefani:**  domenico dot stefani at unitn dot it

**IMPORTANTE:** il testo completo di file da processare e le relative soluzioni sono
disponibili nel seguente archivio zip: :download:`zip <prove_esame_lab/19_06_2020.zip>`

TESTO
-----
Scrivere un programma che  
  

#. prenda in ingresso un file con annotazioni di score di artefatti in ecografie polmonari, fatte da più medici diversi.
#. calcoli per ogni video lo score con pi‘ănnotazioni (score di consenso)
#. restituisca per ogni score il numero di video annotati con quello score di consenso



**ESEMPIO File in input**

video_scores.csv::

    Video	Score M1	Score M2	Score M3	Score M4	Score M5	Score M6
    1		2		1		2		3		3		2	
    2		1		2		1		1		1		2	
    3		3		3		3		3		3		1	
    4		3		3		3		3		3		3


**ESEMPIO DI OUTPUT**

python majority.py::

    Inserire nome file: video_scores.csv
    Majority score counts
    2 (19) 1 (16) 0 (16) 3 (9)


**SUGGERIMENTI**

Si possono implementare 5 funzioni separate:


#. una che legga il file dati e restituisca per ogni video la lista di score, ignorando eventuali valori ’NC’ (non classificabile)
#. una che data una lista di score restituisca lo score più frequente
#. una che data le liste di score di tutti i video, calcoli per ciascuno lo score più frequente (usando la funzione precedente) e restituisca un dizionario di conteggi degli score più frequenti 
#. una che stampi il dizionario di score e conteggi in ordine decrescente per conteggi.
#. una (o un main) che realizzi il programma richiesto usando le funzioni di cui sottostringa_piu_lunga


Soluzione
---------

**LEGGETE E RI LEGGETE la consegna per capire se è chiara**

iniziamo seguendo i suggerimenti:

**suggerimento 1**

    1) una che legga il file dati e restituisca per ogni video la lista di score, ignorando eventuali valori ’NC’ (non classificabile)

**SEMPLICE**
lo abbiamo sempre fatto::


    def load_scores(filename):
        f = open(filename)
        all_scores = []
        f.readline()
        for row in f:               # itero su ogni riga del file in input
            data = row.split()      # splitto la riga
            tmp = []                # uso un array temporaneo
            for i in data[1:]:      # per ogni numero di artefatti in data (senza l'elem in pos 0 [che è il numero video])
                if i != "NC":       # se i non è uguale a NC
                    tmp.append(int(i))   # lo converto in intero e lo appendo a tmp
            all_scores.append((data[0],tmp)) #aggiungo al risultato una tupla, contenente in pos 0 il numero del video
                                             # in pos 1 l'array di score (senza NC)

        f.close()               # chiudo il file
        return all_scores       # ritorno il risultato


**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_scores(filename)
    print(prova)


si, funziona!

**suggerimento 2**

    2) una che data una lista di score restituisca lo score più frequente

mmmm, che cosa ci sta chiedendo? 
data una lista di scores di un determinato video, resituisce lo score piu frequente.
Es data la lista::

    Video 1 = [2,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,4]

la funzione ritorna 1, perche è lo score piu frequente.


**SEMPLICE**::

   def compute_majority_score(scores):
	counts = {}                     # inizializzo un diz
	for score in scores:            # itero su tutti gli scores
		if not score in counts:     # se score non è in count
			counts[score] = 1           # lo aggiungo e ci mento valore 1
		else:			            # altrimenti (se score è in count)
			counts[score] += 1          # incremento il valore di count 

	max_score=-1                            # inizializzo max_score a -1
	max_count=0                             # inizializzo max_count a 0
	for (score,count) in counts.items():    # itero sul dizinario che ho creato sopra
		if count > max_count:               # se il conteggio è maggiore di max_count
			max_score = score               # aggiorno max score
			max_count = count               # aggiorno max count

	return max_score                        # ritorno il valore


**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    file_name = "video_scores.csv"
    data = load_scores(file_name)
    print(data[0])
    print(compute_majority_score(data[0]))


si, funziona!

**suggerimento 3**

    3)  una che data le liste di score di tutti i video, calcoli per ciascuno lo score più frequente (usando la funzione precedente) e restituisca un dizionario di conteggi degli score più frequenti 

mmmm, che cosa ci sta chiedendo? 
ci chiede di calcolare un diz, che abbia come chiave il numero di scores piu frequente di ogni video, e come valore le volte che compare.
Es supponiamo di avere queste liste:: 

    Video 1 = [2,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,4] 
    Video 2 = [2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4] 
    Video 3 = [2,1,3,3,1,1,1,2,2,2,2,2,2,2,2,2,2] 
    Video 4 = [2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]  

Lo score piu frequente è::
    
    score piu freq di video 1 = 1
    score piu freq di video 2 = 3
    score piu freq di video 3 = 2
    score piu freq di video 4 = 3

il dizionario in output è il seguente::

    diz = { 
        2: 1,
        3: 2,
        1: 1,
        }

Ora che abbiamo capito la consegna, scrivere il codice è easy :) ::

    def compute_majority_counts(all_scores):
        majority_counts = {}
        for (video,scores) in all_scores:
            majority_score = compute_majority_score(scores)		
            if not majority_score in majority_counts:
                majority_counts[majority_score] = 1
            else:	
                majority_counts[majority_score] += 1
        return majority_counts



**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    filename = "video_scores.csv"
    all_scores = load_scores(filename)
    majority_counts = compute_majority_counts(all_scores)
    print(majority_counts)



si, funziona!



**suggerimento 4**

	4) una che stampi il dizionario di score e conteggi in ordine decrescente per conteggi.


semplice::

    def print_majority_counts(majority_counts):
        score_list = [(count,score) for (score,count) in majority_counts.items()]
        score_list.sort(reverse=True)
        print("Majority score counts")
        print("\t".join(["%d (%d)" %(score,count) for (count,score) in score_list]))



**suggerimento 5**

	5) una (o un main) che realizzi il programma richiesto usando le funzioni di cui sopra

semplice ci chiede di mettere tutto insieme::

    
    def load_scores(filename):
        f = open(filename)
        all_scores = []
        f.readline()
        for row in f:
            data = row.split()
            all_scores.append((data[0],[int(i) for i in data[1:] if i != 'NC']))
        f.close()
        return all_scores

    def compute_majority_score(scores):
        counts = {}
        for score in scores:
            if not score in counts:
                counts[score] = 1
            else:			
                counts[score] += 1

        max_score=-1
        max_count=0
        for (score,count) in counts.items():
            if count > max_count:
                max_score = score
                max_count = count

        return max_score

    def compute_majority_counts(all_scores):
        majority_counts = {}
        for (video,scores) in all_scores:
            majority_score = compute_majority_score(scores)		
            if not majority_score in majority_counts:
                majority_counts[majority_score] = 1
            else:	
                majority_counts[majority_score] += 1
        return majority_counts

    def print_majority_counts(majority_counts):
        score_list = [(count,score) for (score,count) in majority_counts.items()]
        score_list.sort(reverse=True)
        print("Majority score counts")
        print("\t".join(["%d (%d)" %(score,count) for (count,score) in score_list]))


    filename = input("Inserire nome file: ")
    all_scores = load_scores(filename)
    majority_counts = compute_majority_counts(all_scores)
    print_majority_counts(majority_counts)
