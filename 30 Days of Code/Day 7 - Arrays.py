n = int(input())

arr = list(map(int, input().rstrip().split()))

arr.reverse()
print(*arr)

# print(*arr[::-1])
# print(*list(reversed(arr)))
