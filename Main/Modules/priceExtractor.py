from lxml import html
import requests
def import_price(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price = tree.xpath('//span[@id="ig-product-main-panel-boxprice-contentright-price"]/text()')
    return float(price[0][:5])
def import_price_average():
    page = requests.get("http://www.allkeyshop.com/blog/buy-battlefield-1-cd-key-compare-prices/")
    tree = html.fromstring(page.content)
    price = tree.xpath('//strong[@itemprop="price"]/text()')
    price_list = []
    for val in price:
        price_list.append(float(val[:5]))
    return price_list
if __name__ == "__main__":
    print "%0.2f" % import_price()
