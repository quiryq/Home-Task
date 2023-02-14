def prime(lists):
    for number in lists:
        check = True
        for i in range(2,int(number/2)):
            if number % i == 0:
                check = False
        if check and number != 4 and number != 1:
            prime_numbers.append(number)
    return prime_numbers
prime_numbers=[]
n = int(input())
lists = list(map(float,input().strip().split()))[:n]
print(prime(lists))