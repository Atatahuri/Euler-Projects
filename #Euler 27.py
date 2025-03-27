#Quadratic Primes(Euler 27)
import math 

def is_prime(number): 
    if number < 2: 
        return False
    divisor = 2
    while divisor <= int(math.sqrt(number)):  
        if number % divisor == 0: 
            return False
        else:
            divisor += 1
    return True


# for n in range(100): 
#     if is_prime(n ** 2 + n + 41) == True: 
#         print(n)
#     else:
#         break

n = 0
count  = 0
max_a = 0
max_b = 0

for a in range(-999, 1000): 
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n ** 2 + a * n + b) == True: 
            n += 1
        if count < n:     
            count = n
            max_a = a
            max_b = b
    

print(max_a)
print(max_b)
print(count)
print(max_a * max_b) 
            
         



