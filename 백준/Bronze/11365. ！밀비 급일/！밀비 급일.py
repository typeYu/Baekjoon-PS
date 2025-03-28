while True:
    password = input()
    if password == "END":
        break
    else:
        password = password[::-1]
        print(password)