if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted_arr = sorted(set(arr))

    print(sorted_arr[-2])


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
