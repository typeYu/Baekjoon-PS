import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
array = [] # [점수, 사람] 형식으로 저장해서 정렬 할 배열
result = dict() # 결과를 출력 할 딕셔너리

for _ in range(N):
    name, score = sys.stdin.readline().strip().split()
    if X * 0.05 <= int(score): # 전체 득표율의 5% 이상이면
        result[name] = 0
        for i in range(1, 15): # 1부터 14까지 나눈 값의 점수 집합을 구함
            array.append([int(score) / i, name]) # [점수, 사람] 형식으로 저장

array.sort(key=lambda x: -(x[0])) # 점수를 큰 순으로 정렬
for k in range(14):
    result[array[k][1]] += 1

result = sorted(result.items(), key=lambda x:(x[0])) # 결과를 이름 순 정렬
for r in result:
    print(*r)