n = int(input())

n_to_string = str(n)
first = int(n_to_string[2])
second = int(n_to_string[1])
third = int(n_to_string[0])

for n1 in range(1, first + 1):
    for n2 in range(1, second + 1):
        for n3 in range(1, third + 1):
            result = n1 * n2 * n3
            print(f'{n1} * {n2} * {n3} = {result};')