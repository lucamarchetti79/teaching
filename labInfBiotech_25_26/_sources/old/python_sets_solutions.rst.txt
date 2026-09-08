========================
Python: Sets (Soluzioni)
========================

#. Soluzioni:

   #. Soluzione::

        set_vuoto = {}
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

	
