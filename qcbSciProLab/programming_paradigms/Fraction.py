import math

class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
    
    def getNumerator(self):
        return self.__num
    
    def getDenominator(self):
        return self.__den
    
    def __str__(self):
        out = str(self.__num) + "/" + str(self.__den)
        return out 
    
    def getEgyptianFraction(self):
        ret = []
        n = self.__num
        d = self.__den
        if n == 1:
            return [self]
        
        while n != 0:
            f = math.ceil(d/n)
            ret.append(f)
            n = n*f - d 
            d = d*f
            
        return [Fraction(1,x) for x in ret]
            
        
F = Fraction(7,12)
ef = F.getEgyptianFraction()
outStr = str(F) + " = " + str(ef[0])
for i in range(1,len(ef)):
    outStr += " + " + str(ef[i])
print(outStr)

print("")
F = Fraction(1232,450)
ef = F.getEgyptianFraction()
outStr = str(F) + " = " + str(ef[0])
for i in range(1,len(ef)):
    outStr += " + " + str(ef[i])
print(outStr)

print("")
F = Fraction(186,61)
ef = F.getEgyptianFraction()
outStr = str(F) + " = " + str(ef[0])
for i in range(1,len(ef)):
    outStr += " + " + str(ef[i])
print(outStr)
