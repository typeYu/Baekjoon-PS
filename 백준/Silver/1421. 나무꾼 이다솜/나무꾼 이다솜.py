# 특정 길이로 잘랐을 때 비용이 음수가 되는 나무는 굳이 잘라서 판매할 필요가 없음 주의
# 5,5,6인데 자르는 비용 10, 비용 1일 때 5 2개 팔면 최댓값
N, C, W = map(int, input().split())
woods = []
for _ in range(N):
    woods.append(int(input()))

max_cost = 0
for i in range(1, max(woods) + 1): # 제일 작은 나무 조각(1)부터 제일 큰 나무 길이까지 짤라보기
    total = 0
    for j in range(len(woods)):
        if woods[j] // i == 0:
            continue
        else:
            cut_cost, quot = woods[j] // i, woods[j] // i # 이 나무의 자르는 횟수와 몇 개의 똑같은 길이가 나오는지
            if woods[j] % i == 0:
                cut_cost -= 1
            each_cost = (quot * i * W) - (cut_cost * C)
            if each_cost > 0:
                total += each_cost

    max_cost = max(max_cost, total)

print(max_cost)