arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_sum = -9999999

for i in range(4):
    for j in range(4):
        hourglass_sum = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])

        max_sum = max(max_sum, hourglass_sum)

print(max_sum)
