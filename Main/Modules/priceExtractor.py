from lxml import html
import requests
def import_price(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price = tree.xpath('//span[@id="ig-product-main-panel-boxprice-contentright-price"]/text()')
    return float(price[0][:5])
def import_price_average():
    from library import library
    matrix = []
    for x, val in enumerate(library):
        page = requests.get(library[x]['url-average'])
        tree = html.fromstring(page.content)
        price = tree.xpath('//strong[@itemprop="price"]/text()')
        price_list = []
        for val in price:
            price_list.append(float(val[:5]))
        matrix.append(price_list)
    return matrix
if __name__ == "__main__":
    print "%0.2f" % import_price()
