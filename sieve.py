def sieve_of_eratosthenes(upper_bound=100):
    primes = [2]
    prime = 2
    prime_index = 0
    numbers = list(range(2, upper_bound))
    while True:
        working_index = prime_index+prime
        while working_index < len(numbers):
            numbers[working_index] = 0
            working_index += prime
        if prime_index == len(numbers)-1:
            break
        working_index = prime_index+1
        while numbers[working_index] == 0:
            working_index += 1
            if working_index == len(numbers):
                return primes
        prime_index = working_index
        prime = numbers[prime_index]
        primes.append(prime)

