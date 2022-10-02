import alpaca_trade_api as tradeapi

# Put your Secure and Public Keys here - generate them at Alpaca paper trading account
API_KEY = ''
API_SEC = ''

# Base URL for paper trading (not real money)
BASE_URL = 'https://paper-api.alpaca.markets'

# Open the API connection -- if you want to tradde with real money, change URL accordingly 
API = tradeapi.REST(key_id = API_KEY, secret_key= API_SEC, base_url= BASE_URL)
