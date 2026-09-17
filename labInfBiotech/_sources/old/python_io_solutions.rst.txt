================================
Python: Input-Output (Soluzioni)
================================

Interfaccia Utente
------------------

#. Soluzione::

    risposta = input("qual'e' il tuo piatto preferito? ")

    print("anche a me piace il/la/lo", risposta)

#. Soluzione::

    risposta = input("scrivi due interi: ")
    parole = risposta.split()
    a = int(parole[0])
    b = int(parole[1])

    risposta = input("quanto fa " + str(a) + " " + str(b) " ? ")
    risultato = int(risposta)

    print(a + b == risultato)

#. Soluzione::

    chiave = input("dammi una chiave: ")
    valore = input("dammi un valore: ")

    dizionario = {chiave: valore}
    # oppure
    dizionario = {}
    dizionario[chiave] = valore

    print("dizionario =", dizionario)

#. Soluzione::

    nome = input("dimmi il tuo nome per intero: ")

    parole_aggiustate = [parola[0].upper() + parola[1:].lower()
                         for parola in nome.split()]
    print("il tuo nome e':", " ".join(parole_aggiustate))

Interfaccia Filesystem
----------------------

#. Soluzione::

    f = open("data/aatable", "r")
    # oppure
    f = open("data/aatable")

    righe = f.readlines()
    print(type(righe))                           # list
    print(type(righe[0]))                        # str
    print(len(righe))

    f.close()

#. Soluzione::

    f = open("data/aatable")

    prima_riga = f.readline()
    print("la prima riga e': ", prima_riga)

    righe_restanti = f.readlines()
    print("restavano", len(righe_restanti), "righe")

    righe_restanti_bis = f.readlines()
    print("poi restavano", len(righe_restanti), "righe")

    # Nell'ultimo caso, restavano 0 righe: il primo
    # readlines() aveva gia' letto tutte le righe
    # di f

    f.close()

#. Soluzione::

    f = open("output.txt", "w")
    f.write("prova prova uno due tre prova")
    f.close()

    g = open("output.txt", "r")
    print(g.readlines())
    g.close()

#. Soluzione::

    versi = [
        "S'i fosse fuoco, arderei 'l mondo"
        "s'i fosse vento, lo tempestarei"
    ]

    f = open("poesia.txt", "w")
    f.write("\n".join(versi))
    f.close()

   Ora ci riprovo con ``"a"``::

    f2 = open("poesia2.txt", "a")
    f2.write(versi[0] + "\n")
    f2.close()

    f2 = open("poesia2.txt", "a")
    f2.write(versi[1] + "\n")
    f2.close()

   E se uso ``"w"`` su ``"poesia2.txtx"``::

    f = open("prova2.txt", "w")
    # QUI NON FACCIO ASSOLUTAMENTE NIENTE AD f, LO CHIUDO E BASTA
    f.close()

   mi accorgo che ``"poesia2.txt"`` e' vuoto! Questo succede
   perche' ho usato ``"w"`` al posto di ``"a"``.

#. Scrivo nel file ``trucco.py``::

    me_stesso = open("trucco.py")
    print(me_stesso.read())
    me_stesso.close()

   Eseguo il file per verificare che faccia cio' che voglio: da una shell
   scrivo::

    python3 trucco.py
