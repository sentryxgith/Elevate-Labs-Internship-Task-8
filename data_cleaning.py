import pandas as pd

# Load the dataset
file_path = 'S:\Elevate Labs Internship\Sample - Superstore.csv'  # Make sure this matches your actual file name
df = pd.read_csv(file_path, encoding = 'ISO-8859-1')

# Step 1: Check for missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# Step 2: Remove duplicate rows
df = df.drop_duplicates()


# Step 3: Rename columns (lowercase, underscores, remove special chars)
df.columns = [
    col.strip().lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
    for col in df.columns
]

# Step 4: Convert date columns to datetime if present
for col in df.columns:
    if 'date' in col:
        try:
            df[col] = pd.to_datetime(df[col])
        except Exception:
            pass

# Step 5: Fix data types for numeric columns if needed
numeric_cols = ['quantity', 'sales', 'discount', 'profit']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Save cleaned dataset
cleaned_file_path = 'cleaned_superstore3.csv'
df.to_csv(cleaned_file_path, index=False)

# Print summary info for README
print("\n--- Cleaning Summary ---")
print("Missing values after cleaning:\n", df.isnull().sum())
print("Columns after cleaning:", df.columns.tolist())
print("Final row count:", len(df))
print("Cleaned file saved as:", cleaned_file_path)
