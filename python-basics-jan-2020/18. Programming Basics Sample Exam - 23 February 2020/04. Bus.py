passengers = int(input())
stops_count = int(input())

stop_counter = 1

for stop in range(stops_count):
    for i in range(2):
        current_passengers = int(input())
        if i % 2 == 0:
            passengers -= current_passengers
        else:
            passengers += current_passengers

    if stop_counter % 2 == 0:
        passengers -= 2
    else:
        passengers += 2
    
    stop_counter += 1

print(f'The final number of passengers is : {passengers}')