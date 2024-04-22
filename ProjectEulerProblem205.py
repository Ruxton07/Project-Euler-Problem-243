'''Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Peter beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg. (Decimals)'''

from itertools import product
from collections import Counter
peter_dice = [1, 2, 3, 4]
colin_dice = [1, 2, 3, 4, 5, 6]

peter_outcomes = Counter(sum(roll) for roll in product(peter_dice, repeat=9))
colin_outcomes = Counter(sum(roll) for roll in product(colin_dice, repeat=6))

peter_wins = sum(peter_outcomes[total] * colin_outcomes[other_total] for total in peter_outcomes for other_total in colin_outcomes if total > other_total)
total_outcomes = sum(peter_outcomes.values()) * sum(colin_outcomes.values())

probability = peter_wins / total_outcomes
probability = round(probability, 7)

print(f"The probability that Pyramidal Peter beats Cubic Colin is: {probability}")