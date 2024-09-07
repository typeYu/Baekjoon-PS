# 세 가지 경우: [안먹, 먹, 먹], [먹,안먹,먹], [먹, 먹, 안먹] 인데
# 첫 번째 케이스 같은 경우에는 지금까지 d에 저장되어 있는 수가 d[i - 4]임
import sys
n = int(sys.stdin.readline().strip())
wine = []
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    wine.append(a)

d = [0 for _ in range(n)]
d[0] = wine[0]
if n > 1:
    d[1] = wine[0] + wine[1]
    for i in range(2, n):
        d[i] = max(d[i - 3] + wine[i - 1] + wine[i], d[i - 2] + wine[i], d[i - 1])

print(max(d))