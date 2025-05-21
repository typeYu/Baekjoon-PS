n, k = map(int, input().split())
array = list(map(int, input().split()))

sum = 0
for i in array:
    if i % 2==0:  # 멀티탭 구의 수가 짝수
        sum += i//2
    else:  # 멀티탭 구의 수가 홀수
        sum += i // 2 + 1

if n <= sum:  # 멀티탭 구의 수가 충분하면
    print("YES")
else:  # 멀티탭 구의 수가 모자라면
    print("NO")