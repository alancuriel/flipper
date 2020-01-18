import json
import requests

KEY = "NSIT22619-c5e7-41ee-9311-cbde5b60ca2"
MPN = "MV7N2AM/A"

url = ("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced\
&sortOrder=PricePlusShippingLowest\
&buyerPostalCode=01609&SERVICE-VERSION=1.13.0\
&SECURITY-APPNAME={}\
&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&paginationInput.pageNumber=2\
&keywords={}".format(KEY, MPN))


def main():
	print(url)
	apiResult = requests.get(url)
	print(apiResult)
	parseddoc = apiResult.json()
	print(parseddoc)	


if __name__ == '__main__':
	main()
