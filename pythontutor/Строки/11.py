s = input()

for i in range(len(s)):
    print(s[i] if i % 3 != 0 else "", end="")