import math
import time


start = time.time()
def numDigits(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num = num // 10
    return digits

pandigit = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def isPandigital9(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        arr = numDigits(n)
        if n % i == 0:
            arr.extend(numDigits(i))
            arr.extend(numDigits(n // i))
            arr.sort()
            if arr == pandigit:
                return True
    return False

sumTotal = []
for j in range(2, 10001):
    if isPandigital9(j):
        sumTotal.append(j)
    print(j)


print(sum(sumTotal))
print(time.time() - start)

