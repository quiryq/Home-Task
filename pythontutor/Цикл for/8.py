import math as m

n = int(input())
sum = 0

for i in range(n):
    sum += m.factorial(i +1)

print(sum)