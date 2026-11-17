def solution(n, m, board):
    board = [list(b) for b in board]
    
    def drop(): # 떨어뜨리는 함수
        for j in range(m):
            bottom = n - 1
            for i in range(n - 1, -1, -1):
                if board[i][j] != "X":
                    block = board[i][j]
                    board[i][j] = "X"
                    board[bottom][j] = block
                    bottom -= 1
    
    
    def remove(): # 2 * 2인지 확인하고 없애는 함수
        lets_remove = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != "X" and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    lets_remove.add((i, j))
                    lets_remove.add((i + 1, j))
                    lets_remove.add((i, j + 1))
                    lets_remove.add((i + 1, j + 1))
        
        l = len(lets_remove)
        if l == 0:
            return 0
        else:
            for i, j in lets_remove:
                board[i][j] = "X"
            return l


    answer = 0
    while True:
        cnt = remove()
        if cnt == 0:
            return answer
        else:
            answer += cnt
            drop()
        