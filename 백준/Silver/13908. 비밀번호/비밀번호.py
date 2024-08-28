from itertools import product
n, m = map(int, input().split())

if m != 0:
    count = 0
    allow = list(map(int, input().split()))
    pro = product([0,1,2,3,4,5,6,7,8,9], repeat=n)
    for i in pro:
        discrim = True
        for j in allow:
            if j not in i:
                discrim = False
                break
        if discrim == True:
            count += 1
    print(count)
else:
    print(10 ** n)