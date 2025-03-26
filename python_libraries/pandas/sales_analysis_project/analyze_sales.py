import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Calculate total revenue
total_revenue = df["Revenue ($)"].sum()

# Find the best-selling product (based on Quantity Sold)
best_selling_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()

# Identify the day with the highest sales (based on Revenue)
highest_sales_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

# Save results to sales_summary.txt
summary = f"""
Sales Data Analysis
---------------------
Total Revenue: ${total_revenue:.2f}
Best-Selling Product: {best_selling_product}
Day with Highest Sales: {highest_sales_day}
"""

with open("sales_summary.txt", "w") as file:
    file.write(summary)

# Print insights
print(summary)

# Bonus: Visualize sales trends
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Revenue ($)"].sum()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o", linestyle="-", color="b")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.title("Sales Trends Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()
