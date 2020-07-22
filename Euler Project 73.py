import math
import time, sys
t0 = time.time()
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def SieveOfEratosthenes(n):		# For finding primes
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)+1)):
        if primes[i]:
            k = i
            while k * i <= n:
                primes[k * i] = False
                k += 1
    return primes

ans = 0
total = 12000
primes = SieveOfEratosthenes(total)
for d in range(2, total+1):
    for n in range(math.floor(d/3)+1, math.ceil(d/2)):
        if primes[d]:
            ans += (math.ceil(d/2) - 1 - math.floor(d/3))
            break
        if gcd(d, n) == 1:
            ans += 1
print(ans)
print(time.time() - t0) # 14 Seconds