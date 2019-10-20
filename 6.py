pip install cryptocompy
from cryptocompy import price

price = price.get_current_price(["BTC", "LTC", "ZEC"], ["EUR"])