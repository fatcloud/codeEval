__author__ = 'fatcloud'
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test is '\n':
        continue
    test = test.strip().split()

    for i in range(len(test) - 1):
        print test.pop(),

    print test.pop()

test_cases.close()