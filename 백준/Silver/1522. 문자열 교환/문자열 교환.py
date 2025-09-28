import sys
S = sys.stdin.readline().strip()
a_cnt = S.count('a')
answer = float('inf')
for i in range(len(S)):
    if i + a_cnt < len(S):
        answer = min(answer, S[i:i + a_cnt].count('b'))
    else:
        word = S[i:len(S)]
        for w in range(a_cnt - len(word)):
            word += S[w]
        answer = min(answer, word.count('b'))

print(answer)