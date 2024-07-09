import sys
S = sys.stdin.readline().rstrip().replace('-', ' ')
S = S.split(' ')

# 맨 앞만 front_word가 아니면 한 단어이다?
front_word = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "l'", "d'", "qu'"]
vowel = ['a', 'e', 'i', 'o', 'u', 'h']

result = len(S)
for s in S:
    if s[:2] in front_word:
        if s[2] in vowel:
            result += 1

    elif s[:3] in front_word:
        if s[3] in vowel:
            result += 1

print(result)