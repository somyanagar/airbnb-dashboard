import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import os

# --------------------------------APP-------------------------
pages_folder = os.getcwd() + '/apps'
app=Dash(__name__, use_pages=True, pages_folder=pages_folder, external_stylesheets=[dbc.themes.JOURNAL])
server=app.server
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20%",
    "padding": "2rem 2rem",
    "background-color": "#F8F9FA",
}
sidebar = html.Div(
    [
        # html.H2("StaySpot Analytics", className="display-4"),
        html.Img(src='/assets/Logo.png', style={"width": "100%"}),
        html.Hr(),
        html.P(
            "StaySpot Analytics is your comprehensive dashboard for unlocking valuable insights into Airbnb data.", className="lead"
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Map", href="/", active="exact"),
                html.Br(),
                dbc.NavLink("Statistics", href="/statistics", active="exact"),
            ],
            vertical=True,
            pills=True,
            className='navbar-nav'
        ),
    ],
    style=SIDEBAR_STYLE,
)
app.layout=html.Div([
    sidebar,
    html.Div([
        dash.page_container
        ],
        className='content')
    ])
if __name__ == "__main__":

    app.run_server(port=8051,debug=True)

