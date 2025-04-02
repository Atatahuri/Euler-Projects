#Euler 44

#Extremely inefficient code and with so much math cheating done for finding upper bounds
# import math 
# penthagon = []
# for i in range(1,3000):
#     penthagon.append(i * (3*i - 1)/2)

# smallest_difference = 1000000000000
# for  m in penthagon: 
#     for n in penthagon:
#         if m + n in penthagon and abs(m - n) in penthagon and abs(m - n) < smallest_difference:
#             smallest_difference = abs(m - n)

# print(smallest_difference)

#Efficient code with stonger ideas and no cheating

import math

def is_pentagonal(num):
    # Solve: n(3n - 1)/2 = num
    # 3n^2 - n - 2*num =  W0
    # n = (1 + sqrt(1 + 24*num)) / 6
    discriminant = 1 + 24 * num
    sqrt_disc = math.isqrt(discriminant)
    if sqrt_disc * sqrt_disc != discriminant:  # Must be perfect square
        return False
    n = (1 + sqrt_disc) // 6
    return n > 0 and n * (3 * n - 1) == 2 * num

def pentagonal(n):
    return n * (3 * n - 1) // 2

# Generate pentagonal numbers and test pairs
smallest_difference = None
n = 1
while True:
    pn = pentagonal(n)
    for k in range(1, n):
        pk = pentagonal(k)
        diff = pn - pk
        if is_pentagonal(diff) and is_pentagonal(pn + pk):
            if smallest_difference is None or diff < smallest_difference:
                smallest_difference = diff
                print(f"Found pair: P_{k}={pk}, P_{n}={pn}, D={diff}")
    n += 1
    if smallest_difference is not None and pn > smallest_difference * 2:
        break  # Heuristic: if pn exceeds 2*D, smaller D unlikely

print("Smallest difference:", smallest_difference)
