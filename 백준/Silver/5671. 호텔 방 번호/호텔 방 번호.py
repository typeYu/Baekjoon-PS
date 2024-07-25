while True:
    try:
        N, M = map(int, input().split())
    except:
        break

    result = 0
    for i in range(N, M+1):
        is_repeat = False
        dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0}
        for j in str(i):
            dic[j] += 1

        for k in dic.values():
            if k >= 2:
                is_repeat = True
                break

        if is_repeat == False:
            result += 1

    print(result)