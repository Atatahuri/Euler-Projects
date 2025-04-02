#Euler 43

from itertools import permutations

prime_list = [2, 3, 5, 7, 11, 13, 17]

def permute_number(): 
    digits = "0123456789"
    return (''.join(p) for p in permutations(digits))  # Using generator expression for efficiency

total_sum = 0  
for str_element in permute_number():
    if all(int(str_element[j:j + 3]) % prime_list[j - 1] == 0 for j in range(1, 8)):
        total_sum += int(str_element)
        print(str_element)
        
print("Total sum:", total_sum)
