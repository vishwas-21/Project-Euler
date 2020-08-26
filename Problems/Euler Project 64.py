import math
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
            return len(ans[1])
        vars.append(var)
        ans[1].append(temp)
        a *= -1

ans = 0
for i in range(2, 10000):
    if not math.sqrt(i).is_integer():
        temp = con_frac(i)
        if temp % 2:
            ans += 1
print(ans)