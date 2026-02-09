def prime_factors(n: int) -> list:
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2

    if n > 1:
        factors.append(n)

    return factors

# Сложность: O(√n) по времени, O(log n) по памяти для хранения множителей