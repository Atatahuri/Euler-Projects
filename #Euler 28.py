#Number Spiral Diagonals(Euler 28)
initial = 1
sum = 1
for n in range(1, 501):
    i = 0
    while i < 4:
        initial += 2 * n
        sum += initial
        i += 1
print(sum)

