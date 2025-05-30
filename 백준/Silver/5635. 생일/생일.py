n = int(input())
students = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    dd, mm, yyyy = int(dd), int(mm), int(yyyy)
    students.append((yyyy, mm, dd, name))
students.sort()

print(students[-1][3])
print(students[0][3])
