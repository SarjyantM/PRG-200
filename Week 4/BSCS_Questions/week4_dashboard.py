import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ============================================================
# Streamlit Dashboard Setup
# ============================================================
# set_page_config must be the first Streamlit command
st.set_page_config(page_title="Bhatbhateni Sales Dashboard", layout="wide")

st.title("Bhatbhateni Sales Analysis Dashboard")
st.write("A simple dashboard to explore sales data using Streamlit")

# ============================================================
# Step 1: Load Data
# ============================================================
# @st.cache_data saves the data so it loads only once
@st.cache_data
def load_data():
    df = pd.read_csv("./data/bhatbhateni_sales.csv")
    return df

df = load_data()

# ============================================================
# Step 2: Raw Data Option
# ============================================================
# Checkbox to show or hide the raw data table
if st.checkbox("Show raw data"):
    st.subheader("Raw Sales Data")
    st.write(df)

# ============================================================
# Step 3: Clean the Data
# ============================================================
# Remove exact duplicate rows
df = df.drop_duplicates()

# Fill missing text values with "Unknown"
df["CustomerName"] = df["CustomerName"].fillna("Unknown")
df["ProductCategory"] = df["ProductCategory"].fillna("Unknown")
df["PaymentMethod"] = df["PaymentMethod"].fillna("Unknown")

# Fix missing UnitPrice:
# If UnitPrice is missing, calculate it from TotalAmount / Quantity
for index, row in df.iterrows():
    if pd.isna(row["UnitPrice"]):
        if pd.notna(row["TotalAmount"]) and pd.notna(row["Quantity"]) and row["Quantity"] != 0:
            df.at[index, "UnitPrice"] = row["TotalAmount"] / row["Quantity"]

# If UnitPrice is still missing, fill with median of that category
category_median = df.groupby("ProductCategory")["UnitPrice"].transform("median")
df["UnitPrice"] = df["UnitPrice"].fillna(category_median)

# If still missing, fill with overall median
df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median())

# Recalculate TotalAmount to make sure math is correct
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# ============================================================
# Step 4: Add New Columns
# ============================================================
# Convert Date to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Extract year, month, and month name from Date
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["MonthName"] = df["Date"].dt.month_name()

# Extract weekday name
df["Weekday"] = df["Date"].dt.day_name()

# Check if weekend (Saturday or Sunday)
df["IsWeekend"] = df["Weekday"].isin(["Saturday", "Sunday"])

# Extract city from Branch (format: "City - Area")
df["City"] = df["Branch"].str.split(" - ").str[0]

# ============================================================
# Step 5: Sidebar Filters
# ============================================================
st.sidebar.header("Filters")

# Filter by Branch
branch_options = df["Branch"].unique().tolist()
selected_branches = st.sidebar.multiselect("Select Branch", branch_options, default=branch_options)

# Filter by Product Category
category_options = df["ProductCategory"].unique().tolist()
selected_categories = st.sidebar.multiselect("Select Category", category_options, default=category_options)

# Filter by City
city_options = df["City"].unique().tolist()
selected_cities = st.sidebar.multiselect("Select City", city_options, default=city_options)

# Filter by Payment Method
payment_options = df["PaymentMethod"].unique().tolist()
selected_payments = st.sidebar.multiselect("Select Payment Method", payment_options, default=payment_options)

# Apply all filters to the data
filtered_df = df[
    (df["Branch"].isin(selected_branches)) &
    (df["ProductCategory"].isin(selected_categories)) &
    (df["City"].isin(selected_cities)) &
    (df["PaymentMethod"].isin(selected_payments))
]

# ============================================================
# Step 6: Key Performance Indicators (KPIs)
# ============================================================
st.header("Key Metrics")

# Create 4 columns for metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Revenue", value=f"{filtered_df['TotalAmount'].sum():.2f}")

with col2:
    st.metric(label="Total Transactions", value=len(filtered_df))

with col3:
    st.metric(label="Unique Customers", value=filtered_df["CustomerID"].nunique())

with col4:
    st.metric(label="Avg Transaction", value=f"{filtered_df['TotalAmount'].mean():.2f}")

# ============================================================
# Step 7: Charts Section
# ============================================================
st.header("Sales Visualizations")

# Row 1: Category and City charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Revenue by Product Category")
    # Group by category and sum revenue, sort smallest to largest for horizontal bar
    category_revenue = filtered_df.groupby("ProductCategory")["TotalAmount"].sum().sort_values(ascending=True)
    
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    category_revenue.plot(kind="barh", ax=ax1, color="skyblue")
    ax1.set_xlabel("Total Revenue")
    ax1.set_ylabel("Product Category")
    ax1.set_title("Revenue by Category")
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

with chart_col2:
    st.subheader("Revenue by City")
    # Group by city and sum revenue
    city_revenue = filtered_df.groupby("City")["TotalAmount"].sum().sort_values(ascending=True)
    
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    city_revenue.plot(kind="barh", ax=ax2, color="lightgreen")
    ax2.set_xlabel("Total Revenue")
    ax2.set_ylabel("City")
    ax2.set_title("Revenue by City")
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

# Row 2: Payment and Weekend charts
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("Payment Method Distribution")
    # Count how many transactions used each payment method
    payment_counts = filtered_df["PaymentMethod"].value_counts()
    
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    payment_counts.plot(kind="pie", ax=ax3, autopct="%1.1f%%", colors=["lightblue", "lightgreen", "lightyellow", "lightcoral"])
    ax3.set_ylabel("")
    ax3.set_title("Payment Methods")
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)

with chart_col4:
    st.subheader("Weekend vs Weekday Sales")
    # Group by IsWeekend and sum revenue
    weekend_sales = filtered_df.groupby("IsWeekend")["TotalAmount"].sum()
    
    # Create labels for True/False
    labels = []
    values = []
    for key, value in weekend_sales.items():
        if key:
            labels.append("Weekend")
        else:
            labels.append("Weekday")
        values.append(value)
    
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    ax4.bar(labels, values, color=["lightblue", "lightcoral"])
    ax4.set_ylabel("Total Revenue")
    ax4.set_title("Weekend vs Weekday Sales")
    plt.tight_layout()
    st.pyplot(fig4)
    plt.close(fig4)

# ============================================================
# Step 8: Top Products Table
# ============================================================
st.header("Top 10 Products by Quantity Sold")

# Group by product name, sum quantity, sort descending, take top 10
top_products = filtered_df.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(10)

# Display as a bar chart using Streamlit's built-in chart
st.bar_chart(top_products)

# Also show as a table
st.subheader("Top 10 Products Table")
for i, (product, qty) in enumerate(top_products.items(), 1):
    st.write(f"{i}. {product}: {qty} units")

# ============================================================
# Step 9: Download Cleaned Data
# ============================================================
st.header("Download Data")

# Convert filtered data to CSV for download
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download cleaned data as CSV",
    data=csv,
    file_name="cleaned_sales_data.csv",
    mime="text/csv"
)

# ============================================================
# Step 10: Footer Summary
# ============================================================
st.header("Summary")

st.write(f"""
- Total transactions in filtered data: {len(filtered_df)}
- Total revenue: {filtered_df['TotalAmount'].sum():.2f}
- Number of unique customers: {filtered_df['CustomerID'].nunique()}
- Number of unique products: {filtered_df['ProductName'].nunique()}
- Number of branches: {filtered_df['Branch'].nunique()}
- Number of cities: {filtered_df['City'].nunique()}
""")

st.success("Dashboard loaded successfully!")
