import math
import collections

def isPrime(n):
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

def numOfPrimes(a, b):
    length = 1
    i = 1
    while i > 0:
        if isPrime((i ** 2) + a * i + b):
            length += 1
        else:
            return length
        i += 1

arr = collections.deque([])
for i in range(2, 1000):
    if isPrime(i):
        arr.append(i)


maxNumber = 0
for i in arr:
    for j in arr:
        temp = numOfPrimes(-j, i)
        if temp > maxNumber:
            maxNumber = temp
            af, bf = i, -j
        print(i)

print(maxNumber, af * bf)

# Checked it in three Ways a, b     -a, b      a, -b--ans
# 39 43 3
# 19 -19 19
# 71 971 -61