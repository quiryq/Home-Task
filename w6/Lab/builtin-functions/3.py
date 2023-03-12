def isPali(s):
    return s == s[::-1]
ans = isPali("polilop")
if ans:
    print("Yes")
else:
    print("No")