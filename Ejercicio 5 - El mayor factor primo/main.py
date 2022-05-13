number=600851475143

primeFactor = 1
i = 2

while i <= number:
    if number % i == 0:
        primeFactor = i
        number = number / i
    else:
        i = i + 1

print(primeFactor)