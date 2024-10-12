N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)] # 역슬래시(\)는 파이썬에서 \\로 표시함에 주의
PR, PC = map(int, input().split())

direct_S = ("U", "R", "D", "L")
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_valid(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

def solve():
    result = []
    for i in range(4):
        pr, pc = PR - 1, PC - 1
        count = 1
        d = i
        dy, dx = direct[i][0], direct[i][1]
        visited = set()

        while is_valid(pr, pc):
            if (pr, pc, d) in visited:
                print(direct_S[i], "Voyager", sep="\n")
                exit()
            visited.add((pr, pc, d))
            
            pr += dy
            pc += dx

            if not is_valid(pr, pc):
                break

            if graph[pr][pc] == 'C':
                break
            elif graph[pr][pc] == '/':
                count += 1
                if d == 1 or d == 3:
                    d = (d - 1) % 4
                else:
                    d = (d + 1) % 4
                dy, dx = direct[d][0], direct[d][1]
            elif graph[pr][pc] == '\\':
                count += 1
                if d == 1 or d == 3:
                    d = (d + 1) % 4
                else:
                    d = (d - 1) % 4
                dy, dx = direct[d][0], direct[d][1]
            else:
                count += 1
        result.append((direct_S[i], count))

    return result


resultArr = solve()
resultArr.sort(key=lambda x: -x[1])
print(resultArr[0][0], resultArr[0][1], sep="\n")