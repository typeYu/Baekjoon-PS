import sys
N = sys.stdin.readline().strip()
one, zero = 0, 0
if N[0] == '1':
    one += 1
elif N[0] == '0':
    zero += 1
for i in range(len(N) - 1):
    if N[i] == '1' and N[i+1] == '0':
        zero += 1
    elif N[i] == '0' and N[i+1] == '1':
        one += 1

if zero >= one:
    print(one)
elif zero < one:
    print(zero)


