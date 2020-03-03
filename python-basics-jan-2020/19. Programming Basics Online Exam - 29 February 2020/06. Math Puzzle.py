key =  int(input())

combinations_found = False

for n1 in range(1, 30 + 1):
    for n2 in range(1, 30 + 1):
        for n3 in range(1, 30 + 1):
            sum_result = n1 + n2 + n3
                                    
            if (sum_result == key) and (n1 < n2 < n3):
                combinations_found = True
                print(f'{n1} + {n2} + {n3} = {sum_result}')

            multiplier_result = n1 * n2 * n3

            if (multiplier_result == key) and (n1 > n2 > n3):
                combinations_found = True
                print(f'{n1} * {n2} * {n3} = {multiplier_result}')

if not combinations_found:
    print('No!')