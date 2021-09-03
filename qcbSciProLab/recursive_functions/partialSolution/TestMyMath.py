import MyMath # this imports the module with all the recursive functions

# main program to test the recursive implementations

# variables used during the computations
x = 3
y = 5
u = 1
n = 0
bigN = 12153
v = [1, 0, -3, 4, 10] # array with 5 elements...

print("Factorial of", y, "is:", MyMath.factorialIt(y), "(iterative implementation)")
print("Factorial of", y, "is:", MyMath.factorialRec(y), "(recursive implementation)\n")

print(x, "+", y, "=", MyMath.RecursiveSum(x,y))
print(x, "+", -y, "=", MyMath.RecursiveSum(x,-y))

print(x, "-", y, "=", MyMath.RecursiveDiff(x,y))
print(x, "-", -y, "=", MyMath.RecursiveDiff(x,-y))

print(x, "*", y, "=", MyMath.RecursiveProd(x,y))
print(x, "*", -y, "=", MyMath.RecursiveProd(x,-y))

print(x, "^", y, "=", MyMath.RecursivePower(x,y))
print(x, "^", -y, "=", MyMath.RecursivePower(x,-y))
print(x, "^", u, "=", MyMath.RecursivePower(x,u))
print(x, "^", n, "=", MyMath.RecursivePower(x,n))

print("\nMin of", v, "=", MyMath.RecursiveMin(v))
print("Max of", v, "=", MyMath.RecursiveMax(v))

print("\nThe highest digit of", bigN, "is:", MyMath.RecursiveMaxDigit(bigN))

print('\nNumber of "1" in', bigN, ":", MyMath.RecursiveCountDigit(1,bigN))
print('Number of "3" in', bigN, ":", MyMath.RecursiveCountDigit(3,bigN))
print('Number of "7" in', bigN, ":", MyMath.RecursiveCountDigit(7,bigN))

print("\nThe sum of the elements of", v, "is", MyMath.RecursiveArraySum(v))

