from random import randrange

# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    count['A'] = []
    count['T'] = []
    count['C'] = []
    count['G'] = []
    rowCnt = len(Motifs)
    colCnt = len(Motifs[0])
    for i in range(colCnt):
        _aCnt = 0
        _tCnt = 0
        _cCnt = 0
        _gCnt = 0 
        for r in range(rowCnt):
            c = Motifs[r][i]
            if (c == 'A'):
                _aCnt += 1
            if (c == 'T'):
                _tCnt += 1
            if (c == 'C'):
                _cCnt += 1
            if (c == 'G'):
                _gCnt += 1
        count['A'].append(_aCnt)
        count['T'].append(_tCnt)
        count['C'].append(_cCnt)
        count['G'].append(_gCnt)
        
    return count
# Insert your Count(Motifs) function here from the last Code Challenge.

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    MotifCnt = Count(Motifs)
    for symbol in MotifCnt:
        profile[symbol] = []
        for s in MotifCnt[symbol]:
            profile[symbol].append(s/t)
    return profile

# Insert your Count(Motifs) function here.

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    MotifCnt = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if MotifCnt[symbol][j] > m:
                m = MotifCnt[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    result = 0
    consensus = Consensus(Motifs)
    rowCnt = len(Motifs)
    colCnt = len(Motifs[0])
    for i in range(colCnt):
        for r in range(rowCnt):
            c = Motifs[r][i]
            if (c != consensus[i]):
                result += 1
    return result

def prepareRand(rows:int, cols: int) :
    result = []
    for r in range(rows):
        cl = ''
        for c in range(cols):
            cl += 'ACTG'[randrange(4)] 
        result.append(cl)
    return result

def prepareSample():
    result = []
    result.append('AACGTA')
    result.append('CCCGTT')
    result.append('CACCTT')
    result.append('GGATTA')
    result.append('TTCCGG')
    return result

m = prepareSample()
print(m)

print(Count( m ) )
print(Profile(m))
print(Consensus(m))
print(Score(m))
