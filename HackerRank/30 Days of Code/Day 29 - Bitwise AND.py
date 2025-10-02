# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K


def bitwiseAnd(N, K):
    if ((K - 1) | K) <= N:
        return K - 1
    else:
        return K - 2


t = int(input().strip())

for _ in range(t):
    first_multiple_input = input().rstrip().split()

    count = int(first_multiple_input[0])

    lim = int(first_multiple_input[1])

    res = bitwiseAnd(count, lim)
    print(res)
