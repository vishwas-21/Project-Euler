import math
import time

start = time.time()


def isPrime(n):
    if n == 1:
        return False
    elif n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False


primes = 8
total = 13
n = 7
while primes / total >= 0.1:
    n += 2
    total += 4
    if isPrime(n * n - (n - 1)):
        primes += 1
    if isPrime(n * n - 2 * (n - 1)):
        primes += 1
    if isPrime(n * n - 3 * (n - 1)):
        primes += 1
    print(primes / total)

print(n)

print(time.time() - start)