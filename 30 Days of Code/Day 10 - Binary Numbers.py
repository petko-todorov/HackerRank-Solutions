n = int(input())

to_bin_str = bin(n)[2:]

groups = to_bin_str.split('0')

result = max(len(x) for x in groups)
print(result)
