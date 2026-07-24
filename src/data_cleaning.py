import pandas as pd

df = pd.read_csv("data/raw/flipkart_com-ecommerce_sample.csv")

print("="*60)
print("ORIGINAL DATASET")
print("="*60)

print(f"Rows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumns after cleaning:\n")
print(df.columns.tolist())


duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows Found : {duplicates}")

df.drop_duplicates(inplace=True)

print(f"Rows after removing duplicates : {len(df)}")


print("\nMissing Values\n")

missing = df.isnull().sum()

print(missing[missing > 0])


print("\nDataset Information\n")


df = df.dropna(subset=["retail_price", "discounted_price"])

df["brand"] = df["brand"].fillna("Unknown")

df["description"] = df["description"].fillna("No Description")

df["product_specifications"] = df["product_specifications"].fillna("Not Available")

df["image"] = df["image"].fillna("No Image")


print("\nMissing Values After Cleaning\n")
print(df.isnull().sum())


df = df[df["retail_price"] > 0]
df = df[df["discounted_price"] > 0]

print(f"\nRows after removing invalid prices : {len(df)}")


df.to_csv(
    "Data/cleaned/cleaned_products.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")