a = int(input())
b = int(input())
x = int(input())
y = int(input())

if a == x or b == y or abs(a - x) == abs(b - y):
    print("YES")
else:
    print("NO")
