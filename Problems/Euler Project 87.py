import math
import time

start = time.time()
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, 7100):
    if isPrime(i):
        primes.append(i)

ans = 0
vis = {}
for i in range(len(primes)):
    temp = pow(primes[i], 4)
    if temp >= 50000000:
        break
    for j in range(len(primes)):
        temp1 = temp + pow(primes[j], 3)
        if temp1 >= 50000000:
            break
        for k in range(len(primes)):
            temp2 = temp1 + pow(primes[k], 2)
            if temp2 >= 50000000:
                break
            try:
                _ = vis[temp2]
            except:
                vis[temp2] = True
                ans += 1

print("Answer is", ans)
print(time.time() - start)