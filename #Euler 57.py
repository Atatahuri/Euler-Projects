#Euler 57

from fractions import Fraction

sqrt2_list = []
sqrt2 = []
sqrt2_list.append(Fraction(1,2))
for i in range (1, 1001):
    sqrt2_list.append(Fraction (1, 2 + sqrt2_list[i - 1]))
    sqrt2.append(1 + sqrt2_list[i - 1])


     

counter = 0 

for numbers in sqrt2:
    if len(str(numbers.numerator)) > len(str(numbers.denominator)): 
        counter += 1
print(counter)


     

