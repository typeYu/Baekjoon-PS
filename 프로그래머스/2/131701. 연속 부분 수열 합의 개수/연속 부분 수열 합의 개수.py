def solution(elements):
    result = set()
    l = len(elements)
    elements = elements + elements
    for i in range(1, l + 1):
        for j in range(l):
            result.add(sum(elements[j:j + i]))
    
    return len(result)