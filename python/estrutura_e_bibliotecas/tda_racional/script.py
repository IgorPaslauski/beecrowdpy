import math

def simplificar(numerador, denominador):
    mdc = math.gcd(numerador, denominador)
    return numerador // mdc, denominador // mdc

n = int(input())

for _ in range(n):
    entrada = input().split()

    n1 = int(entrada[0])
    d1 = int(entrada[2])
    op = entrada[3]
    n2 = int(entrada[4])
    d2 = int(entrada[6])

    if op == '+':
        numerador = n1 * d2 + n2 * d1
        denominador = d1 * d2
    elif op == '-':
        numerador = n1 * d2 - n2 * d1
        denominador = d1 * d2
    elif op == '*':
        numerador = n1 * n2
        denominador = d1 * d2
    elif op == '/':
        numerador = n1 * d2
        denominador = n2 * d1

    simpl_num, simpl_den = simplificar(numerador, denominador)

    if simpl_den < 0:
        simpl_num *= -1
        simpl_den *= -1

    print(f"{numerador}/{denominador} = {simpl_num}/{simpl_den}")
