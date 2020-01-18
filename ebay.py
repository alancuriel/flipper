import requests
from bs4 import BeautifulSoup

def getmpn(productname):
    #Get Html from URL Search
    SearchPage = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR9.TRC0.A0.H0.X" + productname + ".TRS1&_nkw=" + productname + "&_sacat=0")
    soup = BeautifulSoup(SearchPage.text, 'html.parser')
    itemlink = soup.find("a", class_="s-item__link")['href']
    itempage = requests.get(itemlink)
    soup = BeautifulSoup(itempage.text, 'html.parser')
    print(soup.find("h2", itemprop="mpn").text)