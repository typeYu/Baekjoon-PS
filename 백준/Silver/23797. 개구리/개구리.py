import sys
S = sys.stdin.readline().strip()
dic = {'K': 0, 'P': 0}

if S[0] == 'K':
    dic['K'] += 1
else:
    dic['P'] += 1

for s in S[1:]:
    if s == 'K':
        if dic['P'] > 0:
            dic['P'] -= 1
        dic['K'] += 1
    elif s == 'P':
        if dic['K'] > 0:
            dic['K'] -= 1
        dic['P'] += 1

print(sum(dic.values()))