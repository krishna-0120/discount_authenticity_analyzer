from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

def create_layout(df):

    total_products = len(df)
    avg_discount = round(df["discount_percentage"].mean(), 2)
    avg_score = round(df["authenticity_score"].mean(), 2)
    high_risk = len(df[df["status"] == "High Risk"])

    return dbc.Container([

        html.H1(
            "Discount Authenticity Analyzer",
            className="text-center mt-4 mb-3"
        ),

        html.P(
            "Analyze product discounts and identify Genuine, Needs Verification and High Risk products.",
            className="text-center text-muted mb-4"
        ),

        dbc.Row([

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2(f"{total_products:,}", className="text-primary"),
                        html.H5("Total Products")
                    ])
                ]),
                width=3
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2(f"{avg_discount}%", className="text-success"),
                        html.H5("Average Discount")
                    ])
                ]),
                width=3
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2(f"{avg_score}", className="text-info"),
                        html.H5("Authenticity Score")
                    ])
                ]),
                width=3
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2(f"{high_risk}", className="text-danger"),
                        html.H5("High Risk Products")
                    ])
                ]),
                width=3
            )

        ], className="mb-4"),

        dbc.Card([

            dbc.CardBody([

                dbc.Row([

                    dbc.Col([

                        html.Label("Status"),

                        dcc.Dropdown(
                            id="status_filter",
                            options=[
                                {"label": i, "value": i}
                                for i in sorted(df["status"].unique())
                            ],
                            multi=True,
                            placeholder="Select Status"
                        )

                    ], width=3),

                    dbc.Col([

                        html.Label("Brand"),

                        dcc.Dropdown(
                            id="brand_filter",
                            options=[
                                {"label": i, "value": i}
                                for i in sorted(df["brand"].unique())
                            ],
                            multi=True,
                            placeholder="Select Brand"
                        )

                    ], width=4),

                    dbc.Col([

                        html.Label("Search Product"),

                        dcc.Input(
                            id="search_product",
                            type="text",
                            placeholder="Search Product...",
                            style={"width": "100%"}
                        )

                    ], width=5)

                ])

            ])

        ], className="mb-4"),

        dash_table.DataTable(

            id="product_table",

            columns=[
                {"name": "Product", "id": "product_name"},
                {"name": "Brand", "id": "brand"},
                {"name": "Discount %", "id": "discount_percentage"},
                {"name": "Rating", "id": "product_rating"},
                {"name": "Score", "id": "authenticity_score"},
                {"name": "Status", "id": "status"}
            ],

            data=[],

            page_size=12,

            row_selectable="single",

            selected_rows=[],

            style_table={
                "overflowX": "auto"
            },

            style_cell={
                "textAlign": "left",
                "padding": "10px",
                "fontFamily": "Arial",
                "fontSize": "14px"
            },

            style_header={
                "backgroundColor": "#0d6efd",
                "color": "white",
                "fontWeight": "bold"
            },

            style_data_conditional=[

                {
                    "if": {
                        "filter_query": '{status} = "High Risk"'
                    },
                    "backgroundColor": "#f8d7da"
                },

                {
                    "if": {
                        "filter_query": '{status} = "Needs Verification"'
                    },
                    "backgroundColor": "#fff3cd"
                },

                {
                    "if": {
                        "filter_query": '{status} = "Genuine"'
                    },
                    "backgroundColor": "#d1e7dd"
                }

            ]

        ),

        html.Br(),

        dbc.Card([

            dbc.CardHeader("Product Details"),

            dbc.CardBody([

                html.Div(
                    id="product_details",
                    children="Select a product from the table."
                )

            ])

        ], className="mb-4"),

        dbc.Row([

            dbc.Col(
                dcc.Graph(
                        id="discount_distribution",
                        style={
                                "height":"380px"
                            },
                        config={
                                "responsive":False
                                }
                        )
            ),

            dbc.Col(
                dcc.Graph(
    id="status_distribution",
    style={"height":"380px"},
    config={"responsive":False}
)
            )

        ]),

        html.Br(),

        dbc.Row([

            dbc.Col(
                dcc.Graph(
    id="top_brands",
    style={"height":"380px"},
    config={"responsive":False}
)
            ),

            dbc.Col(
                dcc.Graph(
    id="top_discount_products",
    style={"height":"380px"},
    config={"responsive":False}
)
            )

        ])

    ], fluid=True)