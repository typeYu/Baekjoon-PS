arr = list(map(int, input().split()))
group1 = max(arr) + min(arr)
print(abs(sum(arr) - group1 * 2))