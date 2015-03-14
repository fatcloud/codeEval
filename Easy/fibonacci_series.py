import sys

fibos = [0, 1]


def f(n):
    n = int(n)
    if n > len(fibos) - 1:
        fibos.append(f(n - 1) + f(n - 2))
    return fibos[n]


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if test != '\n':
        print f(test)

test_cases.close()
