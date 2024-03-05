while True:
    N = float(input())
    if N == -1:
        break
    print(f"Objects weighing {N:0.2f} on Earth will weigh {N * 0.167:0.2f} on the moon.")