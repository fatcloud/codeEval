__author__ = 'fatcloud'


def bubble(test, num):
    num = min(len(test), num)
    for i in range(num):
        for j in range(len(test) - i - 1):
            if test[j] > test[j + 1]:
                tmp = test[j+1]
                test[j + 1] = test[j]
                test[j] = tmp


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    num = int(test[-1])
    test = [int(t) for t in test[0:-2]]
    bubble(test, num)
    print " ".join([str(n) for n in test])

test_cases.close()