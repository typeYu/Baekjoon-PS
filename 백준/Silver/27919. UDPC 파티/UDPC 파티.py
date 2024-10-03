import math
S = input()
count_uc, count_dp = 0, 0
for s in S:
    if s == "C" or s == "U":
        count_uc += 1
    elif s == "D" or s == "P":
        count_dp += 1

if count_uc > math.ceil(count_dp / 2):
    print("U", end='')
if count_dp > 0: # count_uc가 전부 C이면 가능성 있어서
    print("DP", end='')
