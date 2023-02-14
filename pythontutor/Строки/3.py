s = input()
x = (len(s) // 2 + 1 if len(s) % 2 != 0 else len(s) // 2)

for i in range(x, len(s)):
    print(s[i], end="")
for i in range(x):
    print(s[i], end="")
