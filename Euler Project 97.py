import time

start = time.time()
num = 2 ** 17
for i in range(195761):
    num *= 1099511627776
    if len(str(num)) > 10:
        num = int(str(num)[-10:])
num *= 28433
num += 1
print("Answer is", str(num)[-10:])
print(time.time() - start)