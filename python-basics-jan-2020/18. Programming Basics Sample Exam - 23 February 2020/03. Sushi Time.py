import math

sushi_type = input()
restaurant_name = input()
portions = int(input())
delivery = input()

total_price = 0
restaurants = ['Sushi Zone', 'Sushi Time', 'Sushi Bar', 'Asian Pub']

if restaurant_name not in restaurants:
    print(f'{restaurant_name} is invalid restaurant!')
    exit()

if sushi_type == 'sashimi':
    if restaurant_name == 'Sushi Zone':
        total_price = portions * 4.99
    elif restaurant_name == 'Sushi Time':
        total_price = portions * 5.49
    elif restaurant_name == 'Sushi Bar':
        total_price = portions * 5.25
    elif restaurant_name == 'Asian Pub':
        total_price = portions * 4.50
elif sushi_type == 'maki':
    if restaurant_name == 'Sushi Zone':
        total_price = portions * 5.29
    elif restaurant_name == 'Sushi Time':
        total_price = portions * 4.69
    elif restaurant_name == 'Sushi Bar':
        total_price = portions * 5.55
    elif restaurant_name == 'Asian Pub':
        total_price = portions * 4.80
elif sushi_type == 'uramaki':
    if restaurant_name == 'Sushi Zone':
        total_price = portions * 5.99
    elif restaurant_name == 'Sushi Time':
        total_price = portions * 4.49
    elif restaurant_name == 'Sushi Bar':
        total_price = portions * 6.25
    elif restaurant_name == 'Asian Pub':
        total_price = portions * 5.50
elif sushi_type == 'temaki':
    if restaurant_name == 'Sushi Zone':
        total_price = portions * 4.29
    elif restaurant_name == 'Sushi Time':
        total_price = portions * 5.19
    elif restaurant_name == 'Sushi Bar':
        total_price = portions * 4.75
    elif restaurant_name == 'Asian Pub':
        total_price = portions * 5.50

if delivery == 'Y':
    total_price += total_price * (20 / 100)

print(f'Total price: {math.ceil(total_price)} lv.')