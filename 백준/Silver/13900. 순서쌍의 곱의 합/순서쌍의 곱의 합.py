N = int(input())
array = list(map(int, input().split()))
sumArray = sum(array)
result = 0
for i in array:
    sumArray -= i
    result += sumArray * i
print(result)