n1, n2, n3, n4 = map(float, input().split())

m = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if(m>=7.0):
    print(f"Media: {m:.1f}")
    print("Aluno aprovado.")
elif(m<5.0):
    print(f"Media: {m:.1f}")
    print("Aluno reprovado.")
elif(m>=5.0 and m<7.0):
    print(f"Media: {m:.1f}")
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    m = (m+n5)/2
    if(m>=5.0):
        print("Aluno aprovado.")
        print(f"Media final: {m:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {m:.1f}")