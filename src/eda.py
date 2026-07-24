import os
import pandas as pd
import matplotlib.pyplot as plt


print("=" * 70)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 70)

df = pd.read_csv("data/cleaned/featured_products.csv")



os.makedirs("outputs/charts", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)



summary = pd.DataFrame({
    "Metric": [
        "Total Products",
        "Total Brands",
        "Average Retail Price",
        "Average Discounted Price",
        "Average Discount %",
        "Average Rating"
    ],
    "Value": [
        len(df),
        df["brand"].nunique(),
        round(df["retail_price"].mean(),2),
        round(df["discounted_price"].mean(),2),
        round(df["discount_percentage"].mean(),2),
        round(df["product_rating"].mean(),2)
    ]
})

print(summary)

summary.to_csv(
    "outputs/reports/dataset_summary.csv",
    index=False
)


top_brands = (
    df["brand"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,6))

top_brands.plot(kind="bar")

plt.title("Top 10 Brands")

plt.xlabel("Brand")

plt.ylabel("Number of Products")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_10_brands.png"
)

plt.close()



plt.figure(figsize=(10,6))

plt.hist(
    df["discount_percentage"],
    bins=30
)

plt.title("Discount Percentage Distribution")

plt.xlabel("Discount %")

plt.ylabel("Products")

plt.tight_layout()

plt.savefig(
    "outputs/charts/discount_distribution.png"
)

plt.close()



plt.figure(figsize=(10,6))

plt.hist(
    df["discounted_price"],
    bins=30
)

plt.title("Discounted Price Distribution")

plt.xlabel("Price")

plt.ylabel("Products")

plt.tight_layout()

plt.savefig(
    "outputs/charts/price_distribution.png"
)

plt.close()



top_categories = (
    df["product_category_tree"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12,6))

top_categories.plot(kind="bar")

plt.title("Top Categories")

plt.xticks(rotation=70)

plt.tight_layout()

plt.savefig(
    "outputs/charts/top_categories.png"
)

plt.close()



discount_levels = (
    df["discount_level"]
    .value_counts()
)

plt.figure(figsize=(8,5))

discount_levels.plot(kind="bar")

plt.title("Discount Levels")

plt.tight_layout()

plt.savefig(
    "outputs/charts/discount_levels.png"
)

plt.close()

print("\nCharts saved successfully!")

print("\nLocation:")
print("outputs/charts/")

print("\nReport saved:")
print("outputs/reports/dataset_summary.csv")