n = int(input())

def genf(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

for i in genf(n):
    print(i, end=", ")