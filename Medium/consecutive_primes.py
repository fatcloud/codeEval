import sys
test_cases = open(sys.argv[1], 'r')
tests = [int(t.strip()) for t in list(test_cases)]
test_cases.close()



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

results = {}


def encode(*numlist):
    return ' '.join( [str(i) for i in numlist] )


def compute( leader, other ):
    
    threshold = 3

    # the ending condition
    if len(other) is 0:
        return (leader + 1) in primes
    
    
    # check if this is already computed
    if len(other) > threshold:
        try:
            return results[encode(leader,*other)]
        except KeyError:
            pass
    
    # do recursive computation
    ret = 0
    for i in range(len(other)):
        n = other[i]
        l = other[:i] + other[i+1:]
        if (n + leader) in primes:
            ret = ret + compute(n, l)
    
    # save the result if it is hard to compute
    if len(other) > threshold:
        results[encode(leader,*other)] = ret
    
    return ret


for t in tests:

    if t % 2 is 0:
        print compute(1,range(2, t + 1))
    else:
        print 0

