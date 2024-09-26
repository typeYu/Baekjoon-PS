import sys
W, S = map(int, sys.stdin.readline().strip().split())
S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()

dic_S1, dic_S2 = {}, {}
for i in range(ord('a'), ord('z') + 1):
    dic_S1[chr(i)] = 0
    dic_S2[chr(i)] = 0
for i in range(ord('A'), ord('Z') + 1):
    dic_S1[chr(i)] = 0
    dic_S2[chr(i)] = 0

for s in S1:
    dic_S1[s] += 1

result = 0
String = S2[0:W]
for i in String:
    dic_S2[i] += 1
if dic_S1 == dic_S2:
    result += 1

for i in range(S - W):
    delete_string, new_string = S2[i], S2[i + W]
    dic_S2[delete_string] -= 1
    dic_S2[new_string] += 1
    if dic_S1 == dic_S2:
        result += 1

print(result)
