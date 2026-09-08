==============
Lezione 2.1 - Shell: Avanzate
==============

Cosa faremo oggi?
-----------

======================  ======================================================= ===================
comando                 cosa fa                                                 sintassi di esempio
======================  ======================================================= ===================
``nano``                Editor di testo da terminale                            ``> nano file.txt```
``gnome-text-editor``   Editor di testo in modalita' grafica                    ``> gnome-text-editor file.txt &``
``cat``                 Visualizza il contenuto di un file                      ``> cat file.txt```
Wildcards               Codici per indicare piu' testi in un colpo solo         ``> comando *``
======================  ======================================================= ===================

.. vecchia immagine
   .. image:: figures/lez2.png
       :scale: 70 %
       :alt: Riassunto lezione 1.
       :align: center


Creare un File nel terminale
------------------------

Per poter creare un file, è necessario disporre di un editor di testo, nel nostro caso usermo
``nano`` un editor utilizzabile da terminale

**CREARE/APRIRE UN FILE**::

    nano nome_del_file.txt

Per poter salvare le mofiche appena effettuate premere ``Ctrl + S``, mentre per chiudere l'editor 
premere ``Ctrl + X``

**PROVATE VOI**

Create un file.txt e scriveteci un paio di righe::

    nano file.txt
    Ciao mi chiamo bla bla bla ...
    Ctrl + S
    Ctrl + X

|

Creare un File nel sistema grafico
------------------------

Durante il corso, noi utilizzeremo un editor di testo per creare i nostri programmi. In alternativa
alle versioni da terminale, potremo utilizzare un semplice programma chiamato ``gnome-text-editor``::

    gnome-text-editor nome_del_file.txt &

La ``&`` serve a "liberare" il terminale prima della chiusura della finestra dell'editor. 
Se ve la dimenticate, niente paura! Il terminale tornera' disponibile appena chiudete il programma.

**NOTA BENE**

Il programma ``gnome-text-editor`` in alcuni sistemi linux potrebbe chiamarsi ``gedit``. Se sul vostro
computer il comando non funziona, provate con questo nome per lanciare l'applicativo.

**NOTA BENE**

Per configurare al meglio l'editor, si consiglia di entrare nelle impostazioni (pulsante con l'ingranaggio) ed inserire queste impostazioni:

- ridurre il numero di spazi per il carattere TAB a 4 spazi (in genere sono 8)
- inserire spazi invece che tabulazioni
- abilitare l'indentazione automatica
- disabilitare l'andata a capo automatica
- abilitare l'opzione per inserire il numero di riga.

|

Comando cat
------------------

Il comando ``cat`` permette di visualizzare file testuali::

    cat file.txt

**PROVATE VOI**

Ora provate a leggere il file che avete appena scritto.

Il comando ``cat`` stampa a video il contenuto di un file, ma questo puo essere reindirizato su un altra sorgente
ad esempio un file::

    cat prova.txt > nuova_prova.txt

Il comando permette anche di concatenare piu file in un unico file::

    nano prova1.txt
    nano prova2.txt
    cat prova1.txt prova2.txt > concat_prova_1_2.txt

Ora il file concat_prova_1_2.txt contiene la concatenazione dei file prova1 e prova2.

Un altro modo di concatenare l'output si ottiene col doppio maggiore::

    nano prova1.txt
    nano prova2.txt
    cat prova1.txt > concat_prova_1_2.txt
    cat prova2.txt >> concat_prova_1_2.txt

Ora il file concat_prova_1_2.txt contiene nuovamente la concatenazione dei file prova1 e prova2.


|

Wildcards
------------------

La shell esegue quella che si chiama *wildcard expansion*: ogni volta che
incontra l'asterisco ``*`` lo sostituisce con la lista dei file/directory che
"fanno *match*".

**ESEMPIO**. Se eseguo::

    ls *

la shell sostituisce ``*`` con la lista di tutti i file e le directory nella
directory attuale (perche' tutti fanno *match* con ``*``). Invece::

    ls informatica/*

sostituisce ``*`` con la lista dei file in ``informatica``.

Supponendo che in ``informatica`` ci siano solo tre file, chiamati ``test1``,
``test2`` e ``results``, il comando precedente sarebbe equivalente a::

    ls informatica/test1 informatica/test2 informatica/results

Se avessi eseguito::

    ls informatica/test*

la wildcard ``test*`` avrebbe fatto *match* solo con ``test1`` e ``test2``, ed
il comando sarebbe stato equivalente a::

    ls informatica/test1 informatica/test2

Qui ``results`` non fa *match*, quindi non viene incluso.


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
delle wildcards, esegue la *wildcard expansion*: sostituisce all'argomento
incriminato tutti i file che fanno *match* con la wildcard.

.. warning::

    Le wildcards sono simili alle regex, ma non sono la stessa cosa:

    #. Le wildcards sono usate dalla shell per fare il match di **percorsi**.
    #. Le regex sono usate da ``grep`` per fare il match di **righe di testo** contenute in un file (per approfondimenti ``man grep``).
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

    le rose si trovano in montagna

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

**PROVATE VOI** create le seguenti directory e sub-directory

#. data
#. data/deep1
#. data/deep1/1
#. data/deep2
#. data/deep2/1
#. data/deep3
#. data/deep3/1
#. data/deep4
#. data/deep4/1


Stampare a schermo i contenuti della directory data::

    ls data

Per stampare i contenuti delle *directory* che stanno in data::

    ls data/*


Per stampare a schermo solo il contenuto delle directory ``deep0``, ..., ``deep4``::

    ls data/deep*

Mentre per restringere la wildcard alle directory ``deep0`` e ``deep3``::

    ls data/deep[03]

e solo per le directory ``deep0``, ..., ``deep4`` ma non ``deep2``::

    ls data/deep[!2]

|

Per approfondire
------------------------

Se volete approfondire l'uso della shell linux con tanti altri comandi e concetti avanzati,
potete trovare qui delle slide che potete usare come base per lo studio: :download:`IntroduzioneLinux.pdf <data/IntroduzioneLinux.pdf>`

|

Esercizi
--------

#. Create 3 file usando l'editor ``nano`` o ``gnome-text-editor``
#. Copiate i 3 file usando ``cp`` nel folder "prova"
#. Create un quarto file chiamato concat.txt contenente la concatenzione dei 3 file creati

