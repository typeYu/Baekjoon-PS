people = list(map(int, input().split()))
x, _, _ = list(map(int, input().split()))

print(people.index(x) + 1 if x in people else 0)