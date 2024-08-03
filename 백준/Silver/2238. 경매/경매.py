U, N = map(int, input().split())
bids = {}

for _ in range(N):
    name, price = input().split()
    price = int(price)
    if price not in bids:
        bids[price] = []
    bids[price].append(name)

winner_price = None
winner_name = None
min_count = float('inf')

for price, names in bids.items():
    count = len(names)
    if count < min_count:
        min_count = count
        winner_price = price
        winner_name = names[0]
    elif count == min_count and price < winner_price:
        winner_price = price
        winner_name = names[0]

print(winner_name, winner_price)