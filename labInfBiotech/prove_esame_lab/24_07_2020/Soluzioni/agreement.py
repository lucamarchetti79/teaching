def load_data(filename):
	f = open(filename)
	f.readline()
	scores = []
	for row in f:
		data = row.split()
		scores.append([int(i) for i in data[1:]])
	f.close()
	return scores

def annotator_scores(scores, i):
	return [row[i] for row in scores]

def agreement(scores, i, j):
	counts = {}
	scores_i = annotator_scores(scores, i)
	scores_j = annotator_scores(scores, j)

	for l in range(len(scores_i)):
		key = (scores_i[l],scores_j[l])
		if key in counts:
			counts[key] += 1
		else:
			counts[key] = 1
	return counts

def print_agreement_stats(counts, i, j):
	tot_agree = 0
	tot_disagree = 0
	print("M%d\tM%d\tCount" %(i,j))
	for ((si,sj),num) in counts.items():
		print("%d\t%d\t%d" %(si,sj,num))
		if si == sj:
			tot_agree += num
		else:
			tot_disagree += num
	print("Totale accordo: %d" %tot_agree)
	print("Totale disaccordo: %d" %tot_disagree)

filename = input("Inserire nome file: ")
i = int(input("Indice primo medico: ")) 
j = int(input("Indice secondo medico: ")) 

scores = load_data(filename)
counts = agreement(scores, i, j)
print_agreement_stats(counts, i, j)