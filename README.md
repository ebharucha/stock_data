# Stock Data Fetcher

This Python script reads a list of stock symbols from a text file, fetches key financial metrics for each symbol from Yahoo Finance, and outputs the results to a CSV file. The primary metrics collected include:

- **PE (Price-to-Earnings) Ratio**
- **ROE (Return on Equity)**
- **Dividend Yield**
- **Earnings Date**

The data is automatically sorted by the earnings date in chronological order.

## Features

- Reads stock symbols from a plain text file (`stocks.txt`) — one symbol per line.
- Fetches real-time financial data using the `yahooquery` Python library.
- Handles missing or unavailable data gracefully by marking it as `"N/A"`.
- Sorts the resulting data by earnings date, placing stocks with unknown earnings dates at the end.
- Saves the cleaned and sorted data to a CSV file (`stocks_data.csv`) for further analysis.

## Dependencies

- Python 3.9 or higher
- [pandas](https://pandas.pydata.org/)
- [yahooquery](https://pypi.org/project/yahooquery/)

### Install Dependencies

You can install the required packages using pip:

```bash
pip install -r requirements.txt
