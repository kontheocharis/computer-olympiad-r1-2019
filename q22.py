# Q2.2 Constantine Theocharis, Python 3.7

import math

def is_prime(i):
    if i == 1:
        return False
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

def is_right_truncatable(i):
    string_i = str(i)
    length = len(str(i))
    
    digit_array = [int(string_i[:length-c]) for c in range(length)]

    for x in digit_array:
        if not is_prime(x):
            return False
    return True

n = int(input())

primes = []

upper_bound = 100000000

for i in range(2, upper_bound):
    if is_right_truncatable(i):
        primes.append(i)
    if (len(primes) == n):
        print(primes[-1])
        break
