a, b = int(input()), int(input()) -1

if a % 2 == 0:
    for i in range(a - 1, b, -2):
        print(i)
else:
    for i in range(a, b, -2):
        print(i)