import time
start = time.time()


def reverse(string):
    revIter = reversed(str(string))
    revString = ""
    for _ in range(len(str(string))):
        revString += revIter.__next__()
    return revString

def isLychrel(n):
    for _ in range(50):
        rev = reverse(n)
        n += int(rev)
        rev = reverse(n)
        temp = str(n)
        if temp == rev:
            return False
    return True

lychrel = 0
for i in range(1, 10000):
    if isLychrel(i):
        lychrel += 1
print(lychrel)
print(time.time() - start)