===========================
Lezione 9a - Soluzioni
===========================

For e While
---------------------

#. Soluzioni:

   #. Soluzione::

        for numero in range(10):
            print(numero)

   #. Soluzione::

        for numero in range(10):
            print(numero**2)

   #. Soluzione::

        somma_quadrati = 0
        for numero in range(10):
            somma_quadrati = somma_quadrati + numero**2
        print(somma_quadrati)

   #. Soluzione::

        prodotto = 1 # occhio che qui parto da 1!
        for numero in range(1,10):
            prodotto = prodotto * numero
        print(prodotto)

   #. Soluzione::

        volume_di = {
            "A":  67.0, "C":  86.0, "D":  91.0,
            "E": 109.0, "F": 135.0, "G":  48.0,
            "H": 118.0, "I": 124.0, "K": 135.0,
            "L": 124.0, "M": 124.0, "N":  96.0,
            "P":  90.0, "Q": 114.0, "R": 148.0,
            "S":  73.0, "T":  93.0, "V": 105.0,
            "W": 163.0, "Y": 141.0,
        }

        somma_volumi = 0
        for volume in volume_di.values():
            somma_volumi = somma_volumi + volume
        print(somma_volumi)

   #. Soluzione::

        volume_di = {
            "A":  67.0, "C":  86.0, "D":  91.0,
            "E": 109.0, "F": 135.0, "G":  48.0,
            "H": 118.0, "I": 124.0, "K": 135.0,
            "L": 124.0, "M": 124.0, "N":  96.0,
            "P":  90.0, "Q": 114.0, "R": 148.0,
            "S":  73.0, "T":  93.0, "V": 105.0,
            "W": 163.0, "Y": 141.0,
        }

        fasta = """>1BA4:A|PDBID|CHAIN|SEQUENCE
        DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVV"""

        # estraggo la sequenza
        sequenza = fasta.split("\n")[1]

        somma_volumi = 0

        # per ciascun carattere nella sequenza...
        for aa in sequenza:
            volume_di_aa = volume_di[aa]
            somma_volumi = somma_volumi + volume_di_aa

        print(somma_volumi)

   #. Soluzione: adatto il codice dell'esempio sopra::

        lista = [1, 25, 6, 27, 57, 12]

        minimo_fino_ad_ora = lista[0]
        for numero in lista[1:]:
            if numero < minimo_fino_ad_ora:
                minimo_fino_ad_ora = numero

        print("il minimo e':", minimo_fino_ad_ora)

   #. Soluzione: combino l'esempio e l'esercizio sopra::

        lista = [1, 25, 6, 27, 57, 12]

        massimo = lista[0]
        minimo = lista[0]

        for numero in lista[1:]:
            if numero > massimo:
                massimo = numero
            if numero < minimo:
                minimo = numero

        print("minimo =", minimo, "massimo =", massimo)

   #. Soluzione: ``range(0, len(sequenza), 3)`` restituisce ``[0, 3, 6, 9, ...]``,
      che sono le posizioni di inizio delle varie triplette.

      E' sufficiente scrivere::

        sequenza = "ATGGCGCCCGAACAGGGA"

        # parto da una lista vuota
        triplette = []

        for pos_inizio in range(0, len(sequenza), 3):
            tripletta = sequenza[pos_inizio:pos_inizio+3]
            triplette.append(tripletta)

        print(triplette)

   #. Soluzione::

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

        # prima di tutto rompo il testo in righe
        righe = testo.split("\n")

        # creo il dizionario dove metto il risultato voluto
        sequenza_di = {}

        # ora posso iterare sulle varie righe
        for riga in righe:

            if riga[0] == ">":
                # se la riga e' un'intestazione, estraggo il nome
                # della sequenza
                nome = riga.split("|")[0].lstrip(">")
            else:
                # altrimenti, e' la sequenza vera a propria. il
                # nome l'ho ricavato nell'iterazione precedente
                # (che corrisponde alla riga sopra nel file FASTA)
                # quindi lo posso usare per aggiornare il dizionario
                sequenza_di[nome] = riga

        print(sequenza_di)

#. Soluzioni:

   #. Soluzione::

        while input("scrivi 'STOP': ") != "STOP":
            print("devi scrivere 'STOP'...")

   #. Soluzione::

        while input("scrivi stop: ").lower() != "stop":
            print("devi scrivere stop...")

#. Soluzioni:

   #. Soluzione: tutti i numeri in ``range(10)``.

   #. Soluzione: il numero ``0``. Il ``break`` interrompe immediatamente il ``for``.

   #. Soluzione: tutti i numeri in ``range(10)``. Il ``continue`` salta all'iterazione successiva, cosa che Python fa automaticamente quando finisce il corpo del ciclo ``for``. Visto che ``continue`` in questo caso si trova proprio alla fine del corpo del ciclo ``for``, e come se non ci fosse.

   #. Soluzione: il numero ``0``. Nella primissima iterazione, quando ``numero`` vale ``0``, prima Python esegue ``print(numero)``, che stampa appunto ``0``; poi l'``if`` viene eseguito, e cosi' il ``break`` che contiene, che fa interrompere immediatamente il ``for``.

   #. Soluzione: niente. Nella primissima iterazione, quando ``numero`` vale ``0``, l'``if`` viene eseguito e cosi' il ``break`` che contiene, che fa interrompere immediatamente il ``for``. Il ``print`` non viene mai eseguito.

   #. Soluzione: niente. Il corpo del ``while`` non viene mai eseguito, la condizione e' ``False``!

   #. Soluzione: niente. Visto che il corpo del ``while`` non viene mai eseguito (la condizione e' ``False``!), la riga ``condizione = True`` non viene mai eseguita.

   #. Soluzione: ``"la condizione e' vera"`` un numero indefinito di volte. Visto che la condizione e' sempre ``True``, il ``while`` non finisce mai di iterare!

   #. Soluzione: dieci stringhe della forma ``"all'indice 0 c'e' l'elemento 0"``, ``"all'indice 1 c'e' l'elemento 1"``, *etc.*

   #. Soluzione: tutti gli elementi di ``righe`` (processati da ``strip()``) che vengono prima della prima riga vuota, vale a dire ``"riga 1"``, ``"riga 2"`` e ``"riga 3"``. Appena ``riga`` vale ``""`` (il quarto elemento di ``righe``) l'``if`` viene eseguito, e con esso il ``break``, che interrompe il ciclo. Si noti che la quarta riga *non* viene stampata.

#. Soluzione::

    numeri = (0, 1, 1, 0, 0, 0, 1, 1, 2, 1, 2)

    for i in range(len(numeri)):
        numero_in_pos_i = numeri[i]

        if numero_in_pos_i == 2:
            print("la posizione e'", i)
            break

#. Soluzione::

    stringhe = ("000", "51", "51", "32", "57", "26")

    for i in range(len(stringhe)):
        stringa_in_pos_i = stringhe[i]

        if "2" in stringa_in_pos_i:
            print("posizione =", i, "valore =", stringa_in_pos_i)
            break
