===========================
Lezione 11.3 - Python: Simulazione esame 3 (13/2/2020)
===========================

Testo e soluzioni a cura di Andrea Passerini ed Antonio Longa, riviste da Luca Marchetti.

**NOTA 1:** questi esercizi sono relativi alla seconda parte dell'esame, la parte che si svolgera'
al computer. Prima di questa ci sara' una breve parte su foglio protocollo in cui vi sara' chiesto 
di correggere un programma python dato o di scrivere cosa stampa un programma Python fornito
nel testo dell'esercizio.

**NOTA 2:** Per domande sulle soluzioni o sui testi, per favore riferitevi al tutore del corso:

**Domenico Stefani:**  domenico dot stefani at unitn dot it

**IMPORTANTE:** il testo completo di file da processare e le relative soluzioni sono
disponibili nel seguente archivio zip: :download:`zip <prove_esame_lab/13_02_2020.zip>`

TESTO
-----
Scrivere un programma che prenda in ingresso un file di proteine ciascuna rappresentata da
  

#. nome (stile fasta)
#. sequenza di residui
#. sequenza di etichette di legame con RNA dei residui (’+’ = lega , ’-’ non lega)


estragga per ogni proteina la sua sottosequenza di legame più lunga, e stampi l’elenco di proteine e loro rispettiva sottesquenza ordinato per lunghezza della sottosequenza.




**ESEMPIO File in input**

rbp_binding::

    >1A34:A
    TGDNSNVVTMIRAGSYPKVNPTPTWVRAIPFEVSVQSGIAFKVPVGSLFSANFRTDSFTSVTVMSVRAWTQLTPPVNEYSFVRLKPLFKTGDSTEEFEGRASNINTRASVGYRIPTNLRQNTVAADNVCEVRSNCRQVALVISCCFN
    +---------+--------+--++++++-----------------------------------+--+-------------------------------------------------------------------------+-+----
    >1A9N:B
    IRPNHTIYINNMNDKIKKEELKRSLYALFSQFGHVVDIVALKTMKMRGQAFVIFKELGSSTNALRQLQGFPFYGKPMRIQYAKTDSDIISKMRG
    -----+-+-++--++-++---+----------------+++++++++++-+-+---------------------+--+-+++++++++------


**ESEMPIO DI OUTPUT**

python rbp_binding_stats.py::

    inserire nome file: rbp_binding
    1M90:M TSKKKRQRGSRTHGGGSHKNRRGAGHRGGRGDAGRDKHEFHN
    1M90:D RQGWRRRIGNLGPWNPSRVRSTVPQQGQ
    1M90:N RKGSSRRTRFNKGRRSKRMMVNR
    1M90:2 TGAGTPSQGKKNTTTHTKCRRCG
    1M90:C KARGTKWPNVRGVAMNAVDH
    ...


**SUGGERIMENTI**

Si possono implementare 5 funzioni separate:

#. una che legga il file dati e restituisca una mappa proteina → sequenza proteica e sequenza di etichette di legame.
#. una che data una mappa proteina → sequenza proteica e sequenza di etichette ne restituisca una proteina → sottosequenza di binding più lunga in essa contenuta (usando una funzione ausiliaria, vedi sotto)
#. una funzione ausiliaria che data una coppia sequenza proteica, sequenza di etichette di legame restituisca la sottosequenza di binding più lunga
#. una che data una mappa proteina → sottosequenza di binding stampi la lista di coppie proteina, sottosequenza ordinate per lunghezza della sottosequenza
#. una (o un main) che realizzi il programma richiesto usando le funzioni di cui sopra


Soluzione
---------

**LEGGETE E RI LEGGETE la consegna per capire se è chiara**

iniziamo seguendo i suggerimenti:

**suggerimento 1**
    
    1) una che legga il file dati e restituisca una mappa proteina → sequenza proteica e sequenza di etichette di legame.


Quindi dobbiamo creare un diz tipo questo::

    3BSO:A': ('SKISKLVIAELDFYVPRQEPMFRWMRFS', '--------------------')
    3BSO:B': ('SKISKLDFYVPRQEPMFRWMRFS', '---------------++++-')



Soluzione::

    def load_data(filename):
        f = open(filename)
        prots = {}
        for row in f:
            name = row[1:].strip()
            seq = f.readline().strip()
            bind = f.readline().strip()
            prots[name] = (seq,bind)
        f.close()
        return prots



**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_data(filename)
    print(prova)


si, funziona!

**suggerimento 2**
    
    2) una che data una mappa proteina → sequenza proteica e sequenza di etichette ne restituisca una proteina → sottosequenza di binding più lunga in essa contenuta (usando una funzione ausiliaria, vedi sotto)


mmmm, che cosa ci sta chiedendo? 
bho, leggiamo il suggerimento 3

**suggerimento 3**

    3) una funzione ausiliaria che data una coppia sequenza proteica, sequenza di etichette di legame restituisca la sottosequenza di binding più lunga


mmmm, che cosa ci sta chiedendo? 
una funzione che prenda in input una coppia (sequenza proteica, legame(+,-))e restituisca la sottosequenza piu lunga es::

    # DATA LA COPPIA:
    sequ = 'SKISKLDFYVPRQEPMFRWMRFS'
    bind = '+++++++-----------++++-'

    # la funzione ritorna
    'SKISKLD'


**SEMPLICE**::

    def longest_binding(seq, bind):
        longest = ""
        i = bind.find("+")
        while i != -1:
            j = bind.find("-", i)
            if j == -1:
                j = len(seq)
            if j-i > len(longest):
                longest = seq[i:j]
            i = bind.find("+", j)
        return longest


**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_data(filename)
    seq = prots["1A34:A"][0]
    bind = prots["1A34:A"][1]
    seq_piu_lunga = longest_binding(seq, bind)
    print(seq_piu_lunga)   


si, funziona!

Perfetto, ora possiamo passare al suggerimento 2:

**suggerimento 2**

    2) una che data una mappa proteina → sequenza proteica e sequenza di etichette ne restituisca una proteina → sottosequenza di binding più lunga in essa contenuta (usando una funzione ausiliaria, vedi sotto)

mmmm, che cosa ci sta chiedendo? 

ci chiede di calcolare un diz, che abbia come chiave il nome della proteinva, e come valore la sottosequenza piu lunga.

Es supponiamo di avere queste liste:: 

    3BSO:A': ('SKISKLVIAELDFYVPRQEPMFRWMRFS', '-++-----------------')
    3BSO:B': ('SKISKLDFYVPRQEPMFRWMRFS', '---------------++++-')
    3BSO:B': ('SKISKLDFYVPRQEPMFRWMRFS', '+++++++++-------++++-')

il diz risultato è il seguente::

    {    
        3BSO:A': 'KI',
        3BSO:B': 'WMRF',
        3BSO:B': 'SKISKLDF'
    }


Ora che abbiamo capito la consegna, scrivere il codice è easy :) ::

    def longest_bindings(prots):
        prot_longest = {}
        for prot in prots:
            longest = longest_binding(prots[prot][0],prots[prot][1])
            prot_longest[prot] = longest
        return prot_longest



**E' corretto il codice che abbiamo scritto fino ad ora?**
non lo so, ma posso verificarlo::

    prova = load_data(filename)
    diz = longest_bindings(prot)
    print(diz)  


si, funziona!


**suggerimento 4**

	4) una che data una mappa proteina → sottosequenza di binding stampi la lista di coppie proteina, sottosequenza ordinate per lunghezza della sottosequenza

semplice::

    def print_longest(prot_longest):

        l = [(len(bind),prot,bind) for prot,bind in prot_longest.items()]
        l.sort(reverse=True)
        print()
        print("\n".join(["%s\t%s" %(bind,prot) for length,bind,prot in l]))


**suggerimento 5**

	5) una (o un main) che realizzi il programma richiesto usando le funzioni di cui sopra

semplice ci chiede di mettere tutto insieme::


    def load_data(filename):
        f = open(filename)
        prots = {}
        for row in f:
            name = row[1:].strip()
            seq = f.readline().strip()
            bind = f.readline().strip()
            prots[name] = (seq,bind)
        f.close()
        return prots

    def longest_binding(seq, bind):
        longest = ""
        i = bind.find("+")
        while i != -1:
            j = bind.find("-", i)
            if j == -1:
                j = len(seq)
            if j-i > len(longest):
                longest = seq[i:j]
            i = bind.find("+", j)
        return longest

    def longest_bindings(prots):
        prot_longest = {}
        for prot in prots:
            longest = longest_binding(prots[prot][0],prots[prot][1])
            prot_longest[prot] = longest
        return prot_longest

    def print_longest(prot_longest):

        l = [(len(bind),prot,bind) for prot,bind in prot_longest.items()]
        l.sort(reverse=True)
        print()
        print("\n".join(["%s\t%s" %(bind,prot) for length,bind,prot in l]))


    filename = "rbp_binding"
    prots = load_data(filename)
    print(prots)
    print_longest(longest_bindings(prots))
