
def inBinary(n):
    string = bin(n)
    string = string[2:]
    return int(string)

def isPalindrome(n):
    string = ""
    temp = n
    while n > 0:
        string += str(n % 10)
        n = n // 10
    return string == str(temp)

sumPalindromes = 0
for i in range(1, 1000000):
    if isPalindrome(i) and isPalindrome(inBinary(i)):
        sumPalindromes += i
        print(i)

print(sumPalindromes)