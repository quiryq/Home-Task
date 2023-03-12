def myp(*n):
    a = 1
    for i in n:
        a *=i
    return a
print(myp(1, 2, 3, 4))