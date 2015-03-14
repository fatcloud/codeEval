__author__ = 'fatcloud'


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# connected_config must go with a leading one so that the number of digit preserves
# 1 stands for cut and 0 stands for merge
def gen_num_list(connection_config, num_str):
    num_list = []
    bin_list = [c for c in bin(connection_config)[3:]]
    num = num_str[0]
    rest_num_str = num_str[1:]
    for i in range(0, len(bin_list)):
        if bin_list[i] is '0':
            num += rest_num_str[i]
        elif bin_list[i] is '1':
            num_list.append(num)
            num = rest_num_str[i]
    num_list.append(num)
    return num_list

"""
print gen_num_list(16, '12345')
print gen_num_list(0b1, '4')
print gen_num_list(0b11001100011, '09876543212')
"""


def expand(num, buckets, ugly_product):
    num = int(num) % ugly_product

    if num is 0:
        return [n * 2 for n in buckets]

    p_buk = buckets[-num:] + buckets[:-num]         # expand by plus
    n_buk = buckets[num:] + buckets[:num]           # expand by minus

    return [p_buk[i] + n_buk[i] for i in range(len(buckets))]


def ugly_list(ugly_product, dividers):
    temp_list = []
    for i in range(ugly_product):
        for j in dividers:
            if i % j is 0:
                temp_list.append(i)
                break
    return temp_list


def main():
    import sys
    test_cases = open(sys.argv[1], 'r')

    ugly_product = (2 * 3 * 5 * 7)
    ugly_indexs = ugly_list(ugly_product, [2, 3, 5, 7])

    for test in test_cases:
        if test is '\n':
            continue
        # get the line without \n
        num_str = [char for char in test if is_int(char)]

        # initialize the list config_set
        leading_one = 1 << (len(num_str) - 1)
        config_set = range(leading_one, leading_one + 2 ** (len(num_str) - 1))

        ugly_sum = 0
        # compute the number of ugly numbers for each connected configuration
        for connection_config in config_set:

            # initialize buckets for the configuration
            buckets = [0] * ugly_product

            # generate the num_list corresponds to the configuration
            num_list = gen_num_list(connection_config, num_str)

            # insert the first number into buckets
            num = int(num_list[0])
            buckets[num % ugly_product] += 1

            # expand the buckets with the rest numbers in num_list
            for num in num_list[1:]:
                buckets = expand(num, buckets, ugly_product)

            # finally, count how many ugly numbers are there
            ugly_sum += sum([buckets[i] for i in ugly_indexs])

        print ugly_sum

    test_cases.close()


main()

