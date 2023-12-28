import numpy as np
from itertools import combinations

def coin_flips(k, n):
    outcomes = ['h', 't']  # Possible outcomes

    # Generate all combinations of length n
    all_combinations = set(combinations(outcomes * n, n))

    # Filter combinations with exactly k occurrences of 'h'
    filtered_combinations = [combo for combo in all_combinations if combo.count('h') == k]
    print(filtered_combinations)
    # Print the filtered combinations
    for combo in filtered_combinations:
        print(''.join(combo))

# Example usage: Flipping 3 coins, looking for 2 heads
coin_flips(4, 5)
