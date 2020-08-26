import math
import time

start = time.time()
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_count(tot_sum, i, req_sum, primes, n):
    global ans
    if tot_sum == req_sum:
        ans += 1
        return
    for j in range(i, n):
        if tot_sum + primes[j] > req_sum:
            break
        get_count(tot_sum + primes[j], j, req_sum, primes, n)


primes = [2, 3, 5, 7]
i = 10
while True:
    ans = 0
    get_count(0, 0, i, primes, len(primes))
    if ans >= 5000:
        print("Answer is", i)
        print(time.time() - start)
        break
    if is_prime(i):
        primes.append(i)
    i += 1