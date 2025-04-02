#Euler 45

import math

def is_pentagonal(num):
    # Solve: n(3n - 1)/2 = num
    # 3n^2 - n - 2*num =  W0
    # n = (1 + sqrt(1 + 24*num)) / 6
    discriminant = 1 + 24 * num
    sqrt_disc = math.isqrt(discriminant) #isqrt computes the integer sqrt. See how beautifully second degree polynomial solved!
    if sqrt_disc * sqrt_disc != discriminant:  # Must be perfect square
        return False
    n = (1 + sqrt_disc) // 6
    return n > 0 and n * (3 * n - 1) == 2 * num


# def is_triangle(num):
#     # Solve: n(n + 1)/2 = num
#     # n^2 + n - 2*num =  W0
#     # n = (1 + sqrt(1 + 8*num)) / 2
#     discriminant = 1 + 8 * num
#     sqrt_disc = math.isqrt(discriminant) #isqrt computes the integer sqrt. See how beautifully second degree polynomial solved!
#     if sqrt_disc * sqrt_disc != discriminant:  # Must be perfect square
#         return False
#     n = (1 + sqrt_disc) // 2
#     return n > 0 and n * (n + 1) == 2 * num

for hex  in range(10000000):
    if is_pentagonal(hex*(2 * hex - 1)):
        print(hex*(2 * hex - 1))
        

