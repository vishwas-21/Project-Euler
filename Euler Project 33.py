
def simplify(num, den):
    num, den = str(num), str(den)
    if num[0] in den:
        den = den[1] if den[0] == num[0] else den[0]
        num = num[1]
        if den != "0":
            return int(num) / int(den)
        else:
            return 1
    elif num[1] in den:
        den = den[0] if den[1] == num[1] else den[1]
        num = num[0]
        if den != "0":
            return int(num) / int(den)
        else:
            return 1
    return 1

nume = deno = 1
for a in range(10, 100):
    for b in range(a + 1, 100):
        if simplify(a, b) == a / b:
            if a % 10 != 0 and b % 10 != 0:
                print(a, b)
                nume *= a
                deno *= b

print(nume, deno)

