N = int(input())
topping = list(input().split())
quattro = set()
 
for t in topping:
    if t.endswith("Cheese"):
        quattro.add(t)
 
if len(quattro) >= 4:
    print("yummy")
else:
    print("sad")