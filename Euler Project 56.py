import time

start = time.time()
maxDigitalSum = 0
for i in range(1, 101):
    for j in range(1, 101):
        temp = str(pow(i, j))
        digitSum = sum([int(num) for num in temp])
        maxDigitalSum = (digitSum if digitSum > maxDigitalSum else maxDigitalSum)

print(maxDigitalSum)
print(time.time() - start)