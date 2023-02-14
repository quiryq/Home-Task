def polindrome(string):
    left = string[0:int(len(string) / 2)]
    right = string[int(len(string)/2 + 1):len(string)]
    if left[len(left)::-1] == right:
        return True
    else:
        return False
string = str(input())
print(polindrome(string))
def histogram(list):
    histo = ""
    for i in range(len(list)):
        if i == 0:
            histo += "*"*list[i]
        else:
            histo += "\n" + "*"*list[i]
    return histo
n = int(input())
list = list(map(int,input().strip().split()))[:n]
print (histogram(list))