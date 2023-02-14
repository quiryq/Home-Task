a, b = int(input()), int(input()) + 1
d = 1


if a > b:
    d = -1
    b -= 2

for i in range(a, b, d):
    print(i)