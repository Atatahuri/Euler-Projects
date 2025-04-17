#Euler 56


max_sum = 0 
for a in range(1, 101):
    for b in range(1,101): 
        digit_list = []
        for digits in str(a ** b):
            digit_list.append(digits)
            sum = 0
            for i in range(len(digit_list)):
                sum += int(digit_list[i])
                if sum > max_sum:
                    max_sum = sum

print(max_sum)
                    
