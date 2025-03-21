#Euler 31
count = 1
for two in range(101):
    for five in range(41):
        for ten in range(21):
            for twenty in range(11): 
                for fifty in range(4):
                    for hundred in range(3):
                        if 2*two + five * 5 + 10 * ten + 20 * twenty + 50 * fifty + 100 * hundred <= 200:
                            count += 1

print(count)
