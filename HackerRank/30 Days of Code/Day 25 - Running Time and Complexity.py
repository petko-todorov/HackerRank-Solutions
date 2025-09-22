import math


def is_prime(num):
    if num == 0 or num == 1:
        return 'Not prime'
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return 'Not prime'
    else:
        return 'Prime'


for _ in range(int(input())):
    n = int(input())
    print(is_prime(n))
