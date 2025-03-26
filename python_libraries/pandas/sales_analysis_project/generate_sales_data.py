import pandas as pd
import random
from datetime import datetime, timedelta

# Define products
products = ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch", "Monitor"]

# Generate 50 rows of random sales data
data = []
start_date = datetime(2025, 3, 1)

for _ in range(50):
    date = (start_date + timedelta(days=random.randint(0, 9))).strftime("%Y-%m-%d")
    product = random.choice(products)
    quantity_sold = random.randint(1, 20)
    revenue = quantity_sold * random.randint(50, 500)  # Random revenue per unit

    data.append([date, product, quantity_sold, revenue])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Product", "Quantity Sold", "Revenue ($)"])

# Save to CSV
df.to_csv("sales_data.csv", index=False)

print("Sample sales_data.csv file generated successfully!")
