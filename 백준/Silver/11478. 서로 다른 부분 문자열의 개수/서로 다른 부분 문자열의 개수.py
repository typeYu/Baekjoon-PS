S = input()
length = len(S)
set = set()
for i in range(length):
    for j in range(1, length + 1):
        set.add(S[i:j])
set.remove("")
print(len(set))