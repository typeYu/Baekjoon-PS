N = int(input())
people = list(map(int, input().split()))
people.sort()
result = 0
for i in range(len(people) + 1): #1,2,3,4,5
    for j in range(i):
        result += people[j]
print(result)