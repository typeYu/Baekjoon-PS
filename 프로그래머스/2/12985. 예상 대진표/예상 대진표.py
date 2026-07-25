def solution(n,a,b):
    answer = 1
    arr = [i for i in range(1, n + 1)]
    
    while len(arr) >= 2:
        new_arr = []
        for i in range(0, len(arr), 2):
            if i + 1 == len(arr):
                new_arr.append(arr[i])
            elif a in [arr[i], arr[i + 1]] and b in [arr[i], arr[i + 1]]:
                return answer
            elif a in [arr[i], arr[i + 1]]:
                new_arr.append(a)
            elif b in [arr[i], arr[i + 1]]:
                new_arr.append(b)
            else:
                new_arr.append(arr[i])
            
        arr = new_arr
        answer += 1
    
    return answer