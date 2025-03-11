# dp표의 세로가 자릿수인건 쉬운데, 가로 기준이 자릿 수의 뒷 번호인게 어려웠음. 당연하게 첫 번호가 0일 때로 풀었는데 그러면 안 됐음
n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]

print(sum(dp)%10007)