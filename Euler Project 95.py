import time
import math


start = time.time()
def sum_prop_div(n):
    sumProp = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n // i:
                sumProp += i + n // i
            else:
                sumProp += i
    return sumProp


def length_chain(n):
    ans = 1
    dic = {n : True}
    temp = n
    while True:
        if temp >= 1000000:
            return 0
        temp = sum_prop_div(temp)
        try:
            _ = dic[temp]
            if temp == n:
                return ans
            return 0
        except:
            dic[temp] = True
            ans += 1



ma = 0
ans = 0
for i in range(10, 1000000):
    temp = length_chain(i)
    if temp > ma:
        ans = i
        ma = temp
    if i % 25000 == 0:
        print(i, ans, ma, "Time -", time.time() - start)
