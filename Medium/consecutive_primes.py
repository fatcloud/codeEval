import sys
test_cases = open(sys.argv[1], 'r')
tests = [int(t.strip()) for t in list(test_cases)]
test_cases.close()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

results = {}


def compute( leader, other ):

    # the ending condition
    if len(other) is 0:
        return (leader + 1) in primes
    
    
    # check if this is already computed
    try:
        return results[str([leader] + other)]
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
    results[str([leader] + other)] = ret
    
    return ret


for t in tests:

    if t % 2 is 0:
        print compute(1,range(2, t + 1))
    else:
        print 0
