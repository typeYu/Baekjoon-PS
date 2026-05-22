def solution(wallet, bill):
    cnt = 0
    while True:
        if (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[0] <= wallet[1] and bill[1] <= wallet[0]):
            return cnt
        
        if bill[0] <= bill[1]:
            bill = [bill[0], bill[1] // 2]
        else:
            bill = [bill[0] // 2, bill[1]]
            
        cnt += 1