from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
array = list(map(int, input().split()))
lcm_num = array[0]
for i in range(1, N):
    lcm_num = lcm(array[i], lcm_num)

sum_num = 0
for a in array:
    sum_num += lcm_num // a

# 기약 분수로 만들어야 한다..
divide = gcd(lcm_num, sum_num)
lcm_num //= divide
sum_num //= divide
print(f"{lcm_num}/{sum_num}")