for _ in range(int(input())):
    m, n = map(int ,input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    
    count = 0

    for i in range(n) :
        bottom = m - 1
    
        for j in reversed(range(m)) :
            if graph[j][i] == 1:
                count += bottom - j
                bottom -= 1
            
            
    print(count)