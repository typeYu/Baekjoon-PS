N = int(input())
array = list(map(int, input().split()))

# N == 1일 때 유의
if N == 1:
    print(1)
    exit()

array.sort()
grp_biggest = [array[0], array[1]]
answer = 2

for i in range(2, N):
    if array[i] > grp_biggest[0]:
        grp_biggest.remove(grp_biggest[0])
        grp_biggest.append(array[i])
        grp_biggest.sort()
        answer += 1

print(answer)