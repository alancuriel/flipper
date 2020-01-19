import json
import requests
import urllib.parse

KEY = "NSIT22619-c5e7-41ee-9311-cbde5b60ca2"
# testMPN = "MV7N2AM/A"
MAX_PAGES = 10

def get_sold_items_info(mpn,zip='01609'):
    api_response = requests.get(get_sold_url(mpn,zip))
    output = {}

    if api_response.status_code != 200:
        return {}

    result_dict = api_response.json()['findCompletedItemsResponse'][0]
    totalPages = int(result_dict['paginationOutput'][0]['totalPages'][0])
    output['Img'] = result_dict['searchResult'][0]['item'][0]['galleryURL'][0]

    if totalPages > MAX_PAGES:
        totalPages = MAX_PAGES

    
    sum,totalItems = get_items_sum(result_dict['searchResult'][0]['item'])
    
    if totalPages <= 1:
        output['AvgPrice'] = sum/totalItems
        return output

    for i in range(2,totalPages+1):
        api_response = requests.get(get_sold_url(mpn,zip,i))
        result_dict =api_response.json()['findCompletedItemsResponse'][0]
    
        if 'searchResult' in result_dict:
            s,n = get_items_sum(result_dict['searchResult'][0]['item'])
            sum += s
            totalItems += n

    output['AvgPrice'] = sum/totalItems
    return output

def get_sold_url(mpn,zip,page=1):
    params = {
        'OPERATION-NAME': 'findCompletedItems',
        'SERVICE-VERSION': '1.13.0',
        'SECURITY-APPNAME': KEY,
        'buyerPostalCode': zip,
        'RESPONSE-DATA-FORMAT': 'JSON',
        'REST-PAYLOAD': '',
        'paginationInput.pageNumber': str(page),
        'keywords': mpn
    }
    return 'http://svcs.ebay.com/services/search/FindingService/v1?' + urllib.parse.urlencode(params)


def get_items_sum(items):
    total = 0
    n = 0
    for item in items:
        shipping = 0.0
        if 'shippingServiceCost' in item['shippingInfo'][0]:
            shipping = float(item['shippingInfo'][0]['shippingServiceCost'][0]['__value__'])
        price = float(item['sellingStatus'][0]['currentPrice'][0]['__value__'])
        total += shipping + price
        n += 1
    return (total,n)
        

