
# --- imports

import requests
from yahoo_fin import stock_info as si



# --- globals

from Skills.skills_settings import *



# --- functions

def get_stock_price(request, site = 'yahoo'):
    
    # Extract company name
    pos    = request.find("stock price of")
    myfirm = request[pos + len("stock price of "): ]

    # Prevent crashing in case there is no result
    try:
        # Extract the source code from the website
        url = STOCKS_URL[site] + myfirm
        res = requests.get(url)
        # Read the JSON data
        res_json = res.json()
        quotes   = res_json['quotes']
        ticker   = quotes[0]['symbol']
        # Obtain real-time stock price from Yahoo
        price = round(float(si.get_live_price(ticker)), 2)
        # Return the stock price
        stock_msg = f"the stock price for {myfirm} is {price} dollars"
        return stock_msg
    except:
        return None


def get_stock_market(request):
    
    # Obtain real-time index values from Yahoo
    dowj  = round(float(si.get_live_price('^DJI')),  2)
    sp500 = round(float(si.get_live_price('^GSPC')), 2)

    # Announces the index values
    ret = f"The Dow Jones Industry Average is {dowj}. " + \
          f"The S&P 500 is {sp500}."
    return ret



# --- tests

if __name__ == '__main__':
    pass



### --- NOTES
#
#   Use classes
#
#
#
