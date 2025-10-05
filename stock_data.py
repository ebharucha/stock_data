###########################
# ebharucha, 10/5/2025
###########################

import os
from pathlib import Path
import pandas as pd
from yahooquery import Ticker
from datetime import datetime
import time

def get_stock_data(input_stock_symbols):
    with open(input_stock_symbols, "r") as f:
        symbols = [stock.strip() for stock in f if stock.strip()]
    data = []
    for symbol in symbols:
        try:
            ticker = Ticker(symbol)
            current_price = ticker.financial_data[symbol]['currentPrice']
            pe = ticker.summary_detail[symbol]['trailingPE']
            roe = ticker.financial_data[symbol]['returnOnEquity']
            divyield = f'{ticker.summary_detail[symbol]["dividendYield"]*100}%'
            earnings_date = ticker.calendar_events[symbol]['earnings']['earningsDate'][0]
            data.append({"Symbol": symbol,
                         "PE": pe,
                         "ROE": roe,
                         "Dividend Yield": divyield,
                         "Earnings Date": earnings_date}
                       )
            print(f"Fetched: {symbol} - data")
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            data.append({"Symbol": symbol,
                         "PE": pe,
                         "ROE": roe,
                         "Dividend Yield": "N/A",
                         "Earnings Date": earnings_date}
                       )
    # print (data)
    # exit()
    sorted_data = sorted(
        data,
        key=lambda x: datetime.strptime(x['Earnings Date'].replace(':S',''), '%Y-%m-%d %H:%M')
            if x['Earnings Date'] != 'N/A' else datetime.max
    )
    # print (sorted_data)
    return (pd.DataFrame(sorted_data))

if __name__ == "__main__":
    input_stock_symbols = "data/stocks.txt"
    output_stocks_data = "data/stocks_data.csv"
    if not Path(input_stock_symbols).is_file():
        raise FileNotFoundError(f"The file '{input_stock_symbols}' does not exist.")
    df = get_stock_data(input_stock_symbols)
    df.to_csv(output_stocks_data, index=False)
    print(f'✅ Data successfully written to {output_stocks_data}')