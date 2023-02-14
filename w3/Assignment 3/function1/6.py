def reverses(string):
    new_string = " h"
    lists = list(string)
    lists.reverse()
    for i in lists:
        new_string.format(i)
    return new_string
lists = []
string = str(input())
print(reverses(string))
