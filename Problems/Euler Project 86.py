from math import sqrt

N = 1000000

ans = 0
M = 0

while ans < N:
    M += 1
    for a in range(2, 2 * M + 1):
        f = sqrt(a * a + M * M)
        if f.is_integer():
            ans += (a // 2 if a < M else (1 + M - (a + 1) // 2))
print("Answer:", M)