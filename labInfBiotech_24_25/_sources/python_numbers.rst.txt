==============
Lezione 3.2 - Python: Numeri
==============

Numeri: Tipi Fondamentali
-------------------------

Ci sono tre **tipi** numerici fondamentali:

=========== =================================================================
Tipo        Significato
=========== =================================================================
``int``     Rappresenta numeri interi (!)
``float``   Rappresenta numeri razionali a virgola mobile (*float* ing-point)
``bool``    Rappresenta condizioni, puo' essere ``True`` o ``False``
=========== =================================================================

|

.. note::
    I razionali ``float`` hanno precisione limitata: la maggior parte dei
    razionali puo' essere rappresentata solo *approssimatamente* con un
    ``float``.

    Ai fini di questo corso, i dettagli *non* sono importanti.

|

**Esempio**. Creo tre variabili, una per tipo, poi le stampo a schermo con
``print``::

    n = 10
    x = 3.14
    cond = False

    # Stampo le tre variabili
    print(n, x, cond)

    # Idem, inframezzando testo
    print("n =", n, "x =", x, "e la condizione cond vale", cond)

Questa sintassi di ``print`` vale per tutti i tipi di variabili, non solo
quelli numerici.

|

Numeri: Aritmetica
------------------

Tutti i tipi numerici mettono a disposizione le stesse **operazioni aritmetiche**:

=========== ================================
Operazione  Significato
=========== ================================
``a + b``   somma
``a - b``   differenza
``a * b``   prodotto
``a / b``   divisione
``a // b``  divisione intera
``a % b``   resto della divisione (o modulo)
``a ** b``  elevamento a potenza
=========== ================================

|

Il tipo del risultato di ``n operazione m`` e' *automaticamente* il tipo
piu' "complesso" tra i tipi di ``n`` e ``m`` -- per questo si parla di
**conversione automatica**.

La scala di complessita' dei tipi numerici e'::

    bool < int < float

**Esempio**. Ad esempio, se sommo un ``int`` ed un ``float``, otterro' un
``float``::

    risultato = 1.2 + 1             # float + int
    print(risultato)                # 2.2
    print(type(risultato))          # float

Questo perche' e' necessario un ``float`` per rappresentare il valore ``1.2``:
un ``int`` non basterebbe!

.. warning::
    Per evitare errori, e' necessario scegliere il tipo delle variabili in
    modo che il *tipo* del risultato sia sufficientemente "complesso" da
    riuscire a rappresentarne il *valore*.

.. warning::
    State attenti che, come anticipato prima, la accuratezza della matematica fornita da Python
    non e' perfetta. Per questo motivo a volte possono capitare dei risultati inaspettati:
    
    i.	Errore di arrotondamento: 1.1 + 2.2 = 3.3000000000000003
    ii.	Errore di cancellazione: 0.1 + 0.1 + 0.1 - 0.3 = 5.551115123125783e-17

|

Numeri: Confronti
-----------------

Tutti i tipi numerici (e in generale tutto i tipi Python che vedremo durante
il corso) supportano le operazioni di **comparazione**:

=========== =======================================
Operazione  Significato
=========== =======================================
``a == b``  uguale
``a != b``  diverso
``a < b``   minore
``a <= b``  minore o uguale
``a > b``   maggiore
``a >= b``  maggiore o uguale
=========== =======================================

Il risultato di un'espressione di confronto e' sempre un ``bool``: vale
``True`` se la condizione e' soddisfatta, e ``False`` altrimenti.

|

**Esempio**. Aritmetica e confronti possono essere combinati per verificare
condizioni "complesse", come questa::

    na, nc, ng, nt = 2, 6, 50, 4

    risultato = (na + nt) > (nc + ng)
    print(risultato)
    print(type(risultato))

|

I valori Booleani ``bool`` (es. i risultati delle operazioni di confronto)
possono essere combinati attraverso le operazioni logiche:

=========== ==================================================================
Operazione  Significato
=========== ==================================================================
``a and b`` congiunzione: ``True`` se e solo se ``a`` e ``b`` sono ``True``
``a or b``  disgiunzione: ``True`` se almeno una tra ``a`` e ``b`` e' ``True``
``not a``   negazione: ``True`` se ``a`` e' ``False`` e viceversa
=========== ==================================================================

Qui sia ``a`` che ``b`` sono dei ``bool``.

.. warning::
    In generale, fare aritmetica (es. somme) con valori Booleani e costruire
    espressioni logiche con valori interi o razionali e' sconsigliato.

    In questi casi, Python si comporta in modo (deterministico e spiegabile,
    ma decisamente) bizzarro.

|

**Esempio**. ``x > 12`` e ``x < 34`` danno come risultato dei ``bool``, quindi
le posso combinare per ottenere::

    #     int          int
    #      |            |
    print((x > 12) and (x < 34))
    #     \______/     \______/
    #       bool         bool
    #     \___________________/
    #             bool

oppure::

    #          int          int
    #           |            |
    print((not (x > 12)) or (x < 34))
    #          \______/
    #            bool
    #     \____________/    \______/
    #          bool           bool
    #     \________________________/
    #                bool

|

Esempi
------

**Esempio**. Calcolo gli zeri dell'equazione quadratica :math:`x^2 - 1 = 0`::

    a, b, c = 1.0, 0.0, -1.0

    delta = b**2 - 4*a*c

    zero1 = (-b + delta**0.5) / (2 * a)
    zero2 = (-b - delta**0.5) / (2 * a)

    print(zero1, zero2)

Qui uso ``x**0.5`` per calcolare la radice quadrata: :math:`\sqrt{x} = x^\frac{1}{2}`.

|

**Esempio**. Voglio calcolare il `GC-content <https://en.wikipedia.org/wiki/GC-content>`_
di un gene. So che il gene:

- E' lungo 1521 basi.
- Contiene 316 citosine.
- Contiene 235 guanine.

Simbolicamente, il GC-content e' definito come :math:`(g + c) / n`. Per
calcolarlo posso scrivere::

    n, c, g = 1521, 316, 235

    gc_content = (c + g) / n
    print(gc_content)

..    
   pero' il risultato e' ``0``! Perche'?

   Il problema e' che la proporzione, che vale circa ``0.362``, non puo' essere
   espressa come intero: serve un razionale. Pero' visto che sia ``n`` che ``m``
   sono di tipo intero, anche ``gc_content = n / m`` lo sara'::
     
     print type(gc_content)
     
     Ne segue che ``0.362`` viene approssimato dall'intero piu' vicino: ``0``.
     *Oops*!
     
     Per ovviare al problema, e' sufficiente fare in modo che ``gc_content`` sia un
     ``float``. Posso farlo in due modi:
     
     - Modificando il tipo di ``n``, ``m`` o ``g`` fin dall'inizio::
	 
	 n, c, g = 1521.0, 316.0, 235.0

	 gc_content = (c + g) / n
	 print gc_content

	 - Usando esplicitamente una conversione a ``float``::

	     n, c, g = 1521, 316, 235

	     gc_content = float(c + g) / float(n)
	     print gc_content

|

**Esempio**. Per  controllare che ``x`` (il cui valore e' "fuori dal mio
controllo", ma nell'esempio sotto fisso per convenienza) cada nell'intervallo A
:math:`= [10,50]` scrivo::

    x = 17 # ad esempio

    minimo_a, massimo_a = 10, 50

    dentro_a = (minimo_a <= x <= massimo_a)
    print(dentro_a)

oppure::

    dentro_a = ((x >= minimo_a) and (x <= massimo_a))

Assumendo che ``dentro_a``, ``dentro_b`` e ``dentro_c`` indichino che ``x`` e'
nell'intervallo A, B o C, rispettivamente, posso comporre condizioni piu'
complesse::

    # x e' in almeno uno dei tre intervalli
    dentro_almeno_uno = dentro_a or dentro_b or dentro_c

    # x e' sia in A e B, ma non in C
    dentro_a_e_b_ma_non_c = dentro_a and dentro_b and (not dentro_c)

|

Esercizi
--------

#. Creare alcune variabili, controllando ad ogni passaggio che valore e tipo
   siano corretti (usando ``print`` e ``type``):

   #. ``a`` e ``b`` con valore ``12`` e ``23`` come interi.
   #. ``x`` e ``y`` con valore ``21`` e ``14`` come razionali.

#. Usando ``print`` (una sola volta), stampare:

   #. Tutte le variabili di cui sopra sulla stessa riga.
   #. Tutte le variabili di cui sopra, separate da ``;``, sulla stessa riga.
   #. Il testo "il prodotto di ``a`` e ``b`` e' ``a * b``", sostituendo ad
      ``a``, ``b`` e ``a * b`` i valori delle variabili.

#. Determinare valore e tipo di:

   #. Il prodotto di ``a`` e ``b``.
   #. Il quoziente di ``x`` e ``y``.
   #. Il quoziente intero di ``a`` e ``b``.
   #. Il quoziente intero di ``x`` e ``y``.
   #. Il prodotto di ``b`` e ``y``.
   #. ``2`` elevato a ``0``.
   #. ``2`` elevato a ``1.2``.
   #. ``2`` elevato a ``-2``.
   #. La radice quadrata di ``4``.
   #. La radice quadrata di ``2``.

#. Che differenza c'e' tra:

   #. ``10 / 12``
   #. ``10 / 12.0``
   #. ``10 // 12``
   #. ``10 // 12.0``

#. Che differenza c'e' tra:

   #. ``10 % 3``
   #. ``10 % 3.0``

#. Usando ``pi = 3.141592`` e dato ``r = 2.5``, calcolare:

   #. La circonferenza di raggio ``r``: :math:`2 \pi r`.
   #. L'area di un cerchio di raggio ``r``: :math:`\pi r^2`.
   #. Il volume di una sfera di raggio ``r``: :math:`\frac{4}{3} \pi r^3`.

#. Creare due variabili ``a = 100`` e ``b = True``. Usando un numero opportuno
   di variabili ausiliarie (chiamatele come volete!), fate in modo che il
   valore di ``a`` finisca in ``b`` e che quello di ``b`` finisca in ``a``.

   (Scrivere ``a = True`` e ``b = 100`` non vale!)

   Si puo' fare con una sola variabile ausiliaria?

#. Sullo stesso strand di DNA si trovano due geni. Il primo include i
   nucelotidi dalla posizione 10 alla posizione 20, il secondo quelli dalla
   posizione 30 alla posizione 40. Scriviamo queste informazioni cosi'::

    gene1_inizio, gene1_fine = 10, 20
    gene2_inizio, gene2_fine = 30, 40

   Data una variabile ``pos`` che rappresenta una posizione arbitraria sullo
   strand, scrivere dei confronti per verificare se:

   #. ``pos`` si trova nel primo gene.
   #. ``pos`` si trova nel secondo gene.
   #. ``pos`` si trova tra l'inizio del primo gene e la fine del secondo.
   #. ``pos`` si trova tra l'inizio del primo gene e la fine del secondo, ma in nessuno dei due geni.
   #. ``pos`` si trova prima dell'inizio del primo gene o dopo la fine del secondo.
   #. ``pos`` cade in uno dei due geni.
   #. ``pos`` non dista piu' di 10 dall'inizio del primo gene.

#. Date le tre variabili Booleane ``t``, ``u``, e ``v``, scrivere delle
   espressioni che valgono ``True`` se e solo se:

   #. ``t``, ``u``, ``v`` tutte e tre vere.
   #. ``t`` e' vera oppure ``u`` e' vera, ma non entrambe.
   #. Esattamente una delle tre variabili e' falsa.
   #. Esattamente una delle tre variabili e' vera.

