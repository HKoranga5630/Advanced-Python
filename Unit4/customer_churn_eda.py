import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("Unit4/customer_churn.csv")

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# Step 2: Dataset information
print("\n--- DATASET INFORMATION ---")
print("Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

df.info()

# Step 3: Statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include="all").T)

# Step 4: Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Step 5: Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Number of duplicates:", df.duplicated().sum())

# Step 6: Clean column names
df.columns = df.columns.str.strip()

# Step 7: Remove duplicate rows
df = df.drop_duplicates()

# Step 8: Handle missing values
for column in df.columns:
    if df[column].isnull().any():
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].median())
        else:
            mode_values = df[column].mode()
            if not mode_values.empty:
                df[column] = df[column].fillna(mode_values.iloc[0])
            else:
                df[column] = df[column].fillna("Unknown")

# Step 9: Identify the churn column
possible_targets = ["Churn", "Exited", "Attrition"]
target = next(
    (col for col in possible_targets
     if col.lower() in df.columns.str.lower()),
    None
)

if target is not None:
    target = next(
        col for col in df.columns
        if col.lower() == target.lower()
    )

    print("\n--- CHURN DISTRIBUTION ---")
    print(df[target].value_counts(dropna=False))

    print("\n--- CHURN PERCENTAGE ---")
    print(
        (df[target].value_counts(normalize=True, dropna=False) * 100)
        .round(2)
    )

    # Visualise churn distribution
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x=target)
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()

    # Analyse categorical features against churn
    categorical_columns = [
        col for col in df.select_dtypes(include="object").columns
        if col != target
    ]

    for column in categorical_columns[:5]:
        print(f"\n--- {column} VS {target} ---")
        print(pd.crosstab(df[column], df[target], normalize="index").round(3))

    # Analyse numeric features against churn
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

    if numeric_columns:
        print("\n--- NUMERIC FEATURES BY CHURN ---")
        print(df.groupby(target)[numeric_columns].mean().round(2))

        # Correlation heatmap
        if len(numeric_columns) > 1:
            plt.figure(figsize=(10, 7))
            sns.heatmap(
                df[numeric_columns].corr(),
                annot=True,
                cmap="coolwarm",
                fmt=".2f"
            )
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            plt.show()
else:
    print(
        "\nNo recognised churn column found. "
        "Check the dataset for a column named Churn, Exited, or Attrition."
    )

# Step 10: Save the cleaned dataset
df.to_csv("Unit4/cleaned_customer_churn.csv", index=False)

print("\n--- CLEANING SUMMARY ---")
print("Rows after cleaning:", df.shape[0])
print("Columns:", df.shape[1])
print("Remaining missing values:", df.isnull().sum().sum())
print("Cleaned dataset saved as cleaned_customer_churn.csv")