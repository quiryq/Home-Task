def genf(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for i in genf(int(input()), int(input())):
    print(i)