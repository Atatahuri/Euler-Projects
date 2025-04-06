#Euler 49


import math
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



def permute_number(m): 
    str_number = str(m)
    permutation_list = set(int("". join(p)) for p in permutations(str_number))
    sorted_permutation_list = sorted(permutation_list)
    return sorted_permutation_list


for number in range(1000, 10000):
    auxiliary_list = permute_number(number)
    for i in range(len(auxiliary_list)): 
        for j in range(i,len(auxiliary_list)):
            for k in range(j, len(auxiliary_list)):
                if is_prime(auxiliary_list[i]) and is_prime(auxiliary_list[j]) and is_prime(auxiliary_list[k]):
                    if auxiliary_list[k] - auxiliary_list [j] == auxiliary_list [j] - auxiliary_list[i] > 0:
                        print(str(auxiliary_list[i]) + str(auxiliary_list[j]) + str(auxiliary_list[k]))
                    
