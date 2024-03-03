import sys
from collections import deque
sys.setrecursionlimit(10**5)
N, K = map(int, sys.stdin.readline().strip().split())
array = []
for i in range(1, N+1):
    array.append(i)
array = deque(array)
result = []
def yose(array, n):
    while array:
        array.rotate(-n+1)
        num = array.popleft()
        result.append(num)
        yose(array, n)
yose(array, K)
print("<" + ", ".join(map(str, result)) + ">")