# for i in range(1, int(input())):
#     print("".join(str(x) for x in range(1, i)) + str(i) + "".join(str(x) for x in range(i - 1, 0, -1)))

for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
