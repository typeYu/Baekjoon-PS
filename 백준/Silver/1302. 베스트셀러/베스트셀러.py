from collections import Counter
N = int(input())
array = []
for _ in range(N):
    array.append(input())
array.sort()
a = Counter(array).most_common(1)
for i in a:
    print(*i[0], sep="")