import sys
N = sys.stdin.readline().strip()
dic = {i: 0 for i in range(10)}
for n in N:
    dic[int(n)] += 1

if (dic[6] + dic[9]) % 2 == 0:
    count_69 = (dic[6] + dic[9]) // 2
else:
    count_69 = (dic[6] + dic[9]) // 2 + 1
count_other = max(dic[0], dic[1], dic[2], dic[3], dic[4], dic[5], dic[7], dic[8])

print(max(count_other, count_69))
