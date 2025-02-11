Objective

In this assignment, you will write a Python program to fetch historical stock market data for selected companies and analyze key statistics. You will use web APIs to download stock price data and apply basic data analysis techniques to extract insights.
Learning Outcomes

By completing this assignment, you will:

    Use an API to fetch real-world financial data

    Process and extract relevant information from JSON responses

    Compute basic statistical measures (min, max, average, median)

    Handle potential API errors and exceptions

    Format and present your results in a structured manner

Instructions

    Fetching Stock Data:

        Write a function download_data(ticker: str) -> dict that retrieves historical stock data from Nasdaq (or an equivalent financial API).

        Use the requests module to send HTTP requests.

        The function should return a dictionary containing stock prices over a specified period (e.g., last 5 years).

    Data Processing:

        Extract the closing prices from the dataset.

        Return a dictionary that contains min, max, avg, and median

    Error Handling:

        Handle cases where the API request fails (e.g., invalid ticker, no data available).

        Use try-except blocks to manage exceptions.

    User Interaction:

        Allow your program to be called with ticker symbols like so:
        python stocks.py AAPL MSFT GOOGL AMZN TSLA
        Your program should create a stocks.json file with content that looks something like this:

        [

         {

        "min": 56.0925,

        "max": 259.02,

        "avg": 156.66105807478124,

        "medium": 154.51,

        "ticker": "AAPL"

         },

         {

        "min": 135.42,

        "max": 467.56,

        "avg": 298.64867939538584,

        "medium": 286.51,

        "ticker": "MSFT"

         },

         {

        "min": 52.7065,

        "max": 204.02,

        "avg": 121.07864359586317,

        "medium": 121.75,

        "ticker": "GOOGL"

         },

         {

        "min": 81.82,

        "max": 238.15,

        "avg": 148.88451471758154,

        "medium": 154.9955,

        "ticker": "AMZN"

         },

         {

        "min": 24.0813,

        "max": 479.86,

        "avg": 219.45611917263324,

        "medium": 222.415,

        "ticker": "TSLA"

         }

        ]

    Information to get you started:

    Download historic data for a given stock ticker symbol from Nasdaq.com.
    Details about it: https://www.nasdaq.com/market-activity/quotes/historical

    ticker = ticker.upper()
    today = date.today()
    start = str(today.replace(year=today.year - 5))
    base_url = "https://api.nasdaq.com"
    path = f"/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"

