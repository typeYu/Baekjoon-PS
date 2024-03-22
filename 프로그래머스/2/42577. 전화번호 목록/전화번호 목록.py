def solution(phone_book):
    phone_book.sort()
    exist = 0
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            exist += 1
            break
    if exist == 0:
        return True
    else:
        return False