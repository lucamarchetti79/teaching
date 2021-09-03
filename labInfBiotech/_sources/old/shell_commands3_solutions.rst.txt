==========================
Shell: Parte 3 (Soluzioni)
==========================


Wildcards, Parte 2
------------------

#. Soluzioni:
    #. ``echo *`` contiene una *wildcard*; la shell effettua la wildcard
       expansion sostituendo ``*`` con la lista dei path che fanno il match
       con la wildcard. In questo caso ``*`` fa il match con i file e le
       directory contenuti nella directory corrente. Quindi ``echo`` stampa
       a schermo i path che hanno fatto match.
    #. ``echo '*'``: qui la wildcard e' protetta dalle virgolette, niente
       wildcard expansion. ``echo`` stampa il carattere ``*`` a schermo.
    #. ``cat data/simple1/*.txt``?
#. ``cat data/simple1/*.txt``.
#. ``cat data/simple1/*.abc``.
#. ``cat data/simple1/*.txt > temp``.
#. ``cat data/simple1/*.abc >> temp``. Usiamo ``>>`` per non sovrascrivere ``temp``.
#. Soluzioni:
    #. ``ls /usr/bin/[0-9]*``
    #. ``ls /usr/bin/x*x``
    #. ``ls /usr/bin/x* /usr/bin/*x``







Filtri
------

#. Soluzioni:

   #. ``wc A`` stampa il numero di righe, parole e caratteri nel file ``A``.

   #. ``wc`` in ``cat A | wc`` stampa il numero di righe, parole e caratteri
      nello ``stdin``, ch in questo caso combacia con il contenuto di ``A``.

   Quindi in principio fanno la stessa cosa. Attenzione pero' che l'output nei
   due casi e' leggermente diverso.

#. Soluzioni:

   #. ``wc -l A`` stampa il numero di righe nel file ``A``.

   #. ``cat A | tr '\n' ' ' | wc -w`` passa i contenuti di ``A`` alla pipe,
      che li passa a ``tr``, che sostituisce tutti i caratteri di *a capo*
      ``\n`` con spazi (cioe' mette tutto il testo di ``A`` in una riga
      sola, senza ``\n`` alla fine); poi ``wc`` conta le *parole* nel
      risultato.

   Quindi i due comandi fanno cose *completamente* diverse: il primo conta le
   righe, il secondo le parole.

#. ``ls /usr/bin | wc -l``
#. ``ls -S /usr/bin``, oppure::

        ls -l /usr/bin | tr -s ' ' | cut -d' ' -f5,9 | sort -n -k1

#. ``ls -S /usr/bin | tail -n 1``, oppure::

        ls -l /usr/bin | tr -s ' ' | cut -d' ' -f5,9 | sort -n -k1 | head -n 1

#. Soluzioni::

    cat data/numbers.[12] | sort -n

#. Soluzioni::

        cat data/numbers.[12] | sort -n -r

    oppure::

        cat data/numbers.[12] | sort -n | tac

#. Controllo::

        ls /usr/bin | sort | uniq -d

    Non stampa nessun duplicato: la risposta e' no. (Basta pensare che una
    directory non puo' contenere due file con lo stesso nome.)

#. Soluzioni::

    ls data/deep1/*/* > lista1.txt
    ls data/deep2/*/*/* > lista2.txt
    ls data/deep3/*/*/*/* > lista3.txt

#. Soluzioni::

    cat data/deep1/*/* > lista1.txt
    cat data/deep2/*/*/* > lista2.txt
    cat data/deep3/*/*/*/* > lista3.txt

#. Soluzioni::

        cat data/deep1/*/* | grep '[13579]$' | wc -l

    Risposta: 50.

#. Soluzioni:
    - ``echo ACAB | cut -dC -f2`` stampa la scritta ``ACAB``, la passa a
        ``cut``, che usando ``C`` come delimitatore stampa la seconda colonna:
        ``AB``.

    - ``echo BACA | cut -dA -f1,2`` stampa la scritta ``BACA``, la passa a
        ``cut``, che usando ``A`` come delimitatore stampa la prima e seconda
        colonna: ``BAC``.

#. Soluzioni:
    - ``wc -m A`` stampa il numero di caratteri nel file ``A``.
    - ``cat A | wc | tr -s ' ' | cut -d' ' -f4`` stampa i contenuti di
        ``A`` a schermo; poi ``wc`` stampa il numero di righe, parole e caratteri
        a schermo su una sola riga di output; poi ``tr`` riduce spazi multipli
        ad uno solo; infine cut, usando lo spazio `` `` come delimitatore, stampa
        la quarta colonna -- che corrisponde al numero di caratteri nel file.
        Quindi il risultato e' come sopra.

#. Nell'output di ``ls -l`` il proprietario si trova nella terza colonna. Quindi
   e' sufficiente fare::

        ls -l /usr/bin | tr -s ' ' | sort -k 3

#. Ci sono almeno due possibilita'::

        ls -l /usr/bin | tr -s ' ' | sort -k 3 | tac

   oppure::

        ls -l /usr/bin | tr -s ' ' | sort -k 3 -r

#. Per stampare la lista dei file ed ordinarli dal ::

        ls /usr/bin/ -l | tr -s ' ' | sort -n -k 5

   L'output sara' simile a questo::

        $ ls /usr/bin/ -l | tr -s ' ' | sort -n -k 5
        total 260336
        lrwxrwxrwx 1 root root 1 May 6 2013 X11 -> .
        lrwxrwxrwx 1 root root 2 Aug 1 19:50 ghostscript -> gs
        lrwxrwxrwx 1 root root 2 Aug 23 12:49 inimf -> mf
        lrwxrwxrwx 1 root root 2 Dec 13 2014 mcdiff -> mc
        lrwxrwxrwx 1 root root 2 Dec 13 2014 mcedit -> mc
        lrwxrwxrwx 1 root root 2 Dec 13 2014 mcview -> mc
        lrwxrwxrwx 1 root root 2 Jul 3 21:44 unxz -> xz
        lrwxrwxrwx 1 root root 2 Jul 3 21:44 xzcat -> xz
        ...

   I file sono ordinati correttamente; ora dobbiamo estrarre la seconda riga
   (la prima e' un sommario stampato da ``ls``, e dobbiamo scartarla). Per
   estrarre la seconda riga posso aggiungere ``head`` e ``tail``::

        ... | head -n 2 | tail -n 1

   oppure usare ``grep``::

        ... | grep -v '^total' | head -n 1

   In entrambi i casi ottengo una riga sola, simile a questa::

        lrwxrwxrwx 1 root root 1 May 6 2013 X11 -> .

   A questo punto e' sufficiente estrarre la dimension (nel mio caso ``1``)
   aggiungendo ``cut``::

        ... | cut -d' ' -f5

   Ci sono un numero di alternative altrettanto valide.

#. Simile a prima::

        ls /usr/bin -l | tr -s ' ' | sort -n -k 5 | tail -n 1 | cut -d' ' -f9

#. Stampo la lista dei file, estraggo le dimensioni, e uso ``sort | uniq``::

        ls /usr/bin -l | tr -s ' ' | sort -n -k 5 | cut -d' ' -f5 | sort | uniq -d | wc -l

    Il ``wc -l`` alla fine serve per contare il numero di duplicati trovati da
    ``uniq -d``. Nel mio caso ce ne sono 166. In breve, la risposta e' si'.

Espressioni regolari e grep
---------------------------

#. Soluzioni:
        #. ``.``: valida, un carattere qualunque, in qualunque posizione. Leggi: una stringa di almeno un carattere.
        #. ``.*``: valida, un numero arbitrario di caratteri qualunque, anche zero. Leggi: una stringa qualunque.
        #. ``[09]{2}``: valida, esattamente due caratteri ``0`` oppure ``9``. Leggi: fa match con ``00``, ``09``, ``90`` e ``99``.
        #. ``[0-9]{2}``: valida, esattamente due caratteri numerici qualunque. Leggi: stringhe di due caratteri tra ``0`` e ``9``.
        #. ``*``: valida, il carattere asterisco ``*``. (Si noti la differenza con le wildcards!)
        #. ``[``: non valida.
        #. ``[[]``: valida, fa match con la parentesi quadra aperta ``[`` in qualunque posizione.
        #. ``^.3``: valida, fa match con stringhe che iniziano con un carattere qualunque e proseguono con ``3``.
        #. ``^.{3}``: valida, fa il match con stringhe lunghe almeno tre caratteri.
        #. ``.{3}$``: valida, come sopra.
        #. ``^>``: valida, fa match con stringhe che iniziano per ``>``.
        #. ``AA``: valida, fa match con stringhe che contengono la sotto-stringa ``AA``, in qualunque posizione.
        #. ``^AA$``: valida, fa match on la sola stringa ``AA``.
        #. ``aA``: valida, fa match con stringhe che contengono la sotto-stringa ``aA``, in qualunque posizione.
        #. ``[aA]``: valida, fa match con stringhe che contengono una ``a`` o una ``A``, o entrambe, in qualunque posizione.
        #. ``word``: valida, fa match con stringhe che contengono la parola ``word``, in qualunque posizione.
        #. ``w..d``: valida, fa match con stringhe che contengono parole che cominciano con ``w``, finiscono per ``d``, e sono lunghe quattro caratteri.
        #. ``^$``: valida, fa match con righe vuote.
        #. ``[}{]``: valida, fa match con righe che contengono una alemno parentesi graffa.
        #. ``[0-9]+``: valida, fa match con righe che contengono una sotto-stringa numerica lunga almeno un carattere.

#. Soluzioni:
    #. Tutti i caratteri alfanumerici, maiuscoli e minuscoli::

        [a-zA-Z]

    #. Le righe contenenti solo spazi::

        ^[ ]*$

    #. Le righe che contengono punti esclamativi o punti interrogativi::

        [!?]

    #. I giorni della settimana (nel modo piu' compatto possibile) Senza lettere accentate::

            (lune|marte|mercole|giove|vener)di|sabato

        (Non uso lettere accentate per comodita'.)

    #. Le parole di radice ``frazion``-, ad esempio: frazione, frazionario, *etc.*::

        frazion.*

    #. I multipli di 10, i multipli di 5, i numeri dispari::

        [0-9]*0
        [0-9]*[05]
        [0-9]*[13579]

    #. I numeri razionali come frazione::

        [0-9]*/[0-9]*

    #. I numeri razionali in notazione decimale, ad esempio: 1.34, .99, 17., 3::

        [0-9]*(\.[0-9]*)?

    #. I numeri razionali in notazione scientifica, ad esempio: 1.34e10, 1.34e-10::

        [0-9]*(\.[0-9]*|[0-9]+e[+-]?[0-9]+)?

    #. Le somme (esempio: a+b+c+d, a+b, *etc.*) di lunghezza arbitraria, dove a, b, c, ... sono numeri interi::

        [0-9]+(\+[0-9]+)+

    #. Le somme di due moltiplicazioni, cose come: (2 * 3 * 2) + (5 *
       7), (6 * 2) + (4 * 3), *etc.*:
       E' sufficiente generalizzare la soluzione all'esercizio precedente.

#. Sequenze fasta:
   
   Eseguendo un::
     
     cat sequences.fasta
     
   ci si puo' accorgere che nel file si alternano righe di intestazione (che
   cominciano con '>') e relative sequenze. Negli esercizi seguenti, per
   filtrare le intestazioni uso::
     
     cat sequences.fasta | grep -Ev ">"
     
   L'opzione '-v' di grep fa il matching inverso, ovvero tiene le righe che NON fanno
   match con la relativa regex. In alternativa posso usare::
     
     cat sequences.fasta | grep -E "^[^>]"
     
   Per fare match con tutte le righe che non cominciano con '>'.

   #. Soluzioni:

	- Comando::
	    
	    cat sequences.fasta | grep -Ev ">" | grep -E 'F..F$' | wc -l

	  Numero di match: 1

	- Comando::

	    cat sequences.fasta | grep -Ev ">" | grep -E 'RF[^P][IV]' | wc -l

	  Numero di match: 64

	- Comando::

	    cat sequences.fasta | grep -Ev ">" | grep -E '(F..F$|RF[^P][IV])' | wc -l

	  Numero di match: 65	

   #. Soluzioni:

	- Comando::
	    
	    cat sequences.fasta | grep -Ev ">" | grep -E 'YYY.{0,3}H' | wc -l

	  Numero di match: 3

	- Comando::

	    cat sequences.fasta | grep -Ev ">" | grep -E '[^ARNDCEQGHILKMFPSTWYV]' | wc -l

	  Numero di match: 8

	- Comando::

	    cat sequences.fasta | grep -Ev ">" | grep -E '[^ARNDCEQGHILKMFPSTWYV]' | grep -E
	    'YYY.{0,3}H' | wc -l

	  Numero di match: 0

   #. Soluzioni:

	- Comando::
	    
	    cat sequences.fasta | grep -Ev ">"  | grep -E '^[^R][^K].*RK' | wc -l

	  Numero di match: 713

	- Comando::

	    cat sequences.fasta | grep -Ev ">"  | grep -E 'RR[^RK]' | wc -l

	  Numero di match: 604

	- Comando::

	    cat sequences.fasta | grep -Ev ">"  | grep -vE '^[^R][^K].*RK' |
	    grep -vE 'RR[^RK]' | wc -l

	  Numero di match: 49

   #. Soluzioni:

	- Comando::
	    
	    cat sequences.fasta | grep -Ev ">"  | grep -E 'F.[FY]P' | wc -l

	  Numero di match: 44

	- Comando::

	    cat sequences.fasta | grep -Ev ">"  | grep -E '^.+P[TS]AP.+$' | wc -l

	  Numero di match: 19

	- Comando::

	    cat sequences.fasta | grep -Ev ">"  | grep -E '(^.+P[TS]AP.*F.[FY]P|F.[FY]P.*P[TS]AP.+$)' | wc -l

	  Numero di match: 6
