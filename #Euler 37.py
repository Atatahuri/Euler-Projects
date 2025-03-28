#Euler 37
import math
def is_prime(n): 
    if n < 2 : 
        return False
    elif n == 2:
        return True 
    if n % 2 == 0: 
        return False
    else:  
        for i in range(3, int(math.sqrt(n)) + 1, 2): 
            if n % i == 0: 
                return False
        return True
     
# print(is_prime(101))
# print(is_prime(111))
         
 
def truncated_number(number): 
    str_number = str(number)
    list_number = []
    desired_numbers = [number]
    for digit in str_number:
        list_number.append(digit)
    while len(list_number) > 1: 
        del list_number[-1]
        desired_numbers.append(int(''.join(map(str, list_number))))

    for digit in str_number:
        list_number.append(digit)
    while len(list_number) > 1:
        del list_number[0]
        desired_numbers.append(int(''.join(map(str, list_number))))
    return desired_numbers

# print(truncated_number(3797))

sum = 0 
for candidate in range(10, 10 ** 7): 
        if all(is_prime(element) == True for element in truncated_number(candidate)):
            sum += candidate 
            print(candidate) 
print(sum)
            


