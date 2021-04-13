from itertools import permutations

def get_primes(n):
    numbers = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if numbers[i] == True:
            for j in range(i + i, n, i):
                numbers[j] = False

    return {prime: True for prime in [i for i in range(2, n) if numbers[i] == True]}


def solution(numbers):
    numbers = list(numbers)
    primes = get_primes(int(max(numbers) * len(numbers)))
    count = 0
    for i in range(1,len(numbers)+1):
        permute = list(permutations(numbers, i))
        for number in permute:
            number = int(''.join(number))
            if number in primes and primes[number]:
                count += 1
                primes[number] = False
    return count

print(solution("011"))