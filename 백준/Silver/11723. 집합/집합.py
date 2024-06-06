import sys
M = int(sys.stdin.readline().strip())
array = set()
for _ in range(M):
    inputValue = sys.stdin.readline().strip().split()
    a = inputValue[0]
    if len(inputValue) == 2:
        num = int(inputValue[1])
    if a == 'add':
        array.add(num)
    elif a == 'remove':
        if num in array:
            array.remove(num)
    elif a == 'check':
        print(1 if num in array else 0)
    elif a == 'toggle':
        if num in array:
            array.remove(num)
        else:
            array.add(num)
    elif a == 'all':
        array = set(range(1, 21))
    elif a == 'empty':
        array = set()