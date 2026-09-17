===================
Lezione 1 - Soluzioni
===================

Esercizi
--------

#. Create una cartella chiamata "CIBIO"
#. All'interno della cartella "CIBIO" create una cartella "INF" e una cartella "SPORT"
#. Create una cartella "MOLECOLE" dentro la cartella "INF"
#. Rinominate la cartella "SPORT" in "BIOLOGIA"
#. Spostate la cartella "MOLECOLE" nella cartella "BIOLOGIA"

Soluzioni
--------

#. Create una cartella chiamata "CIBIO"::

    mkdir CIBIO

#. All'interno della cartella "CIBIO" create una cartella "INF" e una cartella "SPORT"::

    cd CIBIO
    mkdir INF
    mkdir SPORT
    
#. Create una cartella "MOLECOLE" dentro la cartella "INF"::

    cd INF
    mkdir MOLECOLE
    
#. Rinominate la cartella "SPORT" in "BIOLOGIA"::

    cd ..
    mv SPORT BIOLOGIA
    
#. Spostate la cartella "MOLECOLE" nella cartella "BIOLOGIA"::

    mv INF/MOLECOLE/ BIOLOGIA/
    