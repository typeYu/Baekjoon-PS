import heapq
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

heapq.heapify(array)
result = 0
while True:
    if len(array) == 1:
        break
    else:
        a = heapq.heappop(array)
        b = heapq.heappop(array)
        result += (a + b)
        heapq.heappush(array, a + b)

print(result)