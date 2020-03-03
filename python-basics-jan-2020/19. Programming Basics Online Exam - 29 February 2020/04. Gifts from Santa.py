n = int(input())
m = int(input())
s = int(input())

numbers = []

for num in reversed(range(n, m + 1)):
    if num % 2 == 0 and num % 3 == 0:
        if num == s:
            break

        numbers.append(num)

for match_number in numbers:
    print(match_number, end=' ')