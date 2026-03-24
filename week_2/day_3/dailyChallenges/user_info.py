
user_data = []

for i in range(5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    user_data.append((name, age, score))

sorted_data = sorted(user_data, key=lambda x: (x[0], x[1], x[2]))

# Print the sorted list
print(sorted_data)
