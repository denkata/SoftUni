first_result = input()
second_result = input()
third_result = input()

wins = 0
losses = 0
draws = 0

if first_result[0] > first_result[2]:
    wins += 1
elif first_result[0] == first_result[2]:
    draws += 1
else:
    losses += 1

if second_result[0] > second_result[2]:
    wins += 1
elif second_result[0] == second_result[2]:
    draws += 1
else:
    losses += 1

if third_result[0] > third_result[2]:
    wins += 1
elif third_result[0] == third_result[2]:
    draws += 1
else:
    losses += 1

print(f'Team won {wins} games.')
print(f'Team lost {losses} games.')
print(f'Drawn games: {draws}')