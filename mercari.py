from bs4 import BeautifulSoup
import  requests as req
import json
import  urllib.parse
from typing import  List,Dict

# minPrice is 30% of avg price of ebay and maxPrice is avg price in ebay
def get_items(keyword: str ,minPrice: int ,maxPrice: int) -> List[Dict]:
    soup = get_soup(get_item_url(keyword,minPrice,maxPrice))
    return [json.loads(item.text) for item in soup.find_all('script',{'type':'application/ld+json'})]

def items_avg_price(items: List[Dict]):
    sum = 0
    for item in items:
        sum += int(item['offers']['price'])
    return sum/len(items)

def get_new_sorted_items(items_old):
    return sorted(items_old, key=lambda item: float(item['offers']['price']))

def get_item_url(keyword,minPrice ,maxPrice):
    params = {
        'itemStatuses': '1',
        'keyword': keyword,
        'length' : '1000',
        'maxPrice': str(maxPrice * 100),
        'minPrice': str(minPrice * 100)
    }
    return 'https://www.mercari.com/search/?' + urllib.parse.urlencode(params)

def get_soup(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
    r = req.get(url,headers = headers)
    return BeautifulSoup(r.text)

