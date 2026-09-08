=========================
Python: Liste (Soluzioni)
=========================

.. note::

    In alcune soluzioni uso il carattere ``\`` alla fine di una riga di codice.

    Usato in questo modo, ``\`` spiega a Python che il comando continua alla
    riga successiva. Se non usassi ``\``, Python potrebbe pensare che il
    comando finisca li' e quindi che sia sintatticamente sbagliato -- dando
    errore.

    Potete tranquillamente ignorare questi ``\``.

Operazioni
----------

#. Soluzione::

    lista = []
    print(lista, len(lista))         # controllo

#. Soluzione::

    lista = list(range(5))
    print(lista, len(lista))         # controllo
    print(len(lista))

#. Soluzione::

    lista = [0] * 100
    print(lista, len(lista))         # controllo

#. Soluzione::

    lista_1 = list(range(10))
    lista_2 = list(range(10, 20))

    lista_completa = lista_1 + lista_2
    print(lista_completa)

    print(lista_completa) == list(range(20))   # Ture

#. Soluzione::

    lista = ["sono", "una", "lista"]
    print(lista, len(lista))         # controllo

    print(len(lista[0]))
    print(len(lista[1]))
    print(len(lista[2]))

#. Soluzione::

    lista = [0.0, "b", [3], [4, 5]]

    print(len(lista))                # 4

    print(type(lista[0]))            # float

    print(lista[1], len(lista[1]))   # "b", 1

    print(lista[2], len(lista[2]))   # [3], 1

    print(lista[-1], len(lista[-1])) # [4, 5], 2

    print("b" in lista)              # True

    print(4 in lista)                # False
    print(4 in lista[-1])            # True

#. Soluzione: la prima e' una lista di interi, la seconda una lista
   di stringhe, mentre la terza e' una *stringa*!::

    print(type(lista_1))             # list
    print(type(lista_2))             # list
    print(type(lista_3))            # str

#. Soluzioni::

    # una lista vuota
    lista = []
    print(len(lista))                # 0
    del lista


    # sintassi non valida, Python da' errore
    lista = [}


    # una lista che contiene una lista vuota
    lista = [[]]
    print(len(lista))                # 1
    print(len(lista[0]))             # 0
    del lista


    # non funziona perche' lista non e' definita!
    lista.append(0)


    # questa invece funziona
    lista = []
    lista.append(0)
    print(lista)                     # [0]
    del lista


    # non funziona perche' mancano le virgole!
    lista = [1 2 3]


    # da' errore perche' la lista ha solo 3 elementi!
    lista = list(range(3))
    print(lista[3])


    # estrae l'ultimo elemento
    lista = list(range(3))
    print(lista[-1])
    del lista


    # estrae i primi due elementi (lista[2], il terzo,
    # e' escluso)
    lista = list(range(3))
    sottolista = lista[0:2]
    print(lista)
    del lista


    # estrare tutti gli elementi (lista[3], che 'non
    # esiste', e' escluso)
    lista = list(range(3))
    sottolista = lista[0:3]
    print(lista)
    del lista


    # estrae i primi due elementi (lista[-1], il terzo,
    # e' escluso)
    lista = list(range(3))
    sottolista = lista[0:-1]
    print(lista)
    del lista


    # inserisce in terza posizione la stringa "due"
    lista = list(range(3))
    lista[2] = "due"
    print(lista)
    del lista


    # non funziona: la lista contiene solo tre elementi,
    # quindi non ha una quarta posizione, e Python da'
    # errore
    lista = list(range(3))
    lista[3] = "tre"


    # inserisce in terza posizione la stringa "tre"
    lista = list(range(3))
    lista[-1] = "tre"
    print(lista)
    del lista


    # l'indice deve essere un intero, Python da' errore
    lista = list(range(3))
    lista[1.2] = "uno virgola due"


    # sostituisce il secondo elemento di lista (cioe' 1)
    # con una lista di due stringhe; e' perfettamente
    # legale: le liste *possono* contenere altre stringhe
    lista = list(range(3))
    lista[1] = ["testo-1", "testo-2"]
    print(lista)
    del lista

#. Soluzione::

    matrice = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    prima_riga = matrice[0]
    print(prima_riga)

    secondo_elemento_prima_riga = prima_riga[1]
    # oppure
    secondo_elemento_prima_riga = matrice[0][1]
    print(secondo_elemento_prima_riga)

    somma_prima_riga = matrice[0][0] + matrice[0][1] + matrice[0][2]
    print(somma_prima_riga)

    seconda_colonna = [matrice[0][1], matrice[1][1], matrice[2][1]]
    print(seconda_colonna)

    diagonale = [matrice[0][0], matrice[1][1], matrice[2][2]]
    print(diagonale)

    tre_righe_assieme = matrice[0] + matrice[1] + matrice[2]
    print(tre_righe_assieme)

Metodi
------

#. Prima dichiaro una lista qualunque, ad esempio quella vuota::

    lista = []

   poi aggiungo i vari elementi richiesti con ``append()``::

    lista.append(0)
    lista.append("testo")
    lista.append([0, 1, 2, 3])

#. Soluzione::

    # aggiunge un 3 alla fine della lista
    lista = list(range(3))
    lista.append(3)
    print(lista)
    del lista

    # aggiunge una lista con un 3 dentro alla fine della lista
    lista = list(range(3))
    lista.append([3])
    print(lista)
    del lista

    # aggiunge un 3 (il solo elemento contenuto nella lista [3]) alla
    # fine della lista
    lista = list(range(3))
    lista.extend([3])
    print(lista)
    del lista

    # non funziona: extend() estende una lista con i contenuti
    # di un'altra lista, ma qui 3 *non* e' una lista! Python da'
    # errore
    lista = list(range(3))
    lista.extend(3)

    # sostituisce l'elemento in posizione 0, il primo, con il
    # valore 3
    lista = list(range(3))
    lista.insert(0, 3)
    print(lista)
    del lista

    # inserisce un 3 alla fine di lista
    lista = list(range(3))
    lista.insert(3, 3)
    print(lista)
    del lista

    # inserisce la lista [3] alla fine di lista
    lista = list(range(3))
    lista.insert(3, [3])
    print(lista)
    del lista

    # non funziona: il primo argomento di insert() deve essere
    # un intero, qui gli stiamo dando una lista! Python da' errore
    lista = list(range(3))
    lista.insert([3], 3)

#. Soluzione::

    lista = []
    lista.append(range(10))
    lista.append(range(10, 20))
    print(lista)

   Qui uso ``append()``, che inserisce un *elemento* alla fine di ``lista``.
   In questo caso inserisco due liste, cioe' i risultati di ``range(10)`` e
   ``range(10, 20)``.

   E' chiaro che ``len(lista)`` e' ``2``, visto che ho inserito solo due elementi.

   Invece::

    lista = []
    lista.extend(range(10))
    lista.extend(range(10, 20))
    print(lista)

   fa uso di ``extend()``, che "estende" una lista con un'altra lista. Qui
   la lista finale ha ``20`` elementi, come si evince con::

    print(len(lista))

#. Soluzione::

    lista = [0, 0, 0, 0]
    lista.remove(0)
    print(lista)

   solo la prima ripetizione di ``0`` viene rimossa!

#. Soluzione::

    lista = [1, 2, 3, 4, 5]

    # inverte l'ordine degli elementi di lista
    lista.reverse()
    print(lista)

    # ordina gli elementi di lista
    lista.sort()
    print(lista)

   Il risultato e' che dopo le due operazioni ``lista`` torna al suo
   valore iniziale.

   Invece questo::

    lista = [1, 2, 3, 4, 5]
    lista.reverse().sort()

   *non* si puo' fare. Il risultato di ``lista.reverse()`` e' ``None``::

    lista = [1, 2, 3, 4, 5]
    risultato = lista.reverse()
    print(risultato)

   che certamente non e' una lista, e quindi non ci posso fare sopra ``sort()``.
   Python dara' errore.

#. Sono tentato di scrivere::

    lista = list(range(10))
    lista_inversa = lista.reverse()

    print(lista)                         # modificata!
    print(lista_inversa)                 # None!

   ma questa cosa non funziona: ``reverse()`` modifica ``lista`` e restituisce
   ``None``! Perdipiu' questo codice modifica ``lista`` direttamente, ed io
   non voglio.

   Quindi prima faccio una copia di ``lista``, e poi ordino quella::

    lista = list(range(10))
    lista_inversa = lista[:]            # *non* lista_inversa = lista
    lista_inversa.reverse()
    print(lista)                         # invariata
    print(lista_inversa)                 # invertita

   Invece questo codice::

    lista = list(range(10))
    lista_inversa = lista
    lista_inversa.reverse()
    print(lista)                         # modificata!
    print(lista_inversa)                 # invertita

   non funziona come vorrei: quello che succede e' che ``lista_inversa``
   contiene non una copia di ``lista``, ma un riferimento allo stesso
   oggetto riferito da ``lista``.

   Quindi quando inverto ``lista_inversa`` finisco per invertire anche ``lista``.

#. Come sopra::

    frammenti = [
        "KSYK",
        "SVALVV"
        "GVTGI",
        "VGSSLAEVLKLPD",
    ]
    frammenti_ordinati = frammenti.sort()

   non funziona: ``sort()`` ordina ``lista`` e restituisce ``None``! Quindi
   sono costretto a fare prima una copia di ``frammenti``, e poi ad ordinare
   quella::

    frammenti_ordinati = frammenti[:]
    frammenti_ordinati.sort()
    print(frammenti)                     # invariata
    print(frammenti_ordinati)            # ordinata

#. Soluzione::

    lista = []
    lista.append(lista)

    print(lista)

   crea una lista che contiene se' stessa; ``lista`` e' una struttura che
   in gergo viene detta *ricorsiva*.

   ``lista`` e' chiaramente *infinita* (in termini di annidamento), visto che
   posso farci cose come queste::

    print(lista)
    print(lista[0])
    print(lista[0][0])
    print(lista[0][0][0])
    print(lista[0][0][0][0])
    # ...

   Visto che ``lista`` ha profondita' infinita, Python quando la stampa
   usa un'ellissi ``...`` per indicare che c'e' una quantita' infinita di liste
   dentro a ``lista`` (ed ovviamente non puo' stamparle tutte).

   **Non** vedremo altre strutture ricorsive nel corso.

Metodi Stringhe-Liste
---------------------

#. Soluzione::

    testo = """The Wellcome Trust Sanger Institute
    is a world leader in genome research.""""

    parole = testo.split()
    print(len(parole))


    righe = testo.split("\n")

    prima_riga = righe[0]
    print("la prima riga e':", prima_riga)

    seconda_riga = righe[1]
    print("la seconda riga e':", seconda_riga)


    print("la prima parola della seconda riga e':", seconda_riga.split()[0])

#. Soluzione::

    tabella = [
        "protein | database | domain | start | end",
        "YNL275W | Pfam | PF00955 | 236 | 498",
        "YHR065C | SMART | SM00490 | 335 | 416",
        "YKL053C-A | Pfam | PF05254 | 5 | 72",
        "YOR349W | PANTHER | 353 | 414",
    ]

    prima_riga = tabella[0]
    titoli_colonne_quasi = prima_riga.split("|")
    print(titoli_colonne_quasi)
    # ["protein ", " database ", ...]

    # purtroppo qui i titoli delle colonne contengono spazi superflui
    # per evitarli posso cambiare il delimitatore che do a split()

    titoli_colonne = prima_riga.split(" | ")
    print(titoli_colonne)
    # ["protein", "database", ...]

   Volendo si puo' usare anche ``strip()`` assieme ad una *list comprehension*
   su ``titoli_colonne_quasi``, ma (come appena dimostrato) non e' necessario.

#. Soluzione::

    parole = ["parola_1", "parola_2", "parola_3"]

    print(" ".join(parole))

    print(",".join(parole))

    print(" e ".join(parole))

    print("".join(parole))

    backslash = "\\"
    print(backslash.join(parole))

#. Soluzione::

    versi = [
        "Taci. Su le soglie"
        "del bosco non odo"
        "parole che dici"
        "umane; ma odo"
        "parole piu' nuove"
        "che parlano gocciole e foglie"
        "lontane."
    ]

    poesia = "\n".join(versi)

List Comprehension
------------------

#. Soluzioni:

   #. Soluzione::

        lista_piu_tre = [numero + 3 for numero in lista]

        print(lista_piu_tre)             # controllo

   #. Soluzione::

        lista_dispari = [numero for numero in lista
                         if (numero % 2 == 1)]

   #. Soluzione::

        lista_opposti = [-numero for numero in lista]

   #. Soluzione::

        lista_inversi = [1.0 / numero for numero in lista
                         if numero != 0]

   #. Soluzione::

        primo_e_ultimo = [lista[0], lista[-1]]

   #. Soluzione::

        dal_secondo_al_penultimo = lista[1:-1]

   #. Soluzione::

        lista_dispari = [numero for numero in lista
                         if (numero % 2 == 1)]
        quanti_dispari = len(lista_dispari)
        print(quanti_dispari)

      oppure abbreviando::

        quanti_dispari = len([numero for numero in lista
                              if (numero % 2 == 1)])

   #. Soluzione::

        lista_divisi_per_5 = [float(numero) / 5
                              for numero in lista]

   #. Soluzione::

        lista_multipli_5_divisi = [float(numero) / 5.0)
                                   for numero in lista
                                   if (numero % 5 == 0)]

   #. Soluzione::

        lista_di_stringhe = [str(numero) for numero in lista]

   #. Soluzione::

        # Come sopra, ma iterando su `lista_di_stringhe`
        # piuttosto che direttamente su `lista`
        quanti_dispari = len([stringa for stringa in lista_di_stringhe
                              if (int(stringa) % 5 == 0)])

   #. Soluzione::

        testo = " ".join([str(numero) for numero in lista])

      Occhio che se dimentico di fare ``str(numero)``, ``join()`` si
      rifiuta di funzionare.

#. Soluzioni:

   #. ::

        # andata
        lista_1 = [1, 2, 3]
        lista_2 = [str(x) for x in lista_1]

        # ritorno
        lista_2 = ["1", "2", "3"]
        lista_1 = [int(x) for x in lista_2]

   #. ::

        # andata
        lista_1 = ["nome", "cognome", "eta'"]
        lista_2 = [[x] for x in lista_1]

        # ritorno
        lista_2 = [["nome"], ["cognome"], ["eta'"]]
        lista_1 = [l[0] for l in lista_2]

   #. ::

        # andata
        lista_1 = ["ACTC", "TTTGGG", "CT"]
        lista_2 = [[x.lower(), len(x)] for x in lista_1]

        # ritorno
        lista_2 = [["actc", 4], ["tttgggcc", 6], ["ct", 2]]
        lista_1 = [l[0].upper() for l in lista_2]

#. Soluzione:

   #. ``[x for x in lista]``: crea una copia di ``lista``.
   #. ``[y for y in lista]``: crea una copia di ``lista`` (identico a sopra).
   #. ``[y for x in lista]``: invalida. (Se ``x`` rappresenta l'elemento della lista, cos'e' ``y``?)
   #. ``["x" for x in lista]``: crea una lista piena di stringhe ``"x"`` lunga quanto ``lista``. Il risultato sara': ``["x", "x", ..., "x"]``.
   #. ``[str(x) for x in lista]``: per ogni intero ``x`` in ``lista``, lo converte in stringa con ``str(x)`` e mette il risultato nella lista che sta creando. Il risultato sara': ``["0", "1", ..., "9"]``.
   #. ``[x for str(x) in lista]``: invalida: la trasformazione ``str(...)`` e' nel posto sbagliato!
   #. ``[x + 1 for x in lista]``: per ogni intero ``x`` in ``lista``, aggiunge uno con ``x + 1`` e mette il risultato nella lista che sta creando. Il risultato sara': ``[1, 2, ..., 10]``.
   #. ``[x + 1 for x in lista if x == 2]``: per ogni intero ``x`` in ``lista`` controlla se vale ``2``. Se lo e' mette ``x + 1`` nella lista che sta creando, altrimento lo scarta. Il risultato sara': ``[3]``.

#. Soluzione::

    dna = open("data/dna-fasta/fasta.1").readlines()
    print(" ".join(dna))


    # Rimuovo l'intestazione: due alternative
    dna_no_intestazione = [riga for riga in dna
                           if not riga[0].startswith(">")]
    dna_no_intestazione = [riga for riga in dna
                           if riga[0] != ">"]


    # Si', ci sono caratteri di a capo o spazi
    print(["\n" in riga for riga in dna_no_intestazione])
    print([" " in riga for riga in dna_no_intestazione])

    # Rimuovo i caratteri a capo da tutte le righe
    dna_solo_seq = [riga.strip() for riga in dna_no_intestazione]

    # Ricontrollo per sicurezza: non ci sono caratteri
    # di a capo ne' spazi
    print(["\n" in riga for riga in dna_solo_seq])
    print([" " in riga for riga in dna_solo_seq])


    # Concateno tutte le righe di dna_solo_seq
    sequenza = "".join(dna_solo_seq)


    # Calcolo il numero di "C" e "G"
    num_c = sequenza.count("C")
    num_g = sequenza.count("G")


    # Calcolo il GC-content, facendo attenzione da usare
    # dei float per evitare errori di approssimazione
    gc_content = float(num_c + num_g) / len(sequenza)

#. Soluzione::

    risultato_cdhit = """\
    >Cluster 0
    0 >YLR106C at 100.00%
    >Cluster 50
    0 >YPL082C at 100.00%
    >Cluster 54
    0 >YHL009W-A at 90.80%
    1 >YHL009W-B at 100.00%
    2 >YJL113W at 98.77%
    3 >YJL114W at 97.35%
    >Cluster 52
    0 >YBR208C at 100.00%
    """

    righe = risultato_cdhit.split("\n")

   Per ottenere i nomi dei cluster, devo tenere solo le righe che cominciano
   per ``">"``, e per ciascuna di queste fare lo ``split()`` in modo da poter
   ottenere il secondo elemento (che e' il nome del cluster)::

    nomi_cluster = [riga.split()[1] for riga in righe
                    if riga.startswith(">")]

   Per ottenere i nomi delle proteine, devo tenere solo le righe che *non*
   cominciano per ``">"``, e per ciascuna di queste fare lo ``split()`` e
   tenere il secondo elemento (avendo cura di rimuovere il ``">"`` dal nome
   della proteina)::

    proteine = [riga.split()[1].lstrip(">") for riga in righe
                if not riga.startswith(">")]

   Per ottenere le coppie proteina-percentuale, come nel caso precedente,
   tengo solo le righe che *non* cominciano per ``">"``. Su ciascuna di
   queste faccio ``split()`` e tengo il nome della proteina (secondo elemento)
   e la percentuale (ultimo elemento)::

    coppie_proteina_percentuale = \
        [[riga.split()[1].lstrip(">"), riga.split()[-1].rstrip("%")]
         for riga in righe if not riga.startswith(">")]

   Versione annotata::

    coppie_proteina_percentuale = \
        [[riga.split()[1].lstrip(">"), riga.split()[-1].rstrip("%")]
    #     ^^^^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #       nome proteina, come sopra            percentuale
    #    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #                     coppia proteina-percentuale
         for riga in righe if not riga.startswith(">")]

#. Soluzione::

    righe = open("data/prot-pdb/1A3A.pdb").readlines()


    # ~~~~ prima parte ~~~~

    # Estraggo tutte le righe SEQRES
    righe_seqres = [riga for riga in righe
                    if riga.startswith("SEQRES")]
    print(len(righe_seqres))                     # 48

    # Estraggo i nomi delle catene
    catene = [riga.split()[2] for riga in righe_seqres]
    print(catene)

    # Estraggo da righe_seqres quelle relative alla catena B
    righe_seqres_b = [riga for riga in righe_seqres
                      if riga.split()[2] == "B"]
    print(len(righe_seqres_b))                   # 12

    # Estraggo le sequenze da ciascuna riga di righe_seqres_b,
    # poi concateno per ottenere il risultato voluto.
    sequenze_parziali_B = [" ".join(riga.split()[4:])
                           for riga in righe_seqres_b]
    sequenza_B = "".join(sequenze_parziali_B)


    # ~~~~ seconda parte ~~~~

    # Estraggo tutte le righe HELIX
    righe_helix = [riga for riga in righe
                   if riga.startswith("HELIX")]
    print(len(righe_helix))                      # 30

    # Estraggo dalle righe le posizioni di ciascuna elica
    eliche_inizio_fine = [[int(riga.split()[5]), int(riga.split()[8])]
    #                      ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^
    #                           inizio elica         fine elica
                          for riga in righe_helix]

    # In un secondo passaggio (per comodita') calcolo
    # il risultato voluto
    info_eliche = [coppia + [coppia[1] - coppia[0] + 1]
    #              ^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #           [inizio, fine]       lunghezza
                   for coppia in eliche_inizio_fine]

#. Soluzione::

    matrice = [list(range(0,3)), list(range(3,6)), list(range(6,9))]


    # estraggo la prima riga
    prima_riga = matrice[0]


    # estraggo la prima colonna
    prima_colonna = [matrice[0][i] for i in range(3)]


    # inverto l'ordine delle righe
    sottosopra = matrice[:]
    sottosopra.reverse()
    # oppure
    sottosopra = [matrice[2-i] for i in range(3)]


    # inverto l'ordine delle colonne
    palindromo = []
    # appendo la prima riga di matrice invertita
    palindromo.append([matrice[0][2-i] for i in range(3)])
    # appendo la seconda riga di matrice invertita
    palindromo.append([matrice[1][2-i] for i in range(3)])
    # appendo la terza riga di matrice invertita
    palindromo.append([matrice[2][2-i] for i in range(3)])

    # oppure in un solo passaggio -- ma e' complicato e potete ignorarlo!!!
    palindromo = [[riga[2-i] for i in range(3)]
                   for riga in matrice]


    # ricreo matrice con una sola list comprehension
    matrice_di_nuovo = [list(range(i, i+3)) for i in range(9)
                        if i % 3 == 0]

#. Soluzioni::

    lista = list(range(100))

    lista_quadrati = [numero**2 for numero in numeri]

    lista_differenze_quadrati = \
        [lista_quadrati[i+1] - lista_quadrati[i]
         for i in range(len(lista_quadrati) - 1)]
