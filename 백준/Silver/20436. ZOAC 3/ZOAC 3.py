sl, sr = map(str, input().split())
S = input()

leftKey = {'q': (0, 0), 'w': (1, 0), 'e': (2, 0), 'r': (3, 0), 't': (4, 0),
           'a': (0, 1), 's': (1, 1), 'd': (2, 1), 'f': (3, 1), 'g': (4, 1),
           'z': (0, 2), 'x': (1, 2), 'c': (2, 2), 'v': (3, 2)}
rightKey = {'y': (5, 0), 'u': (6, 0), 'i': (7, 0), 'o': (8, 0), 'p': (9, 0),
            'h': (5, 1), 'j': (6, 1), 'k': (7, 1), 'l': (8, 1),
            'b': (4, 2), 'n': (5, 2), 'm': (6, 2)}

left, right = sl, sr
result = 0
for i in S:
    if i in leftKey:
        result += abs(leftKey[left][0] - leftKey[i][0]) + abs(leftKey[left][1] - leftKey[i][1])
        left = i
        result += 1
    if i in rightKey:
        result += abs(rightKey[right][0] - rightKey[i][0]) + abs(rightKey[right][1] - rightKey[i][1])
        right = i
        result += 1

print(result)