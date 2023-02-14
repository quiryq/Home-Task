s = input()

print(s[2])
print(s[-2])
print(s[:5])
print(s[:len(s) - 2])

for i in range(len(s)):
    print(s[i] if i % 2 == 0 else "", end="")
print()
for i in range(len(s)):
    print(s[i] if i % 2 != 0 else "", end="")
print()
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")
print()
for i in range(len(s) - 1, -1, -2):
    print(s[i], end="")
print()
print(len(s))