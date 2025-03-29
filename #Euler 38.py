# #Euler 38
desired_set = set(range(1,10))
largest_number = 1
concatenated_string = ''
for candidate in range(1,10**6):
    final = '' 
    for i in range(1,20):
        processed_candidate = str(candidate * i)
        final += str(processed_candidate)
        set_final = set(map(int, final))
        if set_final != desired_set:
            continue
        elif len(final) == 9:
            final = int(''.join(map(str, final)))
            if largest_number < final:
                largest_number = final 
                processed_candidate = ''
                final = ''
        break

print(largest_number)

