def ma(n):
    u = 0
    l = 0
    for i in n:
        if i.isupper()== True:
            u += 1
        else:
            l +=1
    print("uppercas:", u, "lower:", l)
ma("sadAS")