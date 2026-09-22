def solution(sticker):
    if len(sticker) < 2:
        return sticker[0]
    
    dp0 = [0] * len(sticker)
    # 0번째에 스티커 붙일 때
    dp0[0] = sticker[0]
    for i in range(1, len(sticker) - 1):
        dp0[i] = max(dp0[i - 2] + sticker[i], dp0[i - 1])
    
    dp1 = [0] * len(sticker)
    # 1번째에 스티커 붙일 때
    dp1[1] = sticker[1]
    for i in range(3, len(sticker)):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
        
    dp2 = [0] * len(sticker)
    # 0번째에도 1번째에도 스티커 붙이지 않을 때
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    
    return max(dp0 + dp1 + dp2)
    