from itertools import product
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = []
    
    for i in range(1, 5 + 1):
        for c in product(vowels, repeat=i):
            answer.append((''.join(c)))
    
    answer.sort()
    return answer.index(word) + 1