#Euler 40
irratonal = [0]
for number in range(1,10 ** 7): 
    str_number =str(number)
    for digit in str_number:
        irratonal.append(digit)
# print(irratonal)
# for power in range(1 , 3):
#     print(int(irratonal[10 ** power]))

product = 1
for power in range(1, 7):
    product *= int(irratonal[10 ** power])
print(product)