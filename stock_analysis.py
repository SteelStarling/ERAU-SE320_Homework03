"""Stock analysis program for SE 320 - Software Construction
Author: Taylor Hancock
Date:   02/10/2025
Class:  SE320 - Software Construction
Assignment: Assignment 03 - API Requests
"""

from datetime import date
from requests import get

def download_data(ticker: str) -> dict:
    """Downloads historic data about the specified stock price
    
    Argument:
        ticker (string): the ticker code to search for

    Returns:
        Dictionary of json output summarizing stock data for the given ticker
    """
    YEAR_PERIOD = 5

    # capitalize (all ticker names capitalized)
    ticker = ticker.upper()

    # calc start date
    today = date.today()
    start = str(today.replace(year=today.year - YEAR_PERIOD))

    # url handling
    base_url = "https://api.nasdaq.com"
    path = f"/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"
    full_url = base_url + path

    # use a header so it works (otherwise it throws an error)
    response = get(full_url, headers={"User-Agent": "Mozilla/5.0"}).json()

    return response

if __name__ == "__main__":
    ticker = "LMT"
    d = download_data(ticker)
    for row in d['data']['tradesTable']['rows']:
        print(f"On {row['date']}, {ticker} opened at {row['open']}")