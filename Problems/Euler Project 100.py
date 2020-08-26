import time
start = time.time()
xk, yk = 15, 21
while yk <= 1000000000000:                                  # The Explanation is in Picture in the same folder
    xk, yk = 3 * xk + 2 * yk - 2, 3 * yk + 4 * xk - 3
print("Answer is", xk)
print(time.time() - start)