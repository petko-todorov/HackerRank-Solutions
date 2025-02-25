# https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = [int(x) for x in input().split()]

pattern = [('.|.' * i).center(m, '-') for i in range(1, n, 2)]
print('\n'.join(pattern))
print('WELCOME'.center(m, '-'))
print('\n'.join(pattern[::-1]))
