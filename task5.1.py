import random

# Initialize counters for each outcome
rolls = [0] * 6
two_sixes_in_a_row = 0

# Simulate rolling the die at least 20 times
for _ in range(20):
    roll = random.randint(1, 6)
    rolls[roll - 1] += 1

    # Check for two consecutive 6s
    if roll == 6:
        two_sixes_in_a_row += 1

# Print the statistics
print(f"Times rolled a 1: {rolls[0]}")
print(f"Times rolled a 6: {rolls[5]}")
print(f"Times rolled two 6s in a row: {two_sixes_in_a_row}")
