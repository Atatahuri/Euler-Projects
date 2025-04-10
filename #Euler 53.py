#Euler 53

def factorial(n):
    factorial = 1 
    for i in range (1, n + 1):
        factorial *= i
    return factorial

def choose(n,r): 
    return factorial(n) / (factorial(r) * factorial( n - r))


count = 0
for r in range(1, 101):
    for n in range(r, 101): 
        if choose(n,r) > 10 ** 6:
            count += 1
print(count)

