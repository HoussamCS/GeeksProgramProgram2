#Challenge 1: Letter Index Dictionary
word=input("Enter a word: ")
letter_index_dict={letter:index for index, letter in enumerate(word)}

letter_index_dict = {}

for index, letter in enumerate(word):
    if letter in letter_index_dict:
        letter_index_dict[letter].append(index)
    else:
        letter_index_dict[letter] = [index]

print(letter_index_dict)


#Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

price = wallet.replace("$", "").replace(",", "")

affordable_items = []
for item, cost in items_purchase.items():
    item_price = cost.replace("$", "").replace(",", "")
    if int(item_price) <= int(price):
        affordable_items.append(item)

if not affordable_items:
    print("Nothing is affordable")
else:
    print("Affordable items:", affordable_items)
