n = 600851475143

i = 2

factors = []

while i * i <= n:
    if n % i == 0:
        n //= i
        factors.append(i)
    else:
        i += 1

if n > 1:
    factors.append(n)

print(max(factors))
