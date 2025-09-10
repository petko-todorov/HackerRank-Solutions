if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    comprehensions = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    result = [x for x in comprehensions if sum(x) != n]
    print(result)

# https://www.hackerrank.com/challenges/list-comprehensions/problem
