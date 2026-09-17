
from statistics import mean 

def load_regions(filename):
	f = open(filename)
	regions = []
	f.readline()

	for row in f:
		data = row.split()
		regions.append((data[0],data[2],int(data[6])))

	f.close()
	return regions

def regions_by_key(regions, key):
	diz = {}

	for region in regions:
		if not region[key] in diz:
			diz[region[key]] = [region[2]]
		else:
			diz[region[key]].append(region[2])

	return diz


def sort_by_avglen(diz):

	l = []

	for key,val in diz.items():
		avgval = mean(val)
		l.append((avgval,key))

	l.sort(reverse=True)
	return l

def print_longest(l, num):
	print("\n".join(["%s\t%.0f" %(name,avglen) for (avglen,name) in l[0:num]]))


filename = input("Inserire nome file: ")
num = int(input("Inserire numero elementi: "))
regions = load_regions(filename)
diz_gene = regions_by_key(regions, 0)
sorted_gene = sort_by_avglen(diz_gene)
print("Genes with longest conserved on average")
print_longest(sorted_gene, num)
diz_chr = regions_by_key(regions, 1)
sorted_chr = sort_by_avglen(diz_chr)
print("Chromosomes with longest conserved on average")
print_longest(sorted_chr, num)


