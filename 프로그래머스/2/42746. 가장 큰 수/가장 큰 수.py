# 5 50 59 세 개를 숫자로 정렬하든 문자로 정렬하든 원하는 결과(59, 5, 50 순서)를 출력하지 못함
# 문자를 원소 길이 제한인 1000에 맞춰 3번 곱해서(555, 505050, 595959) 내림차순 정렬하면 이어 붙여 만들 수 있는 가장 큰 수가 됨
# "0000" 처럼 출력 되는 것을 방지하기 위해 앞자리 체크 필수
def solution(numbers):
    numbers = [str(n) * 3 for n in numbers]
    numbers.sort(reverse=True)
    answer = "".join([n[:len(n) // 3] for n in numbers])
    return answer if answer[0] != '0' else "0"