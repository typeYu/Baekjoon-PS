n = int(input())
student = input().split()
result = {i : 0 for i in student}

for _ in range(n) :
    a = list(input().split())
    for i in a :
        result[i] += 1

sort_dict = sorted(result.items(), key=lambda x: x[1], reverse=True)

for key, value in sort_dict:
    print(key, value)