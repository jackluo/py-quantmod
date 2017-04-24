from setuptools import setup


exec (open('quantmod/version.py').read())  # noqa

setup(
    name='quantmod',
    version=__version__,  # noqa
    author='Jack Luo',
    author_email='jackluo@plot.ly',
    description="Powerful financial charting library based on R's Quantmod.",
    long_description=open('README.md').read(),
    license='MIT',
    keywords=['pandas', 'plotly', 'ta-lib', 'data-visualization',
              'data-science', 'quantitative-finance', 'quantitative-trading'],
    packages=['quantmod'],
    install_requires=[
        'numpy',
        'pandas',
        'pandas_datareader',
        'plotly'
    ]
)
