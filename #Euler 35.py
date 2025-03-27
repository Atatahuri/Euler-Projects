#Euler 35
import math 
from itertools import product
from itertools import permutations
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
# print(is_prime(91))
# print(is_prime(19))
# permuted_number = []
# for number in range (100 , 1000000):
#     string_number = str(number)
#     digits_list = []
#     for digit in string_number: 
#         digits_list.append(digit)
#     permuted_number = list(permutations(digits_list))
#     for j in range (len(str(permuted_number) + 1)):

# def permute_number(n): 
#     str_number = str(n)
#     permutation_list = set(int("". join(p)) for p in permutations(str_number))
#     return permutation_list
# print(permute_number(19))    

def rotation(m):
    rotations = []  # Store all rotations
    new = str(m)  # Convert number to string
    for _ in range(len(new)):  # Loop for the length of the number
        rotations.append(int(new))  # Store the integer version
        new = new[-1] + new[:-1]  # Rotate the string
    
    return rotations  # Return the list of rotations

# Test the function
print(rotation(197))
   

digits = [1, 3, 7, 9]
answer = [2,5]
for i in range(1,7):
    numbers = [int("".join(map(str, p))) for p in product(digits, repeat = i)]
    # for index in range(len(numbers)): 
    #     for count  in range(len(str(numbers[index])) - 1):
    #         int((str(numbers[index]))[count + 1]) == int((str(numbers[index]))[count])
    #         int((str(numbers[index]))[0]) == int((str(numbers[index]))[len(str(numbers[index]))- 1])
    #     if is_prime(int(str(numbers[index]))) and (str(numbers[index])) not in answer: 
    #         answer.append(int(str(numbers[index])))
    #         print(int(str(numbers[index])))
    for number in numbers: 
            if all(is_prime(num) == True for num in rotation(number)) and number not in answer: 
                answer.append(number)
print(answer)
print(len(answer))

        
    
    # for number in numbers: 
    #     permuted_number = permute_number(number)
    #     if all(is_prime(numb) == True for numb in permuted_number) and number not in answer:
    #             answer.append(number)




# print(len(answer))
# print(answer)
# for perm in permute_number(197):
    
   

 



