import sys
input = sys.stdin.readline

q = int(input())  # 출입 기록의 개수

check = {} 
overtime =0    
for i in range(q):
  enter = list(input().split())  # 기록 
  name, data = enter[0], enter[1]
  if data == '-':     # 회사에서 나옴
    if name not in check or check[name] == 0:  # 야근한 경우
      overtime +=1
    elif name in check:    # 야근 안 한 경우
      check[name] -=1
  elif data == '+':    # 들어간 경우
    if name not in check:    
      check[name] = 1    # 들어갔다고 등록
    else:
      check[name] += 1   

# 야근하는 직원 수
print(sum(check.values()) + overtime)