#Euler 41
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


def permute_number(n): 
    str_number = str(n)
    permutation_list = list(int("". join(p)) for p in permutations(str_number))
    return permutation_list

largest_palindrom_prime = 1

for index in range(len(permute_number(1234567))): 
    if is_prime(int(permute_number(1234567)[index])) == True and largest_palindrom_prime < int(permute_number(1234567)[index]) : 
        largest_palindrom_prime = int(permute_number(1234567)[index])

print(largest_palindrom_prime)

#this number in the question can only consists of 7 digits. A number with 4 digits has already given, and any number of digist = 5,6,8,9 will 
#end up having sum of digits divisible by 3, so they can not be prime. Hence, we only need to see if any number with 7 digits is prime or not.