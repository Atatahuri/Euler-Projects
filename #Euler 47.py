#Euler 47
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




# def prime_dec(n): 
#     power_list = []
#     if n % 2 == 0: 
#         two_power = 0
#         while n % (2 ** two_power) == 0: 
#             two_power += 1
#         power_list.append("2" + " ^ " + str(two_power - 1))
#     divisor = 3
#     while n % divisor == 0 and is_prime(divisor):
#         divisor_power = 0
#         while n % (divisor ** (divisor_power)) == 0 : 
#             divisor_power += 1
#         power_list.append(str(divisor) + " ^ " + str(divisor_power - 1))
#         divisor += 2
#     if not power_list:
#         return(n)
#     else:  
#         return (power_list)

def prime_factors(n): 
    prime_factors = []
    if n % 2 == 0: 
        prime_factors.append(2)
    divisor = 3
    for divisor in range(divisor, n, 2):
        if n % divisor == 0 and is_prime(divisor):
            prime_factors.append(divisor)
    return(prime_factors)

for n in range  (1, 1000000):
        if all(len(prime_factors(n + i)) == 4 for i in range(4)):
            print(n)
            break
else:
    print("Loop finished with no result in your range!")





# n = 1
# while (len(prime_factors(n + i)) != 2 for i in range(4)):
#     n += 1
# print(n)







    


