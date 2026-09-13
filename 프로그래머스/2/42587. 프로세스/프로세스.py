from collections import deque
def solution(priorities, location):
    dic = dict()
    for p in priorities:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    sorted_arr = []
    for k, v in dic.items():
        sorted_arr.append([k, v])
    
    sorted_arr.sort(key=lambda x: -x[0])
    sorted_arr = deque(sorted_arr)
    
    priorities = enumerate(priorities)
    priorities = deque(priorities)
    re = 1
    while len(priorities) > 0:
        i, p = priorities.popleft()
        if p == sorted_arr[0][0]:
            if i == location:
                return re
            else:
                re += 1
                sorted_arr[0][1] -= 1
                if sorted_arr[0][1] == 0:
                    sorted_arr.popleft()
        else:
            priorities.append([i, p])