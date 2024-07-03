def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]

def play_game(n, primes):
    remaining_numbers = set(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben
    while True:
        made_move = False
        for prime in primes:
            if prime in remaining_numbers:
                # Remove the prime and its multiples
                multiple = prime
                while multiple <= n:
                    remaining_numbers.discard(multiple)
                    multiple += prime
                made_move = True
                break
        if not made_move:
            return turn  # The player who couldn't make a move loses
        turn = 1 - turn  # Switch turns

def isWinner(x, nums):
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n, primes)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

