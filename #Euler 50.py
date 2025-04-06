#Euler 50
# import math

# def is_prime(n): 
#     if n < 2 : 
#         return False
#     elif n == 2:
#         return True 
#     if n % 2 == 0: 
#         return False
#     else:  
#         for i in range(3, int(math.sqrt(n)) + 1, 2): 
#             if n % i == 0: 
#                 return False
#         return True
    

# def sieve(m): 
#     numbers_list = list(range(2, m + 1))
#     for prime in numbers_list:
#         for  composite in numbers_list:
#             if composite > prime and composite % prime == 0:
#                 numbers_list.remove(composite)
#     return numbers_list



# consecutive_prime_length = 0
# input = 10 ** 4
# for number in sieve(input): 
#     for i in range(sieve(input).index(number),len(sieve(input)) - 1):
#         if is_prime(sum(sieve(input)[sieve(input).index(number) : i + 1] )):
#             if (i +  1 - sieve(input).index(number)) > consecutive_prime_length:
#                 consecutive_prime_length = i + 2 - sieve(input).index(number)



# print(number)
# print(consecutive_prime_length)
            
        
   

import math

def sieve(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(n + 1) if is_prime[x]]

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def longest_consecutive_prime_sum(limit):
    primes = sieve(limit)
    max_length = 0
    result_prime = 0
    
    # Precompute cumulative sums for efficiency
    cumulative_sums = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        cumulative_sums[i + 1] = cumulative_sums[i] + primes[i]
    
    # Check all possible consecutive sums
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            current_sum = cumulative_sums[j + 1] - cumulative_sums[i]
            if current_sum >= limit:
                break
            if is_prime(current_sum):
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
                    result_prime = current_sum
    
    return result_prime, max_length

# Solve for limit of 1,000,000
limit = 10**6
prime, length = longest_consecutive_prime_sum(limit)
print(f"The prime is {prime}, which is the sum of {length} consecutive primes.")