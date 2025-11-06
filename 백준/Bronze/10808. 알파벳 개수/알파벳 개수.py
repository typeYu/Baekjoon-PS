N = input()
array = [0]*26

for i in N:
    array[ord(i)-97] += 1
    
for i in array:
    print(i, end=' ')