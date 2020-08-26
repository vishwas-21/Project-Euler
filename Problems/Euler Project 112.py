def is_bouncy(num):
    temp = list(str(num))
    temp.sort()
    if temp == list(str(num)):
        return False
    temp.reverse()
    if temp == list(str(num)):
        return False
    return True

el = 2
total, bounce_count = 1, 0
p = 0.99
while bounce_count/total < p:
    if is_bouncy(el):
        bounce_count += 1
    el += 1
    total += 1

print(el - 1)