__author__ = 'fatcloud'

primes = [2, 3]


def is_prime(n):
    for i in [i for i in primes if i <= n ** 0.5]:
        if n % i is 0:
            return False
    return True


num = 5

while len(primes) < 1000:
    if is_prime(num):
        primes.append(num)
    num += 2


print sum(primes)