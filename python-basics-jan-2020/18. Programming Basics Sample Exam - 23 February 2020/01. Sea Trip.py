food_money_per_day = float(input())
gifts_money_per_day = float(input())
hotel_money_per_day = float(input())

total_gas_needed = 420 / 100 * 7
total_gast_cost = total_gas_needed * 1.85

total_food_cost = food_money_per_day * 3
total_gifts_cost = gifts_money_per_day * 3
hotel_cost_first_day = hotel_money_per_day * 0.9
hotel_cost_second_day = hotel_money_per_day * 0.85
hotel_cost_third_day = hotel_money_per_day * 0.8

total_hotel_cost = hotel_cost_first_day + hotel_cost_second_day + hotel_cost_third_day

money_needed = total_gast_cost + total_food_cost + total_gifts_cost + total_hotel_cost

print(f'Money needed: {money_needed:.2f}')