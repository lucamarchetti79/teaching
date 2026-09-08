=============
Lezione 5 - Soluzioni
=============

.. note::

    In alcune soluzioni uso il carattere ``\`` alla fine di una riga di codice.

    Usato in questo modo, ``\`` spiega a Python che il comando continua alla
    riga successiva. Se non usassi ``\``, Python potrebbe pensare che il
    comando finisca li' e quindi che sia sintatticamente sbagliato -- dando
    errore.

    Potete tranquillamente ignorare questi ``\``.

Soluzioni Operazioni
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

Soluzioni Metodi
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
