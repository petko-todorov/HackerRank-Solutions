n = int(input())

arr = [int(x) for x in input().split()]

mean = str(f"{sum(arr) / n:.1f}")

sorted_arr = sorted(arr)

median = (sorted_arr[len(sorted_arr) // 2 - 1] + sorted_arr[len(sorted_arr) // 2]) / 2

dictionary = {}
for x in arr:
    dictionary[x] = dictionary.get(x, 0) + 1

mode = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))[0][0]

print(mean)
print(median)
print(mode)
