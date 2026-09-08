==========================
Shell: Parte 1 (Soluzioni)
==========================

#. Stampa a schermo prima ls lista dei contenuti della directory ``data/prot-fasta``,
   poi quelli della directory ``data/prot-pdb``. Quindi e' identico a lanciare::

    ls data/prot-fasta
    ls data/prot-pdb

   separatamente.
#. Stampa il nome del file. Con ``-l``, stampa anche informazioni aggiuntive (proprietario, permessi, *etc.*)
#. Stampa i nomi di tutti i file, ed i contenuti di tutte le directory.
#. Soluzioni:
    #. Il primo non fa niente, il secondo ci sposta nella directory che contiene la directory in cui ci troviamo.
    #. Il primo funziona, il secondo no -- manca uno spazio.
    #. Nessuna.
    #. Il primo stampa la lista dei contenuti della directory corrente. Il secondo
       invece subisce una wildcard expansion: ``*`` viene sostituito con la lista
       di tutti i file nella directory corrente. Quindi ``ls *`` stampa la lista
       dei file nella directory corrente, piu' i contenuti di tutte le directory.
    #. Nessuna.
    #. Il primo funziona, il secondo no -- ``- l`` ha uno spazio di troppo, non e' un'opzione.
#. Si'. Nella wildcard expansion ``../*`` c'e' anche la directory corrente, ``.``.
#. Nessuna.
#. ``ls -l data/empty1`` mostra chiaramente che il file non e' vuoto, mentre ``ls -l data/empty2`` mostra che lo e'.
#. Soluzioni:
    #. Da' errore. Creare directory innestate richiede l'opzione ``-p``.
    #. Da' errore. Rimuovere una directory (in questo caso ``muu/bee/grr``) richiede l'opzione ``-r``.
    #. Funziona. Crea le directory innestate ``muu/bee/grr``, poi cancella ``muu/bee`` e la directory contenuta in essa, ``muu/bee/grr``.
    #. Da' errore. La directory ``muu`` esiste gia' prima della seconda invocazione a ``mkdir``.
    #. Funziona. Crea la directory ``muu``, poi prova a crearla di nuovo. ``mkdir`` non da' errore perche' con ``-p`` gli chiediamo di ignorare il fatto che ``muu`` esiste gia'.
    #. No.
#. ``ls data/deep0; ls data/deep1; ... ;ls data/deep4``, oppure ``ls data/deep*``.
#. ``ls -R data/deep*``.
