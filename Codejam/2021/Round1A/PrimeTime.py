a = 10**15


def get_primes(n):
    sieve = [True] * n
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

check_primes = get_primes(500)

def is_factorized(number, primes):
    i = 0
    new_primes = {}
    new_primes_sum = 0
    my_primes = [num for num in check_primes if num in primes]
    prime = my_primes[i]


    while number != 1:
        if number % prime == 0:
            number = number//prime
            new_primes_sum += prime
            if prime in new_primes:
                new_primes[prime] += 1
            else:
                new_primes[prime] = 1
            if prime not in primes or new_primes[prime] > primes[prime]:
                return False, 0

        else:
            i += 1
            if i == len(my_primes):
                return False, 0
            prime = my_primes[i]


    return True, new_primes_sum


T = int(input())



for t in range(1, T+1):
    count = int(input())
    counts = {}
    primes = {}
    _sum = 0
    for i in range(count):
        prime, count = map(int, input().split())
        primes[prime] = count
        _sum += prime * count

    limit = min([29940, _sum])
    answer = 0

    for i in range(0,limit):
        fatorized, its_sum = is_factorized(_sum - i, primes)

        if fatorized and its_sum == i:
            answer = _sum - its_sum
            break


    print("Case #" + str(t) + ":" , answer)