def solution(phone_number):
    star = len(phone_number[:-4])
    phone_number = phone_number[-4:]
    return star * '*' + str(phone_number)