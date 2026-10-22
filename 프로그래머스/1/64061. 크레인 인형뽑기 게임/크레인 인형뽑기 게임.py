def solution(board, moves):
    answer = 0
    stack = []
    l = len(board)
    for m in moves:
        for i in range(l):
            doll = board[i][m - 1]
            if doll:
                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                board[i][m - 1] = 0
                break

    return answer