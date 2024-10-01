#!/usr/bin/python3
""" Prime Game  """
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    return primes

def is_prime(n, primes):
    return primes[n]

def play_game(n):
    primes = sieve_of_eratosthenes(n)
    numbers = list(range(1, n + 1))
    player = 'Maria'
    while True:
        if not any(is_prime(num, primes) for num in numbers):
            return player
        if player == 'Maria':
            for num in numbers:
                if is_prime(num, primes):
                    numbers = [n for n in numbers if n % num != 0]
                    player = 'Ben'
                    break
        else:
            for num in numbers:
                if is_prime(num, primes):
                    numbers = [n for n in numbers if n % num != 0]
                    player = 'Maria'
                    break

def isWinner(x, nums):
    maria_wins = 0
    for n in nums:
        if play_game(n) == 'Maria':
            maria_wins += 1
    if maria_wins > x / 2:
        return 'Maria'
    elif maria_wins < x / 2:
        return 'Ben'
    else:
        return None
    

