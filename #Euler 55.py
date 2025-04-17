# Euler 55 - Lychrel numbers below 10000
def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

def reversed_number(number): 
    str_number = str(number)
    return int(str_number[::-1])

lychrel_count = 0

for number in range(1, 10000):
    test_number = number
    is_lychrel = True
    
    for period in range(50):
        test_number = test_number + reversed_number(test_number)
        if is_palindrome(test_number):
            is_lychrel = False
            break
    
    if is_lychrel:
        lychrel_count += 1

print(number)
print(lychrel_count)
