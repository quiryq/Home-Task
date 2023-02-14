n = int(input())
fa = 1

for i in range(n):
    fa *= (i+1)
    
print(fa)