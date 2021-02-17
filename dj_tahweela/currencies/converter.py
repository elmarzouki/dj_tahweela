import requests, json 
from django.conf import settings

API_KEY = settings.ALPHAVANTAGE_API_KEY
PREFIX = "Realtime Currency Exchange Rate"
EXCHANGE_RATE = "5. Exchange Rate"
DATE = "6. Last Refreshed"

def get_physical_currnencies():
	"""
	:prams
	:return currencies_codes, currencies_description
	"""
	url = "https://www.alphavantage.co/physical_currency_list/"
	request = requests.get(url)
	currencies = request.content.decode("UTF-8").split('\r\n')
	codes = [x.split(",")[0] for x in currencies if len (x.split(",")[0])<5 and len(x.split(",")[0])>2]
	return codes, currencies 

def get_realtime_exchange_rate(from_currency, to_currency) : 
	"""
        Get the Exchange rate in real time using alphavantage.co
    """
	base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
	url = f"{base_url}&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}" 
	request = requests.get(url)
	result = request.json()
	return result[PREFIX][EXCHANGE_RATE], result[PREFIX][DATE] 

def get_fx(req_type):
	fx = "FX_INTRADAY" # set as default
	if req_type == settings.DAILY:
		fx = "FX_DAILY"
	elif req_type == settings.WEEKLY:
		fx = "FX_WEEKLY"
	elif req_type == settings.MONTHLY:
		fx = "FX_MONTHLY"
	return fx

def get_time_series_exchange_rate(from_currency, to_currency, req_type, interval="5min"):
	fx = get_fx(req_type)
	base_url = r"https://www.alphavantage.co/query?"
	url = f"{base_url}function={fx}&from_symbol={from_currency}&to_symbol={to_currency}"
	url = f"{url}&interval={interval}" if req_type == settings.INTRADAY else url # add interval on fx(INTRADAY) only
	url = f"{url}&apikey={API_KEY}" # add API_KEY
	request = requests.get(url)
	return request.json()


if __name__ == "__main__" : 
	from_currency = "USD"
	to_currency = "EGP"
	get_realtime_exchange_rate(from_currency, to_currency)
	get_time_series_exchange_rate(from_currency, to_currency, settings.INTRADAY)
