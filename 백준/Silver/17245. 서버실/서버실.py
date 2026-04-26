N = int(input())
comp = []
for _ in range(N) :
  comp.extend(list(map(int, input().split())))
 
total = sum(comp)
comp.sort()
 
answer = []  # 정답 후보 시간들 저장
target = total / 2
start, end = 0, comp[-1]  # 쌓여 있는 컴퓨터의 최소 개수와 최대 개수
 
while (start <= end) :
  mid = (start + end) // 2
  temp = 0  # 동작하는 컴퓨터의 수
  for i in range(N**2) :
    if comp[i] >= mid :
      temp += mid
    else :
      temp += comp[i]
 
  if temp < target :
    start = mid + 1
  else :
    end = mid - 1
    answer.append(mid)
print(min(answer))