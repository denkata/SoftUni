singer_price = int(input())
command = input()

income = 0
guests_count = 0

while command != 'The restaurant is full':
    group = int(command)

    if group < 5:
        ticket_price = 100
    else:
        ticket_price = 70

    income += group * ticket_price
    guests_count += group

    command = input()

money_left = income - singer_price

if income >= singer_price:
    print(f'You have {guests_count} guests and {money_left} leva left.')
else:
    print(f'You have {guests_count} guests and {income} leva income, but no singer.')