import time

start = time.time()

def digits(n):
    temp = str(n)
    arr = [int(e) for e in temp]
    arr.sort()
    return arr

i = 1

while True:
    if digits(i) == digits(2 * i) == digits(3 * i) == digits(4 * i) == digits(5 * i) == digits(6 * i):
        print("Answer is", i, 2 * i)
        break
    print(i)
    i += 1
print(time.time() - start)