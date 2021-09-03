import math

def score(a,b):
    mat = {}
    mat["A"] = {"A" : 0, "C" : 4, "G" : 2, "T" : 4, "-" : 8}
    mat["C"] = {"A" : 4, "C" : 0, "G" : 4, "T" : 2, "-" : 8}
    mat["G"] = {"A" : 2, "C" : 4, "G" : 0, "T" : 4, "-" : 8}
    mat["T"] = {"A" : 4, "C" : 2, "G" : 4, "T" : 0, "-" : 8}
    mat["-"] = {"A" : 8, "C" : 8, "G" : 8, "T" : 8, "-" : 8}
    
    return mat[a][b]
    
    
def computeMatrix(X,Y, minLen = 0):
    # + 1 is for leading "-"
    x_len = len(X) + 1
    y_len = len(Y) + 1
    #print(X)
    #print(Y)

    A = []

    #initialize first column to 0 and first row to infinite
    for i in range(x_len - minLen + 1):
        A.append([0])
    for i in range(minLen - 1):
        A.append([math.inf])
    for i in range(y_len - 1):
        A[0].append(math.inf)
    
    # compute the rest of the score matrix
    for i in range(1,x_len):
        for j in range(1,y_len):
            c1 = A[i-1][j] + score(X[i-1], "-")
            c2 = A[i][j-1] + score("-", Y[j-1])
            c3 = A[i-1][j-1] + score(X[i-1],Y[j-1])
            #print("i,j: {},{}".format(i,j))
            A[i].append(min([c1,c2,c3]))
    if minLen != 0:
        for i in range(0,minLen):
            A[-1][i] = math.inf
    return A
    
def plotMatrix(Mat, X,Y):
    X = "-" + X
    outStr = "\t-" +"\t"+ "\t".join(list(Y))

    for i in range(len(X)):
        outStr+="\n" + X[i] +"\t"+ "\t".join([str(x) for x in Mat[i]])
    print(outStr)

def getOverlap(Mat, X,Y):
    X = "-" + X
    Y = "-" + Y
    
    #1. find the rightmost minimum of the last row of Mat
    m = min(Mat[-1])
    mInd = -1
    for i in range(len(Mat[-1])-1,0,-1):
        if Mat[-1][i] == m:
            mInd = i
            break
    j = mInd
    i = len(X) -1 
 
    #2. loop back through the matrix following the minimum values
    S1 = X[i]
    S2 = Y[j]
    #need to count insertions for printing purposes
    emptyY = 0
    while i > 0 and j > 0:
        v1 = Mat[i-1][j-1] #precedence to this if equal
        v2 = Mat[i][j-1]
        v3 = Mat[i-1][j]
        
        m = min([v1,v2,v3])
        if m == v1:
            S1 = X[i-1] + S1
            S2 = Y[j-1] + S2
            i -= 1
            j -= 1
 
        else:
            if m == v2:
                S1 = "-" + S1
                S2 = Y[j-1] + S2
                j -= 1
            else:
                S1 = X[i-1] + S1
                S2 = "-" + S2
                #increase end of Y by one
                emptyY += 1
                i -= 1
                
    #if some parts of the string are left...
    #this should only be for X
    if i > 0:
        S1 = X[0:i+1] + S1
    
    if j > 0:
        S2 = Y[0:j+1] + S2
    
    #add the end to S2:
    S2 = S2 + Y[mInd+1:]
        
    #returns the two strings 
    #and the start and endpoint of
    #alignment on S2 (removing starting "-")
    S1=S1[1:]
    S2=S2[1:]
    return (S1,S2, j, mInd + emptyY)

def printAligns(X,Y, start, end):
    print("Overlap between {} and {}:".format(X,Y))
    outStr = X +"\n"
    S = len(X) - (end - start) 
    for i in range(S):
        outStr+= " "
    outStr +=  Y
    
    print(outStr)
    
    
X = "CTCGGCCCTAGG"
Y = "GGCTCTAGGCCC"
A = computeMatrix(X,Y,minLen = 5)
print("The overlap matrix for {} and {}:".format(X,Y))
plotMatrix(A,X,Y)
(s1,s2,s,e) = getOverlap(A,X,Y)
printAligns(s1,s2,s,e)
print("\n")

X1 = "AATATACATAC"
Y1 = "TACGTACTTA"
B = computeMatrix(X1,Y1, minLen = 4)
print("The overlap matrix for {} and {}:".format(X1,Y1))
plotMatrix(B,X1,Y1)
(s1,s2,s,e) = getOverlap(B,X1,Y1)
printAligns(s1,s2,s,e)
print("\n")

X2 = "ACACGGATT"
Y2 = "CGGTATT"
C = computeMatrix(X2,Y2, minLen = 3)
(s1,s2,s,e) = getOverlap(C,X2,Y2)
printAligns(s1,s2,s,e)
print("\n")

X3 = "GTCAGTCAATCTACTCGGAAACTATACACCG"
Y3 = "AACTATTTCCGTAACACGGATT"
D = computeMatrix(X3,Y3, minLen = 8)
(s1,s2,s,e) = getOverlap(D,X3,Y3)
printAligns(s1,s2,s,e)
print("\n")

X4 = "ATCGGTTCGGTGAAGTAA"
Y4 = "CGGTGACGTTACCATATCCAG"
E = computeMatrix(X4,Y4, minLen = 8)
(s1,s2,s,e) = getOverlap(E,X4,Y4)
printAligns(s1,s2,s,e)
