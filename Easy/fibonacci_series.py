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

fibos = {0: 0, 1: 1}

f_1 = 0
f_2 = 1
i = 2
while i <= max_test:
    f = f_1 + f_2
    if i in tests:
        fibos[i] = f
    f_1 = f_2
    f_2 = f
    i += 1


for t in tests:
    print fibos[t]


