# #Euler 48
# # Define the modulus for the last 10 digits
# # MOD = 10**10

# # # Initialize the sum
# # total = 0

# # # Compute the sum from 1^1 to 1000^1000
# # for n in range(1, 1001):  # 1001 because range is exclusive of upper bound
# #     # Compute n^n mod 10^10 efficiently
# #     term = pow(n, n, MOD)
# #     # Add to total and keep it within mod 10^10
# #     total = (total + term) % MOD

# # # Format the result as a 10-digit string, padding with zeros if needed
# # result = f"{total:010d}"
# # print(result)

# def pow_to_ten_digits(n: int, p: int) -> int:
#     if p == 1:
#         return n
#     res = str(n * pow_to_ten_digits(n, p - 1))
#     return int(res[-10:])

# s = 0
# for i in range(1, 1001):
#     s += pow_to_ten_digits(i, i)

# print(str(s)[-10: ])

print(str(sum([i**i for i in range(1,1001)]))[-10:])
print(999 ** 999)