# In[]:
# Import required libraries

import datetime as dt

import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as plotly
import quantmod as qm


# In[]:
# Create layout

app = dash.Dash("Stock market app")

app.layout = html.Div(
    [
        html.H1('Quantmod demo'),
        core.Dropdown(
            id='dropdown',
            options=[
                {'label': 'PowerShares QQQ Trust Series 1', 'value': 'QQQ'},
                {'label': 'SPDR S&P 500 ETF Trust', 'value': 'SPY'},
                {'label': 'Apple Inc', 'value': 'AAPL'},
                {'label': 'Goldman Sachs Group Inc', 'value': 'GS'},
            ],
            value='SPY',
        ),
        core.Graph(id='output')
    ]
)


# In[]:
# Setup callbacks

@app.callback(Output('output', 'figure'), [Input('dropdown', 'value')])
def update_graph(value):
    # Get Quantmod Chart
    ch = qm.get_symbol(value, start='2016/01/01')
    # Return plot as figure
    return ch.to_figure()


# In[]:
# Main

if __name__ == '__main__':
    app.run_server(debug=True)
