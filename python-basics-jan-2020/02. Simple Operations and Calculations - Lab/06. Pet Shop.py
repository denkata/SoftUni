dogs_count = int(input())
other_animals_count = int(input())

dogs_foood_price = dogs_count * 2.5
other_animals_food_price = other_animals_count * 4

total_cost = dogs_foood_price + other_animals_food_price
total_cost = round(total_cost, 2)

print('%.2f' % total_cost + ' lv.')