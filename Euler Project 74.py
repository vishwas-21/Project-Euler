import math
import time

start = time.time()
def num_non_rp(n):
    arr = [n]
    while True:
        n = sum(math.factorial(int(i)) for i in str(n))
        if n in arr:
            return len(arr)
        else:
            arr.append(n)

num = 0
for i in range(2, 1000001):
    if num_non_rp(i) == 60:
        num += 1

print(num)
print(time.time() - start)