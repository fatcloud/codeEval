import sys
test_cases = open(sys.argv[1], 'r')

tests = []
max_test = 0
for test in test_cases:
    if test != '\n':
        tmp = int(test)
        if tmp > max_test:
            max_test = tmp
        tests.append(tmp)

test_cases.close()

fibos = [0, 1]

for i in range(2, max_test + 1):
    fibos.append(fibos[i-1] + fibos[i - 2])

for t in tests:
    print fibos[t]


