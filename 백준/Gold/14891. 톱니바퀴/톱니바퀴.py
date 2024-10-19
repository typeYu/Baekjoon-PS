from collections import deque
one = deque(input())
two = deque(input())
three = deque(input())
four = deque(input())

def check(first, end):
    if first[2] == end[6]:
        return False
    else:
        return True

for _ in range(int(input())):
    num, direct = map(int, input().split())
    chk1, chk2, chk3 = check(one, two), check(two, three), check(three, four)
    if num == 1:
        one.rotate(direct)
        if chk1:
            two.rotate(-direct)
            if chk2:
                three.rotate(direct)
                if chk3:
                    four.rotate(-direct)
    elif num == 2:
        two.rotate(direct)
        if chk1:
            one.rotate(-direct)
        if chk2:
            three.rotate(-direct)
            if chk3:
                four.rotate(direct)
    elif num == 3:
        three.rotate(direct)
        if chk2:
            two.rotate(-direct)
            if chk1:
                one.rotate(direct)
        if chk3:
            four.rotate(-direct)
    elif num == 4:
        four.rotate(direct)
        if chk3:
            three.rotate(-direct)
            if chk2:
                two.rotate(direct)
                if chk1:
                    one.rotate(-direct)

score = 0
if one[0] == '1':
    score += 1
if two[0] == '1':
    score += 2
if three[0] == '1':
    score += 4
if four[0] == '1':
    score += 8

print(score)