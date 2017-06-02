# In[]:
# Import required libraries

import os

import pandas as pd
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_caching import Cache
import quantmod as qm


# In[]:
# Create layout

app = dash.Dash("Quantmod Full Demo")
app.css.append_css({
    'external_url': (
        'https://rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

# Add caching
# cache = Cache(app.server, config={
#    'CACHE_TYPE': 'redis',
#    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', '127.0.0.1:6379')
# })
# timeout = 60 * 60  # 1 hour

# Controls
sp500 = ['AAPL', 'ABT', 'ABBV', 'ACN', 'ACE', 'ADBE', 'ADT', 'AAP', 'AES',
         'AET', 'AFL', 'AMG', 'A', 'GAS', 'ARE', 'APD', 'AKAM', 'AA', 'AGN',
         'ALXN', 'ALLE', 'ADS', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AAL',
         'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC',
         'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP',
         'AN', 'AZO', 'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR',
         'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK.B', 'BBY', 'BLX', 'HRB',
         'BA', 'BWA', 'BXP', 'BSX', 'BMY', 'BRCM', 'BF.B', 'CHRW', 'CA',
         'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'HSIC', 'KMX', 'CCL',
         'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW',
         'CHK', 'CVX', 'CMG', 'CB', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C',
         'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL',
         'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW',
         'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA',
         'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA',
         'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK',
         'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA',
         'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX',
         'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM',
         'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FISV',
         'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX',
         'FTR', 'GME', 'GPS', 'GRMN', 'GD', 'GE', 'GGP', 'GIS', 'GM',
         'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL',
         'HBI', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HCN',
         'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK',
         'HUM', 'HBAN', 'ITW', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG',
         'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ',
         'JCI', 'JOY', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'GMCR', 'KMB',
         'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LB', 'LLL', 'LH',
         'LRCX', 'LM', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC',
         'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC',
         'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MCK',
         'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT',
         'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI',
         'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL',
         'NFX', 'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL',
         'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY',
         'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO',
         'PAYX', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE',
         'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL',
         'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD',
         'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM',
         'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI',
         'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RLD', 'R', 'CRM', 'SNDK',
         'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SPG', 'SWKS',
         'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK',
         'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY',
         'TROW', 'TGT', 'TEL', 'TE', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN',
         'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TJX', 'TMK',
         'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA',
         'UNP', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'URBN', 'VFC',
         'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO',
         'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'ANTM', 'WFC', 'WDC',
         'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL',
         'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']

etf = ['SPY', 'XLF', 'GDX', 'EEM', 'VXX', 'IWM', 'UVXY', 'UXO', 'GDXJ', 'QQQ']

tickers = sp500 + etf
tickers = [dict(label=str(ticker), value=str(ticker))
           for ticker in tickers]

functions = dir(qm.ta)[9:-4]
functions = [dict(label=str(function[4:]), value=str(function))
             for function in functions]

# Layout
app.layout = html.Div(
    [
        html.H2('Quantmod Charts'),
        html.Div(
            [
                html.Span(
                    core.Dropdown(
                        id='dropdown',
                        options=tickers,
                        value='SPY',
                    ),
                    style={
                        'width': '450px',
                        'display': 'inline-block',
                        'text-align': 'left'
                    },
                ),
                html.Span(
                    core.Dropdown(
                        id='multi',
                        options=functions,
                        multi=True,
                        value=[],
                    ),
                    style={
                        'width': '450px',
                        'display': 'inline-block',
                        'text-align': 'left'
                    },
                ),
            ]
        ),
        html.Div(
            [html.Label('Custom Arguments:'), core.Input(id='arglist')],
            id='arg-controls',
            style={'display': 'none'}
        ),
        core.Graph(id='output')
    ],
    style={
        'width': '900',
        'margin-left': 'auto',
        'margin-right': 'auto',
        'text-align': 'center',
        'font-family': 'overpass',
        'background-color': '#F3F3F3'
    }
)

@app.callback(Output('arg-controls', 'style'), [Input('multi', 'value')])
def display_control(multi):
    if not multi:
        return {'display': 'none'}
    else:
        return {'display': 'inline-block'}

@app.callback(Output('output', 'figure'), [Input('dropdown', 'value'),
                                           Input('multi', 'value'),
                                           Input('arglist', 'value')])
# @cache.memoize(timeout=timeout)
def update_graph_from_dropdown(dropdown, multi, arglist):
    # Get Quantmod Chart
    ch = qm.get_symbol(dropdown, start='2016/01/01')
    # Get functions
    if arglist:
        arglist = arglist.replace('(', '').replace(')', '').split(';')
        arglist = [args.strip() for args in arglist]
        for function, args in zip(multi, arglist):
            if args:
                args = args.split(',')
                newargs = []
                for arg in args:
                    try:
                        arg = int(arg)
                    except:
                        try:
                            arg = float(arg)
                        except:
                            pass
                    newargs.append(arg)

                print(newargs)
                getattr(qm, function)(ch, *newargs)
            else:
                getattr(qm, function)(ch)
    else:
        for function in multi:
            getattr(qm, function)(ch)

    # Return plot as figure
    fig = ch.to_figure(width=900)
    return fig


# In[]:
# Main

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=4002)
