import pandas as pd
import numpy as np



print("=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)

df = pd.read_csv("data/cleaned/cleaned_products.csv")


df["product_rating"] = pd.to_numeric(
    df["product_rating"],
    errors="coerce"
)

df["overall_rating"] = pd.to_numeric(
    df["overall_rating"],
    errors="coerce"
)


median_rating = df["product_rating"].median()

if pd.isna(median_rating):
    median_rating = 3.5

df["product_rating"] = df["product_rating"].fillna(median_rating)
df["overall_rating"] = df["overall_rating"].fillna(median_rating)



df["discount_amount"] = (
    df["retail_price"] -
    df["discounted_price"]
)



df["discount_percentage"] = (
    (df["discount_amount"] /
     df["retail_price"]) * 100
).round(2)



df["savings"] = df["discount_amount"]


def price_category(price):

    if price < 500:
        return "Budget"

    elif price < 2000:
        return "Mid Range"

    elif price < 10000:
        return "Premium"

    else:
        return "Luxury"

df["price_category"] = df["discounted_price"].apply(price_category)



def discount_level(discount):

    if discount < 10:
        return "Low"

    elif discount < 30:
        return "Medium"

    elif discount < 60:
        return "High"

    else:
        return "Mega"

df["discount_level"] = df["discount_percentage"].apply(discount_level)



brand_frequency = df["brand"].value_counts()

df["brand_frequency"] = df["brand"].map(brand_frequency)


df["product_name_length"] = (
    df["product_name"]
    .astype(str)
    .str.len()
)



df["description_length"] = (
    df["description"]
    .astype(str)
    .str.len()
)



df["category_count"] = (
    df["product_category_tree"]
    .astype(str)
    .str.count(">>") + 1
)


df.to_csv(
    "data/cleaned/featured_products.csv",
    index=False
)


print("\nFEATURE ENGINEERING COMPLETED SUCCESSFULLY\n")

print(f"Rows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nNEW FEATURES CREATED")

features = [
    "discount_amount",
    "discount_percentage",
    "savings",
    "price_category",
    "discount_level",
    "brand_frequency",
    "product_name_length",
    "description_length",
    "category_count"
]

for feature in features:
    print("✓", feature)

print("\nPreview\n")

print(df[
    [
        "product_name",
        "retail_price",
        "discounted_price",
        "discount_percentage",
        "price_category",
        "discount_level",
        "brand_frequency",
        "product_rating"
    ]
].head())

print("\nDataset saved as:")

print("data/cleaned/featured_products.csv")