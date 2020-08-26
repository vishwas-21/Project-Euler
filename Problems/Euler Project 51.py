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

def con_3_same(n):
    temp = str(n)[:-1]
    for el in temp:
        if temp.count(el) >= 3:         #Iteration is done only on >=3 because 2 and 1 cannot form eight prime family
            check_prop(n, el, temp.count(el))

def check_prop(n, el, times):
    num = 0
    for i in range(0, 10):
        temp = str(n)
        temp = temp.replace(str(el), str(i), times)
        if is_prime(int(temp)) and len(str(int(temp))) == len(str(n)):
            num += 1
    if num == 8:
        print("Answer is", n)
        print(time.time() - start)
        quit()


n = 1001
while True:
    con_3_same(n)
    n += 1
    print(n)
