import sys

t, s = sys.stdin.readline().split()
t = int(t)

if t == 2:  # snake
    words = s.split('_')
else:  # camel or pascal
    words = []
    word = s[0].lower()
    for c in s[1:]:
        if c.isupper():
            words.append(word)
            word = c.lower()
        else:
            word += c
    words.append(word)

camel = words[0] + ''.join(w.capitalize() for w in words[1:])
snake = '_'.join(words)
pascal = ''.join(w.capitalize() for w in words)

print(camel)
print(snake)
print(pascal)