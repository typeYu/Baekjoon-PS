while True:
    a, b, c = map(int, input().split())
    
    if (a, b, c) == (0, 0, 0):
        break
        
    if (c - b) == (b - a) and (c - b) != 0:
        print("AP", c + (c - b))
    else:
        print("GP", int(c * (c // b)))