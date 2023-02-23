n = int(input())

def power(n):
    for i in range(0, n + 1):
        yield i ** 2

for i in power(n):
    print(i)