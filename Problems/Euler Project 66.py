import numpy
import time
import math
                                    # I Wonder this problem made me to do a lot of Research and the algo is of 64 and 65
start = time.time()
def con_frac(n):
    a = math.floor(math.sqrt(n))
    sqn = math.sqrt(n)
    ans = [a, []]
    b = 1
    vars = [(b, n, a)]
    while True:
        b = (n - a * a) // b
        temp = (sqn + a) // b
        a -= (temp * b)
        var = (b, n, a)
        if var in vars:
            return ans
        vars.append(var)
        ans[1].append(temp)
        a *= -1

def frac_con_of_n(n, ar):
    arr = [ar[0]]
    arr.extend(ar[1] * n)
    num = numpy.int(1)
    den = numpy.int(0)
    for i in range(n - 1, -1, -1):
        num, den = den, num
        num += (den * numpy.int(arr[i]))
    return (num, den)


ma = [0, 0]
for n in range(2, 1000):
    if not math.sqrt(n).is_integer():
        arr = con_frac(n)
        i = 2
        while True:
            x, y = frac_con_of_n(i, arr)
            if ((numpy.int(x) % n) ** 2) % n == 1:
                if ma[0] < x:
                    ma = [x, n]
                break
            i += 2
print("Answer is", ma[1])
print(time.time() - start)