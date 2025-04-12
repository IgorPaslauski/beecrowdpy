valor = float(input())
if valor <= 2000:
    print("Isento")
elif valor <= 3000:
    imposto = (valor - 2000) * 0.08
    print("R$ {:.2f}".format(imposto))
elif valor <= 4500:
    imposto = (1000 * 0.08) + ((valor - 3000) * 0.18)
    print("R$ {:.2f}".format(imposto))
else:
    imposto = (1000 * 0.08) + (1500 * 0.18) + ((valor - 4500) * 0.28)
    print("R$ {:.2f}".format(imposto))

