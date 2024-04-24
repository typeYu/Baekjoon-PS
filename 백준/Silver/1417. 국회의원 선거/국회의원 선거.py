N = int(input())
array = []
dasom = int(input())
for _ in range(N-1):
    array.append(int(input()))
array.sort(reverse=True)
count = 0
if N == 1:
    print(0)
    exit()
while dasom <= array[0]:
    if array[0] >= dasom:
        array[0] -= 1
        dasom += 1
        count += 1
    array.sort(reverse=True)
print(count)