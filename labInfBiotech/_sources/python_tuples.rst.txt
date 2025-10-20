=============
Lezione 6.2 - Python: Tuple
=============

Le tuple sono liste **immutabili**.

Per definire una tupla uso le parentesi tonde::

    partners = ("BIOGRID:112315", "BIOGRID:108607")

.. warning::

    Se voglio creare una tupla con un solo elemento (puo' capitare...)
    devo ricordarmi di usare la virgola, oltre alle parentesi tonde::

        tupla = (0,)
        print(tupla)
        print(type(tupla))
        print(len(tupla))
    
        non_tupla = (0)
        print(non_tupla)
        print(type(non_tupla))

    Come si vede, ``non_tupla`` e' un intero, ``0``.

****


Operazioni
----------

========= =================== ====================================================
Ritorna   Operatore           Significato
========= =================== ====================================================
``int``   ``len(tuple)``      Restituisce la lunghezza della tuple
``tuple`` ``tuple + tuple``   Concatena le due tuple
``tuple`` ``tuple * int``     Replica la tupla
``bool``  ``object in tuple`` Contolla se un oggetto arbitrario appare nella tupla
``tuple`` ``tuple[int:int]``  Estrae una sotto-tupla
========= =================== ====================================================

Le tuple supportanto tutti gli operatori delle stringhe e delle liste,
tranne l'assegnamento.

****

**Esempio**. Creo una tupla con elementi misti::

    proteina = ("2B0Q", "phosphotransferase", "PF03881")

che contiene informazioni su una proteina. Posso accedere ai vari elementi come
farei con una lista::

    id_proteina = proteina[0]
    print(id_proteina)

    nome_proteina = proteina[1]
    print(nome_proteina)

Pero' non posso modificare la tupla::

    >>> proteina[0] = "1A3A"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

****

**Esempio**. Proprio come le liste e gli intervalli, posso usare le
tuple come *input* ad una list comprehension::

    tripla = (1, 2, 3)

    risultato = [2*numero for numero in tripla]
    print(risultato)
    print(type(risultato))

Il risultato di una **list** *comprehension* e' comunque una lista.

****

Metodi
------

======== ======================= =================================================
Ritorna  Metodo                  Significato
======== ======================= =================================================
``int``  ``tuple.index(object)`` Restituisce la posizione di object.
``int``  ``tuple.count(object)`` Conta il numero di ripetizioni di un valore
======== ======================= =================================================

Conversione Lista-Tupla
-----------------------

Per convertire tra liste e tuple uso ``tuple()`` e ``list()``::

    lista = list(range(10))

    tupla = tuple(lista)
    print(tupla, type(tupla))

    lista_2 = list(tupla)
    print(lista_2, type(lista_2))

Ne segue che se *proprio* voglio "modificare" una tupla posso scrivere::

    tupla = ("sono", "una", "tupla")
    print(tupla)

    copia = list(tupla)
    copia.insert(2, "bella")
    tupla = tuple(copia)
    print(tupla)

In realta' quello che ottengo e' una *nuova* tupla che contiene gli elementi
della vecchia tupla in aggiunta a ...

Esercizi
--------

#. Creare:

   #. Una tupla di due interi di valore ``0`` e ``1``.
   #. Una tupla di due stringhe, ``"una"`` e ``"tupla"``.
   #. Una tupla di un solo elemento, ``0``.

      *Hint*: ci sono due modi di farlo: usare la sintassi vista all'inzio
      del capitolo, oppure usare la conversione lista-tupla.

   #. Una tupla di cento elementi: i numeri interi da ``0`` a ``99``.

      *Hint*: posso usare (indirettamente) ``range()``?

   #. Una tupla con due elementi: la *lista* degli interi da ``0`` a ``49`` e
      la *lista* degli interi da ``50`` a ``99``.
   #. Una tupla con due elementi: la *tupla* degli interi da ``0`` a ``49`` e
      la *tupla* degli interi da ``50`` a ``99``.

#. Date ``l = [0, 1, 2]`` e ``t = (0, 1, 2)``, che differenza c'e' tra:

   #. Primo caso::

        x = l
        x[0] = 100
   #. Secondo caso::

        x = t
        x[0] = 100

#. Data la tupla::

    tupla = (0, 1, 2, [3, 4, 5], 6, 7, 8)

   #. Di che tipo e' il primo elemento della tupla? Quanto vale?
   #. Di che tipo e' il quarto elemento della tupla? Quanto vale?
   #. Quanti elementi contiene la tupla?
   #. Quanti elementi contiene la lista contenuta nella tupla?
   #. Cambiare l'ultimo elemento della lista contenuta in ``tupla`` in ``"ultimo"``.
   #. Cambiare l'ultimo elemento di ``tupla`` in ``"ultimo"``. (Si puo' fare?)

