def SymbolArray(Genome, symbol):
   array = {}
   n = len(Genome)
   ExtendedGenome = Genome + Genome[0:n//2]
   for i in range(n):
       array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
   return array


# Reproduce the PatternCount function here.
def PatternCount(Text, Pattern):
   count = 0
   for i in range (len(Text) - len(Pattern) +1):
       if Text[i:i+len(Pattern)] == Pattern:
           count +=1
   return count


print(SymbolArray('AAAAGGGG', 'A'))
