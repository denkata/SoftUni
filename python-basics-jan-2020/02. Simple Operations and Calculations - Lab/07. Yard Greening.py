total_square_meters = float(input())
price_per_square_meter = 7.61
discount_percent = 18

price_before_discount = total_square_meters * price_per_square_meter
total_discount = price_before_discount * (discount_percent / 100)
final_price = price_before_discount - total_discount

print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {total_discount:.2f} lv.')