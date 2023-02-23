def genf(n):
    for i in range(n, -1, -1):
        yield i

for i in genf(int(input())):
    print(i)