import time


start = time.time()
def if_one_added(num, den):
    return num + den, den

total = 0
num, den = 3, 2
for _ in range(2, 1001):
    den, num = if_one_added(num, den)
    num, den = if_one_added(num, den)
    if len(str(num)) > len(str(den)):
        total += 1
print(total)
print(time.time() - start)