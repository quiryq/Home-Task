class Prime():
    def __init__(self, list1):
        self.list1 = list1
    def is_prime(self):
        list12 = []
        for i in self.list1:
            x = 0
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    x += 1
            if x == 0:
                list12.append(i)
        return list12

list11 = list(map(int, input().split()))
fun = Prime(list11)
print(fun.is_prime())