#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    How many of this type of coin can I get with my money? Okay,
        I'll take that many. Now, how much money do I have left?
        And how many coins do I have in my pocket?
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large number for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Populate the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    # If dp[total] is still float('inf'), return -1, otherwise return dp[total]
    return dp[total] if dp[total] != float('inf') else -1
