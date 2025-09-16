n = int(input().strip())

numbers = list(map(int, input().rstrip().split()))
number_of_swaps = 0

for x in range(n):

    for y in range(0, n - 1):
        if numbers[y] > numbers[y + 1]:
            numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]
            number_of_swaps += 1

print(f"Array is sorted in {number_of_swaps} swaps.")
print(f"First Element: {numbers[0]}")
print(f"Last Element: {numbers[-1]}")
