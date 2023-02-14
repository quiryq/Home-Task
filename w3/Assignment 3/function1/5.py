def permitation(strings):
    new_lists = []
    lists = list(strings)
    lists.sort()
    sets = set(lists)
    c = 1
    i = 1
    while i <= len(lists):
        c = c * i
        i += 1
    j = 1
    r = 1
    while j <= (len(lists) - len(sets))+1:
        r = r * j
        j += 1
    return c/r
strings = str(input())
print(permitation(strings))