=========================
Python: Tuple (Soluzioni)
=========================

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


    coppia_di_liste = (range(50), range(50, 100))
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

    print(len(tupla))                    # 9

    print(len(tupla[3]))                 # 3

    tupla[3][-1] = "ultimo"
    print(tupla)
    # ebbene lo posso fare! ho "modificato" la
    # tupla modificando la lista contenuta
    # in essa.

    tupla[-1] = "ultimo"                # errore!
    # non posso modificare la tupla "direttamente"
    # e' un oggetto immutabile
