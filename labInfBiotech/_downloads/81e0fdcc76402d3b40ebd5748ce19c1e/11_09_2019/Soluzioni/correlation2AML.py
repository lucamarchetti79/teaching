from numpy import corrcoef

def load_data(filename):
    f = open(filename)

    header = f.readline().strip().split(",")
    data = []

    for row in f:
        data.append(row.strip().split(","))
        
    f.close()
    return (header, data)


def extract_column(data, i):
    col = []
    for row in data:
        if row[i] == "yes":
            col.append(1)
        else:
            col.append(0)
    return col

def compute_correlations(header, data):

    label = extract_column(data, -1)
    correlations = []

    for i in range(len(header)-1):
        name = header[i]
        column = extract_column(data, i)
        corr = corrcoef(label, column)[0,1]
        correlations.append((corr, name))

    return correlations

def print_correlations(correlations):

    correlations.sort(reverse=True)
    print("gene\tcorrcoef")
    for (corr, name) in correlations:
        print("%s\t%.2f" %(name,corr))

filename=input("Inserire nome file: ")
(header, data) = load_data(filename)
correlations = compute_correlations(header, data)
print_correlations(correlations)
