L, C = map(int, input().split())
array = list(map(str, input().split()))
array.sort()
word = []
def backtraking(depth):
    global word
    if len(word) == L:
        a, b = 0, 0
        for i in word:
            if i in ['a', 'e', 'i', 'o', 'u']:
                a += 1
            else:
                b += 1
        if a >= 1 and b >= 2:
            print("".join(word))
    for i in range(depth, len(array)):
        if array[i] not in word:
            word.append(array[i])
            backtraking(i+1)
            word.pop()
backtraking(0)