def solution(sequence, k):
    start, end = 0, 1
    prefix_sum = sequence[0]
    l = len(sequence)
    answer = [0, l]
    
    while start <= end and end <= l:
        if prefix_sum == k:
            if answer[1] - answer[0] > end - start - 1:
                answer = [start, end - 1]
            prefix_sum -= sequence[start]
            start += 1
        elif prefix_sum < k:
            if end == l:
                break
            prefix_sum += sequence[end]
            end += 1
        else:
            prefix_sum -= sequence[start]
            start += 1
        
    
    return answer