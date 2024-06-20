#!/usr/bin/python3
"""
Main file for testing
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large number for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Populate the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still float('inf'), return -1, otherwise return dp[total]
    return dp[total] if dp[total] != float('inf') else -1
