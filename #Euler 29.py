#Euler 29 
distinct_powers = [] 
for a in range (2,101):
    for b in range(2,101): 
        if a ** b not in distinct_powers: 
            distinct_powers.append(a ** b)

print(len(distinct_powers))
