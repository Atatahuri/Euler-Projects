#Euler 33


# for nominator in range(10 , 100): 
#     for denominator in range(nominator + 1 , 100): 
#         # string_nominator  = str(nominator)
#         # string_denominator = str(denominator)
#         # for index in range(2): 
#         #      list_nominator[index] = string_nominator[index]
#         #      list_denominator[index] = string_denominator[index]
#         list_nominator = []
#         list_denominator = []
#         list_nominator = [int(digit) for digit in str(nominator)]
#         list_denominator = [int(digit) for digit in str(denominator)]
#         if list_nominator[0] == list_denominator[0]:
#             list_nominator.remove(list_nominator[0])
#             list_denominator.remove(list_denominator[0])
#         elif list_nominator[1] == list_denominator[0]:
#             list_nominator.remove(list_nominator[1])
#             list_denominator.remove(list_denominator[0])
#         elif list_nominator[0] == list_denominator[1]:
#             list_nominator.remove(list_nominator[0])
#             list_denominator.remove(list_denominator[1])
#         elif list_nominator[1] == list_denominator[1]:
#             list_nominator.remove(list_nominator[1])
#             list_denominator.remove(list_denominator[1])
#         else: 
#             break
#         if list_denominator[0] != 0 and list_nominator[0] / list_denominator[0] == nominator/denominator:
#             print(str(nominator) +  "/" +  str(denominator))
        
from fractions import Fraction

product_numerator = 1
product_denominator = 1
for numerator in range(10,100):
    for denominator in range (numerator + 1, 100): 
        str_numerator = str(numerator)
        str_denominator = str(denominator)
        for digit in str_numerator: 
            if digit not in str_denominator:
                continue
        for digit in str_numerator:
            if digit in str_denominator and digit != '0':
                reduced_numerator = str_numerator.replace(digit, '',1)
                reduced_denominator = str_denominator.replace(digit, '',1)
                if reduced_numerator and reduced_denominator: 
                    reduced_numerator = int(reduced_numerator)
                    reduced_denominator = int(reduced_denominator)
                    if reduced_denominator != 0 and (reduced_numerator / reduced_denominator) == (numerator / denominator): 
                        print(str(numerator) + "/" + str(denominator))
                        product_numerator *= numerator
                        product_denominator *= denominator
Answer = Fraction(product_numerator, product_denominator)                       
print(Answer)

            
        
        
    
            
