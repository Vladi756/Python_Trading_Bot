import time
import alpaca_trade_api as tradeapi
import numpy as np

# Put your Secure and Public Keys here - generate them at Alpaca paper trading account
API_KEY = ''
API_SEC = ''

# Base URL for paper trading (not real money)
BASE_URL = 'https://paper-api.alpaca.markets'

# Open the API connection -- if you want to tradde with real money, change URL accordingly 
API = tradeapi.REST(key_id = API_KEY, secret_key= API_SEC, base_url= BASE_URL)
# Ticker of stock to be traded - in this case the SPY index which
# tracks the S&P 500. 
symb = 'SPY'

# Default value of position held
pos_held = False

# Modularizing buying and selling stock by creating functions to 
# make the API calls to buy/sell dynamically - dependent on user input. 

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

# Sell function to sell certain amount of stock
def sell(quantity, stock) :
    # Sell Stock through API
    API.submit_order(
    symbol= stock,         
    qty = quantity,              
    side = 'sell',         # Change side to 'sell'
    type = 'market',
    time_in_force = 'gtc'  
)

# Function to return numpy array of the closing proces of the past 5 days
def getData():
    marketData = API.get_barset(symb, 'day', limit=5)
    
    # To store results
    close_prices_list = []
    for bar in marketData[symb]:
        close_prices_list.append(bar.c)
    
    # Convert list to numpy array
    close_list = np.array(close_prices_list, dtype=np.float64)

# Implementing Strategy 

while True: 
    # Let user know the bot is fetching Market data
    print("")
    print("Fetching Price...")

    # Fetch Data by invoking the getData function 
    close_prices_list = getData()

    # Calculate moving average of Data
    movingAverage = np.mean(close_prices_list)
    # Last observation from Market data
    last_price = close_prices_list[4]

    print("Moving Average: " + str(movingAverage))
    print("Las Price:" + str(last_price))

    # This algorithm buys stock when the moving average crosses the most
    # recent closing price. 

    # Buy when moving averge is at least 10 cents below the last price
    if movingAverage + 0.1 < last_price and not pos_held:
        print("Buying Stock...")
        # Invokes function with dynamic values, function performs API call
        buy(1, symb)
        pos_held = True  # Since we now own stock
    
    # If the moving average is at least 10 cents above the last price and we own stock
    elif movingAverage - 0.1 > last_price and pos_held:
        print("Selling Stock...")
        # Same invocation, except now it's selling 
        sell(1, symb)
        pos_held = False
    
    # To let the prices update, sleep, and then run again
    time.sleep(60)