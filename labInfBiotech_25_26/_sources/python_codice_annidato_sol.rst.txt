===========================
Lezione 9b - Soluzioni
===========================

**Codice annidato**

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
