data = {}

n = int(input())

for _ in range(n):
    name, phone = input().split()
    data[name] = phone

try:
    while True:
        search_name = input()
        if search_name in data:
            print(f"{search_name}={data[search_name]}")
        else:
            print("Not found")
except EOFError:
    pass