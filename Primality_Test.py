# Primality Test
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

