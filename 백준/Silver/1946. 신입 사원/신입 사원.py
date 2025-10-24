import sys
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    answer = 1
    people = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        people.append([a, b])
    people.sort()
    min_b = people[0][1]

    for i in range(1, N):
        if min_b < people[i][1]:
            continue
        else:
            min_b = people[i][1]
            answer += 1

    print(answer)