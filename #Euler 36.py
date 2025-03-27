#Euler 36

#This functions take n in decimal and spits out n in base 2 
def binary(n):
    binary = []
    i  = 0
    while n >= 1: 
        binary.append( n % 2)
        n = int(n / 2)
        i += 1
        int_binary = binary[::-1]
    return int(''.join(map(str, int_binary)))


def is_palindrome(number): 
    list = []
    str_number = str(number)
    for digit in str_number:
        list.append(digit)
    if list[::-1] == list:
        return True
    else:
        return False
    


sum = 0
for k in range(1,10 ** 6):
    if is_palindrome(k) == True and is_palindrome(binary(k)) == True:
        sum += k
print(sum)



        
