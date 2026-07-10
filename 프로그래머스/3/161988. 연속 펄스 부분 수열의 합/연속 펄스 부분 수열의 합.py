def solution(sequence):
    arr1, arr2 = [], []
    mul1, mul2 = -1, 1
    
    for i in range(len(sequence)):
        arr1.append(sequence[i] * mul1)
        arr2.append(sequence[i] * mul2)
        mul1 *= -1
        mul2 *= -1

    current1 = arr1[0]
    current2 = arr2[0]
    absolute = max(arr1[0], arr2[0])
    for i in range(1, len(sequence)):
        current1 = max(current1 + arr1[i], arr1[i])
        current2 = max(current2 + arr2[i], arr2[i])
        absolute = max(absolute, current1, current2)
    
    return absolute
    