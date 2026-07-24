def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = [[0, prices[0]]] # index, price
    for i in range(1, len(prices)):
        price = prices[i]
        while stack and stack[-1][1] > price:
            idx, pri = stack.pop()
            answer[idx] = i - idx
        stack.append([i, price])
    
    return answer