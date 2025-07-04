while True:
    try:
        n = int(input()) # 정수 n
    except:
        break

    num = 1    # 1로만 이루어진 수
    count = 1  # 자리수
    while True:
        if num % n != 0:  # n의 배수가 아니라면
            num = num * 10 + 1 # 1로만 이루어진 다음 수로 갱신
            count += 1         # 자리수 세어줌
        else:      # n의 배수라면
            break  # 종료
    
    print(count) # 자리수 출력