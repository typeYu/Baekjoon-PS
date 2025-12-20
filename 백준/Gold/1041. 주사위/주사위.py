N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    answer = 0

    facet_1 = (N - 1) * (N - 2) * 4 + (N - 2) ** 2
    facet_2 = (N - 1) * 4 + (N - 2) * 4
    facet_3 = 4

    min_facet = list()
    min_facet.append(min(dice[0], dice[5]))
    min_facet.append(min(dice[1], dice[4]))
    min_facet.append(min(dice[2], dice[3]))
    min_facet.sort()

    answer += facet_1 * min_facet[0] + facet_2 * sum(min_facet[:2]) + facet_3 * sum(min_facet)

    print(answer)