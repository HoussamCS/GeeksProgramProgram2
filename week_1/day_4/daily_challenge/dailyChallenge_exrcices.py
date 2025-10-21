MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

#  Converting string to 2D list (matrix)
matrix = [list(row) for row in MATRIX_STR.splitlines() if row]

# Iterate through columns to read top-to-bottom
num_rows = len(matrix)
num_cols = len(matrix[0])
decoded_chars = []

for col in range(num_cols):
    for row in range(num_rows):
        decoded_chars.append(matrix[row][col])

# Replace groups of non-alpha characters with a space
import re
message = ''.join(decoded_chars)
decoded_message = re.sub(r'[^A-Za-z]+', ' ', message)

# Print the final decoded message
print(decoded_message.strip())
