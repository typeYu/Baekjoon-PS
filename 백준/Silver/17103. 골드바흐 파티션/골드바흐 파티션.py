T = int(input())

discrimination = [True] * 1000001
for i in range(2, 1000001):
    if discrimination[i]:
        for j in range(i * 2, 1000001, i): # i는 소수로 놔두고 배수부터 끝까지 i만큼 더해가며 false처리
            discrimination[j] = False

for _ in range(T):
    N = int(input())
    count = 0
    for i in range(2, N // 2 + 1): # 소수를 판별하고 중복을 세지 않기 위해 2부터 N // 2 + 1까지만 세기
        if discrimination[i] and discrimination[N - i]:
            count += 1
    print(count)