def agent(lists):
    zero = 0
    seven = 0
    booler = True
    for i in range(len(lists)):
        if seven != 1 and zero < 3:
            if lists[i] == 0:
                zero += 1
            elif lists [i] == 7:
                seven += 1
        elif (seven == 1 and zero == 2):
            break
        else:
            booler = False
            break
    return booler
n = int(input())
lists = list(map(int,input().strip().split())) [:n]
print(agent(lists))

def spy_game(list):
    che = True
    for i in range(len(list)):
        if list[i] == 7:
            che = True
        elif list[i] == 0:
            che = False
    return che

n = int(input())
list = list(map(int,input().strip().split()))[:n]
print(spy_game(list))