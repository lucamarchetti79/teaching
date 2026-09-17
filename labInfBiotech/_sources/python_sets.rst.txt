============
Lezione 7.2 - Python: Sets
============

I set (insiemi) sono una collezione non ordinata di elementi senza ripetizioni. 


Per definire un insieme, posso scrivere::

    sette_nani = {"Brontolo", "Pisolo", "Dotto", ...}

I set possono essere visti come dizionari di *sole chiavi*.
    
La sintassi e'::

    { valore1, valore2, ...}

Posso creare un set vuoto utilizzando la funzione ``set``::

    empty_set = set()
    print(type(empty_set))            # set
    print(len(empty_set))             # 0

    empty_set2 = {}
    print(type(empty_set2))           # dict    
    

La stessa funzione puo' essere utilizzata per creare un set a partire da una lista::

    set_numeri = set([1, 2, 3])
    print(set_numeri)                 # {1, 2, 3}


I set possono essere utilizzati per rimuovere le ripetizioni da una lista::

    lista = [0, 1, 0, 0, 2, 0]
    insieme = set(lista)
    print(insieme)                    # {0, 1, 2}    

****

Operazioni
----------

=========== ======================= ================================================
Ritorna     Operatore               Significato
=========== ======================= ================================================
``int``     ``len(set)``            Restituisce il numero di elementi nel set
``bool``    ``object in set``       Controlla se l'elemento e' presente nel set
``None``    ``set.add(object)``     Inserisce un elemento
``None``    ``set.update(list)``    Inserisce una lista di elementi
``None``    ``set.remove(object)``  Rimuove un elemento (errore se non presente)
``None``    ``set.discard(object)`` Rimuove un elemento
=========== ======================= ================================================

****

**Esempio**. Partendo da un set vuoto::

    numeri_fortunati = set()

    print(numeri_fortunati)              # set()
    print(len(numeri_fortunati))         # 0

inserisco i primi cinque numeri naturali::
  
    primi_cinque = range(5)
    numeri_fortunati.update(primi_cinque)
    print(len(numeri_fortunati))         # 5

inserisco i numeri pari tra 0 e 10 (incluso)::

    pari = [x for x in range(11) if x % 2 == 0]
    numeri_fortunati.update(pari)
    print(len(numeri_fortunati))         # 8

provo a rimuovere ``"0"``::

    numeri_fortunati.discard("0")        # non fa nulla
    numeri_fortunati.remove("0")         # errore

aggiungo la stringa ``"0"`` al set e controllo che sia presente::

    numeri_fortunati.add("0")
    "0" in numeri_fortunati              # True


.. warning::

    Come per i dizionari, *non c'e' alcuna garanzia* che un set preservi l'ordine in cui
    vengono inseriti gli elementi.

.. warning::

    I set sono oggetti **mutabili**, come nel caso delle liste conviene prestare attenzione per evitare situazioni spiacevoli, ad esempio::

      pasto_completo = {'antipasto', 'primo', 'secondo', 'dolce', "caffe'"}

      pasto_ridotto = pasto_completo
      pasto_ridotto.remove('antipasto')
      pasto_ridotto.remove('dolce')

      print(pasto_completo)
      {'primo', 'secondo', "caffe'"}    # Doh!

    Per creare una copia di un set::

      L = {1, 2, 3}
      copia_di_L = set(L)
      copia_di_L.remove(2)
      print(copia_di_L)                 # {1, 3}
      print(L)                          # {1, 2, 3}      
      

Esercizi
----------
#. Creare:

   #. Un set vuoto ``set_vuoto``. Controllare che sia vuoto con ``len()``.

   #. Un set ``primi10`` contenente i primi 10 numeri naturali. Controllare se contiene 10, in caso contrario, inserirlo e ricontrollare che sia presente. Rimuoverlo nuovamente.

   #. Un set ``primi10no7`` contenente i primi 10 numeri naturali, tranne 7 (partendo da ``primi10`` ma lasciandolo inalterato). Controllo che 7 sia presente in ``primi10`` e assente in ``primi10no7``.

   #. Ricreare ``primi10no7``, questa volta utilizzando una list comprehension.



****

Operazioni di unione/intersezione/differenza
----------

=========== ========================= ================================================
Ritorna     Operatore                 Significato
=========== ========================= ================================================
``set``     ``set.union(set)``        Restituisce l'unione di due set
``set``     ``set.intersection(set)`` Restituisce l'intersezione tra due set
``set``     ``set.difference(set)``   Restituisce la differenza tra due set
=========== ========================= ================================================

****

**Esempio**. Creo il set dei primi dieci numeri naturali::

    set_A = set(range(10))

Creo il set dei multipli di 3 compresi tra 0 e 20::

    set_B = set([x for x in range(20) if x % 3 == 0])

Creo l'unione di ``set_A`` e ``set_B``::

    unione = set_A.union(set_B)
    print(unione)                             # {0, 1, 2, 3, .., 8, 9, 12, 15, 18}
  
.. image:: figures/sets_union.png
    :scale: 70 %
    :align: center

Ora creo l'intersezione di ``set_A`` e ``set_B``::

    intersezione = set_A.intersection(set_B)
    print(intersezione)                       # {0, 3, 6, 9}
  
.. image:: figures/sets_intersection.png
    :scale: 70 %
    :align: center

		
**Nota**: le operazioni di unione e intersezione sono simmetriche, per qualsiasi ``set_A`` e ``set_B`` vale::

    set_A.union(set_B) == set_B.union(set_A)                 # True
    set_A.intersection(set_B) == set_B.intersection(set_A)   # True
    
Ottengo i numeri naturali tra 0 e 9 che **NON** sono multipli di 3::

    diff1 = set_A.difference(set_B)
    print(diff1)                              # {1, 2, 4, 5, 7, 8}

.. image:: figures/sets_difference.png
    :scale: 70 %
    :align: center
    
Analogamente, ottengo i multipli di 3 fino al 18 che **NON** sono compresi tra 0 e 9::

    diff2 = set_B.difference(set_A)
    print(diff2)                              # {12, 15, 18}
  
**Nota** al contrario di unione ed intersezione, la differenza non e' simmetrica!

    

Esercizi
--------

#. Per ogni testo, creare l'insieme delle parole che contiene (maiuscole/minuscole non contano)::

        testo_A = "Le due ore di informatica piu' noiose della vostra vita"
        testo_B = "La vita e' come una scatola di cioccolatini"
	testo_C = "Cioccolatini come se piovesse LA La lA laaa"

   #. Contare il numero di parole diverse per ognuno dei tre testi.
      
   #. Ottenere gli insiemi delle parole in comune tra i tre testi: ``condivise_A_B``, ``condivise_A_C``, ``condivise_B_C``.

   #. Dati i set creati precedentemente, ottenere l'insieme delle parole che compaiono in *almeno* due testi, utilizzando soltanto operazioni tra set.

   #. Ottenere l'insieme delle parole che compaiono esattamente in un testo. *Hint* posso farlo utililizzando il risultato precedente?

   #. Ottenere l'insieme delle parole che compaiono ripetute nello stesso testo.
      
