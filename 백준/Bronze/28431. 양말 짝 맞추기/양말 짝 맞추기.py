socks = [int(input()) for _ in range(5)]

pairs = []
for s in socks:
    if s in pairs:
        pairs.remove(s)
    else:
        pairs.append(s)

print(pairs[0])
