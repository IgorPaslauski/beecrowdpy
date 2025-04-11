def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Teste
n = 60
resultado = fibonacci_memo(n)
print(f"O {n}-ésimo número de Fibonacci é: {resultado}")  # Saída: 8