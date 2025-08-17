for i in range(1, int(input()) + 1):
    G = list(map(int, input().split()))
    S = list(map(int, input().split()))
    G_score = G[0] + G[1] * 2 + (G[2] + G[3]) * 3 + G[4] * 4 + G[5] * 10
    S_score = S[0] + (S[1] + S[2] + S[3]) * 2 + S[4] * 3 + S[5] * 5 + S[6] * 10
    if G_score > S_score:
        print(f"Battle {i}: Good triumphs over Evil")
    elif G_score < S_score:
        print(f"Battle {i}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i}: No victor on this battle field")