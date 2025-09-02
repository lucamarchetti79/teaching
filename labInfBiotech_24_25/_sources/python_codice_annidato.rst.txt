===========================
Lezione 9b - Python: Codice annidato
===========================

Posso combinare un numero arbitrario di statement complessi (``if``, ``for`` e
``while``) usando l'indentazione, inclusi cicli innestati.

****

**Esempio**. Voglio simulare un orologio che ha due lancette: ore e minuti::

    for ora in range(24):
        for minuto in range(60):
            print("ora =", ora, "minuro =", minuto)

Qui all'esterno itero sulle ore, mentre all'interno itero sui minuti: ogni
volta che il ``for`` interno finisce le sue sessanta iterazioni, il ``for``
esterno ne completa una.

Posso "estendere" l'orologio per comprendere anche i giorni dell'anno: si
tratta solo di aggiungere un ``for`` sui giorni che contenga il ``for`` delle
ore, cosi'::

    for giorno in range(1, 365+1):
        for ora in range(24):
            for minuto in range(60):
                print(giorno, ora, minuto)

(ignorando gli anni bisestili).

Naturalmente posso "estendere" l'orologio agli anni aggiungendo un altro
``for`` ancora piu' esterno, *etc.*

****

**Esempio**. Voglio sapere se in una lista ci sono elementi ripetuti, e
se ci sono in che posizioni si trovano. Partiamo dalla lista::

    numeri = [5, 9, 4, 4, 9, 2]

L'idea e' di usare due cicli ``for`` innestati per iterare sulle *coppie*
di elementi di ``numeri``.

In pratica, per ciascun elemento (diciamo in posizione ``i``) voglio
controllare se almeno uno di quelli che stanno alla sua destra (diciamo in
posizione ``j``) e' uguale a lui. Immagine::

    +---+---+---+---+---+---+
    | 5 | 9 | 4 | 4 | 9 | 2 |
    +---+---+---+---+---+---+
      ^
      i
        \__________________/
          i possibili valori di j


    +---+---+---+---+---+---+
    | 5 | 9 | 4 | 4 | 9 | 2 |
    +---+---+---+---+---+---+
          ^           ^
          i           doppione!
            \______________/
          i possibili valori di j


    +---+---+---+---+---+---+
    | 5 | 9 | 4 | 4 | 9 | 2 |
    +---+---+---+---+---+---+
              ^   ^
              i   doppione!
                \__________/
          i possibili valori di j

Scrivo::

    posizioni_ripetizioni = []

    for i in range(len(numeri)):
        numero_in_pos_i = numeri[i]

        # ho il numero in posizione i; ora lo voglio
        # confrontare con quelli che lo seguono
        for j in range(i + 1, len(numeri)):
            numero_in_pos_j = numeri[j]

            # ora confronto i due numeri
            if numero_in_pos_i == numero_in_pos_j:

                # sono uguali: aggiungo le loro
                # posizioni alla lista
                posizioni_ripetizioni.append((i, j))

    print(posizioni_ripetizioni)

Okay, ho ottenuto le posizioni dei ripetizioni. Verifico stampando, per ciascuna
coppia di posizioni in ``posizioni_ripetizioni`` i valori corrispondenti::

    for i, j in posizioni_ripetizioni:
        numero_in_pos_i = numeri[i]
        numero_in_pos_j = numeri[j]
        print(numero_in_pos_i, numero_in_pos_j)

****

**Esempio**. Apro un file FASTA e ne leggo i contenuti in una lista di
stringhe::

    righe = open("data/prot-fasta/3J01.fasta").readlines()

Il valore di ``righe`` e'::

    righe = [
        ">3J01:0|PDBID|CHAIN|SEQUENCE",
        "AVQQNKPTRSKRGMRRSHDALTAVTSLSVDKTSGEKHLRHHITADGYYRGRKVIAK",
        ">3J01:1|PDBID|CHAIN|SEQUENCE",
        "AKGIREKIKLVSSAGTGHFYTTTKNKRTKPEKLELKKFDPVVRQHVIYKEAKIK",
        ">3J01:2|PDBID|CHAIN|SEQUENCE",
        "MKRTFQPSVLKRNRSHGFRARMATKNGRQVLARRRAKGRARLTVSK",
        ">3J01:3|PDBID|CHAIN|SEQUENCE",
        # ...
    ]

Voglio convertire ``righe`` in un dizionario dove le chiavi sono le
intestazioni, e i valori corrispondenti sono le sequenze.

Scrivo::

    # parto da un dizionario vuoto
    dizionario = {}

    # per ogni riga...
    for riga in righe:

        if riga[0] == ">":
            # e' una riga di intestazione: la memorizzo
            # nella variabile 'intestazione'
            intestazione = riga

        else:
            # non e' una riga di intestazione: la
            # memorizzo nella variabile 'sequenza'
            sequenza = riga

            # a questo punto ho sia l'intestazione (che
            # ho memorizzato nella riga precedente) sia
            # la sequenza (che ho memorizzato in questa
            # riga): aggiorno il dizionario
            dizionario[intestazione] = sequenza

    # una volta scorse tutte le righe, ho finito
    # di creare il mio dizionario. lo stampo
    print(dizionario)

Funziona, ma c'e' un problema.

Se guardiamo bene, in ``righe`` ci sono casi in cui la sequenza di una catena
proteica occupa piu' righe. Ad esempio::

    righe = [
        # ...
        ">3J01:5|PDBID|CHAIN|SEQUENCE",
        "MAKLTKRMRVIREKVDATKQYDINEAIALLKELATAKFVESVDVAVNLGIDARKSDQNVRGATVLPHGTGRSVRVAVFTQ",
        "GANAEAAKAAGAELVGMEDLADQIKKGEMNFDVVIASPDAMRVVGQLGQVLGPRGLMPNPKVGTVTPNVAEAVKNAKAGQ",
        "VRYRNDKNGIIHTTIGKVDFDADKLKENLEALLVALKKAKPTQAKGVYIKKVSISTTMGAGVAVDQAGLSASVN",
        # ...
    ]

In questo caso il nostro codice non funziona: quando facciamo
``dizionario[intestazione] = sequenza`` mettiamo nel dizionario *solo l'ultima
riga* della sequenza corrente, *dimenticandoci* di tutte quelle che la
precedono!

Per sistemare il codice, devo fare in modo che si ricordi di *tutte* le righe
della sequenza che corrisponde all'intestazione corrente. Scrivo::

    sequenza_di = {}

    for riga in righe:

        if riga[0] == ">":
            intestazione = riga

        else:
            sequenza = riga

            # qui, al posto di mettere nel dizionario la sequenza,
            # metto una lista di TUTTE le righe che compongono
            # la sequenza

            if not intestazione in sequenza_di:
                sequenza_di[intestazione] = []

            sequenza_di[intestazione].append(sequenza)

L'``if not ...`` serve per accertarsi che la lista di righe associata ad
``intestazione`` esista, altrimenti non posso farci ``append()``.

Una alternativa e' questa::

    for riga in righe:

        if riga[0] == ">":
            intestazione = riga
            sequenza_di[intestazione] = []

        else:
            sequenza = riga
            sequenza_di[intestazione].append(sequenza)

In questa versione garantisco che ``sequenza_di[intestazione]`` sia una
lista ogni volta che leggo una nuova intestazione.

Assumiamo che un burlone abbia formattato in modo sbagliato il file
FASTA: ha messo prima le sequenze, e poi le intestazioni corrispondenti.
Esempio::

    fasta_sottosopra = [
        # prima sequenza e prima intestazione
        "AVQQNKPTRSKRGMRRSHDALTAVTSLSVDKTSGEKHLRHHITADGYYRGRKVIAK",
        ">3J01:0|PDBID|CHAIN|SEQUENCE",

        # seconda sequenza e seconda intestazione
        "AKGIREKIKLVSSAGTGHFYTTTKNKRTKPEKLELKKFDPVVRQHVIYKEAKIK",
        ">3J01:1|PDBID|CHAIN|SEQUENCE",
    ]

Il nostro codice non funziona piu': nel codice assumiamo che quando leggiamo
una riga della sequenza, l'intestazione corrispondente sia gia' nota. Pero'
in questo FASTA sottosopra e' vero il contrario!

Riscriviamo il codice in modo da assumere, invece, che e' quando otteniamo
l'*intestazione* che gia' conosciamo la *sequenza*!

Scrivo::

    dizionario = {}
    ultima_sequenza = []

    for riga in righe:

        if riga[0] == ">":
            # e' una riga di intestazione, ho gia' memorizzato
            # la sequenza in 'ultima_sequenza'. aggiorno il
            # dizionario
            intestazione = riga
            dizionario[intestazione] = ultima_sequenza

            # ora che ho messo il valore di 'ultima_sequenza',
            # la faccio ricominciare dalla lista vuota
            ultima_sequenza = []

        else:
            # e' una riga di sequenza, ma ancora non conosco
            # l'intestazione (nel file, viene dopo!). non
            # tocco il dizionario, mi limito a memorizzare
            # la sequenza nella lista 'ultima_sequenza'
            sequenza = riga
            ultima_sequenza.append(sequenza)

    print(dizionario)

****

Esercizi
--------

#. Data la matrice::

    n = 5
    matrice = [list(range(n)) for i in range(n)]

   scrivere un doppio ciclo ``for`` che stampi a schermo tutti gli elementi
   di ``matrice``, uno per riga.

#. Data la matrice::

    n = 5
    matrice = [list(range(n)) for i in range(n)]

   cosa stampano i seguenti frammenti di codice?

   #. ::

        for riga in matrice:
            for elemento in riga:
                print(elemento)

   #. ::

        somma = 0
        for riga in matrice:
            for elemento in riga:
                somma = somma + elemento
        print(somma)

   #. ::

        for i in range(len(matrice)):
            riga = matrice[i]
            for j in range(len(riga)):
                elemento = riga[j]
                print(elemento)

   #. ::

        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                print(matrice[i][j])

   #. ::

        non_lo_so = []
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if i == j:
                    non_lo_so.append(matrice[i][j])
        print(" ".join([str(x) for x in non_lo_so]))

#. Data la lista::

    numeri = [8, 3, 2, 9, 7, 1, 8]

   scrivere un doppio ciclo ``for`` che stampa a schermo tutte le *coppie*
   di elementi di ``numeri``.

#. Modificare la soluzione dell'esercizio sopra in modo che se la coppia ``(i,j)``
   e' gia' stata stampata, allora la coppia simmetrica ``(j,i)`` non venga
   stampata.

   *Hint*. Vedi l'esempio sopra.

#. Fare la stessa cosa con la lista::

    stringhe = ["io", "sono", "una", "lista"]

#. Dato l'intervallo::

    numeri = range(10)

   scrivere un doppio ciclo ``for`` che stampa a schermo solo le coppie di
   elementi di ``numeri`` dove il secondo elemento della coppia e' il doppio
   del primo.

   Il risultato dovra' essere::

    0 0
    1 2
    2 4
    ...

#. Data la lista::

    numeri = [8, 3, 2, 9, 7, 1, 8]

   scrivere un doppio ciclo ``for`` che itera su tutte le coppie degli elementi
   di ``numeri`` e stampa a schermo le coppie di elementi la cui somma e'
   ``10``.

   (E' lecito stampare eventuali "ripetizioni", ad esempio ``8 + 2`` e ``2 + 8``.)

   Il risultato dovra' essere::

    8 2
    3 7
    2 8
    9 1
    ...

   *Hint*. C'e' un esempio che mostra come iterare sulle coppie di elementi
   di una lista. E' sufficiente adattarlo.

#. Come sopra, ma al posto di stampare a schermo, memorizzare le coppie degli
   elementi la cui somma e' ``10`` in una lista ``lista_delle_coppie``.

   Il risultato dovra' essere::

    >>> lista_delle_coppie
    [(8, 2), (3, 7), (2, 8), (9, 1), ...]

#. Date le liste::

    numeri_1 = [5, 9, 4, 4, 9, 2]
    numeri_2 = [7, 9, 6, 2]

   scrivere un doppio ciclo ``for`` che itera sulle due liste e stampa
   a schermo *valori* e *posizioni* degli elementi di ``numeri_1`` che appaiono
   anche in ``numeri_2``.

   Il risultato dovra' essere::

    posizioni: 1, 1; valore ripetuto: 9
    posizioni: 4, 1; valore ripetuto: 9
    posizioni: 5, 3; valore ripetuto: 2

#. Come sopra, ma al posto di stampare a schermo, memorizzare le posizioni
   ed il valore ripetuto una lista di triple della forma ``(posizione_1, posizione_2, valore_ripetuto)``.

#. Data la matrice::

    n = 5
    matrice = [list(range(n)) for i in range(n)]

   scrivere un doppio ciclo ``for`` che trovi l'elemento piu' grande.

   *Hint*. E' sufficiente adattare il codice per trovare il massimo-minimo
   di una lista (che e' ad una dimensione) alla matrice (che ha due dimensioni).

#. Data la lista di sequenze nucleotidiche::

    sequenze = [
        "ATGGCGCCCGAACAGGGA",
        "GTCCCTGTTCGGGCGCCA",
    ]

   voglio ottenere una lista che contenga, per ogni sequenza in ``sequenze``,
   la lista delle sue triplette.

   *Hint*. Si puo' riutilizzare un esercizio precedente.

#. Data la lista::

    numeri = [5, 9, 4, 4, 9, 2]

   scrivere del codice che conta il numero di ripetizioni di ogni elemento, e
   metta il risultato in un dizionario. Il dizionario dovra' somigliare a
   questo::

    num_ripetizioni = {
        5: 1,
        9: 2,
        4: 2,
        2: 1,
    }

   *Hint*. Si puo' modificare uno degli esempi sopra in modo che, invece
   di salvare la posizione delle ripetizioni, incrementi il numero di ripetizioni
   in ``num_ripetizioni``.

   *Hint*. Occhio che se la chiave ``5`` nel dizionario non c'e', non posso
   fare ``num_ripetizioni[5] += 1``, perche' ``num_ripetizioni[5]`` non
   esiste! Vedi l'esempio sulla lettura del file FASTA.

#. Data una lista di cluster di geni (liste), ad esempio::

    gruppi = [["gene1", "gene2"], ["gene3"], [], ["gene4", "gene5"]]

   scrivere un *singolo* ciclo che trova il gruppo piu' grande e lo memorizza in
   una variabile ``gruppo_piu_grande_fino_ad_ora``.

   *Hint*: e' simile a trovare il minimo/massimo di una lista di interi, ma la
   variabile ausiliaria deve contenere la *lista* piu' lunga trovata fin'ora.

#. Data la lista di sequenze::

    sequenze_2HMI = {
        "A": "PISPIETVPVKLKPGMDGPKVKQWPLTEEKI",
        "B": "PISPIETVPVKLKPGMDGPKVKQWPLTEEKI",
        "C": "DIQMTQTTSSLSASLGDRVTISCSASQDISS",
        "D": "QITLKESGPGIVQPSQPFRLTCTFSGFSLST",
        "E": "ATGGCGCCCGAACAGGGAC",
        "F": "GTCCCTGTTCGGGCGCCA",
    }

   scrivere un ciclo for che (iterando sulle coppie chiave-valore del dizionario)
   restituisca un dizionario degli istogrammi (dizionari aminoacido->numero di
   ripetizioni) di ciascun elemento di ``sequenze_2HMI``.

   *Hint*. Calcolare un istogramma richiede esso stesso un ciclo ``for``: quindi
   in totale ci si puo' aspettare che ci siano due cicli ``for`` innestati.

   Il risultato (un dizionario di dizionari) dovra' somigliare a questo::

        istogrammi = {
            "A": {
                "P": 6,
                "I": 3,
                "S": 1,
                #...
            },
            "B": {
                "P": 6,
                "I": 3,
                "S": 1,
                #...
            },

            #...

            "F": {
                "A": 1,
                "C": 7,
                "G": 6,
                "T": 4,
            }
        }

#. Data la lista di stringhe::

    tabella = [
        "protein domain start end",
        "YNL275W PF00955 236 498",
        "YHR065C SM00490 335 416",
        "YKL053C-A PF05254 5 72",
        "YOR349W PANTHER 353 414",
    ]

   scrivere del codice che prenda i nomi delle colonne dalla prima riga
   di ``tabella`` e:

   - per ciascuna riga compili un dizionario di questo tipo::

        dizionario = {
            "protein": "YNL275W",
            "domain": "PF00955",
            "start": "236",
            "end":, "498"
        }

   - appenda il dizionario ad una lista.

#. Date::

        alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
        alfabeto_mai = alfabeto_min.upper()

   scrivere un ciclo (``for`` o ``while``) che, partendo da un dizionario
   vuoto, inserisca tutte le coppie chiave-valore::

        "a": "A",
        "b": "B",
        ...

   cioe' che mappi dal carattere *i*-esimo di ``alfabeto_min`` al carattere
   *i*-esimo di ``alfabeto_mai``.

   Poi usare il dizionario cosi' costruito per implementare un ciclo ``for``
   che, data una stringa arbitraria, ad esempio::

        stringa = "sono una stringa"

   abbia lo stesso effetto di ``stringa.upper()``.

#. Scrivere un modulo che chiede all'utente il percorso a *due* file di
   testo, e stampa a schermo le righe dei due file, una per una, appaiate:
   le righe del primo file vanno stampate sulla sinistra, le righe del
   secondo sulla destra.

   Se il primo file contiene::

        prima riga
        seconda riga

   ed il secondo::

        ACTG
        GCTA

   il risultato deve essere::

        prima riga ACTG
        seconda riga GCTA

   *Hint*. Attenzione che i due file potrebbero avere lunghezze diverse.
   In questo caso (opzionalmente) le righe "mancanti" vanno stampate
   come se fossero righe vuote.

#. Scrivere un modulo che, dato il file ``data/dna-fasta/fasta.1``:

   #. Legga i contenuti del file FASTA in un dizionario.

   #. Calcoli quante volte ogni nucleotide appare in ciascuna sequenza.

   #. Calcoli il GC-content della sequenza.

   #. Calcoli la AT/GC-ratio della sequenza.

