from dash import Input, Output, html
from charts import (
    discount_distribution,
    status_distribution,
    top_brands,
    top_discount_products
)

def register_callbacks(app, df):

    @app.callback(
        Output("product_table", "data"),
        Output("discount_distribution", "figure"),
        Output("status_distribution", "figure"),
        Output("top_brands", "figure"),
        Output("top_discount_products", "figure"),
        Input("status_filter", "value"),
        Input("brand_filter", "value"),
        Input("search_product", "value")
    )
    def update_dashboard(status, brand, search):

        filtered = df.copy()

        if status:
            filtered = filtered[
                filtered["status"].isin(status)
            ]

        if brand:
            filtered = filtered[
                filtered["brand"].isin(brand)
            ]

        if search:
            filtered = filtered[
                filtered["product_name"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        table = filtered[
            [
                "product_name",
                "brand",
                "discount_percentage",
                "product_rating",
                "authenticity_score",
                "status"
            ]
        ].to_dict("records")

        return (
            table,
            discount_distribution(filtered),
            status_distribution(filtered),
            top_brands(filtered),
            top_discount_products(filtered)
        )

    @app.callback(
        Output("product_details", "children"),
        Input("product_table", "derived_virtual_data"),
        Input("product_table", "selected_rows")
    )
    def show_product_details(rows, selected):

        if rows is None or len(rows) == 0:
            return "No products available."

        if not selected:
            return "Select a product from the table."

        product = rows[selected[0]]

        return html.Div([

            html.H4(product["product_name"]),

            html.Hr(),

            html.P(f"Brand: {product['brand']}"),
            html.P(f"Discount Percentage: {product['discount_percentage']:.2f}%"),
            html.P(f"Product Rating: {product['product_rating']}"),
            html.P(f"Authenticity Score: {product['authenticity_score']}"),
            html.P(f"Status: {product['status']}")

        ])