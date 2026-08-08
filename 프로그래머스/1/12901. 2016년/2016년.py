def solution(a, b):
    DOW = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    date = [0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    
    return DOW[(date[a] + b) % 7]