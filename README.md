# Python_Trading_Bot

A trading bot which uses the Alpaca trading API to fetch data and execute trades. Note that the bot is configured to perform paper trades only, meaning it does not use real money. 

## 1. Fetching the Data 

The Alpaca API is very intuitive and has useful functions to help:

> `barset = api.get_barset('AAPL', 'day', limit=5)`

Gets the daily price data for Apple over the last 5 trading days. This is how the bot fetches data from the market. 

## 2. Buying & Selling Stock 

The bot has functions which make it more modular as well as dynamic. The functions are invoked based on the trading strategy one chooses, when they are invoked they perform API buy/sell calls (depending on the function). 

The user specifies which stock and the quantity of stock they wish to buy/sell in the function call itself. 

<code>
# Buy function to buy certain amount of stock
def buy(quantity, stock) :
    # Buy Stock through API
        API.submit_order(
        symbol= stock,         
        qty = quantity,       # Quantity
        side = 'buy',         # To indicate buying
        type = 'market',
        time_in_force = 'gtc' # Good 'til Cancelled 
)
</code>

The above is the buy function the bot uses. 







