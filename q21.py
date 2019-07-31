# Q2.1 Constantine Theocharis, Python 3.7

import math

def is_prime(i):
    if i == 1:
        return False
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

n = int(input())

primes = []

upper_bound = 100000000

for i in range(1, upper_bound):
    if is_prime(i):
        primes.append(i)
    if (len(primes) == n + 1):
        print(primes[-1])
        break
