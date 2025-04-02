#Euler 46

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

test_value = 9
while True:
    if is_prime(test_value) == False:
            if all(is_prime(test_value - 2 * (n **2)) == False for n in range(int(math.sqrt(test_value / 2)) + 1)):
                print(test_value)
            else: 
                test_value += 2
    else: 
        test_value += 2
                

               

