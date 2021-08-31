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
    if b < 0:
        return RecursiveSum(a,-b)
    if b == 0:
        return a
    else:
        return RecursiveDiff(a,b-1) - 1
    
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
    if esp < 0:
        return 1/RecursivePower(a,-esp)
    if esp == 0:
        return 1
    else:
        return RecursiveProd(a,RecursivePower(a,esp-1)) # triple recursion! Prod uses recursive sum

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
    return __RecursiveMax(v,1,v[0])

def __RecursiveMax(v,i,max):
    """RECURSIVE private function to compute max(v)."""

    # max stores the current max value, i stores the next element of v to check...
    if i == len(v):
        return max
    if v[i] > max:
        return __RecursiveMax(v,i+1,v[i])
    return __RecursiveMax(v,i+1,max)

def RecursiveMaxDigit(n):
    """RECURSIVE function to find the highest digit of n."""
    return __RecursiveMaxDigit(n,n%10)

def __RecursiveMaxDigit(n,max):
    """RECURSIVE private function to find the highest digit of n."""

    # max stores the current highest digit, n stores the remaining digits of n...
    if n < 10:
        if max > n:
            return max
        else:
            return n
    else:
        lastDigit = n%10
        firstPart = int(n/10)
        if lastDigit > max:
            return __RecursiveMaxDigit(firstPart,lastDigit)
        else:
            return __RecursiveMaxDigit(firstPart,max)

def RecursiveCountDigit(c,n):
    """RECURSIVE function to compute how many times the digit c appears in n."""
    if n < 10:
        if n == c:
            return 1
        else:
            return 0 
    else:
        lastDigit = n%10
        firstPart = int(n/10)
        if lastDigit == c:
            return 1 + RecursiveCountDigit(c,firstPart)
        else:
            return RecursiveCountDigit(c,firstPart)

def RecursiveArraySum(v):
    """RECURSIVE function to sum all the elements of the array v."""
    return __RecursiveArraySum(v,0,0)

def __RecursiveArraySum(v,i,sum):
    """RECURSIVE private function to sum all the elements of the array v."""

    # sum stores the sum of the first i array elements...
    if i == len(v):
        return sum
    return __RecursiveArraySum(v,i+1,sum+v[i])

