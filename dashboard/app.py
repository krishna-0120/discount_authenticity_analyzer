import pandas as pd
from dash import Dash
import dash_bootstrap_components as dbc

from dashboard.layout import create_layout
from dashboard.callbacks import register_callbacks

df = pd.read_csv("data/cleaned/scored_products.csv")

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

app.title = "Discount Authenticity Analyzer"

app.layout = create_layout(df)

register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=True)