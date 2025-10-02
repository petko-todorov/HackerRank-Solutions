n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()


def get_median(sub):
    m = len(sub)
    if m % 2 == 0:
        return (sub[m // 2 - 1] + sub[m // 2]) // 2
    else:
        return sub[m // 2]


if n % 2 == 0:
    q2 = (arr[n // 2 - 1] + arr[n // 2]) // 2
    lower = arr[:n // 2]
    upper = arr[n // 2:]
else:
    q2 = arr[n // 2]
    lower = arr[:n // 2]
    upper = arr[n // 2 + 1:]

q1 = get_median(lower)
q3 = get_median(upper)

print(q1)
print(q2)
print(q3)
