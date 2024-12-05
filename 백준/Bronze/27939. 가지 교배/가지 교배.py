import sys
input = sys.stdin.readline

# 입력
n = int(input())
kind = list(input().rstrip().split())
m, k = map(int, input().split())    # 조수와 품종의 수

assist = []
for _ in range(m):
    assist.append(list(map(int, input().split())))

# 조수들은 모두 흰색이어야 W 가능
# 교수는 흰색 한 1개라도 있어야 W 가능
for i in assist:
    for j in i:
        if kind[j-1] == "P":
            break;
    else:
        print("W")
        break;
else:
    print("P")