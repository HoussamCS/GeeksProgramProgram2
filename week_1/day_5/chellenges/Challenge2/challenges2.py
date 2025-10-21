# Exercice 1:
# Pattern 1
rows = 3
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

# Pattern 2
rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (i + 1))


# Pattern 3
rows = 5

# Upper part
for i in range(1, rows + 1):
    print('*' * i)

# Lower part
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * i)



# Exercice 2:
my_list = [2, 24, 12, 354, 233]

for i in range(len(my_list) - 1):        # Loop through all elements except the last
    minimum = i                          # Assume current index 'i' holds the smallest value
    for j in range(i + 1, len(my_list)): # Compare with all elements after index 'i'
        if my_list[j] < my_list[minimum]:# If a smaller element is found
            minimum = j                  # Update 'minimum' to new smaller element’s index
            if minimum != i:             # If the smallest element isn't already in position
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]  # Swap them

print(my_list)

