
def load_scores(filename):
	f = open(filename)
	all_scores = []
	f.readline()
	for row in f:
		data = row.split()
		all_scores.append((data[0],[int(i) for i in data[1:] if i != 'NC']))
	f.close()
	return all_scores

def compute_majority_score(scores):
	counts = {}
	for score in scores:
		if not score in counts:
			counts[score] = 1
		else:			
			counts[score] += 1

	max_score=-1
	max_count=0
	for (score,count) in counts.items():
		if count > max_count:
			max_score = score
			max_count = count

	return max_score

def compute_majority_counts(all_scores):
	majority_counts = {}
	for (video,scores) in all_scores:
		majority_score = compute_majority_score(scores)		
		if not majority_score in majority_counts:
			majority_counts[majority_score] = 1
		else:	
			majority_counts[majority_score] += 1
	return majority_counts

def print_majority_counts(majority_counts):
	score_list = [(count,score) for (score,count) in majority_counts.items()]
	score_list.sort(reverse=True)
	print("Majority score counts")
	print("\t".join(["%d (%d)" %(score,count) for (count,score) in score_list]))


filename = input("Inserire nome file: ")
all_scores = load_scores(filename)
majority_counts = compute_majority_counts(all_scores)
print_majority_counts(majority_counts)
