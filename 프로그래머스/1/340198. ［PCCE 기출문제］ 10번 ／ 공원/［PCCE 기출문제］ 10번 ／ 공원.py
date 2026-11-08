def solution(mats, park):
    n, m = len(park), len(park[0])
    answer = -1
    mats.sort(reverse=True)
    
    def vertify(i, j, mat):
        for di in range(mat):
            for dj in range(mat):
                if i + di >= n or j + dj >= m or park[i + di][j + dj] != "-1":
                    return False
        
        return True
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                for mat in mats:
                    if vertify(i, j, mat):
                        answer = max(answer, mat)
                        break
    
    return answer
                                
                