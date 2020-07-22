
def numDigits(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num = num // 10
    return digits

pandigit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
maxPandigit = []

def isPandigital9(n):
    i = 1
    global maxPandigit
    arr = []
    string = ""
    while len(arr) < 9:
        arr.extend(numDigits(n * i))
        string = string + str(n * i)
        i += 1
    if len(arr) > 9:
        return False
    else:
        arr.sort()
        if arr == pandigit:
            maxPandigit.append(int(string))
            return True
        else:
            return False

for i in range(1, 10000):
    isPandigital9(i)
    print(i)


print(maxPandigit)
print("Max is", max(maxPandigit))