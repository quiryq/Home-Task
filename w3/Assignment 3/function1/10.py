def unique(list):
    i = 0
    while i < len(list):
        j = 0
        while j < len(list):
            if list[i] == list[j] and i!=j:
                list.pop(j)
            j += 1
        i += 1
    return list
n = int(input())
list = list(map(str,input().strip().split()))[:n]
print (unique(list))