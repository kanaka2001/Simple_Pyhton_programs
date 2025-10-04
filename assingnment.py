def primeFactoers(number):
    for index in range (0,500, 1):
        prime = number % 2
        print(prime)
        if (prime == 0):
            break

primeFactoers(10)
