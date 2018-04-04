<div align="center">
  <img src="https://raw.githubusercontent.com/jackwluo/py-quantmod/master/assets/banner.png"><br><br>
</div>

# Quantmod

[![Documentation Status](https://readthedocs.org/projects/py-quantmod/badge/?version=latest)](http://py-quantmod.readthedocs.io/en/latest/?badge=latest)

A powerful financial charting library based on R's Quantmod.

Quantmod makes creating interactive financial charts easy and intuitive. Furthermore, Quantmod has over 50 technical indicators built-in, in addition to a variety of technical and quantitative financial tools.

<div align="center">
  <img src="https://raw.githubusercontent.com/jackwluo/py-quantmod/master/assets/demo.gif"><br><br>
</div>

## Main features

#### Intuitive API

Financial charting should not hinder your research and trading.
Quantmod aims to provide the most user-friendly API so that you don't need to worry about making charts.

#### Fully interactive financial charts

Built on top of Plotly, Quantmod provides interactive, D3.js charting out of the box. No more Matplotlib images!
Easily toggle indicators simply by clicking on them, infinitely zoom on any graph, choose preset date ranges and more.

#### Pandas DataFrame integration

Because Pandas is the lingua franca of Python data science, Quantmod is tightly based upon the DataFrame object.
Easily switch from Series/DataFrame to Chart, and vice-versa.

#### 50+ technical indicators and statistical tools

From EMA, to RSI, to BBANDS, to ULTOSC, Quantmod has nearly every indicator out of the box.
Indicators are implemented with custom bindings to industry standard Ta-Lib; Python-only technical implementations coming soon.

#### Plotly Dash integration

Quantmod integrates nicely with Dash, allowing you to build modern React webapps in pure Python.
The stock market app above takes less than 5 minutes and 50 lines to make.

#### Data acquisition engine

Quantmod has end-of-day data acquisition functionality via get_symbol().
Tick data acquisition for past month (via built-in scraping) coming soon.

#### Theming engine

Choose from included Quantmod themes or design your own to customize chart appearance.

## Installation

Install from PyPI:

    pip install quantmod

Or build package from source:

    python setup.py install

Ta-Lib is additionally required for technical indicator support.

### Dependencies

Quantmod requires plotly, pandas and pandas_datareader to work properly (hard dependencies).

In addition, an installation of Ta-Lib is strongly recommended as it is required for technical indicator support.

The hard dependencies should be automatically installed with pip, but Ta-Lib requires a longer install.

First install the C/C++ package.

For Mac:

    brew install ta-lib

For Windows:

    Download ta-lib-0.4.0-msvc.zip and unzip to C:\ta-lib
  https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-msvc.zip

For Linux:

    Download ta-lib-0.4.0-src.tar.gz and:  
    $ untar and cd
    $ ./configure --prefix=/usr
    $ make
    $ sudo make install
  http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

Then install the Python library:

    pip install TA-Lib

## Documentation

Read the full documentation over at:

http://py-quantmod.readthedocs.io/en/latest/

If you prefer learning by example, hands-on tutorials are coming soon.

## Getting started

See the start_here.ipynb notebook provided in the repository.

## Dash integration

See the dash_example notebooks provided in the repository.

## License

MIT
