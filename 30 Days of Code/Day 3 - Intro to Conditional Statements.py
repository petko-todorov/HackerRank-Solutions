number = int(input())

if number % 2 != 0:
    print("Weird")
elif 2 <= number <= 5:
    print("Not Weird")
elif 6 <= number <= 20:
    print("Weird")
else:
    print("Not Weird")
