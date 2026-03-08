n, m = map(int, input().split())
a_list = list(map(int, input().split()))
safe = sum(a_list[i] - 1 for i in range(n))
print("OUT" if safe < m else "DIMI")