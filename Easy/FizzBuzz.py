__author__ = 'fatcloud'

import sys
from sys import stdout
f = open(sys.argv[1], 'r')

for test in f:
    test = (test.strip()).split()
    fizz, buzz, num = [int(ret) for ret in test]
    for i in range(1, num + 1):

        # print F, B, FB or number
        if i % fizz is 0 and i % buzz is 0:
            stdout.write('FB')
        elif i % fizz is 0:
            stdout.write('F')
        elif i % buzz is 0:
            stdout.write('B')
        else:
            stdout.write(str(i))

        # print a white space
        if i < num:
            stdout.write(' ')
        else:
            stdout.write('\n')


f.close()

