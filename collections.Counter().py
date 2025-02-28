# from collections import Counter

number_of_shoes = int(input())
shoe_sizes = [int(x) for x in input().split()]
customers_count = int(input())

result = 0
for x in range(customers_count):
    size_by_customer, price = [int(x) for x in input().split()]

    if size_by_customer in shoe_sizes:
        result += price
        shoe_sizes.remove(size_by_customer)

print(result)
