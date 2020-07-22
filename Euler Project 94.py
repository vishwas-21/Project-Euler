import math
import time

start = time.time()
xk = 5      # We know this satisfies +1 condition
yk = 4      # Here yk is the root part of area
totalPerm = 0
while 3 * xk + 1 <= 1000000000:     # Solving +1 condition using Recursive Solutions
    totalPerm += (3 * xk + 1)
    xk, yk = (7 * xk + 8 * yk - 2), (6 * xk + 7 * yk - 2)
i = 2
while True:     # As we dont know any value which satisfies -1 condition we are finding one
    s = (3 * i - 1) / 2
    area = math.sqrt(s * (s - i) * (s - i) * (s - i + 1))
    if area.is_integer():
        xk = i
        yk = math.sqrt(3 * i * i + 2 * i - 1) // 2
        break
    i += 1
while 3 * xk - 1 <= 1000000000:     # As we found one value other can be obtained by recursive solutions
    totalPerm += (3 * xk - 1)
    xk, yk = (7 * xk + 8 * yk + 2), (6 * xk + 7 * yk + 2)
print("Answer is", int(totalPerm))
print(time.time() - start)