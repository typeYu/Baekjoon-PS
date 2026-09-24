def solution(n, costs):
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    answer = 0
    
    def find_parents(x):
        if parents[x] != x:
            parents[x] = find_parents(parents[x])
        return parents[x]

    def union(x, y):
        p_x = find_parents(x)
        p_y = find_parents(y)

        if p_x >= p_y:
            parents[p_y] = p_x
        else:
            parents[p_x] = p_y
        
    
    for x, y, cst in costs:
        if find_parents(x) != find_parents(y):
            union(x, y)
            answer += cst
    
    return answer