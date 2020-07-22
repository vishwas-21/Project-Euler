import decimal
import time

start = time.time()
decimal.getcontext().prec = 105
s = 0
for i in range(1, 101):
    temp = str(decimal.Decimal(i).sqrt())
    print(s)
    if temp.count("."):
        s += sum(int(e) for e in temp[temp.index(".") + 1:101]) + sum(int(e) for e in temp[:temp.index(".")])
print(s)
print(time.time() - start)