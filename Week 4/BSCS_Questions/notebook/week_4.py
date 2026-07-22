# ============================================================
# Bhatbhateni Sales Data Analysis
# Beginner Level - Simple Step-by-Step Code
# ============================================================

# Step 1: Import libraries
# pandas helps us work with tables (like Excel)
# matplotlib helps us draw charts
import pandas as pd
import matplotlib.pyplot as plt

print("Step 1: Libraries loaded!")


# Step 2: Load the data
# We read the CSV file into a table called df
df = pd.read_csv("../data/bhatbhateni_sales.csv")
print("Step 2: Data loaded!")
print(f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")


# ============================================================
# Step 3: Look at the data
# ============================================================

# Show first 5 rows to understand the structure
print("\n--- First 5 rows ---")
print(df.head())

# Show column names
print("\n--- Column names ---")
print(df.columns.tolist())


# ============================================================
# Step 4: Check data quality issues
# ============================================================

# Check missing values in each column
print("\n--- Missing values per column ---")
missing = df.isnull().sum()
for col, count in missing.items():
    if count > 0:
        print(f"{col}: {count} missing values")


# Check for fully duplicate rows
print("\n--- Duplicate rows ---")
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")


# ============================================================
# Step 5: Clean the data
# ============================================================

# Remove exact duplicate rows
df = df.drop_duplicates()
print("\n--- Duplicates removed ---")

# Fill missing CustomerName with "Unknown"
df["CustomerName"] = df["CustomerName"].fillna("Unknown")

# Fill missing ProductCategory with "Unknown"
df["ProductCategory"] = df["ProductCategory"].fillna("Unknown")

# Fill missing PaymentMethod with "Unknown"
df["PaymentMethod"] = df["PaymentMethod"].fillna("Unknown")

# Fix missing UnitPrice:
# If UnitPrice is missing, calculate it from TotalAmount / Quantity
for index, row in df.iterrows():
    if pd.isna(row["UnitPrice"]):
        if pd.notna(row["TotalAmount"]) and pd.notna(row["Quantity"]) and row["Quantity"] != 0:
            df.at[index, "UnitPrice"] = row["TotalAmount"] / row["Quantity"]

# If UnitPrice is still missing, fill with the category median
category_median = df.groupby("ProductCategory")["UnitPrice"].transform("median")
df["UnitPrice"] = df["UnitPrice"].fillna(category_median)

# If still missing, fill with overall median
df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median())

print("--- Missing values cleaned ---")

# Recalculate TotalAmount to make sure it is correct
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]


# ============================================================
# Step 6: Add useful new columns
# ============================================================

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Extract year and month from Date
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["MonthName"] = df["Date"].dt.month_name()

# Extract day of week
df["Weekday"] = df["Date"].dt.day_name()

# Check if the day is Saturday or Sunday (weekend)
df["IsWeekend"] = df["Weekday"].isin(["Saturday", "Sunday"])

# Extract city name from Branch (format: "City - Area")
df["City"] = df["Branch"].str.split(" - ").str[0]

print("Step 6: New columns created!")


# ============================================================
# Step 7: Simple Analysis with Answers
# ============================================================

print("\n" + "=" * 50)
print("SALES ANALYSIS RESULTS")
print("=" * 50)

# Q1: Which product category has the most transactions?
category_counts = df["ProductCategory"].value_counts()
top_category = category_counts.index[0]
print(f"\n1. Most sold category: {top_category}")
print(f"   Number of transactions: {category_counts.iloc[0]}")

# Q2: Which branch has the highest total revenue?
branch_revenue = df.groupby("Branch")["TotalAmount"].sum().sort_values(ascending=False)
top_branch = branch_revenue.index[0]
print(f"\n2. Highest revenue branch: {top_branch}")
print(f"   Total revenue: {branch_revenue.iloc[0]:.2f}")

# Q3: Which city has the highest total revenue?
city_revenue = df.groupby("City")["TotalAmount"].sum().sort_values(ascending=False)
print(f"\n3. Highest revenue city: {city_revenue.index[0]}")

# Q4: What is the most common payment method?
payment_counts = df["PaymentMethod"].value_counts()
common_payment = payment_counts.index[0]
print(f"\n4. Most common payment method: {common_payment}")

# Q5: What is the average transaction amount?
avg_transaction = df["TotalAmount"].mean()
print(f"\n5. Average transaction amount: {avg_transaction:.2f}")

# Q6: Which product is sold the most by quantity?
product_qty = df.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False)
print(f"\n6. Top product by quantity: {product_qty.index[0]}")
print(f"   Total quantity sold: {product_qty.iloc[0]}")

# Q7: Weekend vs Weekday sales
weekend_sales = df.groupby("IsWeekend")["TotalAmount"].sum()
weekend = weekend_sales.get(True, 0)
weekday = weekend_sales.get(False, 0)
print(f"\n7. Weekend sales: {weekend:.2f}")
print(f"   Weekday sales: {weekday:.2f}")

# Q8: Top 5 customers by total spending
customer_spend = df.groupby("CustomerName")["TotalAmount"].sum().sort_values(ascending=False).head(5)
print(f"\n8. Top 5 customers by total spend:")
for i, (name, amount) in enumerate(customer_spend.items(), 1):
    print(f"   {i}. {name}: {amount:.2f}")

# Q9: Monthly revenue trend
monthly_revenue = df.groupby(["Year", "Month"])["TotalAmount"].sum()
print(f"\n9. Monthly revenue (first few months):")
print(monthly_revenue.head())

# Q10: Number of repeat customers vs one-time customers
customer_counts = df.groupby("CustomerID").size()
repeat = sum(customer_counts > 1)
one_time = sum(customer_counts == 1)
print(f"\n10. Repeat customers: {repeat}")
print(f"    One-time customers: {one_time}")


# ============================================================
# Step 8: Simple Charts
# ============================================================

# Chart 1: Sales by Product Category
category_revenue = df.groupby("ProductCategory")["TotalAmount"].sum().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
category_revenue.plot(kind="barh", color="skyblue")
plt.title("Total Sales by Product Category", fontsize=14)
plt.xlabel("Total Revenue")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig("../images/chart1_category_sales.png")
print("\nChart 1 saved: chart1_category_sales.png")
plt.close()

# Chart 2: Sales by City
city_sales = df.groupby("City")["TotalAmount"].sum().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
city_sales.plot(kind="barh", color="lightgreen")
plt.title("Total Sales by City", fontsize=14)
plt.xlabel("Total Revenue")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("../images/chart2_city_sales.png")
print("Chart 2 saved: chart2_city_sales.png")
plt.close()

# Chart 3: Payment Method Distribution
payment_counts = df["PaymentMethod"].value_counts()
plt.figure(figsize=(8, 8))
payment_counts.plot(kind="pie", autopct="%1.1f%%", colors=["lightblue", "lightgreen", "lightyellow", "lightcoral"])
plt.title("Payment Method Distribution", fontsize=14)
plt.ylabel("")
plt.tight_layout()
plt.savefig("../images/chart3_payment_method.png")
print("Chart 3 saved: chart3_payment_method.png")
plt.close()


# ============================================================
# Step 9: Save cleaned data
# ============================================================

# Save the cleaned data to a new CSV file
df.to_csv("../data/week4_cleaned_sales.csv", index=False)
print("\nCleaned data saved to: week4_cleaned_sales.csv")

# ============================================================
# Step 10: Simple Summary
# ============================================================

print("\n" + "=" * 50)
print("ANALYSIS COMPLETE!")
print("=" * 50)
print(f"Total transactions analyzed: {len(df)}")
print(f"Total revenue: {df['TotalAmount'].sum():.2f}")
print(f"Number of unique customers: {df['CustomerID'].nunique()}")
print(f"Number of unique products: {df['ProductName'].nunique()}")
print(f"Number of branches: {df['Branch'].nunique()}")
print(f"Number of cities: {df['City'].nunique()}")
