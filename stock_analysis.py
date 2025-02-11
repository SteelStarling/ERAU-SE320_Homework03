"""Stock analysis program for SE 320 - Software Construction
Author: Taylor Hancock
Date:   02/10/2025
Class:  SE320 - Software Construction
Assignment: Assignment 03 - API Requests
"""

import requests

def download_data(ticker: str) -> dict:
    """Downloads historic data about the specified stock price
    
    Argument:
        ticker (string): the ticker code to search for

    Returns:
        Dictionary of json output summarizing stock data for the given ticker
    """
    YEAR_PERIOD = 5

    ticker = ticker.upper()
    today = date.today()
    start = str(today.replace(year=today.year - 5))
    base_url = "https://api.nasdaq.com"
    path = f"/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"
