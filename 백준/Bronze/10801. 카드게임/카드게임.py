import sys
A_list = list(map(int, sys.stdin.readline().strip().split()))
B_list = list(map(int, sys.stdin.readline().strip().split()))
a, b = 0, 0
for i in range(10):
    if A_list[i] > B_list[i]:
        a += 1
    elif B_list[i] > A_list[i]:
        b += 1

if a > b:
    print("A")
elif a == b:
    print("D")
else:
    print("B")