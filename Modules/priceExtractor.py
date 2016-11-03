from lxml import html
import requests
url = "https://www.instant-gaming.com/it/1421-comprare-key-origin-battlefield-1/"
page = requests.get(url)
tree = html.fromstring(page.content)
price = tree.xpath('//span[@id="ig-product-main-panel-boxprice-contentright-price"]/text()')
print price[0][:5]
