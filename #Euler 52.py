#Euler 52
digit_set = set()
digit_set_x = set()

number = 100000
for x in range(2,7):
    str_number = str(number)
    for digit in str_number: 
        digit_set.add(digit)
    str_number_x= str(number * x)
    for digit in str_number_x:
        digit_set_x.add(digit)
    if digit_set != digit_set_x:
        number += 1
        x = 2
    else:
        digit_set_x = set()

limit = 1000000000    
if number < limit: 
    print(number)

# def has_same_digits(x):
#     base_digits = sorted(str(x))
#     for i in range(2, 7):
#         if sorted(str(i * x)) != base_digits:
#             return False
#     return True

# number = 1
# while True:
#     if has_same_digits(number):
#         print(number)
#         break
#     number += 1