import sys
while True:
    meter = sys.stdin.readline().rstrip()
    N = len(meter) # 문자열 길이 저장(주행 거리 숫자 개수)
    if meter == "0":
        break

    count = 0
    while True:
        if meter == meter[::-1]:
            print(count)
            break
        else:
            meter_int = int(meter) + 1
            count += 1
            meter = ('0' * (N - len(str(meter_int)))) + str(meter_int)