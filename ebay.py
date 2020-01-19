import requests
from bs4 import BeautifulSoup

def getmpn(productname):
    #Get Html from URL Search
    SearchPage = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR9.TRC0.A0.H0.X" + productname + ".TRS1&_nkw=" + productname + "&_sacat=0")
    #Add text to beautiful soup
    soup = BeautifulSoup(SearchPage.text, 'html.parser')
    #find item link
    itemlink = soup.find("a", class_="s-item__link")['href']
    itempage = requests.get(itemlink)
    #pass new link into soup
    soup = BeautifulSoup(itempage.text, 'html.parser')
    #return mpn

    mpn = soup.find("h2", itemprop="mpn")

    if not mpn:
        mpn = " "
    else:
        mpn = soup.find("h2", itemprop="mpn").text

    return mpn

def getbrandmodel(productname):
    #Get Html from URL Search
    SearchPage = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR9.TRC0.A0.H0.X" + productname + ".TRS1&_nkw=" + productname + "&_sacat=0")
    #Add text to beautiful soup
    soup = BeautifulSoup(SearchPage.text, 'html.parser')
    #find item link
    itemlink = soup.find("a", class_="s-item__link")['href']
    itempage = requests.get(itemlink)
    #pass new link into soup
    soup = BeautifulSoup(itempage.text, 'html.parser')
    #return mpn

    model = soup.find("h2", itemprop="model")
    brand = soup.find("h2", itemprop="brand")

    # FIX THIS LOGIC TOOO *************************
    if not model and not brand:
        model = " "
        brand = " "
    elif model and not brand:
        brand = " "
        model = soup.find("h2", itemprop="model").text
    elif not model and brand:
        model = " "
        brand = soup.find("h2", itemprop="brand").text
    else:
        model = soup.find("h2", itemprop="model").text
        brand = soup.find("h2", itemprop="brand").text

    return model + " " + brand
