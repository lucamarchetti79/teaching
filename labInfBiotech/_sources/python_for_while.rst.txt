===========================
Lezione 9a - Python: Codici iterativi (cicli)
===========================

Codice iterativo: ``for``
-------------------------

``for`` permette di scrivere codice che viene ripetuto (una ed una sola volta)
per ciascun elemento di una *collezione* (stringa, lista, tupla, dizionario).

La sintassi di ``for`` e'::

    collezione_di_oggetti = range(10) # ad esempio (i numeri da 0 a 10 escluso)

    for elemento in collezione_di_oggetti:
        codice_che_fa_qualcosa_con_elemento(elemento)

Questo ciclo ``for`` esegue ``codice_che_fa_qualcosa_con_elemento()`` per
ciascun elemento in ``collezione_di_oggetti``, in ordine dal primo all'ultimo.

``elemento`` e' una variabile Python che prende il valore di ciascun elemento
di ``collezione_di_oggetti``, dal primo all'ultimo: viene "creata" sul momento
quando scriviamo il ciclo ``for``.

Proprio come con le *list comprehension*, il nome che le diamo e' arbitrario.

.. warning::

    Se ``collezione_di_oggetti`` e' un dizionario, ``for`` itera sulle *chiavi*.

    Occhio che l'*ordine* delle chiavi in un dizionario non e' ovvio. Si
    veda sopra la sezione sui dizionari.

.. warning::

    Spesso si utilizza il ciclo ``for`` accoppiato con l'istruzione ``range`` gia' vista
    in precedenza. Ricordiamoci che l'istruzione ``range`` puo' prendere fino a tre
    parametri::
        range(start,end,step)
        range(20) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        range(5,20) = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        range(5,20,2) = [5, 7, 9, 11, 13, 15, 17, 19]

****

**Esempio**. Questo ciclo ``for``::

    lista = [1, 25, 6, 27, 57, 12]

    for numero in lista:
        print(numero)

itera su tutti gli elementi del risultato di ``lista``: prima l'elemento ``1``,
poi l'elemento ``25``, *etc.*, fino a ``12``, e li stampa nell'ordine in
cui appaiono nella lista.

Ad ogni iterazione il valore dell'elemento corrente viene *automaticamente*
messo nella variabile ``numero``, mentre il ``print`` ne stampa il valore.

Posso ottenere lo stesso comportamento anche senza il ciclo ``for``, cosi'::

    numero = lista[0]   # prima iterazione
    print(numero)

    numero = lista[1]   # seconda iterazione
    print(numero)

    numero = lista[2]   # terza iterazione
    print(numero)

    # ...

    numero = lista[5]   # ultima iterazione
    print(numero)

Il ``for`` permette di compattare questo codice in due sole righe.

****

**Esempio**. Piuttosto che stampare gli elementi della lista, voglio stampare
la loro *somma*.

Modifico il ``for`` dell'esempio sopra::

    lista = [1, 25, 6, 27, 57, 12]

    somma = 0
    for numero in lista:
        somma = somma + numero

    print("la somma e'", somma)

Ho creato una variabile di supporto ``somma`` che inizializzo a ``0``.

Poi scorro su tutti i numeri contenuti in ``lista``, e man mano li aggiungo a
``somma``.

Una volta terminato il ciclo ``for``, ``somma`` varra' (per costruzione)::

    lista[0] + lista[1] + ... + lista[-1]

che e' esattamente la somma degli elementi.

****

**Esempio**. Piuttosto che calcolare la somma degli elementi della lista,
voglio trovare il massimo.

L'idea e' questa:

* Itero la lista con un ``for``.

* Creo una nuova variabile ``massimo_fino_ad_ora`` in cui memorizzo
  l'elemento piu' grande che ho trovato fino ad ora. Il valore viene
  aggiornato ad ogni iterazione del ciclo ``for``.

* Per ogni elemento della lista (cioe' in ogni iterazione del ``for``) controllo
  se l'elemento che ho sotto mano e' piu' grande di ``massimo_fino_ad_ora``:

  * Se non lo e', non faccio niente.

  * Se lo e', aggiorno ``massimo_fino_ad_ora``.

* Quando il ``for`` avra' finito di scorrere sugli elementi della lista,
  ``massimo_fino_ad_ora`` conterra' (*suspance*!) il massimo elemento trovato
  fino ad ora.

**PROVATE VOI**

****

**Esempio**. Data la seguente tabella (che potrebbe essere il risultato
di ``readlines()`` su un file)::

    tabella = [
        "protein domain start end",
        "YNL275W PF00955 236 498",
        "YHR065C SM00490 335 416",
        "YKL053C-A PF05254 5 72",
        "YOR349W PANTHER 353 414",
    ]

voglio convertirla in un dizionario fatto cosi'::

    dati = {
        "YNL275W": ("PF00955", 236, 498),
        "YHR065C": ("SM00490", 335, 416),
        "YKL053C-A": ("PF05254", 5, 72),
        "YOR349W": ("PANTHER", 353, 414)
    }

che contiene per ogni dominio (riga) di ``tabella``, esclusa l'intestazione,
come chiave la proteina corrispondente (prima colonna) e come valore le
informazioni associate (altre colonne: nome, inizio e fine del dominio).

**PROVATE VOI**

****

**Esempio**. ``break`` permette di *interrompere* il ciclo ``for``. Ad
esempio::

    percorso = input("scrivi un percorso a file: ")
    righe = open(percorso).readlines()

    for riga in righe:
        riga = riga.strip()
        print("ho letto:", riga)

        if len(riga) == 0:
            # se la riga e' vuota, esco dal ciclo
            break

    # <--- il break ci porta immediatamente QUI

legge le righe dal file indicato dall'utente, e le stampa una per una. Pero'
appena incontra una riga vuota (vedi l'``if``), esce dal ciclo.

**Esempio**. ``continue`` permette di passare all'iterazione successiva del
``for``. Ad esempio::

    percorso = input("scrivi un percorso a file: ")
    righe = open(percorso).readlines()

    for riga in righe:
        # <--- il continue ci riporta QUI, ma all'iterazione
        #      (e quindi all'elemento di righe) successivo

        riga = riga.strip()
        print("ho letto:", riga)

        if riga[0] == ">":
            print("intestazione")
            continue

        print("sequenza")

legge le righe del file indicato dall'utente, che supponiamo essere un
file fasta. Stampa ogni riga che incontra. Poi, se la riga e' un'intestazione,
stampa ``"intestazione"`` ed il ``continue`` *fa saltare a Python tutto cio'
che c'e' tra il continue stesso e la fine dell'iterazione corrente del ciclo for*.

In altre parole, salta all'iterazione successiva. Python riprende noncurante
l'esecuzione all'elemento successivo di ``righe``, e riprende ad eseguire il
``for``.

Codice iterativo: ``while``
---------------------------

``while`` permette di scrivere codice che viene ripetuto finche' una
condizione e' vera.

La sintassi e'::

    while condizione:
        condizione = codice_che_fa_qualcosa_e_aggiorna_condizione()

Il codice all'interno del ``while`` viene ripetuto un numero *indefinito*
di volte: dipende da quanto ci mette ``condizione`` a diventare ``False``.

****

**Esempio**. Scrivo un ciclo ``while`` che chiede all'utente se vuole
fermarsi, e continua a chiedere finche' l'utente non risponde ``"si"``::

    while input("vuoi che mi fermi? ") != "si":
        print("se non rispondi 'si' non mi fermo!")

****

**Esempio**. Esattamente come con il ``for``, posso usare ``continue`` e
``break`` per alterare il flusso del ciclo. Ad esempio::

    while True:
        risposta = input("qual'e la capitale d'Italia? ")

        if risposta.lower() == "roma":
            print("giusto!")
            break

        print("riprova!")

    # <--- il break ci porta QUI
    print("finito")

questo codice continua a girare finche' l'utente non risponde ``"roma"`` (con
maiuscole o minuscole, poco importa).

Riscrivo il ciclo per fare in modo che chieda all'utente se continuare o meno::

    while True:
        risposta = input("qual'e' la capitale d'Italia? ")
        if risposta.lower() == "roma":
            print("giusto!")
            break                   # esce dal while
	else:
	    print("doh!")

        risposta = input("vuoi riprovare? ")
        if risposta.lower() == "no":
            print("va bene")
            break                   # esce dal while

****

Esercizi
--------

#. Scrivere un ciclo ``for`` che:

   #. Stampi a schermo gli elementi di ``range(10)``, uno per riga.

   #. Stampi a schermo il quadrato degli elementi di ``range(10)``, uno per riga.

   #. Stampi a schermo la somma dei *quadrati* di ``range(10)``.

   #. Stampi a schermo il *prodotto* degli elementi di ``range(1,10)``.

   #. Dato il dizionario::

        volume_di = {
            "A":  67.0, "C":  86.0, "D":  91.0,
            "E": 109.0, "F": 135.0, "G":  48.0,
            "H": 118.0, "I": 124.0, "K": 135.0,
            "L": 124.0, "M": 124.0, "N":  96.0,
            "P":  90.0, "Q": 114.0, "R": 148.0,
            "S":  73.0, "T":  93.0, "V": 105.0,
            "W": 163.0, "Y": 141.0,
        }

      che codifica il volume di ciascun aminoacido, stampi a schermo la
      somma dei valori.

   #. Dato il dizionario::

        volume_di = {
            "A":  67.0, "C":  86.0, "D":  91.0,
            "E": 109.0, "F": 135.0, "G":  48.0,
            "H": 118.0, "I": 124.0, "K": 135.0,
            "L": 124.0, "M": 124.0, "N":  96.0,
            "P":  90.0, "Q": 114.0, "R": 148.0,
            "S":  73.0, "T":  93.0, "V": 105.0,
            "W": 163.0, "Y": 141.0,
        }

      che codifica il volume di ciascun aminoacido, e la stringa FASTA::

        fasta = """>1BA4:A|PDBID|CHAIN|SEQUENCE
        DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVV"""

      stampi a schermo il volume totale della proteina (leggi: la somma
      dei volumi di tutti i suoi residui).

      *Hint*. Prima conviene estrarre la sequenza vera e propria da ``fasta``,
      poi, per ciascun carattere nella sequenza (``for carattere in sequenza``)
      prendere dal dizionario il volume corrispondente e sommarlo al totale.

   #. Trovi il valore *minimo* della lista ``[1, 25, 6, 27, 57, 12]``.

      *Hint*. Si veda l'esempio sopra in cui troviamo il *massimo* della
      lista. E' sufficiente adattare la logica che decide quando aggiornare
      la variabile ausiliaria (e magari rinominarla da ``massimo_fino_ad_ora``
      a ``minimo_fino_ad_ora``).

   #. Trovi sia il *massimo* che il *minimo* della lista ``[1, 25, 6, 27, 57, 12]``.

      *Hint*. E' necessario usare *due* variabili ausiliarie: ``massimo_fino_ad_ora``
      e ``minimo_fino_ad_ora``.

   #. Data la sequenza nucleotidica::

        sequenza = "ATGGCGCCCGAACAGGGA"

      restituisca la lista di tutte le sue sotto-sequenze di tre nucleotidi.
      La soluzione deve essere::

        ["ATG", "GCG", "CCC", "GAA", "CAG", "GGA"]

      *Hint*: conviene iterare sul risultato di ``range(0, len(sequenza), 3)``
      ed aggiungere man mano ogni tripletta ad una lista vuota preventivamente
      creata.

   #. Dato il testo (in formato FASTA)::

        testo = """>2HMI:A|PDBID|CHAIN|SEQUENCE
        PISPIETVPVKLKPGMDGPKVKQWPLTEEKIKALVEICTEMEKEGKISKI
        >2HMI:B|PDBID|CHAIN|SEQUENCE
        PISPIETVPVKLKPGMDGPKVKQWPLTEEKIKALVEICTEMEKEGKISKI
        >2HMI:C|PDBID|CHAIN|SEQUENCE
        DIQMTQTTSSLSASLGDRVTISCSASQDISSYLNWYQQKPEGTVKLLIYY
        >2HMI:D|PDBID|CHAIN|SEQUENCE
        QITLKESGPGIVQPSQPFRLTCTFSGFSLSTSGIGVTWIRQPSGKGLEWL
        >2HMI:E|PDBID|CHAIN|SEQUENCE
        ATGGCGCCCGAACAGGGAC
        >2HMI:F|PDBID|CHAIN|SEQUENCE
        GTCCCTGTTCGGGCGCCA"""

      restituisca un dizionario ``sequenza_di`` che abbia come chiavi i
      nomi delle sequenze cosi' come sono scritti nelle intestazioni
      (il primo sara' ``2HMI:A``, il secondo ``2HMI:B``, *etc.*), e come
      valore la sequenza corrispondente.

      Il risultato dovra' somigliare a questo::

        sequenza_di = {
            "2HMI:A": "PISPIETVPVKLKPGMDGPKVKQW...",
            "2HMI:B": "PISPIETVPVKLKPGMDGPKVKQW...",
            # ...
        }

      *Hint*. Conviene prima spezzare ``testo`` nelle sue righe. Poi si puo'
      iterare sulle righe cosi' ottenute: se una riga e' di intestazione,
      mi salvo il nome della sequenza corrispondente; se la riga invece e'
      una sequenza, aggiorno il dizionario con il nome ottenuto alla riga
      sopra e la sequenza ottenuta dalla riga corrente.

#. Scrivere un ciclo ``while`` che:

   #. Continui a chiedere all'utente di scrivere ``"STOP"``. Se l'utente scrive
      ``"STOP"`` (in maiuscolo) termina, senno' scrive all'utente ``"devi scriviere 'STOP'..."``
      e continua.

   #. Come sopra, ma deve terminare anche se l'utente risponde ``"stop"`` in
      minuscolo.

#. Che cosa stampa a schermo questo codice?

   #. ::

        for numero in range(10):
            print("processo l'elemento", numero)

   #. ::

        for numero in range(10):
            print("processo l'elemento", numero)
            break

   #. ::

        for numero in range(10):
            print("processo l'elemento", numero)
            continue

   #. ::

        for numero in range(10):
            print(numero)
            if numero % 2 == 0:
                break

   #. ::

        for numero in range(10):
            if numero % 2 == 0:
                break
            print(numero)

   #. ::

        condizione = False
        while condizione:
            print("la condizione e' vera")

   #. ::

        condizione = False
        while condizione:
            print("la condizione e' vera")
            condizione = True

   #. ::

        condizione = True
        while condizione:
            print("la condizione e' vera")

   #. ::

        numeri = range(10)

        i = 0
        while i < len(numeri):
            print("all'indice", i, "c'e' l'elemento", numeri[i])
	    i += 1

   #. ::

        righe = [
            "riga 1",
            "riga 2",
            "riga 3",
            "",
            "riga 5",
            "riga 6",
        ]

        for riga in righe:
            riga = riga.strip()
            if len(riga) == 0:
                break
            else:
                print("ho letto:", riga)

#. Data la tupla::

    numeri = (0, 1, 1, 0, 0, 0, 1, 1, 2, 1, 2)

   scrivere un ciclo che itera su ``numeri``, si ferma appena incontra il
   valore ``2`` e ne stampa a schermo la *posizione*.

#. Data la tupla::

    stringhe = ("000", "51", "51", "32", "57", "26")

   scrivere un ciclo che itera su ``stringhe``, si ferma appena incontra
   una stringa che contiene un carattere ``"2"``, e stampa a schermo
   *posizione* e *valore* della stringa sulla quale si e' fermato.

   La soluzione e': posizione ``3``, valore ``"32"``.
