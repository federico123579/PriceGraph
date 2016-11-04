from lxml import html
import requests
def import_price():
    url = "https://www.instant-gaming.com/it/1421-comprare-key-origin-battlefield-1/"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price = tree.xpath('//span[@id="ig-product-main-panel-boxprice-contentright-price"]/text()')
    return float(price[0][:5])
if __name__ == "__main__":
    print "%0.2f" % import_price()
