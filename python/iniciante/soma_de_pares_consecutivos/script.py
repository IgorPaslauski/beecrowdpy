while (True):
    n = int(input())
    if n == 0:
        break

    if n % 2 != 0:
        n += 1
    total = 0
    for i in range(5):
        total += n
        n+=2
    print(total)