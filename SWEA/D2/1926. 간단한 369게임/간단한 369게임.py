S = input()
is_369 = ['3', '6', '9']
for num in range(1, int(S) + 1):
    result = ''
    for j in str(num):
        if j in is_369:
            result += '-'

    if result == '':
        print(num, end=' ')
    else:
        print(result, end=' ')