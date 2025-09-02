n = int(input())

for _ in range(n):
    string = input()
    even, odd = string[::2], string[1::2]
    print(even, odd)
