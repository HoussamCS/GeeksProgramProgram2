import random


# Generating list of 20000 random numbers
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

# Set to keep track of numbers we've seen
seen = set()

# Set to store found pairs (avoid duplicates)
pairs = set()

# Iterate through the list
for number in list_of_numbers:
    complement = target_number - number
    if complement in seen:
        # Add pair in a sorted tuple to avoid duplicates like (1000,2728) and (2728,1000)
        pairs.add(tuple(sorted((number, complement))))
    seen.add(number)

# Printting all pairs
for pair in pairs:
    print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}")

# Printting total number of pairs
print(f"Total pairs found: {len(pairs)}")
