import sys
for _ in range(int(sys.stdin.readline())):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    dic = {}

    # W를 한 번 순회하며 문자열: 인덱스 형태로 딕셔너리에 저장
    for i in range(len(W)):
        if W[i] not in dic:
            dic[W[i]] = [i]
        else:
            dic[W[i]].append(i)

    # 다시 딕셔너리를 한 바퀴 순회하며 어떤 문자를 K개 포함하는 가장 짧은 문자열과
    # 첫 번째와 마지막 글자가 같은 가장 긴 문자열을 구한다.

    shortest = float('inf') # 가장 짧은 연속문자열 길이
    longest = 0 # 가장 긴 연속문자열 길이

    for word in dic:
        if len(dic[word]) < K:
            continue

        for pcs in range(len(dic[word]) - K + 1):
            ans = dic[word][pcs + K - 1] - dic[word][pcs] + 1

            shortest = min(shortest, ans)
            longest = max(longest, ans)

    print(shortest, longest) if shortest != float('inf') else print(-1)