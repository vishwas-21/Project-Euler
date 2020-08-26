import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

el = 1
for i in range(2,1000000):
    if is_prime(i):                         # As we need greatest numbers with least relatively prime numbers its better
        if el * i <= 1000000:               # to form a number with primes to avoid divisible by other numbers
            el *= i
        else:
            print("Answer is ", el)
            break

