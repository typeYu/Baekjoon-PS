S = input()
S1 = S.split('-')
result = sum(map(int, S1[0].split('+')))
for i in S1[1:]:
    result -= sum(map(int, i.split('+')))
print(result)