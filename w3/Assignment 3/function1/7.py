def dublicates(lists):
    a = 0
    for i in range(len(lists) -1):
        if lists[i] == lists[i+1] and lists[i] == 3:
            a += 1
    tf = ""
    if a >= 1:
        tf = "True"
    else:
        tf = "False"
        
number = int(input())
lists = list(map(int,input().strip().split()))
print(dublicates)
