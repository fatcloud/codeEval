import sys
test_cases = open(sys.argv[1], 'r')

def divide(num,divider):
    #print num, divider
    #a = raw_input("press enter to proceed")
    if num < divider:
        return 0, num
    elif num == divider:
        return 1, 0
    else:
        i = 1
        while (divider << i) <= num:
            i = i + 1
        i = i - 1
        
        d, r = divide(num - (divider << i), divider)
        return d + (1 << i), r
        

for test in test_cases:
    target, tool = test.strip().split(',')
    target, tool = int(target), int(tool)
    t, r = divide(target, tool)
    if r is 0:
        print t * tool
    else:
        print (t + 1) * tool
test_cases.close()