import plotly.express as px

CHART_HEIGHT = 450

def discount_distribution(df):

    fig = px.histogram(
        df,
        x="discount_percentage",
        nbins=30,
        title="Discount Percentage Distribution"
    )

    fig.update_layout(
    height=380,
    autosize=False,
    template="plotly_white"
)

    return fig


def status_distribution(df):

    fig = px.pie(
        df,
        names="status",
        title="Status Distribution"
    )

    fig.update_layout(
    height=380,
    autosize=False,
    template="plotly_white"
)

    return fig


def top_brands(df):

    brands = (
        df["brand"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    brands.columns = ["brand", "count"]

    fig = px.bar(
        brands,
        x="brand",
        y="count",
        title="Top 10 Brands"
    )

    fig.update_layout(
    height=380,
    autosize=False,
    template="plotly_white"
)

    return fig


def top_discount_products(df):

    products = (
        df.sort_values(
            by="discount_percentage",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        products,
        x="discount_percentage",
        y="product_name",
        orientation="h",
        title="Top 10 Highest Discounts"
    )

    fig.update_layout(
    height=380,
    autosize=False,
    template="plotly_white"
)

    return fig