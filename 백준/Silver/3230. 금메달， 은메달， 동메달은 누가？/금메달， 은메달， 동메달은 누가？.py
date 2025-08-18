import sys

input = sys.stdin.readline;
N, M = map(int, input().split());

first_rank = [];
for i in range(1, N + 1):
    r = int(input());
    first_rank.insert(r - 1, i);

qualifiers = first_rank[:M];
start_order = list(reversed(qualifiers));

second_rank = [];
for athlete in start_order:
    r2 = int(input());
    second_rank.insert(r2 - 1, athlete);

print(second_rank[0]);
print(second_rank[1]);
print(second_rank[2]);
