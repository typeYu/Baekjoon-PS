import sys
vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    S = sys.stdin.readline().strip()
    if S == 'end':
        break
    is_vowel = False
    for s in S:
        if s in vowel:
            is_vowel = True

    is_two = False
    for s in range(len(S) - 1):
        if S[s] == S[s + 1]:
            if S[s] == 'e' or S[s] == 'o':
                continue
            else:
                is_two = True

    is_three = False
    for s in range(len(S) - 2):
        if S[s] in vowel and S[s + 1] in vowel and S[s + 2] in vowel:
            is_three = True
        elif S[s] not in vowel and S[s + 1] not in vowel and S[s + 2] not in vowel:
            is_three = True

    if is_vowel and not is_two and not is_three:
        print(f"<{S}> is acceptable.")
    else:
        print(f"<{S}> is not acceptable.")