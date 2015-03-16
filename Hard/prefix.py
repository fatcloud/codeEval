def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if test is '\n':
        continue

    # begin computation
    temp_stack = []
    items = test.split()
    while len(items) > 0:

        item = items.pop()
        # print temp_stack, items, item, not item.isalpha()
        if is_int(item):
            temp_stack.append(item)
        else:
            num1 = int(temp_stack.pop())
            num2 = int(temp_stack.pop())
            if item is '+':
                temp_stack.append(num1 + num2)
            elif item is '*':
                temp_stack.append(num1 * num2)
            elif item is '/':
                temp_stack.append(num1 / num2)

    print temp_stack[0]

test_cases.close()
