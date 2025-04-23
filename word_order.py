n = int(input())

words = [input() for x in range(n)]

number_of_distinct = len(set(words))

result = {}
for word in words:
    result[word] = result.get(word, 0) + 1

print(number_of_distinct)
print(' '.join(str(x) for x in result.values()))
