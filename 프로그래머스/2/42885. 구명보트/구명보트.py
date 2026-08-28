from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    
    while len(people) > 0:
        if len(people) > 1 and people[-1] + people[0] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            people.pop()
            answer += 1
    
    return answer