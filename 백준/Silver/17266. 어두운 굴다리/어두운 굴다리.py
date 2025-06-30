D = int(input())
N = int(input())

nums = list(map(int,input().split()))

dist = [ nums[0]]+[ (nums[i]-nums[i-1]+1)//2 for i in range(1,N)]+[D-nums[-1]]

print(max(dist))