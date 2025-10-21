# Exercise: Student Grade Summary
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Step 1: Initialize empty dictionaries
student_averages = {}
student_letter_grades = {}

# Step 2: Calculate averages and assign letter grades
for student, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[student] = avg

    # Assign letter grade
    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"
    
    student_letter_grades[student] = letter

# Step 3: Calculate class average
class_average = sum(student_averages.values()) / len(student_averages)

# Step 4: Print report
print("Student Grade Summary:\n")
for student in student_grades:
    print(f"{student}: Average = {student_averages[student]:.2f}, Grade = {student_letter_grades[student]}")

print(f"\nClass Average: {class_average:.2f}")


# Exercise:Advanced Data Manipulation and Analysis
# Initial Data
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Step 1: Add total_price to each transaction
for sale in sales_data:
    sale["total_price"] = sale["price"] * sale["quantity"]

# Step 2: Total sales per product
product_sales = {}
for sale in sales_data:
    product = sale["product"]
    product_sales[product] = product_sales.get(product, 0) + sale["total_price"]

# Step 3: Total spending per customer
customer_spending = {}
for sale in sales_data:
    cid = sale["customer_id"]
    customer_spending[cid] = customer_spending.get(cid, 0) + sale["total_price"]

# Step 4: High-value transactions (> $500)
high_value_transactions = [sale for sale in sales_data if sale["total_price"] > 500]
high_value_transactions.sort(key=lambda x: x["total_price"], reverse=True)

# Step 5: Identify loyal customers (more than one purchase)
purchase_count = {}
for sale in sales_data:
    cid = sale["customer_id"]
    purchase_count[cid] = purchase_count.get(cid, 0) + 1

loyal_customers = [cid for cid, count in purchase_count.items() if count > 1]

# Step 6 (Bonus): Insights
product_quantities = {}
for sale in sales_data:
    product = sale["product"]
    product_quantities[product] = product_quantities.get(product, 0) + sale["quantity"]

average_transaction_value = {p: product_sales[p] / product_quantities[p] for p in product_sales}
most_popular_product = max(product_quantities, key=product_quantities.get)

# Step 7: Print Results
print("📦 Total Sales per Product:", product_sales)
print("💰 Customer Spending:", customer_spending)
print("💎 High Value Transactions (> $500):", high_value_transactions)
print("🤝 Loyal Customers:", loyal_customers)
print("📊 Average Transaction Value per Product:", average_transaction_value)
print("🔥 Most Popular Product:", most_popular_product)

