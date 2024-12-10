import sys
num = sys.stdin.readline().strip()
odd = [1, 3, 5, 7, 9]
maxNum, minNum = 0, float('inf')

def recursion(num, count):
    global minNum, maxNum

    if len(num) == 1:
        if int(num) in odd:
            count += 1
        maxNum = max(maxNum, count)
        minNum = min(minNum, count)
        return
    elif len(num) == 2:
        for i in range(2):
            if int(num[i]) in odd:
                count += 1
        recursion(str(int(num[0]) + int(num[1])), count)
    else:
        for n in num:
            if int(n) in odd:
                count += 1

        for i in range(2, len(num)):
            for j in range(1, i):
                recursion(str(int(num[0:j]) + int(num[j:i]) + int(num[i:len(num) + 1])), count)

recursion(num, 0)
print(minNum, maxNum)