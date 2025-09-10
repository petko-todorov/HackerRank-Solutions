# https://www.hackerrank.com/challenges/no-idea/problem

happiness = 0

n, m = [int(x) for x in input().split()]

integers = [int(i) for i in input().split()]

a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

for i in integers:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)
