import sys


def cnt():
    if dic["A"] >= A and dic["C"] >= C and dic["G"] >= G and dic["T"] >= T:
        return 1
    return 0


S, P = map(int, sys.stdin.readline().strip().split())
string = sys.stdin.readline().strip()
A, C, G, T = map(int, sys.stdin.readline().strip().split())
answer = 0
dic = {"A": 0, "C": 0, "G": 0, "T": 0}

# 초깃값
for char in string[:P]:
    dic[char] += 1

answer += cnt()

start, end = 0, P
for i in range(S - P):
    dic[string[start]] -= 1
    dic[string[end]] += 1
    answer += cnt()

    start += 1
    end += 1

print(answer)