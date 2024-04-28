from collections import deque
N, K, T = map(int, input().split())
array = list(map(int, input().split()))
mini, maxi = [], []
for i in array:
    if i >= T:
        maxi.append(i)
    else:
        mini.append(i)
maxi.sort()
mini.sort()
maxi = deque(maxi)
for _ in range(K):
    if not mini:
        break
    else:
        T += mini.pop()
        while maxi and T > maxi[0]:
            mini.append(maxi.popleft())
print(T)