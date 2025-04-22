# C만큼 반복하면 시간초과가 됨, A = A ^ B XOR은 홀수만큼 연산 하면 A ^ B, 짝수 연산 하면 A가 됨
A, B, C = map(int, input().split())
# XOR = 같으면 0, 다르면 1
if C % 2 == 0:
    print(A)
else:
    print(A ^ B)