#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve(n):
        """ Return a list of primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def count_primes(n):
        """ Return the number of primes up to n """
        primes = sieve(n)
        return len(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if count_primes(n) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

