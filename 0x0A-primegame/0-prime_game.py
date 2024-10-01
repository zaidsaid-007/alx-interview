#!/usr/bin/python3
""" Prime Game  """
def is_prime(n):
    """ Check if a number is prime """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_primes(n):
    """ Calculate a list of prime numbers up to n """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    """ Returns the winner of the Prime Game """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primes = calculate_primes(num)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
