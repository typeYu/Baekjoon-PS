from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}:", end=' ')
    c = combinations([i for i in range(1, 12)], 2)
    is_S = False
    for a, b in c:
        if a < b and a + b == n:
            if is_S:
                print(", ", end='')
            print(f"{a} {b}", end='')
            is_S = True
        
    print()