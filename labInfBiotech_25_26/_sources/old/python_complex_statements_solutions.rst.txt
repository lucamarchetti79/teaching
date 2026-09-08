=======================================
Python: Statement Complessi (Soluzioni)
=======================================

Codice condizionale: ``if``
---------------------------

#. Soluzione::

    numero = int(input("scrivi un numero: "))

    if numero % 2 == 0:
        print("pari")
    else:
        print("dispari")

   Uso ``else`` perche' pari e dispari sono le uniche due possibilita'.

   Volendo, posso esplicitare la terza possibilita', cioe' il caso in cui
   ``numero`` non e' ne' pari ne' dispari, cosi'::

    if numero % 2 == 0:
        print("pari")
    elif numero % 2 == 1:
        print("dispari")
    else:
        print("impossibile!")

   ma il codice nell'``else`` non verra' eseguito per nessun valore di ``numero``!

   Visto che le due possibilita' (``numero`` e' pari, ``numero`` e' dispari)
   sono mutualmente esclusive, posso anche permettermi di scrivere::

    if numero % 2 == 0:
        print("pari")
    if numero % 2 == 1:
        print("dispari")

   perche' anche in assenza dell'``else``, uno e solo uno dei due
   ``if`` puo' essere eseguito.

#. Soluzione::

    numero = float(input("scrivi un razionale: "))

    if numero >= -1 and numero <= 1:
        print("okay")

   Non servono ne'``elif`` (c'e' una sola condizione) ne' ``else`` (se la
   condizione e' falsa, non devo fare niente).

#. Soluzione::

    risposta = input("scrivi due numeri separati da spazio: ")

    parole = risposta.split()
    numero1 = int(parole[0])
    numero2 = int(parole[1])

    if numero1 > numero2:
        print("primo")
    elif numero2 > numero1:
        print("secondo")
    else:
        print("nessuno dei due")

   In alternativa::

    risposta = input("scrivi due numeri separati da spazio: ")

    numeri = [int(parola) for parola in risposta.split()]

    if numeri[0] > numeri[1]:
        print("primo")
    elif numeri[0] < numeri[1]:
        print("secondo")
    else:
        print("nessuno dei due")

#. Soluzione::

    oroscopo_di = {
        "gennaio": "fortuna estrema",
        "febbraio": "fortuna galattica",
        "marzo": "fortuna incredibile",
        "aprile": "ultra-fortuna",
    }

    mese = input("dimmi il tuo mese di nascita: ")

    if mese in oroscopo_di:
        print(oroscopo_di[mese])
    else:
        print("non disponibile")

#. Soluzione::

    percorso = input("scrivi il percorso: ")

    righe = open(percorso, "r").readlines()
    if len(righe) == 0:
        print("vuoto")
    elif len(righe) < 100:
        print("piccolo", len(righe))
    elif len(righe) < 1000:
        print("medio", len(righe))
    else:
        print("grande", len(righe))

   Si noti che non e' necessario specificare per intero le condizioni: nel
   codice abbrevio ``100 < len(righe) < 1000`` con ``len(righe) < 1000``. Me
   lo posso permettere perche' quando ``len(righe)`` e' minore di ``100``
   eseguo il primo ``elif``: il secondo ``elif`` non viene neanche considerato.

#. Soluzione::

    punto1 = [float(parola) for parola
              in input("scrivi tre coordinate: ").split()]

    punto2 = [float(parola) for parola
              in input("scrivi tre coordinate: ").split()]

    if punto1[0] >= 0 and punto1[1] >= 0 and punto1[2] >= 0 and \
       punto2[0] >= 0 and punto2[1] >= 0 and punto2[2] >= 0:
        diff_x = punto1[0] - punto2[0]
        diff_y = punto1[1] - punto2[1]
        diff_z = punto1[2] - punto2[2]

        print("la distanza e'", (diff_x**2 + diff_y**2 +  diff_z**2)**0.5)

   Si noti che il ``print`` e' *dentro* l'``if``.

#. Soluzione: sappiamo che ``numero`` e' un intero arbitrario (puo' essere
   qualunque intero deciso dall'utente). Il codice che ci interessa e' questo::

    if numero % 3 == 0:
        print("divide 3!")
    elif numero % 3 != 0:
        print("non divide 3!")
    else:
        print("boh")

   L'``if``, l'``elif`` e l'``else`` formano una catena: solo uno tra loro
   viene eseguito.

   #. L'``if`` viene eseguito se e solo se ``numero`` e' divisibile per tre.

   #. L'``elif`` viene eseguito se e solo se l'``if`` precedente non viene
      eseguito e se ``numero`` *non* e' divisibile per tre.

   #. L'``else`` viene eseguito quando ne' l'``if`` ne' l'``elif`` vengono
      eseguito.

   Visto che non ci sono numeri che non siano ne' divisibili ne' non-divisibili
   per ``3``, non resta alcuna altra possibilita'. O viene eseguito l'``if``,
   o viene eseguito l'``elif``: l'``else`` non viene *mai* eseguito.

   Quindi la risposta e' no.

#. Soluzione: come sopra, ``numero`` e' un intero arbitrario. Il codice e'::

    numero = int(input("scrivi un numero: "))
    if numero % 2 == 0:
        print("divide 2!")
    if numero % 3 == 0:
        print("divide 3!")
    if numero % 2 != 0 and numero % 3 != 0:
        print("boh")

   Qui non ci sono "catene" di ``if``, ``elif`` ed ``else``: ci sono tre ``if``
   indipendenti.

   #. Il primo ``if`` viene eseguito se e solo se ``numero`` e' divisibile per
      due.

   #. Il secondo ``if`` viene eseguito se e solo se ``numero`` e' divisibile
      per tre.

   #. Il terzo ``if`` viene eseguito se e solo se ``numero`` *non* e' divisibile
      ne' per due, ne' per tre.

   Se ``numero`` e' es. 6, che e' divisibile sia per due che per tre, allora i
   primi due ``if`` vengono entrambi eseguiti, mentre il terzo non viene
   eseguito.

   Se ``numero`` e' es. 5, che non e' divisibile ne' per due ne' per tre, allora
   i primi due ``if`` *non* vengono eseguiti; in compenso viene eseguito il
   terzo.

   Quindi la risposta e' si'.

   (Altri esempi: per ``numero = 2`` viene eseguito solo il primo ``if``, per
   ``numero = 3`` solo il secondo. Si noti pero' che non c'e' verso di *non*
   eseguire nessuno uno dei tre ``if``.)

#. Soluzione::

    risposta = input("somma o prodotto?: ")

    if risposta == "somma":
        numero1 = int(input("numero 1: "))
        numero2 = int(input("numero 2: "))
        print("la somma e'", numero1 + numero2)

    elif risposta == "prodotto":
        numero1 = int(input("numero 1: "))
        numero2 = int(input("numero 2: "))
        print("il prodotto e'", numero1 * numero2)

   Usare un ``if`` o un ``elif`` non altera l'esecuzione del programma.

   Posso semplificare cosi'::

    risposta = input("somma o prodotto?: ")
    numero1 = int(input("numero 1: "))
    numero2 = int(input("numero 2: "))

    if risposta == "somma":
        print("la somma e'", numero1 + numero2)

    elif risposta == "prodotto":
        print("il prodotto e'", numero1 * numero2)

Codice iterativo
----------------

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
                nome = riga.split("|")[0]
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

Codice annidato
---------------

#. Soluzione::

    n = 5
    matrice = [list(range(n)) for i in range(n)]

    for riga in matrice:
        for elemento in riga:
            print(elemento)

#. Soluzione:

   #. Tutti gli elementi della matrice.
   #. La *somma* di tutti gli elementi della matrice.
   #. Di nuovo tutti gli elementi della matrice.
   #. Di nuovo tutti gli elementi della matrice.
   #. La lista degli elementi sulla diagonale.

#. Uso due cicli ``for`` per iterare sulle coppie di elementi::

    numeri = [8, 3, 2, 9, 7, 1, 8]

    for numero_1 in numeri:
        for numero_2 in numeri:
            print(numero_1, numero_2)

   E' molto simile all'esempio dell'orologio!

#. Scrivo::

    numeri = [8, 3, 2, 9, 7, 1, 8]

    coppie_gia_stampate = []

    for i in range(len(numeri)):
        for j in range(len(numeri)):

            coppia = (numeri[i], numeri[j])

            # controllo se ho gia' stampato la coppia simmetrica
            if (coppia[1], coppia[0]) in coppie_gia_stampate:
                continue

            # se arrivo qui vuol dire che non ho gia' stampato la coppia
            # simmetrica (altrimenti avrei fatto `continue`), quindi stampo
            # la coppia; poi aggiorno coppie_gia_stampate
            print(coppia)

            coppie_gia_stampate.append(coppia)

#. Come sopra.

#. Soluzione::

    numeri = range(10)

    for elemento_1 in numeri:
        for elemento_2 in numeri:
            if 2 * elemento_1 == elemento_2:
                print(elemento_1, elemento_2)

#. Soluzione::

    numeri = [8, 3, 2, 9, 7, 1, 8]

    for elemento_1 in numeri:
        for elemento_2 in numeri:
            if elemento_1 + elemento_2 == 10:
                print(elemento_1, elemento_2)

#. Soluzione::

    numeri = [8, 3, 2, 9, 7, 1, 8]

    # parto da una lista vuota
    lista_delle_coppie = []

    for elemento_1 in numeri:
        for elemento_2 in numeri:
            if elemento_1 + elemento_2 == 10:
                # aggiorno la lista con append()
                lista_delle_coppie.append((elemento_1, elemento_2))

    # stampo la lista che ho appena costruito
    print(lista_delle_coppie)

#. Soluzione::

    numeri_1 = [5, 9, 4, 4, 9, 2]
    numeri_2 = [7, 9, 6, 2]

    # qui itero sulla *prima* lista
    for i in range(len(numeri_1)):
        numero_in_pos_i = numeri_1[i]

        # qui itero sulla *seconda* lista
        for j in range(len(numeri_2)):
            numero_in_pos_j = numeri_2[j]

            if numero_in_pos_i == numero_in_pos_j:
                print("posizioni:", i, j, "; valore ripetuto:", numero_in_pos_i)

#. Soluzione::

    numeri_1 = [5, 9, 4, 4, 9, 2]
    numeri_2 = [7, 9, 6, 2]

    # parto da una lista vuota
    lista_delle_triplette = []

    # qui itero sulla *prima* lista
    for i in range(len(numeri_1)):
        numero_in_pos_i = numeri_1[i]

        # qui itero sulla *seconda* lista
        for j in range(len(numeri_2)):
            numero_in_pos_j = numeri_2[j]

            if numero_in_pos_i == numero_in_pos_j:
                # al posto di stampare, aggiorno la lista
                lista_delle_triplette.append((i, j, numero_in_pos_i))

    # stampo la lista che ho appena costruito
    print(lista_delle_triplette)

#. Soluzione::

    n = 5
    matrice = [list(range(n)) for i in range(n)]

    # inizializzo con il primo elemento (un qualunque altro elemento
    # andrebbe comunque bene)
    max_elemento_fino_ad_ora = matrice[0][0]

    # itero...
    for riga in matrice:
        for elemento in riga:
            # se trovo un elemento piu' grande di max_elemento_fino_ad_ora,
            # aggiorno quest'ultimo
            if elemento > max_elemento_fino_ad_ora:
                max_elemento_fino_ad_ora = elemento

    print(max_elemento_fino_ad_ora)

#. Soluzione::

    sequenze = [
        "ATGGCGCCCGAACAGGGA",
        "GTCCCTGTTCGGGCGCCA",
    ]

    # parto da una lista vuota
    risultato = []

    # itero...
    for sequenza in sequenze:
        # spezzo la sequenza corrente in triplette
        triplette = []
        for i in range(0, len(sequenza), 3):
            triplette.append(sequenza[i:i+3])

        # appendo (*non* extend()!!!) le triplette
        # ottenute alla lista risultato
        risultato.append(triplette)

    # stampo la lista che ho appena costruito
    print(risultato)

#. Soluzione::

    numeri = [5, 9, 4, 4, 9, 2]

    num_ripetizioni = {}

    for numero in numeri:
        if not numero in num_ripetizioni:
            num_ripetizioni[numero] = 1
        else:
            num_ripetizioni[numero] += 1

   o in alternativa::

    numeri = [5, 9, 4, 4, 9, 2]

    num_ripetizioni = {}

    for numero in numeri:
        if not numero in num_ripetizioni:
            num_ripetizioni[numero] = 0
        num_ripetizioni[numero] += 1

   oppure, sfruttando ``count()``::

    numeri = [5, 9, 4, 4, 9, 2]

    num_ripetizioni = {}

    for numero in numeri:
        if not numero in num_ripetizioni:
            num_ripetizioni[numero] = numeri.count(numero)

   Si noti che in quest'ultima variante, l'``if`` (ma non il suo "contenuto"!)
   e' opzionale.

   .. warning::

    Nella formulazione originale, l'esercizio richiedeva di usare due cicli
    ``for`` innestati. Una possibile soluzione a questa versione dell'esercizio
    e' la seguente::

        numeri = [5, 9, 4, 4, 9, 2]

        num_ripetizioni = {}

        for numero in numeri:
            if numero in num_ripetizioni:
                continue
            else:
                num_ripetizioni[numero] = 0
                for numero_2 in numeri:
                    if numero == numero_2:
                        num_ripetizioni[numero] += 1

    Una versione meno "ottimizzata"::

        numeri = [5, 9, 4, 4, 9, 2]

        num_ripetizioni = {}

        for numero in numeri:
            num_ripetizioni[numero] = 0
            for numero_2 in numeri:
                if numero == numero_2:
                    num_ripetizioni[numero] += 1

#. Soluzione::

    gruppi = [["gene1", "gene2"], ["gene3"], [], ["gene4", "gene5"]]

    # inizializzo con il primo gruppo
    gruppo_piu_grande_fino_ad_ora = gruppi[0]

    # itero...
    for gruppo in gruppi[1:]:
        if len(gruppo) > len(gruppo_piu_grande_fino_ad_ora):
            gruppo_piu_grande_fino_ad_ora = gruppo

    print(gruppo_piu_grande_fino_ad_ora)

#. Soluzione::

    sequenze_2HMI = {
        "A": "PISPIETVPVKLKPGMDGPKVKQWPLTEEKI",
        "B": "PISPIETVPVKLKPGMDGPKVKQWPLTEEKI",
        "C": "DIQMTQTTSSLSASLGDRVTISCSASQDISS",
        "D": "QITLKESGPGIVQPSQPFRLTCTFSGFSLST",
        "E": "ATGGCGCCCGAACAGGGAC",
        "F": "GTCCCTGTTCGGGCGCCA",
    }

    # parto dal dizionario vuoto
    istogrammi = {}

    for chiave, sequenza in sequenze_2HMI.items():

        # associo a questa chiave un istogramma vuoto
        istogrammi[chiave] = {}

        for residuo in sequenza:
            if not residuo in istogrammi[chiave]:
                istogrammi[chiave][residuo] = 1
            else:
                istogrammi[chiave][residuo] += 1

    # stampo il risultato
    print(istogrammi)

    # stampo il risultato in modo piu' leggibile
    for chiave, istogramma in istogrammi.items():
        print(chiave)
        print(istogramma)
        print()

#. Soluzione::

    tabella = [
        "protein domain start end",
        "YNL275W PF00955 236 498",
        "YHR065C SM00490 335 416",
        "YKL053C-A PF05254 5 72",
        "YOR349W PANTHER 353 414",
    ]

    # come prima cosa estraggo i nomi delle colonne dalla prima riga
    nomi_colonne = tabella[0].split()

    # parto da una lista vuota
    righe_come_dizionari = []

    # ora itero sulle altre righe
    for riga in tabella[1:]:

        # compilo il dizionario per questa riga
        dizionario = {}
        parole = riga.split()
        for i in range(len(parole)):

            # estraggo la parola corrispondente
            parola = parole[i]

            # estraggo il nome della colonna corrispondente
            nome_colonna = nomi_colonne[i]

            # aggiorno il dizionario
            dizionario[nome_colonna] = parola

        # ho compilato il dizionario per la riga corrente,
        # aggiorno la lista completa
        righe_come_dizionari.append(dizionario)

    # ho finito! stampo il risultato (una riga per volta,
    # per renderlo un po' piu' leggibile)
    for riga_come_dizionario in righe_come_dizionari:
        print(riga_come_dizionario)

#. Soluzione::

    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mai = alfabeto_min.upper()

    # costruisco il dizionario
    min_to_mai = {}
    for i in range(len(alfabeto_min)):
        min_to_mai[alfabeto_min[i]] = alfabeto_mai[i]


    stringa = "sono una stringa"

    # converto la stringa
    caratteri_convertiti = []
    for carattere in stringa:
        if carattere in min_to_mai:
            # e' un carattere alfabetico, lo devo convertire
            caratteri_convertiti.append(min_to_mai[carattere])
        else:
            # non e' un carattere alfabetico, non lo converto
            caratteri_convertiti.append(carattere)
    stringa_convertita = "".join(caratteri_convertiti)

    print(stringa_convertita)

#. Soluzione::

    righe_1 = open(input("percorso 1: ")).readlines()
    righe_2 = open(input("percoros 2: ")).readlines()

    # devo stare attento perche' i due file possono essere di
    # lunghezza diversa!
    max_righe = len(righe_1)
    if len(righe_2) > max_righe:
        max_righe = len(righe_2)

    # itero sulle righe di entrambi i file
    for i in range(max_righe):

        # prendo la i-esima riga del primo file,
        # sempre che esista
        if i < len(righe_1):
            riga_1 = righe_1[i].strip()
        else:
            riga_1 = ""

        # prendo la i-esima riga del secondo file,
        # sempre che esista
        if i < len(righe_2):
            riga_2 = righe_2[i].strip()
        else:
            riga_2 = ""

        print(riga_1 + " " + riga_2)

#. Soluzione::

    # qui leggo il file fasta
    fasta_come_dizionario = {}
    for riga in open("data/dna-fasta/fasta.1").readlines():

        # mi sbarazzo di eventuali a capo
        riga = riga.strip()

        if riga[0] == ">":
            intestazione = riga
            fasta_come_dizionario[intestazione] = ""

        else:
            fasta_come_dizionario[intestazione] += riga

    # itero sulle coppie intestazione-sequenza
    for intestazione, sequenza in fasta_come_dizionario.items():

        print("processo", intestazione)

        # conto quante volte appare ogni nucleotide
        conta = {}
        for nucleotide in ("A", "C", "T", "G"):
            conta[nucleotide] = sequenza.count(nucleotide)
        print("le conte sono", conta)

        # calcolo il gc-content
        gc_content = (conta["G"] + conta["C"]) / float(len(sequenza))
        print("il GC-content e'", gc_content)

        # calcolo il AT/GC-ratio
        somma_at = conta["A"] + conta["T"]
        somma_cg = conta["C"] + conta["G"]
        at_gc_ratio = float(somma_at) / float(somma_cg)
        print("la AT/GC-ratio e'", at_gc_ratio)
