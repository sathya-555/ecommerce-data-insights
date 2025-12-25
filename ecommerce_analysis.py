import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

# Total Sales
df["total_price"] = df["quantity"] * df["price"]

# Top-selling products
top_products = df.groupby("product")["quantity"].sum()

# Peak shopping hours
peak_hours = df.groupby("order_hour")["order_id"].count()

# User retention
user_orders = df.groupby("user_id")["order_id"].count()

# Visualization
plt.figure()
top_products.plot(kind='bar')
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.show()

plt.figure()
peak_hours.plot(kind='line')
plt.title("Peak Shopping Hours")
plt.xlabel("Hour")
plt.ylabel("Orders")
plt.show()

plt.figure()
user_orders.plot(kind='pie', autopct='%1.1f%%')
plt.title("User Order Distribution")
plt.ylabel("")
plt.show()
