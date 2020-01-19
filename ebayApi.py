import json
import requests
import urllib.parse
import threading 
from multiprocessing import Pool, Manager
import numpy as np 
import os
import math

# KEY = "NSIT22619-c5e7-41ee-9311-cbde5b60ca2"
# testMPN = "MV7N2AM/A"
# MAX_PAGES = 92


class ebayAPI(object):
    def __init__(self, MPN):
        self.MPN = MPN
        self.KEY = "UnfazedL-0d37-44f2-ac5e-83646964e7d9"

    def get_sold_url(self, _zip, page=1):
        params = {
            'OPERATION-NAME': 'findCompletedItems',
            'SERVICE-VERSION': '1.13.0',
            'SECURITY-APPNAME': self.KEY,
            'buyerPostalCode': _zip,
            'RESPONSE-DATA-FORMAT': 'JSON',
            'REST-PAYLOAD': '',
            'paginationInput.pageNumber': '{}'.format(page),
            'keywords': self.MPN
        }
        return 'http://svcs.ebay.com/services/search/FindingService/v1?' + urllib.parse.urlencode(params)

    def get_total_pages(self, _zip ='01609'):
        api_response = requests.get(self.get_sold_url(_zip))
        print(api_response.status_code)
        result_dict = api_response.json()['findCompletedItemsResponse'][0]
        totalPages = int(result_dict['paginationOutput'][0]['totalPages'][0])
        img = result_dict['searchResult'][0]['item'][0]['galleryURL'][0]
        print('MPN:{}, Total pages number:{}, Image-logo:{}'.format(self.MPN, totalPages, img))
        return img, totalPages

    def get_first_img(self, _zip ='01609'):
        api_response = requests.get(self.get_sold_url(_zip))
        result_dict = api_response.json()['findCompletedItemsResponse'][0]
        img = result_dict['searchResult'][0]['item'][0]['galleryURL'][0]
        print('MPN:{}, Image-logo:{}'.format(self.MPN, img))
        return img


    def get_items_sum(self,items):
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

    def func_test(self, page, _zip='01609'):
        api_response = requests.get(self.get_sold_url(_zip, page))

        result_dict =api_response.json()['findCompletedItemsResponse'][0]

        if 'searchResult' in result_dict:
            s,n = self.get_items_sum(result_dict['searchResult'][0]['item'])
            return s/n

    def get_sold_items_info(self):
        pool = Pool(os.cpu_count())
        img = self.get_first_img()
        # size = int(np.rint(total_pages/2))
        sample = [1,2,3] # list(np.random.randint(low=4, high=total_pages-1, size=size)) + [1,2,3]
        lst = list(filter(None, pool.map(self.func_test, (sample))))
        # print('lst:{} \n lst_count:{} vs size:{} - Thus {} are missing due to network connection and/or scappring issues'.format(lst,len(lst), size, len(lst) - size))
        AvgPrice = math.floor(np.mean(lst))
        return {'Img':img,'AvgPrice':AvgPrice}


# def get_sold_items_info(mpn,zip='01609'):
#     api_response = requests.get(get_sold_url(mpn,zip))
#     output = {}

#     if api_response.status_code != 200:
#         return {}

#     result_dict = api_response.json()['findCompletedItemsResponse'][0]
#     totalPages = int(result_dict['paginationOutput'][0]['totalPages'][0])
#     output['Img'] = result_dict['searchResult'][0]['item'][0]['galleryURL'][0]

#     if totalPages > MAX_PAGES:
#         totalPages = MAX_PAGES

    
#     sum,totalItems = get_items_sum(result_dict['searchResult'][0]['item'])
    
#     if totalPages <= 1:
#         output['AvgPrice'] = sum/totalItems
#         return output

#     for i in range(2,totalPages+1):
#         api_response = requests.get(get_sold_url(mpn,zip,i))
#         result_dict =api_response.json()['findCompletedItemsResponse'][0]
    
#         if 'searchResult' in result_dict:
#             s,n = get_items_sum(result_dict['searchResult'][0]['item'])
#             sum += s
#             totalItems += n
#             print(s, n)

#     output['AvgPrice'] = sum/totalItems
#     return output

# def get_sold_url(mpn,zip,page=1):
#     params = {
#         'OPERATION-NAME': 'findCompletedItems',
#         'SERVICE-VERSION': '1.13.0',
#         'SECURITY-APPNAME': KEY,
#         'buyerPostalCode': zip,
#         'RESPONSE-DATA-FORMAT': 'JSON',
#         'REST-PAYLOAD': '',
#         'paginationInput.pageNumber': str(page),
#         'keywords': mpn
#     }
#     return 'http://svcs.ebay.com/services/search/FindingService/v1?' + urllib.parse.urlencode(params)


# def get_items_sum(items):
#     total = 0
#     n = 0
#     for item in items:
#         shipping = 0.0
#         if 'shippingServiceCost' in item['shippingInfo'][0]:
#             shipping = float(item['shippingInfo'][0]['shippingServiceCost'][0]['__value__'])
#         price = float(item['sellingStatus'][0]['currentPrice'][0]['__value__'])
#         total += shipping + price
#         n += 1
#     return (total,n)
         

def main():

    lol = ebayAPI("MV7N2AM/A")
    print(lol.get_sold_items_info())


if __name__ == '__main__':
    main()

