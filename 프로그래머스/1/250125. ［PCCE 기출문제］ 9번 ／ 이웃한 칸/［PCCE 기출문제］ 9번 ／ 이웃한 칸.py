def solution(board, h, w):
    d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    l = len(board)
    
    answer = 0
    for dy, dx in d:
        ny, nx = h + dy, w + dx
        if 0 <= ny < l and 0 <= nx < l and board[ny][nx] == board[h][w]:
            answer += 1
    
    return answer