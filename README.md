# 🛍️ Discount Authenticity Analyzer

An interactive Python dashboard that analyzes e-commerce discounts and identifies whether a product's discount appears genuine, requires verification, or is potentially high risk.
Built using Python, Pandas, Plotly, and Dash, this project demonstrates the complete data analytics workflow—from raw data cleaning to an interactive business dashboard.

---

## Project Overview

Online shopping platforms often advertise large discounts that may not always reflect genuine savings. This project analyzes retail and discounted prices, applies a rule-based scoring engine, and classifies products into authenticity categories.

The dashboard allows users to:

- Explore product discounts
- Analyze discount patterns
- Identify potentially misleading discounts
- Filter products by brand and status
- Search products instantly
- View detailed product information

---

## Features

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Rule-Based Authenticity Scoring
- Interactive Dashboard
- Dynamic Filters
- Search Functionality
- KPI Cards
- Brand Analytics
- Discount Distribution
- Risk Classification

---

## Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Dash
- Dash Bootstrap Components

---

## Dashboard

The dashboard includes:

- Total Products KPI
- Average Discount
- Average Authenticity Score
- High Risk Products
- Product Search
- Brand Filter
- Status Filter
- Product Details
- Discount Distribution
- Status Distribution
- Top Brands
- Top Discounted Products

---

## Authenticity Classification

Products are classified into three categories:

| Score | Classification |
|-------|----------------|
| High | Genuine |
| Medium | Needs Verification |
| Low | High Risk |

The scoring considers:

- Discount Percentage
- Product Rating
- Brand Presence
- Price Category
- Discount Level

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Discount-Authenticity-Analyzer.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
python dashboard/app.py
```

## Future Improvements

- Machine Learning Risk Prediction
- User Authentication
- PDF Report Generation
- Export Filtered Results
- Cloud Deployment

---

## Author

**A Vamshi Krishna**

---