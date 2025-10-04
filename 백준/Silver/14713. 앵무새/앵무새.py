from collections import deque
N = int(input())
words = []
for _ in range(N):
    words.append(deque(input().split()))
L = list(input().split())

for l in L:
    for word in words:
        if len(word) > 0 and word[0] == l:
            word.popleft()
            break
    # 문장 L이 앵무새가 말한 말 중 없을 때
    else:
        print("Impossible")
        exit()

for word in words:
    if len(word) != 0:
        print("Impossible")
        exit()
else:
    print("Possible")