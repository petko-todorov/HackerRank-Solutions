# https://www.hackerrank.com/challenges/most-commons/problem

if __name__ == '__main__':
    string = input()

    result = {}
    for s in string:
        result[s] = result.get(s, 0) + 1

    for key, value in sorted(result.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(key, value)
