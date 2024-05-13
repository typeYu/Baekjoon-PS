T = int(input())
d = [1] * 10000
for i in range(2, 10000):
    d[i] = d[i-1] + d[i-2]
for i in range(1, T+1):
    P, Q = map(int, input().split())
    a = d[P - 1] % Q
    print(f"Case #{i}: {a}")