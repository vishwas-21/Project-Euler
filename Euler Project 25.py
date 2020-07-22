import time
start = time.time()
def fib(n):
    a = b = 1
    i = 2
    for i in range(2, n):
        a, b = b, a + b
    return b

num = 1000
number = 1
while 1:
    test = str(fib(number))
    if len(test) == num:
        print(number)
        break
    number += 1
print(time.time() - start)