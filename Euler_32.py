# #Euler 32
import os
unique_products = set()  # Use a set to avoid duplicates

# Check if a number string is 1-9 pandigital
def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")

# Try different multiplicand/multiplier splits that yield 9-digit concatenations
for multiplicand in range(1, 100):  
    for multiplier in range(1, 10000 // multiplicand):  
        product = multiplicand * multiplier
        combined = f"{multiplicand}{multiplier}{product}"

        # Check if it's a 1-9 pandigital number
        if is_pandigital(combined):
            unique_products.add(product)

# Compute the sum of unique products
result = sum(unique_products)
print("Sum of all pandigital products:", result)
print("Current file path:", os.path.abspath(__file__))
