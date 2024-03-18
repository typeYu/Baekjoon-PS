def solution(arr):
    result = []
    result.append(arr[0])
    for i in arr[1:]:
        if i == result[-1]:
            continue
        else:
            result.append(i)
    return result