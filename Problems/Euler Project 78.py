import time
start = time.time()
# p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) ... where 1, 2, 5, 7 are pentagonal numbers

arr = [1, 1]
n = 2
MOD = 1000_000
while True:
    i = 1
    k = 1
    pa = 0
    while True:
        a = (3 * i * i - i) // 2
        b = (3 * i * i + i) // 2
        if a > n:
            break
        a = n - a
        pa += (k * arr[a]) 
        pa = (pa + MOD) % MOD
        if b > n:
            break
        b = n - b
        pa += (k * arr[b])
        pa = (pa + MOD) % MOD
        k *= -1
        i += 1
    if pa == 0:
        break
    arr.append(pa)
    n += 1

print(f"Answer: {n}")
print(f"Time: {time.time() - start}")
