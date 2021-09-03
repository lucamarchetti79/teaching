============================
Python: Funzioni (Soluzioni)
============================

#. Soluzione: lo stesso tipo del valore che gli passo! La funzione restituisce
   il valore dell'argomento senza toccarlo.

   #. un intero.
   #. un dizionario.
   #. una lista.
   #. un razionale.

#. Soluzione: la somma o concatenazione dei due argomenti. Quindi:

   #. un intero.
   #. una lista.
   #. una stringa.

#. Soluzione::

    def stampa_pari_dispari(numero):
        if numero % 2 == 0:
            print("pari")
        else:
            print("dispari")

    stampa_pari_dispari(98)
    stampa_pari_dispari(99)

   Occhio che ``stampa_pari_dispari()`` stampa gia' da se' a schermo,
   non e' necessario fare::

    print(stampa_pari_dispari(99))

   altrimenti Python stampera'::

    pari
    None

   Il ``None`` viene dal ``print`` aggiuntivo: visto che ``stampa_pari_dispari()``
   non ha ``return``, il suo risultato e' sempre ``None``. Il ``print`` aggiuntivo
   stampa proprio questo ``None``.

#. Soluzione::

    def calcola_pari_dispari(numero):
        if numero % 2 == 0:
            return "pari"
        else:
            return "dispari"

    print(calcola_pari_dispari(98))
    print(calcola_pari_dispari(99))

   In questo caso invece, visto che non c'e' nessun ``print`` in ``calcola_pari_dispari()``,
   e' necessario aggiungere a mano un ``print`` che ne stampi il risultato!

#. Soluzione::

    def controlla_alfanumerico(stringa):
        caratteri_alfanumerici = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        alfanumerica = True
        for carattere in stringa:
            if not carattere in caratteri_alfanumerici:
                alfanumerica = False

        return alfanumerica

    # testo la funzione
    print(controlla_alfanumerico("ABC123"))
    print(controlla_alfanumerico("A!%$*@"))

   Posso anche usare ``break`` per interrompere il ciclo ``for`` appena trovo
   un carattere alfanumerico (e' impossibile che una stringa dove ho appena
   trovato un carattere non-alfanumerico ridiventi alfanumerica), cosi'::

    def controlla_alfanumerico(stringa):
        caratteri_alfanumerici = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        alfanumerica = True
        for carattere in stringa:
            if not carattere in caratteri_alfanumerici:
                alfanumerica = False
                break # <-- esco dal for

        # <-- il break mi fa arrivare qui
        return alfanumerica

    # testo la funzione
    print(controlla_alfanumerico("ABC123"))
    print(controlla_alfanumerico("A!%$*@"))

   In alternativa, visto che quando faccio ``break`` arrivo direttamente al
   ``return``, posso saltare un passaggio e fare direttamente ``return``::

    def controlla_alfanumerico(stringa):
        caratteri_alfanumerici = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        for carattere in stringa:
            if not carattere.upper() in caratteri_alfanumerici:
                # ho incontrato un carattere non alfanumerico
                # posso rispondere False
                return False

        # arrivo alla fine del for solo se non ho mai fatto `return`, il
        # che succede solo se la condizione dell'`if` e' sempre stata False
        # per tutti i caratteri: vuol dire che sono tutti caratteri alfanumerici
        # rispondo True
        return True

    # testo la funzione
    print(controlla_alfanumerico("ABC123"))
    print(controlla_alfanumerico("A!%$*@"))

#. Soluzione::

    def domanda():
        percorso = input("scrivi un percorso: ")
        print(open(percorso).readlines())

    # la testo
    domanda()

#. Soluzione::

    def wc(stringa):
        num_caratteri = len(stringa)
        num_a_capo = stringa.count("\n")
        num_parole = len(stringa.split()) # split rompe sia sugli spazi che sugli a-capo
        return (num_caratteri, num_a_capo, num_parole)

    # la testo
    print(wc("sono\nuna bella\nstringa"))

#. Soluzione::

    def stampa_dizionario(un_dizionario):
        # l'ordine in cui vanno stampate le righe non importa, percio'
        # posso usare l'ordine naturale in cui mi vengono fornite da
        # `items()`
        for chiave, valore in un_dizionario.items():
            print(chiave, "->", (str(valore * 100.0) + "%"))

    # la testo

    dizionario = {
        "arginina": 0.7,
        "lisina": 0.1,
        "cisteina": 0.1,
        "istidina": 0.1,
    }

    stampa_dizionario(dizionario)

#. Soluzione::

    def stampa_dizionario_ordinato(un_dizionario):
        # estraggo le chiavi e le ordino
        chiavi_ordinate = list(un_dizionario.keys())
        chiavi_ordinate.sort()

        # ora stampo le coppie chiave-valore in ordine
        for chiave in chiavi_ordinate:
            valore = un_dizionario[chiave]

            print(chiave, "->", (str(valore * 100.0) + "%"))

    # la testo

    dizionario = {
        "arginina": 0.7,
        "lisina": 0.1,
        "cisteina": 0.1,
        "istidina": 0.1,
    }

    stampa_dizionario_ordinato(dizionario)

#. Soluzione::

    # presa dall'esempio
    def calcola_fattoriale(n):
        fattoriale = 1
        for k in range(1, n+1):
            fattoriale = fattoriale * k
        return fattoriale

    def crea_lista_di_fattoriali(n):
        lista_di_fattoriali = []
        for i in range(n):
            lista_di_fattoriali.append(calcola_fattoriale(i))
        return lista_di_fattoriali

    # la testo
    print(crea_lista_di_fattoriali(2))
    print(crea_lista_di_fattoriali(4))
    print(crea_lista_di_fattoriali(6))

   qui ho *riutilizzato* la funzione ``calcola_fattoriale()`` definita in uno
   degli esempi.

#. Soluzione::

    def conta_carattere(testo, carattere_voluto):
        conta = 0
        for carattere in testo:
            if carattere == carattere_voluto:
                conta += 1
        return conta

    # la testo
    print(conta_carattere("abbaa", "a"))
    print(conta_carattere("abbaa", "b"))
    print(conta_carattere("abbaa", "?"))

   oppure, piu' semplicemente, posso sfruttare ``count()``::

    def conta_carattere(testo, carattere_voluto):
        return testo.count(carattere_voluto)

    # la testo
    print(conta_carattere("abbaa", "a"))
    print(conta_carattere("abbaa", "b"))
    print(conta_carattere("abbaa", "?"))

#. Soluzione::

    def conta_caratteri(testo, caratteri_voluti):
        conta = {}
        for carattere_voluto in caratteri_voluti:
            conta[carattere_voluto] = conta_carattere(testo, carattere_voluto)
        return conta

    # la testo
    print(conta_caratteri("abbaa", "ab?"))

   dove ho riutilizzato la funzione dell'esercizio precedente.

#. Soluzione::

    def distanza(coppia1, coppia2):
        x1, y1 = coppia1
        x2, y2 = coppia2

        dx = x1 - x2
        dy = y1 - y2

        return (float(dx)**2 + float(dy)**2)**0.5

    # la testo
    print(distanza((0, 0), (1, 1)))
    print(distanza((2, 3), (3, 2)))

#. Soluzione::

    def sottostringa(prima, seconda):
        return seconda in prima

    # la testo
    print(sottostringa("ACGT", "T"))
    print(sottostringa("ACGT", "x"))

#. Soluzione::

    def sottostringhe_non_vuote(stringa):
        sottostringhe = []

        # tutte le possibili posizioni in cui far iniziare la sottostringa
        for inizio in range(len(stringa)):

            # tutte le poss. posizioni in cui far finire la sottostringa
            for fine in range(inizio + 1, len(stringa) + 1):

                # estraggo la sottostringa ed aggiorno la lista
                sottostringhe.append(stringa[inizio:fine])
        return sottostringhe

    # la testo
    print(sottostringhe_non_vuote("ACTG"))

#. Soluzione::

    def conta_sottostringhe(pagliaio, ago):
        ripetizioni = 0
        for inizio in range(len(pagliaio)):
            for fine in range(inizio+1, len(pagliaio)+1):

                # stampo quanto vale la sottostringa, per sicurezza
                print(inizio, fine, ":", pagliaio[inizio:fine], "==", ago, "?")

                # controllo se la sottostringa e' uguale ad `ago`
                if pagliaio[inizio:fine] == ago:
                    print("ho trovato una ripetizione!")
                    ripetizioni += 1

        return ripetizioni

    # la testo
    print(conta_sottostringhe("ACTGXACTG", "ACTG"))

#. Soluzione::

    def sottostringa_piu_lunga(stringa1, stringa2):

        # riutilizzo la soluzione sopra
        sottostringhe1 = sottostringhe_non_vuote(stringa1)
        sottostringhe2 = sottostringhe_non_vuote(stringa2)

        # controllo tra tutte le coppie di sottostringhe
        # quale e' quella piu' lunga che appare sia in
        # stringa1 che in stringa2
        piu_lunga = ""
        for sottostringa1 in sottostringhe1:
            for sottostringa2 in sottostringhe2:

                # se sono uguali e piu' lunghe della sottostringa
                # comune piu' lunga trovata fin'ora...
                if sottostringa1 == sottostringa2 and \
                   len(sottostringa1) > len(piu_lunga):

                    # aggiorno
                    piu_lunga = sottostringa1

        return piu_lunga

    # la testo
    print(sottostringa_piu_lunga("ACTG", "GCTA"))
    print(sottostringa_piu_lunga("", "ACTG"))
    print(sottostringa_piu_lunga("ACTG", ""))
