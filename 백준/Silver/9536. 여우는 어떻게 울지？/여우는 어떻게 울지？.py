import sys
for _ in range(int(sys.stdin.readline())):
    record = list(sys.stdin.readline().strip().split())
    while True:
        try:
            _, _, sound = sys.stdin.readline().strip().split()
            for _ in range(record.count(sound)):
                record.remove(sound)
        except:
            break

    print(*record)