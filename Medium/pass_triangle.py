__author__ = 'fatcloud'

ans = []


def search(triangle, row, index):
    if ans[row][index] is None:
        ans[row][index] = triangle[row][index] +\
            max(search(triangle, row + 1, index),
                search(triangle, row + 1, index + 1))

    return ans[row][index]


import sys

test_cases = open(sys.argv[1], 'r')
tri = []
for test in test_cases:
    nums = [int(n) for n in test.strip().split()]
    tri.append(nums)
test_cases.close()

ans = [[None] * i for i in range(1, len(tri))]
ans.append(tri[-1])
print search(tri, 0, 0)




