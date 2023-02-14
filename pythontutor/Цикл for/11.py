n = int(input())
b = n
p = 0

for i in range(1, n):
    b += i
    p += int(input())

print(b - p)