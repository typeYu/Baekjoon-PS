dic = {"R": (0, 1), "L": (0, -1), "B": (1, 0), "T": (-1, 0), "RT": (-1, 1), "LT": (-1, -1), "RB": (1, 1), "LB": (1, -1)}
location = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7, "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
x_convert = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
y_convert = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}

def able(y, x):
    if 0 <= y < 8 and 0 <= x < 8:
        return True
    return False

king, stone, N = input().split()
king_x, king_y = location[king[0]], location[king[1]]
stone_x, stone_y = location[stone[0]], location[stone[1]]
for _ in range(int(N)):
    move = input()
    stone_move = False
    dy, dx = dic[move]
    king_ny, king_nx = king_y + dy, king_x + dx
    if king_ny == stone_y and king_nx == stone_x:
        stone_ny, stone_nx = stone_y + dy, stone_x + dx
        stone_move = True

    if able(king_ny, king_nx):
        if stone_move:
            if able(stone_ny, stone_nx):
                king_y, king_x = king_ny, king_nx
                stone_y, stone_x = stone_ny, stone_nx

        else:
            if able(stone_y, stone_x):
                king_y, king_x = king_ny, king_nx

print(f"{x_convert[king_x]}{y_convert[king_y]}")
print(f"{x_convert[stone_x]}{y_convert[stone_y]}")