import sys
N = int(sys.stdin.readline().rstrip())
people = []
for _ in range(N):
    people.append(int(sys.stdin.readline().rstrip()))

people.sort(reverse=True)
result = 0
for i in range(N):
    money = people[i] - i
    if money >= 1:
        result += money
print(result)