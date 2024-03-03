def solution(arr):
    minar = min(arr)
    arr.remove(minar)
    if arr:
        return arr
    else:
        return [-1]