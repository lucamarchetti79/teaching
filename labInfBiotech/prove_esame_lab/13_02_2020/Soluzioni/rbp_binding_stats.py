
def load_data(filename):
	f = open(filename)
	prots = {}
	for row in f:
		name = row[1:].strip()
		seq = f.readline().strip()
		bind = f.readline().strip()
		prots[name] = (seq,bind)
	f.close()
	return prots

def longest_binding(seq, bind):
	longest = ""
	i = bind.find("+")
	while i != -1:
		j = bind.find("-", i)
		if j == -1:
			j = len(seq)
		if j-i > len(longest):
			longest = seq[i:j]
		i = bind.find("+", j)
	return longest

def longest_bindings(prots):
	prot_longest = {}
	for prot in prots:
		longest = longest_binding(prots[prot][0],prots[prot][1])
		prot_longest[prot] = longest
	return prot_longest


def print_longest(prot_longest):

	l = [(len(bind),prot,bind) for prot,bind in prot_longest.items()]
	l.sort(reverse=True)
	print()
	print("\n".join(["%s\t%s" %(bind,prot) for length,bind,prot in l]))


filename = input("inserire nome file: ")
prots = load_data(filename)
print_longest(longest_bindings(prots))

