============
Lezione 7.2 - Soluzioni
============

Esercizi
----------
#. Creare:

   #. Un set vuoto ``set_vuoto``. Controllare che sia vuoto con ``len()``.

   #. Un set ``primi10`` contenente i primi 10 numeri naturali. Controllare se contiene 10, in caso contrario, inserirlo e ricontrollare che sia presente. Rimuoverlo nuovamente.

   #. Un set ``primi10no7`` contenente i primi 10 numeri naturali, tranne 7 (partendo da ``primi10`` ma lasciandolo inalterato). Controllo che 7 sia presente in ``primi10`` e assente in ``primi10no7``.

   #. Ricreare ``primi10no7``, questa volta utilizzando una list comprehension.

#. Per ogni testo, creare l'insieme delle parole che contiene (maiuscole/minuscole non contano)::

        testo_A = "Le due ore di informatica piu' noiose della vostra vita"
        testo_B = "La vita e' come una scatola di cioccolatini"
	testo_C = "Cioccolatini come se piovesse LA La lA laaa"

   #. Contare il numero di parole diverse per ognuno dei tre testi.
      
   #. Ottenere gli insiemi delle parole in comune tra i tre testi: ``condivise_A_B``, ``condivise_A_C``, ``condivise_B_C``.

   #. Dati i set creati precedentemente, ottenere l'insieme delle parole che compaiono in *almeno* due testi, utilizzando soltanto operazioni tra set.

   #. Ottenere l'insieme delle parole che compaiono esattamente in un testo. *Hint* posso farlo utililizzando il risultato precedente?

   #. Ottenere l'insieme delle parole che compaiono ripetute nello stesso testo.
      



Soluzioni 
---------


#. Soluzioni:

   #. Soluzione::

        set_vuoto = set()
        print(set_vuoto)
        print(len(set_vuoto))                        # 0

   #. Soluzione::

        primi10 = set(range(10))
	print(10 in primi10)                         # False
	primi10.add(10)
	print(10 in primi10)                         # True
	primi10.remove(10)	

   #. Soluzione, provo cosi'::	
      
        primi10no7 = primi10
	primi10no7.remove(7)
	print(7 in primi10)                          # False
	
      Ricordo che i set sono strutture **mutabili**::
     
	primi10 = set(range(10))                     # Ricreo il set originale
        primi10no7 = set(primi10)
	primi10no7.remove(7)
	print(7 in primi10)                          # True
	print(7 in primi10no7)                       # False
	
   #. Soluzione::

        primi10no7 = set([x in range(10) if x != 7])
	print(primi10no7)                            # Controllo

#. Soluzione:

     Convertendo i testi in minuscolo::
     
       tA_lower = testo_A.lower()
       tB_lower = testo_B.lower()
       tC_lower = testo_C.lower()

     Creo gli insiemi delle parole contenute nei testi::

       parole_in_A = set(tA_lower.split())
       parole_in_B = set(tB_lower.split())
       parole_in_C = set(tC_lower.split())

    #. Conto per ogni testo il numero di parole diverse::

	 len(parole_in_A)                             # 10
	 len(parole_in_B)                             # 8
	 len(parole_in_C)                             # 6

    #. Ottengo le parole in comune utilizzando l'intersezione::

	 condivise_A_B = parole_in_A.intersection(parole_in_B)
	 condivise_A_C = parole_in_A.intersection(parole_in_C)
	 condivise_B_C = parole_in_B.intersection(parole_in_C)

       Controllo::

	 print(condivise_A_B)           # {'vita', 'di'}
	 print(condivise_A_C)           # set()
	 print(condivise_B_C)           # {'la', 'cioccolatini', 'come'}	
	

    #. Soluzione::
	 
	 almeno_in_2 = condivise_A_B.union(condivise_A_C).union(condivise_B_C)
	 print(almeno_in_2)             # {'vita', 'di', 'la', 'cioccolatini', 'come'}

    #. Creo l'insieme di tutte le parole contenute nei tre testi::

	 tutte_le_parole = parole_in_A.union(parole_in_B).union(parole_in_C)
       
       Ottengo le parole che appaiono esattamente in **UN* testo::

	 solo_in_uno = tutte_le_parole.difference(almeno_in_2)
	 print(solo_in_uno)
	 {'le', 'una', 'se', 'vostra', 'della', 'laaa', "piu'", 'ore', "e'", \
	 'piovesse', 'scatola', 'noiose', 'informatica', 'due'}


    #. Ci sono diversi modi per farlo. Una soluzione (consideriamo solo testo_A per brevita')::

	 ripetute_in_A = set([p for p in parole_in_A \
	                      if tA_lower.count(p) > 1])

	
