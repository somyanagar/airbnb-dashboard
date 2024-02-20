import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


# --------------------------------APP-------------------------
app=Dash(__name__, use_pages=True, pages_folder='apps', external_stylesheets=[dbc.themes.JOURNAL])
server=app.server
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "22rem",
    "padding": "2rem 2rem",
    "background-color": "#f8f9fa",
   
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Map", href="/", active="exact"),
                html.Br(),
                dbc.NavLink("Statistics", href="/statistics", active="exact"),
                html.Br(),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
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
    dash.page_container
])

if __name__ == "__main__":
    app.run_server(port=8080,debug=True)