while True:
    n = int(input())
    if n == 0:
        break

    N = [0] * 1000
    total = 0.0

    for i in range(1, n + 1):
        N[i] = float(input()) * 100
        total += N[i]

    total = total / n

    valorMenor = 0.0
    valorMaior = 0.0

    for l in range(1, n + 1):
        if N[l] < total:
            diff = (total - N[l])
            valorMenor += int(diff) / 100.0
        else:
            diff = (N[l] - total)
            valorMaior += int(diff) / 100.0
    if valorMenor > valorMaior:
        print(f"${valorMenor:.2f}")
    else:
        print(f"${valorMaior:.2f}")
