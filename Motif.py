from random import randrange

# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    rowCnt = 0
    colCnt = 0
    for c in Motifs[0]:
        print(c)
    return count

def prepare(rows:int, cols: int) :
    result = []
    for r in range(rows):
        cl = ''
        for c in range(cols):
            cl += 'ACTG'[randrange(4)] 
        result.append(cl)
    return result
m = prepare(5,6)
print(m)

print(Count( m ) )
    
