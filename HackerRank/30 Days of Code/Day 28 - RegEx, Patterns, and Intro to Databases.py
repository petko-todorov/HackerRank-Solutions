import re

n = int(input().strip())

data = []
for _ in range(n):
    first_multiple_input = input().rstrip().split()

    first_name = first_multiple_input[0]

    email_id = first_multiple_input[1]

    data.append(first_name) if re.findall("\w[a-zA-Z]*@gmail.com", email_id) else None

[print(x) for x in sorted(data)]
