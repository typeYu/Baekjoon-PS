def pet(o, w, commands):
    currentPet = w
    for command in commands:
        action, n = command
        if action == 'F':
            currentPet += n
        elif action == 'E':
            currentPet -= n

        if currentPet <= 0:
            return "RIP"

    if currentPet <= 0:
        return "RIP"
    elif o * 0.5 < currentPet < 2 * o:
        return ":-)"
    else:
        return ":-("


scenario_number = 1
while True:
    o, w = map(int, input().split())  # 적정 체중, 실제 체중
    if o == 0 and w == 0:
        break
    commands = []
    while True:
        S, n = input().split()
        N = int(n)
        if S == '#' and N == 0:
            break
        commands.append((S, N))

    result = pet(o, w, commands)
    print(f"{scenario_number} {result}")
    scenario_number += 1
