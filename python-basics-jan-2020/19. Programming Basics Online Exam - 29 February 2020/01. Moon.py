import math

average_speed = float(input())
fuel_per_100km = float(input())

total_distance = 384400 * 2
time_needed = total_distance / average_speed

print(math.ceil(time_needed + 3))
print(round(fuel_per_100km * total_distance / 100))