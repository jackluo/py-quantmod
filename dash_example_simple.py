# In[]:
# Import required libraries

import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output
import quantmod as qm


# In[]:
# Create layout

app = dash.Dash("Stock market app")
app.css.append_css({
    'external_url': (
        'https://rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

app.layout = html.Div(
    [
        html.H1('Quantmod Demo | 5-minute App'),
        core.Dropdown(
            id='dropdown',
            options=[
                dict(label='PowerShares QQQ Trust Series 1', value='QQQ'),
                dict(label='SPDR S&P 500 ETF Trust', value='SPY'),
                dict(label='Apple Inc', value='AAPL'),
                dict(label='Goldman Sachs Group Inc', value='GS'),
            ],
            value='SPY',
        ),
        core.Dropdown(
            id='multi',
            options=[
                dict(label='EMA', value='EMA'),
                dict(label='RSI', value='RSI'),
                dict(label='MACD', value='MACD'),
                dict(label='BBANDS', value='BBANDS'),
            ],
            multi=True,
            value=[],
        ),
        core.Graph(id='output')
    ]
)


# In[]:
# Setup callbacks

@app.callback(Output('output', 'figure'), [Input('dropdown', 'value'),
                                           Input('multi', 'value')])
def update_graph_from_dropdown(dropdown, multi):
    # Get Quantmod Chart
    ch = qm.get_symbol(dropdown, start='2016/01/01')

    if 'EMA' in multi:
        ch.add_EMA()
    if 'RSI' in multi:
        ch.add_RSI()
    if 'MACD' in multi:
        ch.add_MACD()
    if 'BBANDS' in multi:
        ch.add_BBANDS()

    # Return plot as figure
    return ch.to_figure()


# In[]:
# Main

if __name__ == '__main__':
    app.run_server(debug=True, port=4001)
