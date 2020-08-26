string = ""
for i in range(1, 185188):
    string = string + str(i)
    i += 1
    print(i)

print("Answer is")
print(int(string[0]) * int(string[10 - 1]) * int(string[100 - 1]) * int(string[1000 - 1]) * int(string[10000 - 1]) * int(string[100000 - 1]) * int(string[1000000 - 1]))

