import time

start = time.time()
def rproper_form(num, den):
    while True:
        for i in range(2, num + 1):
            if num % i == 0 and den % i == 0:
                num //= i
                den //= i
                break
        else:
            break
    return num, den

dep = 3 / 7
mi = float('inf')
ans = [0, 1]
for den in range(2, 1000001):
    for num in range(ans[0] * den // ans[1], 3 * den // 7):
        pre = num / den
        if 0 < dep - pre < mi:
            mi = dep - pre
            ans = [num, den]
            break

print(rproper_form(ans[0], ans[1]))
print(time.time() - start)