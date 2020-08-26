import time
def counting_rect(m, n):
    return (m * (m + 1) * n * (n + 1)) // 4

start = time.time()
i = 1
diff = [float('inf'), 0, 0]
target = 2000000
while (i * (i + 1) // 2) <= target:
    j = 1
    temp = 0
    while temp <= target:
        temp = counting_rect(i, j)
        if abs(temp - target) < diff[0]:
            diff[0] = abs(temp - target)
            diff[1], diff[2] = i, j
        j += 1
    i += 1

print("Answer is", diff[1] * diff[2])
print(time.time() - start)