=============
Lezione 6.2 - Soluzioni
=============

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




Soluzioni
---------


#. Soluzioni::

    coppia_di_interi = (0, 1)
    print(type(coppia_di_interi))            # tuple


    coppia_di_stringhe = ("una", "tupla")
    print(type(coppia_di_stringhe))          # tuple


    un_solo_elemento = (0,)
    print(type(un_solo_elemento))            # tuple
    print(len(un_solo_elemento))             # 1

    un_solo_elemento_alt = tuple([0])
    print(type(un_solo_elemento_alt))        # tuple
    print(len(un_solo_elemento_alt))         # 1

    sbagliato = (0)
    print(type(sbagliato))                   # int
    print(len(sbagliato))                    # errore!


    cento_elementi = tuple(range(100))
    print(type(cento_elementi))              # tuple


    coppia_di_liste = (list(range(50)), list(range(50, 100)))
    print(type(coppia_di_liste))
    print(type(coppia_di_liste[0]))


    coppia_di_tuple = (tuple(range(50)), tuple(range(50, 100)))
    print(type(coppia_di_tuple))
    print(type(coppia_di_tuple[0]))

#. Soluzioni::

    l = [0, 1, 2]
    t = (0, 1, 2)

    # x si riferisce ad una lista, il codice sostituisce
    # il primo elemento con 100
    x = l
    x[0] = 100

    # x ora si riferisce ad una tupla, che e' immutabile:
    # non posso sostituire i suoi elementi, Python da'
    # errore
    x = t
    x[0] = 100                          # errore!

#. Soluzioni::

    tupla = (0, 1, 2, [3, 4, 5], 6, 7, 8)

    print(tupla[0])                      # 0
    print(type(tupla[0]))                # int

    print(tupla[3])                      # [3, 4, 5]
    print(type(tupla[3]))                # list

    print(len(tupla))                    # 7

    print(len(tupla[3]))                 # 3

    tupla[3][-1] = "ultimo"
    print(tupla)
    # ebbene lo posso fare! ho "modificato" la
    # tupla modificando la lista contenuta
    # in essa.

    tupla[-1] = "ultimo"                # errore!
    # non posso modificare la tupla "direttamente"
    # e' un oggetto immutabile
