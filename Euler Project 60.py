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

def check_pri(n1, n2):
    if is_prime(int(str(n1) + str(n2))) and is_prime(int(str(n2) + str(n1))):
        return True
    return False

def get_primes(pr, n):
    for i in range(2, n):
        if is_prime(i):
            pr.append(i)
    return pr


n = 10000
pr = []
get_primes(pr, n)
print("Got Primes")
n = len(pr)
for i in range(0, n):
    for j in range(i, n):
        if check_pri(pr[i], pr[j]):
            for k in range(j, n):
                if check_pri(pr[i], pr[k]) and check_pri(pr[j], pr[k]):
                    for l in range(k, n):
                        if check_pri(pr[i], pr[l]) and check_pri(pr[j], pr[l]) and check_pri(pr[k], pr[l]):
                            for m in range(k, n):
                                if check_pri(pr[i], pr[m]) and check_pri(pr[j], pr[m]) and check_pri(pr[k],
                                                                                                     pr[
                                                                                                         m]) and check_pri(
                                    pr[l], pr[m]):
                                    print("Answer is", pr[i] + pr[j] + pr[k] + pr[l] + pr[m])
                                    print(pr[i], pr[j], pr[k], pr[l], pr[m])
                                    print(time.time() - start)
                                    quit()

print(time.time() - start, "No Answer")