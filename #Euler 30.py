#Euler 30
sum = 0
for number in range(2,1000000):
    string_number = str(number)
    desired_number = 0
    for i in range(len(string_number)): 
        desired_number += (int(string_number[i]))**5
    if desired_number == number: 
        sum += desired_number
        print(desired_number)

print(sum)