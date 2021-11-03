# Python module providing the recursive function implementations

def factorialIt(n):
    """ITERATIVE function to compute n! = n*(n-1)*(n-2)*...*1."""
    if n == 0:
        return 1
    else:
        fat = 1
        for i in range(n,1,-1):
            fat = fat*i
        return fat

def factorialRec(n):
    """RECURSIVE function to compute n! = n*(n-1)*(n-2)*...*1."""
    if n == 0:
        return 1
    else:
        return n*factorialRec(n-1)

def RecursiveSum(a,b):
    """RECURSIVE function to compute a+b."""
    if b < 0:
        return RecursiveDiff(a,-b)
    if b == 0:
        return a
    else:
        return 1 + RecursiveSum(a,b-1)

def RecursiveDiff(a,b):
    """RECURSIVE function to compute a-b."""

    raise Exception("TODO IMPLEMENT ME !")
    
def RecursiveProd(a,b):
    """RECURSIVE function to compute a-b."""
    if b < 0:
        return -RecursiveProd(a,-b)
    if b == 0:
        return 0
    else:
        #return a+RecursiveProd(a,b-1) # solution with simple recursion (fastest solution)
        #return RecursiveSum(a,RecursiveProd(a,b-1)) # double recursion, less efficient
        return RecursiveSum(RecursiveProd(a,b-1),a) # double recursion, more efficient!

def RecursivePower(a,esp):
    """RECURSIVE function to compute a^esp."""

    raise Exception("TODO IMPLEMENT ME !")

def RecursiveMin(v):
    """RECURSIVE function to compute min(v)."""
    return __RecursiveMin(v,1,v[0])

def __RecursiveMin(v,i,min):
    """RECURSIVE private function to compute min(v)."""
    
    # min stores the current min value, i stores the next element of v to check...
    if i == len(v):
        return min
    if v[i] < min:
        return __RecursiveMin(v,i+1,v[i])
    return __RecursiveMin(v,i+1,min)

def RecursiveMax(v):
    """RECURSIVE function to compute max(v)."""

    raise Exception("TODO IMPLEMENT ME !")

def RecursiveMaxDigit(n):
    """RECURSIVE function to find the highest digit of n."""

    raise Exception("TODO IMPLEMENT ME !")

def RecursiveCountDigit(c,n):
    """RECURSIVE function to compute how many times the digit c appears in n."""

    raise Exception("TODO IMPLEMENT ME !")

def RecursiveArraySum(v):
    """RECURSIVE function to sum all the elements of the array v."""

    raise Exception("TODO IMPLEMENT ME !")

