S = input()
dic = {}
for i in S: # 개수 저장
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

countOdd, Odd = 0, ''
for s, num in dic.items(): # 홀수가 두개 이상이면 종료
    if num % 2 == 1:
        countOdd += 1
        Odd = s
    if countOdd >= 2:
        print("I'm Sorry Hansoo")
        exit()

dicSorted = sorted(dic.items(), key=lambda x: x[0])
result = ''

for s, num in dicSorted:
    for i in range(num // 2):
        result += s

print(result + Odd + result[::-1])