#Euler34

def factorial(n): 
    if n == 0 or n == 1:
        return 1 
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact



factorial_list = []
for i in range(10): 
    factorial_list.append(factorial(i))

for number in range(1, 10 ** 7): 
    str_number = str(number)
    factorial_sum = 0
    for index in range(len(str_number)):
        factorial_sum += factorial_list[int(str_number[index])]
    if factorial_sum == number: 
        print(number)

