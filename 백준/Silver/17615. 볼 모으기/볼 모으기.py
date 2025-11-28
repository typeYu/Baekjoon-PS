import sys
N = int(sys.stdin.readline())
balls = sys.stdin.readline().strip()

red_right = balls.rstrip('R')
red_left = balls.lstrip('R')
blue_right = balls.rstrip('B')
blue_left = balls.lstrip('B')

answer = min(red_right.count('R'), red_left.count('R'), blue_right.count('B'), blue_left.count('B'))

print(answer)