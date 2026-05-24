def solution(s, n):
    print(ord('a'), ord('z'), ord('A'), ord('Z'))
    answer = ""
    for i in s:
        if i == " ":
            answer += i
        else:
            ans = ord(i) + n
            if (65 <= ord(i) < 91 and 91 <= ans) or (97 <= ord(i) < 123 and 123 <= ans):
                ans -= 26
            
            answer += chr(ans)
    
    return answer