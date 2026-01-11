# union find 함수 선언이 아니라 set 활용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])
parties = [] # 모든 진실을 알고 있는 사람들 추가 후 다시 파티 cnt를 세야 하기 때문에 선언

for _ in range(m):
    parties.append(set(list(map(int, input().split()))[1:]))

for _ in range(m):
    for party in parties: # 각 파티마다
        if party & truth: # 만약 현재 파티에 있고 진실을 알고 있는 사람이 있다면
            truth.update(party)

cnt = 0
for party in parties:
    if not (party & truth): # 만약 현재 파티에 있고 진실을 알고 있는 사람이 없다면
        cnt += 1

print(cnt)