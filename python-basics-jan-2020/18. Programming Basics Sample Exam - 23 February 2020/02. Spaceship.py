import math

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
crew_average_height = float(input())

ship_capacity = ship_width * ship_height * ship_length
capacity_per_crew_member = 2 * 2 * (crew_average_height + 0.4)

capacity_count = math.floor(ship_capacity / capacity_per_crew_member)

if 3 <= capacity_count <= 10:
    print(f"The spacecraft holds {capacity_count} astronauts.")
elif capacity_count < 3:
    print("The spacecraft is too small.")
elif capacity_count > 10:
    print("The spacecraft is too big.")