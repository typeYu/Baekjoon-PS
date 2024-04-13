def fibo(N):
    if N == 1 or N == 2:
        return 1
    return fibo(N - 1) + fibo(N - 2)

def dp(N):
    d = [0] * 100
    d[1] = 1
    d[2] = 1
    count = 0
    for i in range(3, N+1):
        count += 1
        d[i] = d[i-1] + d[i-2]
    return count

N = int(input())
print(fibo(N), dp(N))