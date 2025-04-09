# #Euler 51

# import math 

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# candidate_list = []
# prime_family_count = 0
# candidate = 56000
# while prime_family_count != 8:
#     str_candidate = str(candidate)
#     for digits in str_candidate:
#         candidate_list.append(digits)
#         for i in range(len(candidate_list)):
#             for j in range(i, len(candidate_list) + 1):
#                 for digit in range(10):
#                     if j == len(candidate_list): 
#                         candidate_list [i] = digit 
#                         candidate_list.append(digit)
#                         int_result = int(''.join(map(str, candidate_list)))
#                     else: 
#                         candidate_list[i] = digit
#                         candidate_list[j] = digit
#                         int_result = int(''.join(map(str, candidate_list)))
#                     if is_prime(int_result): 
#                         prime_family_count += 1
# candidate += 1
# prime_family_count = 0
# print(candidate - 1)


                    
                    
    
import math

# Sieve of Eratosthenes to generate primes up to n
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(n + 1) if is_prime[i]]
    return is_prime, primes

# Convert number to string, replace digits based on pattern, and check family size
def check_prime_family(num, positions):
    str_num = str(num)
    family = []
    # Replace digits at specified positions with 0-9
    for d in range(10):
        digits = list(str_num)
        for pos in positions:
            digits[pos] = str(d)
        # Skip if leading digit becomes 0
        if digits[0] == '0':
            continue
        candidate = int(''.join(digits))
        if is_prime_array[candidate]:
            family.append(candidate)
    return family

# Generate all possible replacement patterns for a given digit length
def generate_patterns(length):
    patterns = []
    from itertools import combinations
    for r in range(1, length):  # At least 1 digit replaced, up to length-1
        for pos in combinations(range(length), r):
            patterns.append(pos)
    return patterns

# Main logic
LIMIT = 1000000  # Adjust as needed
is_prime_array, primes = sieve(LIMIT)

for prime in primes:
    str_prime = str(prime)
    digit_length = len(str_prime)
    # Generate patterns for this digit length once
    patterns = generate_patterns(digit_length)
    for pattern in patterns:
        family = check_prime_family(prime, pattern)
        if len(family) == 8:
            print(f"Smallest prime: {min(family)}")
            exit()

                        