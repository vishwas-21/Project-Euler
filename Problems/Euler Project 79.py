data = [
    319,
    680,
    180,
    690,
    129,
    620,
    762,
    689,
    762,
    318,
    368,
    710,
    720,
    710,
    629,
    168,
    160,
    689,
    716,
    731,
    736,
    729,
    316,
    729,
    729,
    710,
    769,
    290,
    719,
    680,
    318,
    389,
    162,
    289,
    162,
    718,
    729,
    319,
    790,
    680,
    890,
    362,
    319,
    760,
    316,
    729,
    380,
    319,
    728,
    716
]

def is_valid(a: str):
    for el in data:
        el = str(el)
        i1 = a.index(el[0])
        try:
            i2 = a.index(el[1], i1 + 1)
        except ValueError:
            return False
        try:
            i3 = a.index(el[2], i2 + 1)
        except ValueError:
            return False
        # print(i1, i2, i3)
    return True


from itertools import permutations
chars = list(set("".join(str(x) for x in data)))

answers = []
for el in permutations(chars):
    if is_valid("".join(el)):
        answers.append(int("".join(el)))
    
print("Answer:", min(answers))