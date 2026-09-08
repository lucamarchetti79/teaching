==============
Shell: Parte 3
==============

Wildcards, Parte 2
------------------

Le wildcard piu' importanti sono:

==========  ===========================================================
wildcard    fa *match* con
==========  ===========================================================
``akz``     il testo "``akz``"
``*``       una stringa qualunque (anche vuota)
``?``       un carattere qualunque
``[akz]``   un carattere solo tra ``a``, ``k`` e ``z``
``[a-z]``   un carattere alfabetico qualunque
``[0-9]``   una cifra qualunque
``[!1b]``   un carattere qualunque che non sia ``1`` o ``b``
``[!a-e]``  un carattere qualunque che non sia ``a``, ``b``, ..., ``e``
==========  ===========================================================

Quando la shell incontra un comando dove uno (o piu') degli argomenti contiene
delle wildacrds, esegue la *wildcard expansion*: sostituisce all'argomento
incriminato tutti i file che fanno *match* con la wildcard.

.. warning::

    Le wildcards sono simili alle regex, ma non sono la stessa cosa:

    #. Le wildcards sono usate dalla shell per fare il match di **percorsi**.
    #. Le regex sono usate da ``grep`` per fare il match di **righe di testo** contenute in un file.
    #. Le regole che determinano il *match* di wildcards e regex sono diverse.

****

**Esempio**. La wildcard::

    le rose sono *se

fa *match* con::

    le rose sono rosse

ma anche con::

    le rose sono costose

e::

    le rose sono grosse

ma non con::

    i maneggi abitano in montagna

Le wildcard possono essere combinate, ad esempio::

    test?[a-z][!0-9]

fa il *match* con tutti i percorsi che cominciano con ``test``, proseguono con
un carattere qualunque, poi con un carattere alfabetico ed infine con un
carattere non numerico.

****

**Esempio**. Un esempio piu' realistico. Il comando::

    cat data/dna-fasta/*.[12]

fa *match* con tutti i file nella directory ``data/dna-fasta`` il cui filename
e' composto di una-stringa-qualunque, seguita da un punto, seguito da ``1`` o
``2`` e nient'altro. Nel nostro caso i soli file a fare *match* sono::

    data/dna-fasta/fasta.1
    data/dna-fasta/fasta.2

Dopo la wildcard expansion il comando precedente diventa::

    cat data/dna-fasta/fasta.1 data/dna-fasta/fasta.2

****

**Esempio**. Per stampare a schermo i contenuti della directory data, scrivo::

    ls data

Per stampare i contenuti delle *directory* che stanno in data::

    ls data/*

qui la wildcard ``*`` viene espansa in::

    aatable deep0 ... deep4 dna-fasta empty1 empty2 prot-fasta prot-pdb simple1

Per stampare a schermo solo il contenuto delle directory ``deep0``, ..., ``deep4``::

    ls data/deep*

Mentre per restringere la wildcard alle directory ``deep0`` e ``deep3``::

    ls data/deep[03]

e solo per le directory ``deep0``, ..., ``deep4`` ma non ``deep2``::

    ls data/deep[!2]

|

Esercizi
--------

#. Cosa fa il comando:
    #. ``echo *``?
    #. ``echo '*'``?
    #. ``cat data/simple1/*.txt``?
#. Stampare il contenuto dei file ``.txt`` in ``data/simple1``.
#. Stampare il contenuto dei file ``.abc`` in ``data/simple1``.
#. Concatenare il contenuto dei file ``.txt`` in ``data/simple1`` in un nuovo file ``temp``.
#. Concatenare il contenuto dei file ``.abc`` in ``data/simple1`` ed aggiungerlo in coda a ``temp``.
#. Tra i file in ``/usr/bin``, trovare con ``ls`` quelli che:
    #. Iniziano per una cifra.
    #. Iniziano e finiscono per ``x``.
    #. Iniziano o finiscono per ``x``.

|
|

Filtri
------

La shell mette a disposizione un numero di comandi che agiscono da *filtri*:
il loro scopo e' permettervi di estrarre righe/colonne da file di testo,
ordinare i dati, sostituire caratteri, ed in generale calcolare statistiche
sui dati.

======= ======================================= ======================
comando funzione                                opzioni principali
======= ======================================= ======================
wc      conta caratteri, parole e righe         ``-m``, ``-w``, ``-l``
sort    ordina righe                            ``-f``, ``-n`, ``-r``
uniq    rimuove righe consecutive identiche     ``-c``, ``-d``
cut     stampa una o piu' colonne               ``-d``, ``-f``
tr      traduce caratteri                       ``-d``, ``-s``
grep    seleziona righe in base ad una *regex*  ``-E``, ``-i``, ``-v``
======= ======================================= ======================

Vediamoli all'opera.

|

****

**Esempio**. Creo un file con due righe di testo::

    echo uno > file; echo due >> file

Controllo quante righe ho scritto::

    wc -l file

****

**Esempio**. Per contare il numero di righe di ``data/numers.1``::

    wc -l data/numbers.1

Per contare quanti file e directory ci sono nella home::

    ls ~ | wc -l

****

**Esempio**. Concateniamo i file in ``data/dna-fasta``::

    cat data/dna-fasta/* > all_fastas

Vogliamo stampare le righe di ``all_fastas`` in ordine alfanumerico::

    sort all_fastas

Ed ora vogliamo copiarle in un file::

    sort all_fastas > sorted_fastas

Possiamo ottenere lo stesso effetto con una pipeline::

    cat data/dna-fasta/* | sort > sorted_fastas

****

**Esempio**. I file ``data/numbers.1`` e ``data/numbers.2`` contengono liste
di numeri. Vogliamo controllare se ci sono doppioni usando ``uniq``.

C'e' un problema: ``uniq`` trova solo doppioni *sequenziali*. Se lo applico
a questo testo::

    aaaa
    bbbb
    bbbb
    aaaa

``uniq`` riesce si' a capire che ``bbbb`` e' ripetuto, ma non ci riesce con
``aaaa``.

Quindi se voglio trovare *tutti* i doppioni indipendentemente dall'ordine in
cui si trovano nel file che mi interessa, devo prima usare ``sort`` per
avvicinare le righe identiche. Nel nostro caso, faccio::

    sort data/numbers.1 > temp1
    sort data/numbers.2 > temp2
    uniq -d temp1
    uniq -d temp2

Non ci sono ripetizioni nei singoli file. Ci sono forse doppioni nei file
presi assieme?

Siamo tentati di usare::

    cat temp[12] | uniq -d

Pero' non e' detto che il concatenamento di due file ordinati produca un file
ordinato. Quindi usamo di nuovo ``sort``::

    cat temp[12] | sort | uniq -d

Il numero ``3`` appare piu' volte! Quante? Verifichiamo::

    cat temp[12] | sort | uniq -d -c

Due volte. In alternativa::

    cat temp[12] | sort | uniq -d | wc -l

Provate a ripetere il codice costruendo incrementalemente la pipeline.

****

**Esempio**. Il comando ``tr`` permette di sostituire (tradurre) caratteri con
altri caratteri. Data una sequenza nucleotidica voglio sostituire tutte le
timine ``T`` con uracile ``U``, scrivo::

    echo TATAAA | tr 'T' 'E'

Tra gli usi piu' comuni di ``tr``:

- Tradurre da maisucolo a minuscolo (e viceversa)::

    echo 'voglio diventare grande!' | tr 'a-z' 'A-Z'

- Sostituire i caratteri (nascosti) "a capo", ``\n``, con altri. Confrontate::

    ls data

  e::

    ls data | tr '\n' ','

- Rimuovere ripetizioni di caratteri, con l'opzione ``-s`` (*squeeze*)::

    echo 'voglio     uno     spazio     solo!' | tr -s ' '

- Rimuovere caratteri estranei con ``-d``, ad esempio da una sequenza proteica::

    echo 'xixxxox sxxxonxxo uxxxxnaxx xxxxproxxxtxexxinxa' | tr -d ' '

****

**Esempio**. Il comando ``cut`` estrae *colonne* (non *righe*!) dallo ``stdin``.
Ha due opzioni fondamentali (e poco opzionali):

- ``-d`` specifica il separatore: il carattere che separa le colonne.

- ``-f`` specifica quali colonne (*fields*, campi) estrarre.

Ad esempio, assumete di avere un file con questo testo::

    nome cognome anno-di-nascita
    Marco Rossi 1989
    Luisa Bianchi 1981
    Dante Alighieri 1265

Qui le colonne sono separate da semplici spazi. Posso estrarre la colonna dei
nomi con::

    cut -d' ' -f1 file

e quella delle date con::

    cut -d' ' -f3 file

Se volessi estrarre solo i nomi saltando la prima riga::

    tail -n +2 file | cut -d' ' -f1

oppure::

    cut -d' ' -f1 file | tail -n +2

o ancora::

    cat file | cut ... | tail ...

Assumete che il file contenga::

    nome,cognome,anno-di-nasciata,impatto-sui-posteri
    Dante,Alighieri,1265,9
    Marcel,Proust,1871,7
    Homer,Simpson,1989,10

Qui la virgola funge da separatore. Per estrarre i cognomi, scrivo::

    tail -n +2 file | cut -d',' -f2

Possiamo anche estrarre piu' di una colonna, ad esempio nome, cognome e data
di nascita::

    tail -n +2 file | cut -d',' -f1,2,3

oppure::

    tail -n +2 file | cut -d',' -f1-3

Per estrarre nome, cognome e impatto::

    tail -n +2 file | cut -d',' -f1,2,4

Per estrarre tutte le colonne dall'anno in poi::

    tail -n +2 file | cut -d',' -f3-

|

Esercizi
--------

#. Confronta ``wc A`` e ``cat A | wc``.
#. Confronta ``wc -l A`` e ``cat A | tr '\n' ' ' | wc -w``.
#. Quanti file sono contenuti in ``/usr/bin/``?
#. Stampare i file in ``/usr/bin`` ordinati per dimensione, sia con ``ls`` da solo che con ``ls | sort ...``.
#. Stampare solo il file piu' piccolo in ``/usr/bin``.
#. Stampare i numeri in ``data/numbers.1`` e ``data/numbers.2`` ordinati dal piu' piccolo al piu' grande.
#. Stampare i numeri in ``data/numbers.1`` e ``data/numbers.2`` ordinati dal piu' grande al piu' piccolo.
#. Ci sono file doppi in ``/usr/bin``?
#. Scrivere in ``listaN.txt`` la lista di tutti i file in ``data/deepN``, per N=1,2,3.
#. Scrivere in ``dataN.txt`` i contenuti di tutti i file in ``data/deepN``, per N=1,2,3.
#. Quante repliche dispari di ``KrustyIlKlown`` ci sono in ``data/deep1``?
#. Cosa fa ``echo ACAB | cut -dC -f2``? E ``echo BACA | cut -dA -f1,2``?
#. Compara ``wc -m A`` e ``cat A | wc | tr -s ' ' | cut -d' ' -f4``
#. Stampa i file in ``/usr/bin`` ordinati per proprietario. (Si veda ``-k`` nel manuale di ``sort``).
#. Come sopra, ma in ordine inverso. E' necessario ``tac``?
#. Stampare solo la dimensione del file piu' piccolo in ``/usr/bin``.
#. Stampare solo il nome del file piu' grande in ``/usr/bin``.
#. Ci sono file di dimensioni identiche in ``/usr/bin``? Quanti?

|
|

Espressioni regolari e ``grep``
-------------------------------

``grep`` serve per estrarre *righe* che combaciano con una data espressione
regolare: viene usato spesso per *filtrare* le righe di un file (o dello
``stdin``) alle quali siamo interessati, scartando tutte le altre.

La sintassi e'::

    grep regex file

oppure::

    cat file | grep regex

Una lista (non esaustiva) delle **regex estese**:

=========================== ================================================
Simbolo                     Fa match con
=========================== ================================================
``testo``                   La stringa ``testo``
``.``                       Un carattere qualunque
``[abc]``                   Un carattere qualunque tra ``a``, ``b`` e ``c``
``[a-z]``                   Un carattere nell'intervallo ``a``, ..., ``z``
``[^abc]``                  Un carattere che *non* sia ``a``, ``b``, o ``c``
``$``                       La fine della riga (il carattere ``\n``)
``^``                       L'inizio della riga (il carattere dopo ``\n``)
``regex*``                  almeno zero ripetizioni di regex
``regex+``                  almeno una ripetizione di regex
``regex{n}``                n ripetizioni di regex
``regex{n,m}``              tra le n e le m ripetizioni di regex
``(regex1|regex2)``         regex1 oppure regex2
=========================== ================================================

|

.. warning::

    Spesso useremo regex estese. Per fare in modo che ``grep`` le riconosca,
    useremo l'opzione ``-E``.

.. warning::

    Le regex hanno alcuni caratteri speciali in comune con le wildcards.

    Percio' quando invochiamo ``grep``, e' necessario inibire i caratteri
    speciali della regex usata, in modo che la shell non esegua la wildcard
    expansion.

    Il modo piu' semplice di farlo e' usare virgolette::

        grep 'regex' file

    oppure::

        cat file | grep 'regex'

****

Opzioni principali di ``grep``:

======= ======================================
opzione funzione                              
======= ======================================
``-v``  matching inverso
``-o``  mostra soltanto il pattern trovato
``-i``  ignora distinzione maiuscole/minuscole
======= ======================================

**Esempio**. Le seguenti regex combaciano con:

- ``.*``, tutte le stringhe (anche la stringa vuota).
- ``.+``, tutte le stringhe (ma non quella vuota).
- ``abc``, tutte le stringhe che *contengono* ``abc``.
- ``[abc]``, tutte le stringhe che contengono almeno una tra ``a``, ``b``, e ``c``.
- ``^abc``, tutte le stringhe che iniziano per ``abc``.
- ``abc$``, tutte le stringhe che finiscono per ``abc``.
- ``^abc$``, la sola stringa ``abc``.
- ``^.*$``, tutte le stringhe terminate da un carattere di a capo ``\n``.
- ``[a-z]``, tutte le stringhe che contengono almeno un carattere alfabetico minuscolo.
- ``^[A-Z ]$``, tutte le stringhe che contengono solo caratteri alfabetici maiuscoli e spazi.
- ``^[01 ]{3+}$``, tutte le stringhe di almeno tre caratteri che rappresentano parole binarie.
- ``ant(onio|idiluviano)``, tutte stringhe che contengono ``antonio`` o ``antidiluviano`` (o entrambi).
- ``^[ ,](X{10}|Y{10})[ ,]``, tutte le stringhe che iniziano con uno spazio o una virgola, seguito da dieci ``X`` o dieci ``Y``, seguiti da uno spazio o una virgola.

****

**Esempio**. Per costruire regex che facciano *match* con caratteri speciali
(ad esempio il punto ``.``), posso usare l'escaping o inserirli tra parentesi
quadre.  Ad esempio::

    grep '.' data/aatable

estrae "tutte le righe che contengono almeno un carattere", mentre::

    grep '\.' data/aatable
    grep '[.]' data/aatable

estraggono "tutte le righe che contengono un punto".

.. note::

    L'opzione ``--color`` chiede a ``grep`` di colorare  il match.

****

**Esempio**. Prendiamo il file ``1A34.fasta`` da `qui <http://www.rcsb.org/pdb/explore/explore.do?structureId=1a34>`_.
Contiene la sequenza aminoacidica delle tre catene della proteina 1A34::

    >1A34:A|PDBID|CHAIN|SEQUENCE
    MGRGKVKPNRKSTGDNSNVVTMIRAGSYPKVNPTPT
    WVRAIPFEVSVQSGIAFKVPVGSLFSANFRTDSFTS
    VTVMSVRAWTQLTPPVNEYSFVRLKPLFKTGDSTEE
    FEGRASNINTRASVGYRIPTNLRQNTVAADNVCEVR
    SNCRQVALVISCCFN
    >1A34:B|PDBID|CHAIN|SEQUENCE
    AAAAAAAAAA
    >1A34:C|PDBID|CHAIN|SEQUENCE
    UUUUUUUUUU

Ogni catena compare come un'intestazione (o *header*) che comincia col
carattere ``>``, seguita dalla sequenza vera e propria.

Per estrarre le intestazioni, sfrutto il fatto che cominciano per ``>``::

    grep '>' 1A34.fasta

Il risultato e'::

    >1A34:A|PDBID|CHAIN|SEQUENCE
    >1A34:B|PDBID|CHAIN|SEQUENCE
    >1A34:C|PDBID|CHAIN|SEQUENCE

Ancora meglio, costringo ``grep`` a cercare ``>`` all'inizio della riga (e non,
ad esempio, nel bel mezzo di una sequenza proteica)::

    grep '^>' 1A34.fasta

Per estrarre invece le sequenze::

    grep -v '^[^>]' 1A34.fasta

****

**Esempio**. Se siamo interessati a scoprire se, tra le catene in
``data/prot-fasta/`` quali contengono la sequenza "``DP``" (leggi: acido
aspartico seguito da prolina)::

    grep DP data/prot-fasta/*.fasta

Il risultato e'::

    data/prot-fasta/3J00.fasta:FVIDADHEHIAIKEANNLGIPV...
    data/prot-fasta/3J00.fasta:PRRRVIGQRKILPDPKFGSELL...
    data/prot-fasta/3J00.fasta:SMQDPIADMLTRIRNGQAANKA...
    data/prot-fasta/3J01.fasta:AKGIREKIKLVSSAGTGHFYTT...
    data/prot-fasta/3J01.fasta:EYDPNRSANIALVLYKDGERRY...
    data/prot-fasta/3J01.fasta:ARNLHKVDVRDATGIDPVSLIA...

Quindi si', abbiamo risposto alla nostra domanda: ci sono ben due proteine
(``3F00`` e ``3J01``) che includono il pattern "``DP``".

Per controllare di non avere mai fatto match con le intestazioni, scrivo::

    grep DP data/prot-fasta/*.fasta | grep '^>'

``grep`` non stampa niente, percio' non abbiamo mai tenuto intestazioni. Bene.
Per evitare sorprese, possiamo filtrare via le intestazioni a priori con::

    grep -v DP data/prot-fasta/*.fasta | grep -v '^>'

****

**Esempio**. Costruiamo una pipeline complessa.

Dato l'output di ``grep DP ...``, voglio stampare il nome delle proteine che
contengono la sequenza ``DP``. L'output di ``grep`` era::

    data/prot-fasta/3J00.fasta:FVIDADHEHIAIKEANNLGIPV...
    data/prot-fasta/3J00.fasta:PRRRVIGQRKILPDPKFGSELL...
    data/prot-fasta/3J00.fasta:SMQDPIADMLTRIRNGQAANKA...
    data/prot-fasta/3J01.fasta:AKGIREKIKLVSSAGTGHFYTT...
    data/prot-fasta/3J01.fasta:EYDPNRSANIALVLYKDGERRY...
    data/prot-fasta/3J01.fasta:ARNLHKVDVRDATGIDPVSLIA...

Usiamo ``cut`` per tagliare la colonna dei nomi dei file (che contiene ``3J00``
e ``3J01``). Come prima cosa, uniformiamo i delimitatori con ``tr``::

    grep DP data/prot-fasta/*.fasta | tr '/.' ' '

ottenendo::

    data prot-fasta 3J00 fasta:FVIDADHEHIAIKEANNLGIPV...
    data prot-fasta 3J00 fasta:PRRRVIGQRKILPDPKFGSELL...
    data prot-fasta 3J00 fasta:SMQDPIADMLTRIRNGQAANKA...
    data prot-fasta 3J01 fasta:AKGIREKIKLVSSAGTGHFYTT...
    data prot-fasta 3J01 fasta:EYDPNRSANIALVLYKDGERRY...
    data prot-fasta 3J01 fasta:ARNLHKVDVRDATGIDPVSLIA...

Ora uso ``cut`` per tenere solo la colonna giusta::

    grep DP data/prot-fasta/*.fasta | tr './' ' ' | cut -d' ' -f3

ottenendo::

    3J00
    3J00
    3J00
    3J01
    3J01
    3J01

A questo punto uso ``sort`` e ``uniq`` per rimuovere le ripetizioni::

    grep ... | tr '/.' ' ' | cut -d' ' -f3 | sort | uniq

ottenendo::

    3J00
    3J01

In alterantiva posso invocare ``cut`` due volte::

    grep DP ... | cut -d'/' -f3 | cut -d'.' -f1 | ...

.. note::

    Ci sono molti comandi utilissimi che non fanno parte del corso. Per chi
    fosse interessato, una lista dei piu' importanti:

    - ``paste``, il contrario di ``cut``: concatena colonne orizzontalmente.
    - ``rev``, stampa una riga dalla fine all'inizio.
    - ``sed``, permette di rimuovere o sostituire intere stringhe -- un ``tr`` molto piu' potente
    - ``awk``, permette manipolazioni arbitrariamente complesse, ad esempio di fare aritmetica
    - ``bc``, un calcolatore
    - e molti, molti altri ancora...

|

Esercizi
--------

#. Cosa significano le seguenti regex (se valide)?
    #. ``.``
    #. ``.*``
    #. ``[09]{2}``
    #. ``[0-9]{2}``
    #. ``*``
    #. ``[``
    #. ``[[]``
    #. ``^.3``
    #. ``^.{3}``
    #. ``.{3}$``
    #. ``^>``
    #. ``AA``
    #. ``^AA$``
    #. ``aA``
    #. ``[aA]``
    #. ``word``
    #. ``w..d``
    #. ``^$``
    #. ``[}{]``
    #. ``[0-9]+``

#. Scrivere una regex che facciano *match* con:
    #. Tutti i caratteri alfanumerici, maiuscoli e minuscoli
    #. Le righe contenenti solo spazi
    #. Le righe che contengono punti esclamativi o punti interrogativi
    #. I giorni della settimana (nel modo piu' compatto possibile) Senza lettere accentate. La shell non le digerisce.
    #. Le parole di radice ``frazion``-, ad esempio: frazione, frazionario, *etc.*
    #. I multipli di 10, i multipli di 5, i numeri dispari
    #. I numeri razionali come frazione, ad esempio: p/q
    #. I numeri razionali in notazione decimale, ad esempio: 1.34, .99, 17., 3
    #. I numeri razionali in notazione scientifica, ad esempio: 1.34e10, 1.34e-10
    #. Le somme (esempio: a+b+c+d, a+b, *etc.*) di lunghezza arbitraria, dove a, b, c, ... sono numeri interi
    #. Le somme di due moltiplicazioni, cose come: (2 * 3 * 2) + (5 * 7), (6 * 2) + (4 * 3), *etc.*

#. Sequenze fasta:
    .. note::
        Nei prossimi esercizi faremo uso di questo file ``sequences.fasta``:

            https://drive.google.com/open?id=0B0wILN942aEVcXhqZFlGdTh0U3c

        Gli esercizi chiedono di contare quante sequenze nel file FASTA contengono
        (o meno) contengono un motivo data. Il motivo puo' essere naturalmente
        espresso da una (o piu') regex.

        - Quando scrivo "residuo1; residuo2; residuo3" intendo "residuo1; seguito
          nella sequenza da residuo2; seguito da residuo3". Ometto i vari "seguito da"
          per compattezza.

        - Quando scrivo "un aminoacido qualunque", intendo un carattere qualunque,
          per semplicita'.

        Per contare quante sequenze, si consiglia l'uso di ``wc`` in pipe con
        ``grep``.

    #. Calcolare quante sequenze contengono i seguenti motivi:

       - Una fenilalanina (F); due aminoacidi arbitrari; un'altra fenilalanina.
         Il motivo deve apparire alla fine della sequenza.

       - Una arginina (R); una fenilalanina; un aminoacido che non e' una prolina
         (P); una isoleucina (I) oppure una valina (V).

       - Calcolare inoltre quante sequenze includono almeno uno dei due motivi.

    #. Calcolare quante sequenze contengono i seguenti motivi:

       - Tre tirosine (Y); al piu' tre amino acidi qualunque; una istidina (H).

       - Un aminoacido non standard o un residuo sconosciuto X.

       - Ci sono sequenze che soddisfano entrambe le condizioni?

       .. note::
          Gli aminoacidi standard sono: A R N D C E Q G H I L K M F P S T W Y V.

    #. Calcolare quante sequenze contengono i seguenti motivi:

       - Un arginina (R); una lisina (K). Il motivo non deve apparire all'inizio
         della sequenza.

       - Due arginine seguite da un amino acido che non sia ne' una arginina, ne'
         una lisina.

       - Nessuno dei due motivi precedenti.

    #. Clacolare quante sequenze contengono i seguenti motivi:

       - Una fenilalanina (F); un aminoacido qualunque; una fenilalanina o una
         tirosina (Y); una prolina (P).

       - Una prolina; una treonina (T) o una serina (S); una alanina (A); un'altra
         prolina. Il motivo non deve apparire ne' all'inizio, ne' alla fine della
         sequenza.

       - Il primo motivo seguito dal secondo, oppure il secondo seguito dal primo.
