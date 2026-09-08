==========================
Shell: Parte 2 (Soluzioni)
==========================

#. Soluzioni:
    #. ``mkdir informatica``. Verifico che sia vuota con ``ls informatica``.
    #. ``mkdir esercizi``.
    #. ``cd informatica``. Verifico con ``pwd``.
    #. ``mv ../esercizi ../esercizi-shell``. Verifico con ``ls ..``.
    #. ``cp -r ../esercizi-shell .``. Verifico con ``ls``.
    #. ``rm -r ../esercizi-shell``.
    #. ``echo 'esercitazioni di informatica' > esercizi-shell/README``. Verifico con ``cat esercizi-shell/README``.
    #. ``echo 'Parte 1, introduzione alla shell' >> esercizi-shell/README``. Idem.
    #. ``cd``.
#. Soluzioni:
    #. ``mkdir original``, seguito da ``echo '*' > original/a``.
    #. Per comodita', entro in ``temp`` con ``cd temp``. Dopo ogni passaggio, faccio::

            cd ..
            rm -r temp
            cp -r original temp
            cd temp

       Soluzioni:

        #. ``cp a b; cp a c``. Verifico con ``ls; cat b; cat c``.
        #. ``echo a`` stampa la stringa "``a``" a schermo; ``ls a`` stampa il
           nome del file ``a`` (che e' ``a``...); ``cat a`` stampa il contenuto
           del file ``a``, cioe' le due righe che abbiamo scritto prima.
        #. Nessuna. ``mv a b`` rinomina ``a`` in ``b``. ``cp a b; rm aa`` prima
           fa prima una copia di ``a`` chiamata ``b``, poi rimuove ``a``.
        #. Nel primo caso mi ritrovo con tre copie di ``a``, nel second con un
           solo file: ``c``.
        #. ``mv a z`` rinomina ``a`` in ``z``; quindi ``z`` e' un file.
           ``mkdir z; mv a z`` prima crea una directory ``z``, poi ci mette dentro ``a``.
        #. ``echo a z`` stampa a schermo la stringa ``a z``.
           ``mkdir z; echo a z`` fa la stessa cosa, ma crea anche una directory di nome ``z``.
        #. Cosi'::

            echo qualcosa > a1
            ...
            echo qualcosa > a10
            rm a*

#. Soluzioni:
    #. Da' errore. ``-e`` non e' un'opzione valida per ``ls``.
    #. Si pianta. ``cat`` si aspetta un file di input: noi non glielo diamo,
       e lui resta in attesa. Dato che ``cat`` e' fermo, il resto della pipeline
       resta in attesa. Siamo costretti ad uccidere la pipeline con ``Control-c``.
    #. Da' errore. ``.`` e' una directory, ``cat`` si aspetta un file.
    #. Stampa la stringa "``cat``" a schermo. (Non esegue il comando ``cat``...)
    #. Stampa il contenuto del file ``a`` (se esiste), ma visto che lo ``stdout``
       e' rediretto, mette l'output di ``cat`` nel file ``b``. E' equivalente
       a ``cp a b``.
    #. Da' errore: ``<<`` non e' un operatore di redirezione valido.
    #. Non ha senso: stiamo cercando di redirigere lo ``stdout`` di ``head`` sia
       verso il file ``a`` che, con la pipe ``|``, verso lo ``stdin`` di ``tail``.
    #. ``ls`` mette in ``a`` la lista dei file nella directory corrente; fin
       qui tutto ok. Mai ``rm`` non supporta la redirezione, si aspetta invece
       il nome di un file! Quindi finisce per dare errore.
    #. Scrive il testo "``KrustyIlKlown``" nel file ``a``.
    #. Il primo ``tac`` legge ``FILE1`` lo stampa a schermo rovesciato; pero'
       la pipe ne redirige lo ``stdout`` al secondo ``tac``: l'effetto
       complessivo e' che ``FILE1`` viene stampato a schermo nel verso giusto.
       Infine, l'ultimo ``>`` mette il contenuto di ``FILE1`` in ``FILE2``.
       Il tutto e' equivalente a ``cp FILE1 FILE2``.
#. Soluzioni:
    #. Stampa le *prime* dieci righe di ``a`` in ``b``.
    #. Idem.
    #. Idem.
    #. Stampa le *ultime* dieci righe di ``a`` in ``b``.
#. Soluzioni:
    #. Stampa ``a`` sottosopra, prende le prime venticinque righe, le mette in ``b``. Quindi ``b`` contiene le ultime venticinque righe di ``a`` sottosopra.
    #. Stampa ``a``, prende le ultime venticinque righe, le mette in ``b``. Quindi ``b`` contiene ultime venticinque righe di ``a`` ma *non* sottosopra.
#. Soluzioni:
    #. Stampa le prime dieci righe di ``a``.
    #. Mette le prime dieci righe di ``a`` nel file ``temp``, poi stampa le ultime dieci righe di ``a``.
#. Soluzioni:
    #. Stampa ``file`` e ne tiene solo le prime dieci righe.
    #. Si pianta. Come sopra, ``cat`` si aspetta un file in input; non non glielo diamo
       e lui resta in attesa.
#. Soluzioni:
    #. Stampo le prime n del file, di queste tengo solo l'ultima: ``head -n n file | tail -n 1``.
    #. Assumiamo che tot=n+m. Stampo le ultime tot righe del file, di queste tengo solo le ultime m: ``head -n tot file | tail -n m``.
#. Soluzioni:
    #. Eseguo::

        head -n 50 data/a | tail -n 25 > data/b
        head -n 25 data/a >> data/b
        tail -n 50 data/a >> data/b

    #. Come sopra, ma il secondo comando diventa::

        head -n 25 data/a | tac >> data/b
