import sys
n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(input())

dic = {}
count = 0
for num in array:
    complement = x - num
    if complement in dic:
        count += 1
    dic[num] = True

print(count)