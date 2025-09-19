from collections import deque

def solution(numbers, direction):
    numbers_deque = deque(numbers)
    
    if direction == "right":
        numbers_deque.rotate(1)
    else:
        numbers_deque.rotate(-1)
    
    return list(numbers_deque)