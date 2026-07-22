# Bhatbhateni Sales Data Analysis

## Project Overview

This project analyzes sales data from Bhatbhateni supermarket. The analysis is performed using Python with `pandas` for data processing and `matplotlib` for visualization. A Streamlit dashboard is also available for interactive exploration.

## Dataset Description

- **File**: `bhatbhateni_sales.csv`
- **Records**: Transaction-level sales records
- **Columns**: TransactionID, Date, CustomerID, CustomerName, Branch, ProductCategory, ProductName, Quantity, UnitPrice, TotalAmount, PaymentMethod

---

## Data Quality Issues Found in Raw Data

### 1. Missing Values (Nulls)

| Column | Missing Count | Description |
|--------|--------------|-------------|
| CustomerName | Several | Customer identity missing for some transactions |
| ProductCategory | Several | Category not recorded for some products |
| UnitPrice | Several | Price per unit missing, though TotalAmount exists |
| PaymentMethod | Several | Payment type not recorded for some transactions |

### 2. Duplicate Rows

- **Exact duplicates**: Rows where all columns are identical to a previous row
- These are true duplicates, not genuine repeated purchases
- Cause: Likely data entry errors or system export issues

### 3. Logical Inconsistencies

- **TotalAmount mismatch**: Some rows had `TotalAmount != Quantity * UnitPrice`
- This happened because `UnitPrice` was missing or manually entered incorrectly

---

## Data Cleaning Decisions

### 1. Duplicate Removal

**Decision**: Remove exact duplicate rows using `df.drop_duplicates(keep="first")`.

**Justification**: Duplicate rows would artificially inflate counts and revenue totals. Keeping the first occurrence preserves the original transaction while eliminating redundant entries.

---

### 2. Missing CustomerName

**Decision**: Fill with `"Unknown"`.

**Justification**: CustomerName is an identity field. Dropping these rows would lose transaction and revenue data. `"Unknown"` preserves the transaction while clearly marking incomplete identity data.

---

### 3. Missing ProductCategory

**Decision**: Fill with `"Unknown"`.

**Justification**: ProductCategory is descriptive. While we could attempt to infer categories from ProductName, a safe fallback is `"Unknown"` to prevent grouping errors in analysis. This preserves the row and flags it for manual review if needed.

---

### 4. Missing UnitPrice

**Decision** (3-step imputation):

1. **Calculate from available data**: If `TotalAmount` and `Quantity` exist, compute `UnitPrice = TotalAmount / Quantity`
2. **Category median fallback**: If still missing, use the median UnitPrice of that product category
3. **Overall median fallback**: If category is also unknown, use the overall median UnitPrice

**Justification**: UnitPrice is critical for accurate `TotalAmount` calculation and revenue analysis. Deriving it from existing data (TotalAmount / Quantity) is mathematically sound. Median is used instead of mean to avoid skew from outliers. This preserves rows that would otherwise be unusable for revenue calculations.

---

### 5. Missing PaymentMethod

**Decision**: Fill with `"Unknown"`.

**Justification**: PaymentMethod is a descriptive field that does not affect revenue or quantity calculations. Dropping these rows would discard valid sales transactions. `"Unknown"` prevents null errors in grouping operations while indicating incomplete data.

---

### 6. TotalAmount Recalculation

**Decision**: After fixing UnitPrice, recalculate `TotalAmount = Quantity * UnitPrice`.

**Justification**: Ensures mathematical consistency across the dataset. This corrects any previous calculation errors and provides a reliable foundation for all revenue-based analysis.

---

## How to Run the Analysis

### Prerequisites

Install required libraries:

```bash
pip install pandas matplotlib streamlit
```

### Run the Script

```bash
python BSCS_Questions/week_4.py
```

This will:
1. Load and display raw data info
2. Clean the data (remove duplicates, fill nulls)
3. Perform 10 analysis questions with printed answers
4. Generate 3 charts saved as PNG files in `BSCS_Questions/`
5. Save cleaned data to `BSCS_Questions/week4_cleaned_sales.csv`

### Run the Dashboard

```bash
streamlit run BSCS_Questions/week4_dashboard.py
```

The dashboard includes:
- Sidebar filters for Branch, Category, City, and Payment Method
- KPI cards showing total revenue, transactions, customers, and average transaction
- 4 interactive charts: category revenue, city revenue, payment method distribution, weekend vs weekday sales
- Top 10 products bar chart and table
- Download button for filtered cleaned data

---

## Output Files

| File | Description |
|------|-------------|
| `chart1_category_sales.png` | Bar chart of sales by product category |
| `chart2_city_sales.png` | Bar chart of sales by city |
| `chart3_payment_method.png` | Pie chart of payment method distribution |
| `week4_cleaned_sales.csv` | Cleaned dataset ready for further analysis |

---

## Notes

- All cleaning operations preserve the original row count (except duplicate removal) to maximize data retention.
- Missing data flags (`"Unknown"`) are used instead of row deletion to avoid losing valuable transaction information.
- The cleaning logic is intentionally simple and well-commented for beginner-level understanding.
