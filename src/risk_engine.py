import pandas as pd
import numpy as np




print("=" * 60)
print("RISK ENGINE")
print("=" * 60)

df = pd.read_csv("data/cleaned/featured_products.csv")



df["authenticity_score"] = 50



df.loc[df["discount_percentage"] <= 60, "authenticity_score"] += 25

df.loc[
    (df["discount_percentage"] > 60) &
    (df["discount_percentage"] <= 80),
    "authenticity_score"
] += 10

df.loc[df["discount_percentage"] > 80, "authenticity_score"] -= 20



df.loc[df["product_rating"] >= 4, "authenticity_score"] += 20

df.loc[
    (df["product_rating"] >= 3) &
    (df["product_rating"] < 4),
    "authenticity_score"
] += 10

df.loc[df["product_rating"] < 3, "authenticity_score"] -= 15



df.loc[df["brand"] != "Unknown", "authenticity_score"] += 20

df.loc[df["brand"] == "Unknown", "authenticity_score"] -= 20



df.loc[
    df["price_category"].isin(["Premium", "Luxury"]),
    "authenticity_score"
] += 10



df.loc[df["discount_level"] == "Mega", "authenticity_score"] -= 15



df["authenticity_score"] = df["authenticity_score"].clip(0, 100)



conditions = [
    df["authenticity_score"] >= 70,
    (df["authenticity_score"] >= 40) &
    (df["authenticity_score"] < 70),
    df["authenticity_score"] < 40
]

choices = [
    "Genuine",
    "Needs Verification",
    "High Risk"
]

df["status"] = np.select(
    conditions,
    choices,
    default="Needs Verification"
)



df.to_csv(
    "data/cleaned/scored_products.csv",
    index=False
)



print("\nSTATUS COUNT\n")

print(df["status"].value_counts())

print("\nAVERAGE AUTHENTICITY SCORE")

print(round(df["authenticity_score"].mean(), 2))

print("\nTOP 10 HIGH RISK PRODUCTS\n")

high_risk = (
    df[df["status"] == "High Risk"]
    .sort_values(
        by="authenticity_score"
    )
)

print(
    high_risk[
        [
            "product_name",
            "brand",
            "discount_percentage",
            "product_rating",
            "authenticity_score"
        ]
    ].head(10)
)

print("\nDataset saved to:")

print("data/cleaned/scored_products.csv")