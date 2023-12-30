# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    arr = SkewArray(Genome)
    mn = ArrayMin(arr)
    lastPos = 0
    while(lastPos > -1):
        lastPos = FindInArray(mn, arr, lastPos)
        if(lastPos > -1):
            positions.append(lastPos)
            lastPos += 1
    return positions

def FindInArray(item, array, start):
    end = len(array)
    if (start >= end):
        return -1;
    idx = 0
    pos = -1
    for i in array[start:end]:
        if (i == item):
            pos = start + idx
            break
        idx += 1
    return pos

def ArrayMin(array):
    mn = array[0]
    for i in array:
        if (mn > i):
            mn = i
    return mn

# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    result = [0]
    result[0] = 0
    for i in range (0, len(Genome)):
        result.append(result[i])
        if Genome[i] == 'C':
            result[i+1] = result[i+1] -1
        else:
            if Genome[i] == 'G':
                result[i+1] = result[i+1] +1
    return result

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    result = 0
    for i in range(len(p)):
        #print(i, p, q)
        if (p[i] != q[i]):
            result += 1
    return result

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    pos = 0
    ln = len(Pattern)
    while ((pos + ln) <= len(Text)):
        #print(Text[pos: pos+ln])
        if ( HammingDistance(Pattern, Text[pos: pos + ln]) <= d):
            positions.append(pos)
        pos += 1

    return positions

import matplotlib.pyplot as plt
import numpy as np


def FasterSymbolArray(Genome, symbol):
   array = {}
   n = len(Genome)
   window_len = n//2
   ExtendedGenome = Genome + Genome[0:window_len]
   # take first one
   # look at the first half of Genome to compute first array value
   array[0] = PatternCount(Genome[0:window_len], symbol)

   # we took first on already so we start from 1 not 0
   for i in range(1, n):
       #compare the Molcule-Out to the Molcule-In i.e. previous to last of the Window
       #  => 4 cases 
       # 1) equal: same value goes to compare base,
       # 2) not equal & non is equal to symbol: same value goes to compare base  
       # 3) we lose i.e pervious (base-1) was our Target 'A' then subtract 1 from previous entry (base-1) 
       # 4) we win our symbol 'A' then add 1 to previous entry (base-1)
       array[i] = array[i-1]
       if ExtendedGenome[i-1] == symbol:
         array[i] = array[i-1] -1
       if ExtendedGenome[i + window_len -1] == symbol:
         array[i] = array[i-1] +1
   return array


# Reproduce the PatternCount function here.
def PatternCount(Text, Pattern):
   count = 0
   for i in range (len(Text) - len(Pattern) +1):
       if Text[i:i+len(Pattern)] == Pattern:
           count +=1
   return count

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

print(MinimumSkew('CATTCCAGTACTTCGATGATGGCGTGAAGA'))
print(HammingDistance('CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA', 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'))
print(ApproximatePatternMatching('AATCCTTTCA', 'CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA', 3))