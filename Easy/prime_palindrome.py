__author__ = 'fatcloud'

factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def is_prime(n):
    for i in factors:
        if n % i is 0:
            return False

    return True


def is_palindrome(n):
    exp = str(n)
    end = len(exp) - 1
    for i in range((end + 1) / 2):
        if exp[i] is not exp[end - i]:
            return False

    return True


def ans(n):
    for i in range(n, 0, -1):
        if is_palindrome(i) and is_prime(i):
            return i


print ans(1000)