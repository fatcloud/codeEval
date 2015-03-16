__author__ = 'fatcloud'


def evaluate(item):
    rev_item = item[::-1]
    order = 0
    return sum([ord(rev_item[i]) * (123 ** i) for i in range(len(item))])


def expand(item_list):
    sorted(item_list, key=ord)
    ret = []
    for i in range(len(item_list)):
        



import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print evaluate(test)

test_cases.close()