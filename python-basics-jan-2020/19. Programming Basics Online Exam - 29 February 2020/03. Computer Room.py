month = input()
hours = int(input())
people_count = int(input())
day_period = input()

first_period = ['march', 'april', 'may']
second_period = ['june', 'july', 'august']

price = 0

if month in first_period:
    if day_period == 'day':
        price = 10.50
    else:
        price = 8.40
elif month in second_period:
    if day_period == 'day':
        price = 12.60
    else:
        price = 10.20

if people_count >= 4:
    price *= 0.9

if hours >= 5:
    price *= 0.5

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {(price * people_count) * hours:.2f}')