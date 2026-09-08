===========================
Lezione 8b - Soluzioni
===========================

If
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

