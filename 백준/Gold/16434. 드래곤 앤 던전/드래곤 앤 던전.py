import sys
N, atk = map(int, sys.stdin.readline().strip().split())
rooms = []
for _ in range(N):
    t, a, h = map(int, sys.stdin.readline().strip().split())
    rooms.append((t, a, h))

def each_room(atk, max_hp):
    cur_hp = max_hp
    for t, a, h in rooms:
        if t == 1:
            my_attack_count = h // atk if h % atk == 0 else h // atk + 1
            monsters_attack_count = cur_hp // a if cur_hp % a == 0 else cur_hp // a + 1
            if my_attack_count > monsters_attack_count:
                return False
            else:
                cur_hp -= (my_attack_count - 1) * a
        elif t == 2:
            atk += a
            if cur_hp + h >= max_hp:
                cur_hp = max_hp
            else:
                cur_hp += h
    return True


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if each_room(atk, mid):
            end = mid - 1
        else:
            start = mid + 1
    return start

print(binary_search(1, 1000000 * 1000000 * N))