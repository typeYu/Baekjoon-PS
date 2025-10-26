import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
dic = {'B': 0, "S": 0, 'A': 0}
for s in S:
    dic[s] += 1

if dic['B'] == dic['S'] == dic['A']:
    print("SCU")
else:
    if dic['B'] == max(dic.values()):
        print('B', end='')
    if dic['S'] == max(dic.values()):
        print('S', end='')
    if dic['A'] == max(dic.values()):
        print('A', end='')