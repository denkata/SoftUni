command = input()

adults = 0
kids = 0

while command != 'Christmas':
    age = int(command)

    if age > 16:
        adults += 1
    else:
        kids += 1

    command = input()

toys_cost = kids *  5
sweaters_cost = adults * 15

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {toys_cost}')
print(f'Money for sweaters: {sweaters_cost}')