S = input()
cam = {"C", "A", "M", "B", "R", "I", "D", "G", "E"}
for s in S:
    if s not in cam:
        print(s, end='')