import sys
input = sys.stdin.readline

# 입력
ans = 0
for i in [3, 2, 1]:
    tmp = input().rstrip()

    if tmp not in ['Fizz', 'Buzz', 'FizzBuzz']:
        ans = int(tmp) + i

# 출력
if ans%3 == 0 and ans%5 == 0:
    print('FizzBuzz')
elif ans%3 == 0:
    print('Fizz')
elif ans%5 == 0:
    print('Buzz')
else:
    print(ans)