import math
import time
start = time.time()
def propDivisors(n):
    sumProp = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n // i:
                sumProp += (i + n // i)
            else:
                sumProp += i
    return sumProp


sumTotal = 0
nums = [n for n in range(2, 10001)]
while nums:
    a = nums.pop(0)
    b = propDivisors(a)
    if a == propDivisors(b) and a != b:
        sumTotal += a + b
        try:
            nums.remove(b)
        except:
            pass
print(sumTotal)
print(time.time() - start)